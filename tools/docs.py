#!/usr/bin/env python3
"""
Regenerate the two README tables that must never drift from the files: the template
contents list and the placeholder reference.

    python3 tools/docs.py           # rewrite the tables in README.md
    python3 tools/docs.py --check   # fail if they are out of date (use in CI)

Both tables are derived from what is actually in src/ and templates/, so a template
that is added, renamed or given a new placeholder cannot silently fall out of the docs.
Everything between the marker comments is generated; everything else is hand-written.
"""

import io
import os
import re
import sys
import glob
import collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))

import demo

README = os.path.join(ROOT, 'README.md')
PLACEHOLDERS = os.path.join(ROOT, 'PLACEHOLDERS.md')
PREVIEW = os.path.join(ROOT, 'index.html')
SAMPLE_START = '/* generated:sample */'
SAMPLE_END = '/* /generated:sample */'
OPTIONS_START = '<!-- generated:options -->'
OPTIONS_END = '<!-- /generated:options -->'

# The demo values live in tools/demo.py and nowhere else. Both the Example column below
# and the preview page read from there, so they cannot disagree about what a token means.
EXAMPLE = demo.VALUES
HTML_EXAMPLE = demo.HTML_VALUES

CONTENTS_START = '<!-- generated:contents -->'
CONTENTS_END = '<!-- /generated:contents -->'
PLACEHOLDERS_START = '<!-- generated:placeholders -->'
PLACEHOLDERS_END = '<!-- /generated:placeholders -->'

CATEGORY_TITLE = {
    'account': 'Account and security',
    'billing': 'Billing and subscription',
    'orders': 'Orders',
    'lifecycle': 'Lifecycle',
    'ops': 'Operational',
    'consent': 'Consent and legal',
}
CATEGORY_ORDER = ['account', 'billing', 'orders', 'lifecycle', 'ops', 'consent']

NOTE = {
    '[COMPANY_ADDRESS]': '**Legally required** in commercial mail — see [Compliance](#compliance).',
    '[UNSUBSCRIBE_URL]': '**Legally required** in commercial mail. Commercial templates only.',
    '[EXPIRY_ABSOLUTE]': 'An absolute time **with a timezone**. Always paired with the relative form.',
    '[EXPIRY_RELATIVE]': 'How long a link or code lasts, in words.',
    '[RETENTION_PERIOD]': 'How long data survives after an account lapses. Not the same thing as a link expiry.',
    '[RETENTION_END_DATE]': 'The date data is deleted. Paired with the period above, and never an expiry.',
    '[EVENT_IP]': 'Shown only in the sign-in alert, where the copy says it is approximate.',
    '[FIRST_NAME]': 'Give your platform a fallback; an empty value leaves a dangling comma.',
    '[OTP_CODE]': 'Must stay one contiguous run of characters — see [`partials/README.md`](partials/README.md).',
    '[AMOUNT]': 'Render money to **two decimal places**, or the decimal column will not align.',
    '[CURRENCY]': 'Bound to the figure with `&nbsp;` so it cannot wrap onto its own line.',
    '[SHIPPING_ADDRESS]': '**Renders differently in each part**: separate the lines with `<br>` in the `.html` and with real newlines in the `.txt`. Substituting one string into both breaks one of them.',
    '[BILLING_ADDRESS]': 'Same as `[SHIPPING_ADDRESS]`: `<br>` in the `.html`, newlines in the `.txt`.',
    '[DELIVERY_ESTIMATE]': 'An estimate, and the copy says so. Never present it as a guarantee.',
    '[REFUND_DAYS]': 'A range, not a date: the store releases the money but the card issuer decides when it lands.',
    '[DATA_NOT_INVOLVED]': 'Name what was **not** affected as explicitly as what was. Readers assume the worst.',
    '[WORKAROUND_TEXT]': 'Write "There is no workaround" when there is none. An empty value renders a panel that says only "Important:".',
    '[MAINTENANCE_START]': 'Always carries a timezone. A maintenance window without one is useless to half its readers.',
    '[NEXT_UPDATE_TIME]': 'The one commitment an incident notice can honestly make. Always carries a timezone.',
    '[TRACKING_NUMBER]': 'Tracking often shows no movement for a few hours after the label is created; the copy warns about this.',
}


def meta_of(part_path):
    head = io.open(part_path, encoding='utf-8').read().split('--- html')[0]
    meta = {}
    for line in head.splitlines():
        if ':' in line and not line.startswith('---'):
            k, v = line.split(':', 1)
            meta[k.strip()] = v.strip()
    return meta


def contents_table():
    by = collections.defaultdict(list)
    for f in sorted(glob.glob(os.path.join(ROOT, 'src', '*', '*.part'))):
        rel = os.path.relpath(f, os.path.join(ROOT, 'src'))[:-len('.part')]
        by[rel.split(os.sep)[0]].append((rel.replace(os.sep, '/'), meta_of(f)))

    out = ["Each template ships as `<name>.html` plus a hand-written `<name>.txt` sibling.",
           "The **Footer** column is the legal class: `transactional` mail carries no unsubscribe",
           "link, `commercial` mail carries the full opt-out block — see [Compliance](#compliance)."]
    for cat in CATEGORY_ORDER:
        if cat not in by:
            continue
        out += ['', f'**{CATEGORY_TITLE[cat]}**', '',
                '| Template | Suggested subject | Footer |', '| --- | --- | --- |']
        for rel, meta in sorted(by[cat]):
            name = rel.split('/')[1]
            out.append(f"| [`{name}`](templates/{rel}.html) | {meta.get('subject','')} | {meta.get('footer','')} |")
    return '\n'.join(out)


def placeholder_reference():
    """The full reference, as its own file.

    138 rows is a reference, not orientation. In the README it pushed everything people
    actually read — how it is built, compliance, testing — past line 400, and the widest
    row ran to 676 characters because it listed all 33 templates that use it.
    """
    templates = sorted(glob.glob(os.path.join(ROOT, 'templates', '*', '*.html')))
    where = collections.defaultdict(list)
    per_template = collections.defaultdict(set)
    for f in templates:
        rel = os.path.relpath(f, os.path.join(ROOT, 'templates')).replace(os.sep, '/')[:-5]
        for ph in set(re.findall(r'\[[A-Z0-9_]+\]', io.open(f, encoding='utf-8').read())):
            where[ph].append(rel)
            per_template[rel].add(ph)

    shared = sorted(p for p in where if len(where[p]) == len(templates))
    out = [
        '# Placeholder reference',
        '',
        'Every token in every template. You almost certainly do not need this page — open the',
        'template you are using and the tokens are right there, in `[UPPERCASE]`. This is for',
        'looking one up, or for wiring the whole set into a sending platform at once.',
        '',
        'The [README](README.md) covers the handful that are shared across all templates and the',
        'handful whose meaning is easy to get wrong.',
        '',
        '---',
        '',
        '## By template',
        '',
        'What one template needs, which is usually the question you actually have.',
        '',
    ]
    for rel in sorted(per_template):
        toks = ' '.join(f'`{t}`' for t in sorted(per_template[rel]))
        out += [f'**[`{rel}`](templates/{rel}.html)**', '', toks, '']

    out += ['---', '', '## Every token, alphabetically', '',
            '| Placeholder | Example | Used by |', '| --- | --- | --- |']
    for ph in sorted(where):
        users = sorted(where[ph])
        used = 'every template' if len(users) == len(templates) else ', '.join(
            u.split('/')[1] for u in users)
        ex = EXAMPLE.get(ph, '')
        note = NOTE.get(ph, '')
        # the notes are written for the README, where "#compliance" resolves; from this
        # file the same anchor is dead, so point it back at the README
        note = re.sub(r'\]\(#', '](README.md#', note)
        cell = (note + ' ' if note else '') + used
        out.append(f"| `{ph}` | {('`' + ex + '`') if ex else ''} | {cell} |")
    out += ['', f'{len(where)} placeholders across {len(templates)} templates. '
                f'{len(shared)} are used by every template.', '']
    return '\n'.join(out)


def placeholder_table():
    templates = sorted(glob.glob(os.path.join(ROOT, 'templates', '*', '*.html')))
    where = collections.defaultdict(list)
    for f in templates:
        name = os.path.basename(f)[:-5]
        for ph in set(re.findall(r'\[[A-Z0-9_]+\]', io.open(f, encoding='utf-8').read())):
            where[ph].append(name)

    shared = sorted(p for p in where if len(where[p]) == len(templates))
    local = sorted((p for p in where if len(where[p]) < len(templates)),
                   key=lambda p: (-len(where[p]), p))

    def row(ph, with_users):
        note = NOTE.get(ph, '')
        if with_users:
            users = ', '.join(sorted(set(where[ph])))
            note = (note + ' ' if note else '') + f'Used by: {users}.'
        ex = EXAMPLE.get(ph, '')
        return f"| `{ph}` | {('`' + ex + '`') if ex else ''} | {note.strip()} |"

    tricky = [p for p in ('[EXPIRY_ABSOLUTE]', '[EXPIRY_RELATIVE]', '[RETENTION_PERIOD]',
                          '[RETENTION_END_DATE]', '[SHIPPING_ADDRESS]', '[AMOUNT]',
                          '[CURRENCY]', '[OTP_CODE]') if p in where]

    out = ['**Set once for your product.** Every template uses these.', '',
           '| Placeholder | Example | Notes |', '| --- | --- | --- |']
    out += [row(p, False) for p in shared]
    out += ['', '**Worth reading before you fill them in.** Most tokens are named after what they',
            'hold and need no explanation. These are the ones where the meaning is not obvious,',
            'and where getting it wrong produces a bug rather than a typo.', '',
            '| Placeholder | Example | Notes |', '| --- | --- | --- |']
    out += [row(p, False) for p in tricky]
    out += ['', f'The other {len(local) - len(tricky)} are template-specific and named after what '
                f'they hold. Full list: **[PLACEHOLDERS.md](PLACEHOLDERS.md)**.']
    return '\n'.join(out)


def preview_options():
    """The <select> in the preview page, generated from what is actually on disk.

    data-example says whether this entry has a filled-in twin under examples/. The
    preview's "Sample data" button swaps the path rather than substituting tokens in
    the browser, so it works when index.html is opened straight off the filesystem.
    """
    groups = collections.defaultdict(list)
    for f in sorted(glob.glob(os.path.join(ROOT, 'templates', '*', '*.html'))):
        rel = os.path.relpath(f, ROOT).replace(os.sep, '/')
        groups[rel.split('/')[1]].append(rel)

    lines = []
    for cat in CATEGORY_ORDER:
        if cat not in groups:
            continue
        lines.append(f'      <optgroup label="{cat}">')
        for rel in groups[cat]:
            name = os.path.basename(rel)[:-5]
            has = os.path.exists(os.path.join(ROOT, rel.replace('templates/', 'examples/', 1)))
            lines.append(f'        <option value="{rel}" data-example="{1 if has else 0}">'
                         f'{name}</option>')
        lines.append('      </optgroup>')
    lines.append('      <optgroup label="reference">')
    lines.append('        <option value="partials/components.html" data-example="0">'
                 'components</option>')
    lines.append('      </optgroup>')
    return '\n'.join(lines)


def preview_sample():
    """The demo values index.html substitutes. Same source as the docs table, so the two
    can never disagree about what a placeholder means."""
    used = set()
    for f in glob.glob(os.path.join(ROOT, 'templates', '*', '*.html')) + \
             [os.path.join(ROOT, 'partials', 'components.html')]:
        used |= set(re.findall(r'\[[A-Z0-9_]+\]', io.open(f, encoding='utf-8').read()))
    lines = ['  var SAMPLE = {']
    entries = []
    for ph in sorted(used):
        val = HTML_EXAMPLE.get(ph, EXAMPLE.get(ph))
        if val is None:
            continue
        entries.append(f"    '{ph}': '{val}'")
    lines.append(',\n'.join(entries))
    lines.append('  };')
    return '\n'.join(lines)


def splice(text, start, end, body):
    a = text.index(start) + len(start)
    b = text.index(end)
    return text[:a] + '\n' + body + '\n' + text[b:]


def main():
    check_only = '--check' in sys.argv
    current = io.open(README, encoding='utf-8').read()
    for marker in (CONTENTS_START, CONTENTS_END, PLACEHOLDERS_START, PLACEHOLDERS_END):
        if marker not in current:
            print(f'README.md is missing the marker {marker}')
            return 1

    updated = splice(current, CONTENTS_START, CONTENTS_END, contents_table())
    updated = splice(updated, PLACEHOLDERS_START, PLACEHOLDERS_END, placeholder_table())

    n_templates = len(glob.glob(os.path.join(ROOT, 'templates', '*', '*.html')))
    n_ph = len(set(re.findall(r'\[[A-Z0-9_]+\]',
                              ''.join(io.open(f, encoding='utf-8').read()
                                      for f in glob.glob(os.path.join(ROOT, 'templates', '*', '*.html'))))))

    preview_current = io.open(PREVIEW, encoding='utf-8').read()
    preview_updated = splice(preview_current, SAMPLE_START, SAMPLE_END, preview_sample())
    preview_updated = splice(preview_updated, OPTIONS_START, OPTIONS_END, preview_options())

    reference_current = io.open(PLACEHOLDERS, encoding='utf-8').read() \
        if os.path.exists(PLACEHOLDERS) else ''
    if (updated == current and preview_updated == preview_current
            and reference_current == placeholder_reference()):
        print(f'docs are up to date ({n_templates} templates, {n_ph} placeholders)')
        return 0
    if check_only:
        print('docs are OUT OF DATE — run: python3 tools/docs.py')
        return 1
    io.open(README, 'w', encoding='utf-8').write(updated)
    io.open(PREVIEW, 'w', encoding='utf-8').write(preview_updated)
    io.open(PLACEHOLDERS, 'w', encoding='utf-8').write(placeholder_reference())
    print(f'docs regenerated ({n_templates} templates, {n_ph} placeholders)')

    # scan the templates, not the README: the README also mentions tokens in prose
    in_templates = set()
    for f in glob.glob(os.path.join(ROOT, 'templates', '*', '*.html')):
        in_templates |= set(re.findall(r'\[[A-Z0-9_]+\]', io.open(f, encoding='utf-8').read()))
    missing = [p for p in sorted(in_templates) if p not in EXAMPLE]
    if missing:
        print('placeholders with no example value in tools/docs.py: ' + ', '.join(missing))
    return 0


if __name__ == '__main__':
    sys.exit(main())

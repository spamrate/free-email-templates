#!/usr/bin/env python3
"""
Assemble the shipped templates from the shared shell plus per-template body sources.

This script is for MAINTAINERS. Users of this library never run it: the files in
templates/ are self-contained, dependency-free HTML that you copy and paste.

The point of it is consistency. Fifty-odd templates share one <head>, one <style>
block, one header and two footer variants. Hand-editing that shell in every file is
how template libraries drift; regenerating it is how they stay identical.

    python3 tools/assemble.py           # build everything, then check it
    python3 tools/assemble.py --check   # check only, do not write (use in CI)

Source format — src/<category>/<name>.part:

    --- meta
    title: Confirm your email address
    aria: Confirm your email address
    preheader: One click and your account is ready.
    subject: Confirm your email address
    footer: transactional          # or: commercial
    reason: You are receiving this email because someone signed up ...
    --- html
    <tr>
    <td class="sm-pad" style="padding:32px 32px 0 32px;">
    ...
    </td>
    </tr>
    --- text
    Body of the plain-text part. Hard-wrapped at 72 columns.
"""

import os
import re
import sys
import textwrap

import demo

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'src')
OUT = os.path.join(ROOT, 'templates')
DEMO_OUT = os.path.join(ROOT, 'examples')
TOOLS = os.path.join(ROOT, 'tools')
sys.path.insert(0, TOOLS)

MAX_LINE = 800          # RFC 5322 hard limit is 998; leave room for ESP link rewriting
TXT_WRAP = 72
STYLE_CAP = 16 * 1024   # Gmail truncates a <style> element past 16 KB
HTML_CAP = 60 * 1024    # keep well under Gmail's ~102 KB clipping after encoding


def read(path):
    with open(path, encoding='utf-8') as f:
        return f.read()


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)


def parse(path):
    """Split a .part file into its meta / html / text sections."""
    raw = read(path)
    chunks = re.split(r'(?m)^--- (meta|html|text)\s*$\n', raw)
    if chunks[0].strip():
        raise ValueError(f'{path}: content before the first --- section')
    sections = dict(zip(chunks[1::2], chunks[2::2]))
    for required in ('meta', 'html', 'text'):
        if required not in sections:
            raise ValueError(f'{path}: missing --- {required} section')

    meta = {}
    for line in sections['meta'].splitlines():
        if not line.strip():
            continue
        if ':' not in line:
            raise ValueError(f'{path}: meta line is not key: value -> {line!r}')
        k, v = line.split(':', 1)
        meta[k.strip()] = v.strip()
    for required in ('title', 'aria', 'preheader', 'subject', 'footer', 'reason'):
        if required not in meta:
            raise ValueError(f'{path}: meta is missing "{required}"')
    if meta['footer'] not in ('transactional', 'commercial'):
        raise ValueError(f'{path}: footer must be transactional or commercial')

    return meta, sections['html'].strip('\n'), sections['text'].strip('\n')


def build(meta, html_body, text_body):
    shell = read(os.path.join(TOOLS, 'shell.html'))
    footer = read(os.path.join(TOOLS, f"footer-{meta['footer']}.html"))
    footer = footer.replace('@@FOOTER_REASON@@', meta['reason'])

    html = (shell
            .replace('@@TITLE@@', meta['title'])
            .replace('@@ARIA_LABEL@@', meta['aria'])
            .replace('@@PREHEADER@@', meta['preheader'])
            .replace('@@CARD_ROWS@@', html_body)
            .replace('@@FOOTER@@', footer))

    def wrap(text):
        # placeholders can expand at send time, so wrap the authored form and let the
        # sender's own values be shorter or longer; a [TOKEN] never gets split
        return '\n'.join(textwrap.wrap(text, TXT_WRAP, break_long_words=False,
                                       break_on_hyphens=False)) or text

    unsub = '\nUnsubscribe:\n\n[UNSUBSCRIBE_URL]\n' if meta['footer'] == 'commercial' else '\n'
    txt = (read(os.path.join(TOOLS, 'shell.txt'))
           .replace('@@PREHEADER@@', wrap(meta['preheader']))
           .replace('@@TEXT_BODY@@', text_body)
           .replace('@@FOOTER_REASON@@', wrap(meta['reason']))
           .replace('@@TEXT_UNSUB@@', unsub))
    return html, txt


VOID = {'meta', 'br', 'img', 'hr', 'input', 'link', 'area', 'base', 'col',
        'embed', 'param', 'source', 'track', 'wbr'}


def tag_balance(html):
    """Return a list of nesting errors, ignoring anything inside comments."""
    from html.parser import HTMLParser

    class P(HTMLParser):
        def __init__(self):
            super().__init__(convert_charrefs=False)
            self.stack, self.err = [], []

        def handle_starttag(self, tag, attrs):
            if tag not in VOID:
                self.stack.append((tag, self.getpos()[0]))

        def handle_endtag(self, tag):
            if tag in VOID:
                return
            if not self.stack:
                self.err.append(f'line {self.getpos()[0]}: stray </{tag}>')
                return
            if self.stack[-1][0] != tag:
                self.err.append(
                    f'line {self.getpos()[0]}: </{tag}> but innermost open is '
                    f'<{self.stack[-1][0]}> from line {self.stack[-1][1]}')
                for i in range(len(self.stack) - 1, -1, -1):
                    if self.stack[i][0] == tag:
                        del self.stack[i:]
                        return
                return
            self.stack.pop()

    p = P()
    p.feed(html)
    return p.err + [f'unclosed <{t}> from line {ln}' for t, ln in p.stack]


def check(name, html, txt):
    """Every invariant the library promises. Returns a list of problems."""
    bad = []
    hl = html.split('\n')
    tl = txt.split('\n')

    bad += [f'{name}.html: {e}' for e in tag_balance(html)]

    if '{{' in html or '}}' in html:
        bad.append(f'{name}.html: contains {{{{ or }}}} — breaks Handlebars-style ESPs')
    for i, l in enumerate(hl, 1):
        if len(l) > MAX_LINE:
            bad.append(f'{name}.html:{i}: line is {len(l)} bytes (max {MAX_LINE})')
        if l != l.rstrip():
            bad.append(f'{name}.html:{i}: trailing whitespace')
        if any(ord(c) > 127 for c in l):
            bad.append(f'{name}.html:{i}: non-ASCII character — use an HTML entity')
    if re.search(r'\S!important|!IMPORTANT', html):
        bad.append(f'{name}.html: !important needs a space before it and must be lowercase')
    if 'overflow' in html:
        bad.append(f'{name}.html: the literal token "overflow" is rewritten by Orange webmail')
    for m in re.finditer(r'<!--(.*?)-->', html, re.S):
        if '->' in m.group(1):
            bad.append(f'{name}.html: "->" inside a comment — Yahoo ends the comment early')
    if re.search(r'style="[^"]*/\*', html):
        bad.append(f'{name}.html: CSS comment inside a style attribute — Orange drops the attribute')
    if re.search(r'@@[A-Z_]+@@', html) or re.search(r'@@[A-Z_]+@@', txt):
        bad.append(f'{name}: an @@SLOT@@ was left unfilled')

    style = re.search(r'<style>(.*?)</style>', html, re.S)
    if style and len(style.group(1).encode()) > STYLE_CAP:
        bad.append(f'{name}.html: <style> is over 16 KB — Gmail truncates it')
    if len(html.encode()) > HTML_CAP:
        bad.append(f'{name}.html: {len(html.encode())} bytes — too close to Gmail clipping')

    # data tables keep their semantics; layout tables must not pretend to have any
    for tbl in re.findall(r'<table[^>]*>.*?</table>', html, re.S):
        open_tag = re.match(r'<table[^>]*>', tbl).group(0)
        if 'role="presentation"' not in open_tag:
            continue
        # strip any nested table before looking for <th>, so a data table inside a layout
        # wrapper is not blamed on the wrapper
        inner = re.sub(r'<table[^>]*>.*</table>', '', tbl, flags=re.S)
        if re.search(r'<th[\s>]', inner):
            bad.append(f'{name}.html: a role="presentation" table contains <th>')
    # <th[\s>] and not <th[^>]*> — the latter also matches the literal <thead> tag, which
    # has no scope and never should have one
    for m in re.finditer(r'<th[\s>][^>]*>', html):
        if 'scope=' not in m.group(0):
            bad.append(f'{name}.html: <th> without scope — {m.group(0)[:60]}')

    # 72 columns is a readability convention, not a limit; RFC 5322's hard limit is 998.
    # The hand-written sources are held to 72 strictly. The generated demo copies cannot
    # be: a "Label: value" row is a data table rendered as text, and wrapping it would
    # need a leading-space continuation, which is itself banned. So those rows are
    # allowed to run long, and only the prose around them is held to 72.
    is_demo = name.startswith('examples/')
    label_row = re.compile(r'^[A-Z][A-Za-z /-]{0,24}: \S')
    for i, l in enumerate(tl, 1):
        if len(l) <= TXT_WRAP or l.strip().startswith('['):
            continue
        unwrappable = is_demo and (label_row.match(l) or l.startswith('http'))
        if unwrappable:
            if len(l) > 400:
                bad.append(f'{name}.txt:{i}: unwrappable line is {len(l)} chars — too long even '
                           f'for a table row')
        else:
            bad.append(f'{name}.txt:{i}: line is {len(l)} chars (wrap at {TXT_WRAP})')
        if l.startswith(' '):
            bad.append(f'{name}.txt:{i}: leading space')
        if l.startswith('>') or l.startswith('From '):
            bad.append(f'{name}.txt:{i}: line starts with ">" or "From "')
        if l == '-- ':
            bad.append(f'{name}.txt:{i}: bare "-- " is read as a signature separator')
        if l != l.rstrip():
            bad.append(f'{name}.txt:{i}: trailing whitespace')
        if any(ord(c) > 127 for c in l):
            bad.append(f'{name}.txt:{i}: non-ASCII character')
    if re.search(r'&[a-zA-Z#0-9]+;', txt):
        bad.append(f'{name}.txt: contains an HTML entity — write the character')
    if len(txt.split()) < 40:
        bad.append(f'{name}.txt: under 40 words')

    ph_h = set(re.findall(r'\[[A-Z0-9_]+\]', html))
    ph_t = set(re.findall(r'\[[A-Z0-9_]+\]', txt))
    for p in sorted(ph_t - ph_h):
        bad.append(f'{name}: {p} is in the .txt but not the .html')

    # the plain-text part must share vocabulary with the HTML part (SpamAssassin MPART_ALT_DIFF)
    # the preheader div is deliberately NOT stripped: it is real content that appears in both
    # parts, so excluding it here but not from the text part would be an asymmetric comparison
    visible = re.sub(r'<(style|head)[\s\S]*?</\1>', '', html)
    visible = re.sub(r'<!--[\s\S]*?-->', '', visible)
    visible = re.sub(r'<[^>]+>', ' ', visible)
    visible = re.sub(r'&[a-zA-Z#0-9]+;', ' ', visible)
    hw = {w.lower().strip('.,:;!?()') for w in visible.split() if w.isalpha()}
    tw = {w.lower().strip('.,:;!?()') for w in txt.split() if w.isalpha()}
    extra = sorted(tw - hw)
    if extra:
        bad.append(f'{name}.txt: words absent from the HTML part: {", ".join(extra[:8])}')

    return bad


def main():
    check_only = '--check' in sys.argv
    parts = sorted(
        os.path.join(dp, f)
        for dp, _, fns in os.walk(SRC)
        for f in fns if f.endswith('.part'))
    if not parts:
        print('no sources found in src/')
        return 1

    problems, built = list(demo.check_arithmetic()), []
    for path in parts:
        rel = os.path.relpath(path, SRC)[:-len('.part')]
        try:
            meta, hb, tb = parse(path)
        except ValueError as e:
            problems.append(str(e))
            continue
        html, txt = build(meta, hb, tb)
        problems += check(rel, html, txt)

        # the same source, with the demo company substituted in
        demo_html = demo.substitute(html, demo.for_html())
        demo_txt = demo.rewrap_text(demo.substitute(txt, demo.for_text()))
        problems += check('examples/' + rel, demo_html, demo_txt)
        left = set(re.findall(r'\[[A-Z0-9_]+\]', demo_html + demo_txt))
        if left:
            problems.append(f'examples/{rel}: no demo value for {", ".join(sorted(left))} '
                            f'— add one to tools/demo.py')

        if not check_only:
            write(os.path.join(OUT, rel + '.html'), html)
            write(os.path.join(OUT, rel + '.txt'), txt)
            write(os.path.join(DEMO_OUT, rel + '.html'), demo_html)
            write(os.path.join(DEMO_OUT, rel + '.txt'), demo_txt)
        built.append((rel, meta['footer'], len(html.encode()), len(txt.encode())))

    verb = 'checked' if check_only else 'built'
    print(f'{verb} {len(built)} template(s)\n')
    print(f"{'template':38s} {'footer':14s} {'html':>7s} {'txt':>6s}")
    for rel, foot, hb_, tb_ in built:
        print(f'{rel:38s} {foot:14s} {hb_:7d} {tb_:6d}')

    if problems:
        print(f'\n{len(problems)} problem(s):')
        for p in problems:
            print('  ' + p)
        return 1
    print('\nall invariants pass')
    return 0


if __name__ == '__main__':
    sys.exit(main())

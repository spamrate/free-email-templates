# src/ — template sources

**You do not need this directory to use the templates.** Copy from
[`templates/`](../templates) instead; those files are complete and need no build step.

This is where the templates are *written*. Each `.part` holds only what makes one template
different from the others — its copy and its markup. The shared `<head>`, `<style>` block,
header and footer come from [`tools/`](../tools) at build time, which is what keeps all 38
templates byte-identical outside their body copy.

```
src/<category>/<name>.part   ->   templates/<category>/<name>.{html,txt}
                             ->   examples/<category>/<name>.{html,txt}
```

## The format

```
--- meta
title: Confirm your email address        the <title> element
aria: Confirm your email address         the aria-label on the article wrapper
preheader: One click and you are set     inbox preview text, 60-90 characters
subject: Confirm your email address      suggested subject line
footer: transactional                    transactional | commercial - a legal class
reason: You are receiving this because   the one-line "why you got this" in the footer
--- html
<tr>...</tr>                             the rows that go inside the card table
--- text
The plain-text part, wrapped at 72 columns.
```

`footer` is not a style choice. `transactional` renders no unsubscribe link, because
attaching one to operational mail can suppress messages the recipient needs. `commercial`
renders the full opt-out block that CAN-SPAM requires for promotional mail. See
**Compliance** in the [main README](../README.md).

## After editing

```bash
python3 tools/assemble.py     # rebuild, and reject anything that breaks an invariant
```

Do not edit `templates/` or `examples/` by hand — the next build overwrites them.

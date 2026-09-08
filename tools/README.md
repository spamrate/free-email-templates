# tools/ — the generator

**You do not need this directory to use the templates.** Copy from
[`templates/`](../templates) instead; those files are complete and need no build step.

This turns [`src/`](../src) into the shipped `templates/` and `examples/`. Python 3 standard
library only — nothing to install.

| File | What it is |
| --- | --- |
| `assemble.py` | Wraps each `src/*.part` in the shared shell, writes `templates/` and `examples/`, and refuses to build anything that breaks an invariant |
| `docs.py` | Regenerates the README tables and the preview page's demo values from what is actually on disk |
| `demo.py` | The fictional company used in `examples/`. The only place those values live |
| `shell.html`, `shell.txt` | The `<head>`, `<style>` block and header every template shares |
| `footer-transactional.html`, `footer-commercial.html` | The two footers, one per legal class |

```bash
python3 tools/assemble.py          # rebuild everything
python3 tools/assemble.py --check  # validate without writing (use in CI)
python3 tools/docs.py              # refresh the README tables and preview data
python3 tools/docs.py --check      # fail if they are stale
```

## Why a generator at all

The shared shell is 6.7 KB repeated in all 38 templates — 250 KB of the 589 KB in
`templates/`. One edit here propagates to every file; by hand it would be 38 edits that all
have to come out identical. That is the failure mode that killed every unmaintained free
email-template library, so the generator is the point rather than a convenience.

## What `assemble.py` checks

Tag balance parsed properly, not by regex. Line length against RFC 5322. ASCII only. No
`{{` (breaks Handlebars-style platforms). No literal `overflow` token (Orange webmail
rewrites it). No `->` inside an HTML comment (Yahoo ends the comment early). Every `<th>`
carries `scope`; no `role="presentation"` table contains one. Plain-text wrapping, URL
placement and leading characters. Whether the text part shares its vocabulary with the HTML
part, which is what stops SpamAssassin's `MPART_ALT_DIFF` firing. And whether the demo money
actually adds up.

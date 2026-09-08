# Components

[`components.html`](components.html) is a real, previewable page containing every markup
primitive this library uses beyond "heading, paragraphs, one button, footer". Each block is
delimited by an HTML comment naming it. Open it in [the preview page](../index.html), copy the
block you need, paste it into a template.

It is documentation, not a sendable email — it has no compliance footer, because it is never sent.

---

## The one rule that matters most

**Every table in an email is either a layout table or a data table, and they are marked up in
opposite ways. Mixing them is the most common accessibility defect in shipped commerce templates.**

| | Layout table | Data table |
| --- | --- | --- |
| Purpose | Positioning. It is a grid because email has no other layout engine. | Real tabular data: line items, totals, order metadata. |
| `role="presentation"` | **Required**, on every one, including nested ones — the role does not inherit | **Must not be present.** It strips rows, cells and headers from the accessibility tree |
| `<th>`, `scope`, `<caption>` | **Never.** A stray `<th>` or even an empty `summary` flips a screen reader's heuristic into data-table mode | **Required.** `<th scope="col">` per column, `<th scope="row">` on each row's label cell, `<caption>` as the accessible name |
| In this file | 10 of them | 3 of them: line items, totals, label/value |

Get it backwards and a receipt reads aloud as `Merino crew sweater 1 120.00 Wool socks 3 36.00` —
one flat run with no way to tell a quantity from a price.

Two real-world reference points: Postmark's receipt gets `role="presentation"` right on its
wrappers but ships its line-item table with no `scope` and no `caption`; Foundation's `order.html`
has no `role="presentation"` at all, so its layout tables are announced as data tables — the exact
inverse error.

Do not hide the `<caption>` with `display:none` — that removes it from the accessibility tree too.
Render it small, as here.

---

## Shared contract

Everything in the library is built to these numbers. Change one and you must change the others.

| | Value |
| --- | --- |
| Content width | 600px (`max-width` on a div, plus an mso ghost table) |
| Card padding | 32px desktop, 20px under 600px (`.sm-pad`) |
| Usable width inside the card | 536px desktop |
| Line-item table columns | **60 / 15 / 25** — item / qty / amount |
| Totals table columns | 65 / 35 |
| Label-value columns | 45 / 55 |
| Button padding | 12px 32px at 16px text = 48px tall |

**The button's Outlook padding is arithmetic, not cascade.** `mso-text-raise` is a percentage of
`font-size`, so 12px vertical padding on 16px text is 75% on the `<span>` and double that, 150%, on
the `<i>`. Change the padding and you must recompute both, or Outlook renders a different height
from every other client. Horizontal padding works the same way: `&emsp;` is 1em, scaled by
`mso-font-width:200%` to the 2em (32px) side padding.

---

## Per-primitive notes

**1. Line-item table.** Column widths live in HTML `width` attributes, not CSS: the Word engine
ignores `table-layout` entirely. Three columns is the hard limit — a four-column table cannot
degrade at 320px, and horizontal scroll is not a fallback (iOS Mail scales the whole message down
instead, which is why `x-apple-disable-message-reformatting` is in the head; other mobile clients
clip). Fold variant, SKU and unit price into the item cell as extra lines. The Word engine honours
**no** wrapping properties at all — `word-wrap`, `overflow-wrap`, `word-break` and `<wbr>` all fail
— so a long unbroken SKU widens the table past its container. Hard-wrap long identifiers before
they reach the template.

**2. Totals.** Right alignment is set twice, as the `align` attribute *and* an inline style: the
attribute is supported everywhere, the style covers clients that normalise attributes. Never
`text-align:end`/`start` — the flow-relative keywords are dead in Outlook Windows, Yahoo and AOL.
Always render two decimal places so right alignment produces a true decimal column; there is no
decimal-alignment mechanism in email. The grand total is marked by `<strong>` **and** a border,
never by a background fill alone — a 4% grey fill inverts into the body colour in dark mode and the
separation vanishes, while a border survives inversion as a visible line either way.

**3. One-time code.** The code is **one contiguous text node**. Do not split the digits into
per-`<span>` boxes and do not insert spacer characters: both break select-and-copy, which is how the
code is actually used. `letter-spacing` is visual only, so it does not contaminate the clipboard —
but Outlook Windows support is buggy and it is reported not working at all in current Outlook 365,
so the code must be legible at zero tracking. Never a webfont: Outlook accepts the `@font-face`
declaration, ignores the remote font, and falls back to Times New Roman while ignoring the rest of
your stack. `user-select` is stripped everywhere, so you can neither break selection nor use
`user-select:all` to make one tap grab the code.

*The screen-reader problem, stated honestly.* Many screen readers announce `482913` as "four
hundred eighty-two thousand nine hundred thirteen". Every web fix is unavailable here: `aria-label`
is stripped by Yahoo and AOL, `aria-labelledby` breaks because Gmail and Outlook.com prefix `id`
values but not the reference. There are three options and each costs something:

| Option | Gain | Cost |
| --- | --- | --- |
| **Contiguous digits + "6-digit code" in the sentence** (shipped default) | Paste always works | Readout is still a single number; only the digit count is conveyed |
| Grouped digits: `482 913` | Most readers announce two 3-digit groups; sighted users transcribe more accurately | Paste breaks unless your verifier strips whitespace |
| Contiguous + visually-hidden spelled-out copy | Correct readout and correct paste | Select-all-and-copy can catch the hidden copy in some clients and corrupt the paste |

The default is the first, because a failed paste means a failed sign-in and there is no fallback
inside the email. Switch to grouping only if you control the verifier and it strips whitespace.

**4. Label / value.** This is tabular data, so it is a data table with `<th scope="row">` labels —
that is what makes "Order number" announce together with `#10023`. Single column by default:
correct at every width, correct in a screen reader, no ghost tables and no media queries needed.
Reserve two-column for genuinely independent side-by-side blocks (see primitive 10), because when
inline-blocks stack the reading order is block-then-block, which is right for blocks and wrong for
a matrix.

**5. List.** Real `<ul>`/`<ol>`/`<li>`, so a screen reader announces "list, 3 items" and offers
item-by-item navigation. The indent is a **left margin on the `<li>`**, never padding on the `<ul>`
— client defaults for list padding vary wildly and Outlook ignores `list-style-position`. Use the
`list-style-type` longhand: Gmail drops the entire `list-style` shorthand if it contains a
`list-style-image`. Do not use the `reversed` attribute on `<ol>` (unsupported everywhere tested)
or `value` on `<li>` (Outlook closes the list and opens a new one). Set `color` on the `<li>`, not
just a wrapper — the bullet marker takes the `<li>` colour, so they invert together.

**6. Buttons.** Both are `<a>`. Never `<button>`, never `role="button"` — email has no JavaScript,
so a fake button is a control no keyboard user can operate. The ghost button declares an
**explicit** `background-color`, not `transparent` and not omitted: an inverting client flips
background and border together, and an undeclared background leaves the border contrasted against a
page colour it was never designed for — the button disappears. This is the single most common
dark-mode casualty. Stacked rather than side by side, because two padded buttons do not fit at
320px. `border-radius` is dropped in Outlook Windows; square corners there are an acceptable
degradation and not worth VML.

**7. Callout.** A text-only library has no icon, so **the word is the icon**: lead with a bold
`Important:`. Colour must never be the only signal (WCAG 1.4.1). No background image, no gradient —
and this is enforced by support data, not just by our text-only rule: `linear-gradient` is dead in
all Outlooks, Yahoo and AOL, and Gmail **removes the entire style attribute or `<style>` tag** when
it finds a `url()` in it, which can destroy styling far beyond the panel. Do not use `role="alert"`
or `aria-live`: nothing in an email is live, and Yahoo and AOL strip ARIA anyway.

**8. Digest item.** **The item title is the link.** Never "Read more" — a screen reader user picks
from a links-only list where the surrounding copy is gone, and eight identical links are unusable.
ARIA cannot rescue this. This is also the primitive most likely to hit Gmail's ~102 KB clipping, so
cap the item count and put the "view all" link near the top as well as the bottom.

**9. Expiry.** Prose, not a component. State an **absolute** timestamp with a timezone **and** the
relative duration: you cannot compute the reader's local time at open, a relative-only deadline is
already wrong by the time the message clears a queue, and it is wrong again on every reopen.

*No live countdown, ever.* Email has no JavaScript, so "live" means a third-party animated GIF
regenerated per open, and it fails exactly where it matters: Outlook 2007–2019 cannot animate and
shows the first frame as though it were current; Apple Mail caches the image so a reopen shows a
stale number; image blocking removes the deadline entirely; and it puts required transactional
information behind a remote request with alt text that cannot update. A static timestamp is more
accurate, always visible, readable aloud, and survives forwarding and printing.

**10. Address block.** Two independent blocks, **not** a matrix — so a layout table with
`role="presentation"`, never `<th>Billing</th><th>Shipping</th>` (a screen reader would announce a
column header against each line fragment). Each label sits in the same cell as its address so they
cannot separate when the columns stack. Stacking needs no media query: two 220px minimums cannot
both fit a 320px viewport, and the ghost table keeps them side by side in the Word engine, which
ignores `min-width`. Line breaks are `<br>` only — one `<p>` per line picks up Outlook's own
margins, and `white-space:pre` is unsupported in Outlook Windows and the Gmail and Yahoo apps.
`<address>` gets an explicit `font-style:normal`, because it is italic by default in some renderers.

---

## Stacking policy

**One technique, library-wide:** the ghost-table + `display:inline-block` hybrid with
`min-width`/`max-width` and `font-size:0` on the wrapper. It stacks with no media query at all,
which is what makes it work in Gmail with a non-Google account, where there is no `<style>` block.

Banned: `calc()` and `max()` (dead in Outlook.com, Outlook iOS/Android, Yahoo and AOL — the "Fab
Four" techniques collapse silently), and media-query-dependent stacking (dead in Gmail with a
non-Google account and in Outlook Windows, which ignores `@media` entirely). Media queries stay in
the library for typography and alignment polish only.

Budget for one more failure mode: new Outlook 365 on Windows has been observed ignoring style-block
CSS and stacking hybrid columns vertically, so **every hybrid layout must be acceptable stacked.**

---

## Verified, and not verified

Contrast is calculated, and both palettes render as intended in a headless browser — the components
were checked by dumping computed styles with the dark block forced on. Two dark-mode bugs were
found and fixed that way: the one-time code and the callout panel each had an inner cell carrying an
inline light background while the dark rule overrode only the text colour, producing light text on a
light ground. If you add a component, check the computed background **and** colour of every nested
cell, not just the wrapper.

| Colour pair | Light | Dark |
| --- | --- | --- |
| Code / table header / ghost label | 17.4:1 | 14.5:1 |
| Callout text | 12.3:1 | 12.4:1 |
| Totals label | 8.9:1 | 8.1:1 |
| Digest link | 8.7:1 | 8.1:1 |
| Ghost border (non-text, needs 3:1) | 5.3:1 | 5.0:1 |

**What is not verified:** caniemail has no test entry for `<th>`, the `scope` attribute,
`<caption>`, `<thead>`/`<tfoot>`, or `role="presentation"` as a value. What is measured is that
`<table>` is supported in every client tested, that `role` works in Yahoo and AOL only on the
`<table>` tag — which is exactly where it is needed — and that HEY and Mail.ru do not support
`<caption>` (Mail.ru re-emits its text before the table, which is acceptable degradation). Treat
`<th scope>` and `<caption>` as *shipped in production* (WooCommerce sends them) rather than as
*measured support*, and send yourself a test before relying on them.

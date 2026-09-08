# Free Email Templates

**38 transactional and lifecycle email templates. Text only, dark-mode ready, MIT licensed,
no build step.**

> ### Built and maintained by [SpamRate](https://spamrate.is)
>
> A template makes your email *render*. It cannot make it *arrive*. If a message lands in
> spam, none of the work below matters.
>
> **[Run a free email deliverability test →](https://spamrate.is/email-deliverability-test)**
> See where your email actually lands at Gmail, Outlook, Yahoo, Zoho and AOL — real
> mailboxes, not a simulated score. Free plan, no credit card.

Copy a file into your project as-is, or use it as the starting point for your own. One
self-contained `.html` per template, with a hand-written plain-text sibling. Built for SaaS
products, online stores, and any team that has to send this mail and would rather not spend
a week re-learning Outlook's rendering quirks.

- **Responsive** — single-column, fluid, readable at 320px and at 600px+.
- **Text only** — every word is live text. Nothing is baked into an image, so nothing
  disappears when images are blocked or a screen reader is used.
- **Dark mode** — a hand-authored dark palette, plus a light palette chosen to survive the
  clients that force their own inversion on you.
- **Accessible** — semantic headings, `role="presentation"` on layout tables and real
  `<th scope>` on data tables, `lang`/`dir`, descriptive link text, WCAG AA/AAA contrast in
  both palettes.
- **Two copies of every template** — one with `[PLACEHOLDER]` tokens, one filled in with a
  fictional company so you can read it as a real email.
- **MIT licensed** — use it commercially, no attribution required.

```bash
git clone https://github.com/spamrate/free-email-templates.git
```

---

## Contents

Every template exists twice:

| | Path | What it is |
| --- | --- | --- |
| **Template** | `templates/<category>/<name>.html` | `[PLACEHOLDER]` tokens. This is the one you copy. |
| **Example** | `examples/<category>/<name>.html` | The same file with a fictional company filled in. Read it to see what the template becomes, or open it to check a render. |

Both are generated from one source, so they can never drift apart. See
[Examples](#examples) for the company in them.

<!-- generated:contents -->
Each template ships as `<name>.html` plus a hand-written `<name>.txt` sibling.
The **Footer** column is the legal class: `transactional` mail carries no unsubscribe
link, `commercial` mail carries the full opt-out block — see [Compliance](#compliance).

**Account and security**

| Template | Suggested subject | Footer |
| --- | --- | --- |
| [`account-locked`](templates/account/account-locked.html) | Your [PRODUCT_NAME] account is locked | transactional |
| [`email-change-new`](templates/account/email-change-new.html) | Confirm your new email address | transactional |
| [`email-change-old`](templates/account/email-change-old.html) | Your [PRODUCT_NAME] email is changing | transactional |
| [`magic-link`](templates/account/magic-link.html) | Your sign-in link for [PRODUCT_NAME] | transactional |
| [`new-device-signin`](templates/account/new-device-signin.html) | Sign-in from a new device or location | transactional |
| [`otp-code`](templates/account/otp-code.html) | Your sign-in code for [PRODUCT_NAME] | transactional |
| [`password-changed`](templates/account/password-changed.html) | Your [PRODUCT_NAME] password was changed | transactional |
| [`password-reset`](templates/account/password-reset.html) | Reset your [PRODUCT_NAME] password | transactional |
| [`verify-email`](templates/account/verify-email.html) | Confirm your email for [PRODUCT_NAME] | transactional |

**Billing and subscription**

| Template | Suggested subject | Footer |
| --- | --- | --- |
| [`card-expiring`](templates/billing/card-expiring.html) | Your [PRODUCT_NAME] card expires soon | transactional |
| [`payment-failed-1`](templates/billing/payment-failed-1.html) | Your [PRODUCT_NAME] payment failed | transactional |
| [`payment-failed-2`](templates/billing/payment-failed-2.html) | Second notice: your payment failed | transactional |
| [`payment-failed-final`](templates/billing/payment-failed-final.html) | Final notice: your subscription pauses | transactional |
| [`receipt`](templates/billing/receipt.html) | Your [PRODUCT_NAME] payment receipt | transactional |
| [`renewal-reminder`](templates/billing/renewal-reminder.html) | Your [PRODUCT_NAME] subscription renews | transactional |
| [`subscription-cancelled`](templates/billing/subscription-cancelled.html) | [PRODUCT_NAME] subscription cancelled | transactional |
| [`trial-ending`](templates/billing/trial-ending.html) | Your [PRODUCT_NAME] trial is ending | transactional |

**Orders**

| Template | Suggested subject | Footer |
| --- | --- | --- |
| [`delivered`](templates/orders/delivered.html) | Your order [ORDER_NUMBER] was delivered | transactional |
| [`order-cancelled`](templates/orders/order-cancelled.html) | Order [ORDER_NUMBER] has been cancelled | transactional |
| [`order-confirmation`](templates/orders/order-confirmation.html) | Your [COMPANY_NAME] order is confirmed | transactional |
| [`refund-issued`](templates/orders/refund-issued.html) | Your refund for order [ORDER_NUMBER] | transactional |
| [`return-label`](templates/orders/return-label.html) | Your [PRODUCT_NAME] return is approved | transactional |
| [`shipped`](templates/orders/shipped.html) | Your order [ORDER_NUMBER] has shipped | transactional |

**Lifecycle**

| Template | Suggested subject | Footer |
| --- | --- | --- |
| [`collaboration-notification`](templates/lifecycle/collaboration-notification.html) | [ACTOR_NAME] commented on [OBJECT_NAME] | transactional |
| [`digest`](templates/lifecycle/digest.html) | [PRODUCT_NAME] digest for [PERIOD_LABEL] | commercial |
| [`feature-announcement`](templates/lifecycle/feature-announcement.html) | [FEATURE_NAME] is now in [PRODUCT_NAME] | commercial |
| [`re-engagement`](templates/lifecycle/re-engagement.html) | Your [PRODUCT_NAME] account is unused | commercial |
| [`team-invitation`](templates/lifecycle/team-invitation.html) | [INVITER_NAME] invited you to [TEAM_NAME] | commercial |
| [`welcome`](templates/lifecycle/welcome.html) | Welcome to [PRODUCT_NAME] | commercial |

**Operational**

| Template | Suggested subject | Footer |
| --- | --- | --- |
| [`incident-open`](templates/ops/incident-open.html) | [PRODUCT_NAME] incident: investigating | transactional |
| [`incident-resolved`](templates/ops/incident-resolved.html) | [PRODUCT_NAME] incident resolved | transactional |
| [`quota-exceeded`](templates/ops/quota-exceeded.html) | You have reached your [QUOTA_NAME] limit | transactional |
| [`scheduled-maintenance`](templates/ops/scheduled-maintenance.html) | Scheduled [PRODUCT_NAME] maintenance | transactional |

**Consent and legal**

| Template | Suggested subject | Footer |
| --- | --- | --- |
| [`data-breach`](templates/consent/data-breach.html) | Your [PRODUCT_NAME] data was breached | transactional |
| [`double-opt-in`](templates/consent/double-opt-in.html) | Confirm your [PRODUCT_NAME] subscription | transactional |
| [`dsar-acknowledgement`](templates/consent/dsar-acknowledgement.html) | Your data request has been received | transactional |
| [`terms-change`](templates/consent/terms-change.html) | Changes to the [PRODUCT_NAME] terms | transactional |
| [`unsubscribe-confirmed`](templates/consent/unsubscribe-confirmed.html) | You are unsubscribed from [LIST_NAME] | transactional |
<!-- /generated:contents -->

**Reference**

| File | What it is |
| --- | --- |
| [`partials/components.html`](partials/components.html) | Every markup primitive, in one previewable page |
| [`partials/README.md`](partials/README.md) | How each primitive works and what breaks if you change it |
| [`index.html`](index.html) | Local preview — any template at 375 / 480 / desktop / full width, with sample values |

See [Roadmap](#roadmap) for what is coming.

### What is in here, and what you actually need

**If you just want a template, you need one directory: `templates/`.** Everything else is
either a nicer way to read the same thing, or the machinery that keeps the 38 files
consistent. Nothing here has to be installed, built, or run.

| You are... | You need | You can ignore |
| --- | --- | --- |
| **Using a template** | `templates/` — copy the `.html` and its `.txt` | everything else |
| **Deciding which one to use** | `examples/` to read them filled in, or `index.html` to preview | `src/`, `tools/` |
| **Changing a template's markup** | `partials/` — what every component is and what breaks if you edit it | `src/`, `tools/` |
| **Maintaining this library** | `src/` and `tools/` — see [Maintaining](#maintaining) | — |

```
templates/<category>/<name>.html        what you copy — self-contained, no dependencies
templates/<category>/<name>.txt         its plain-text sibling
examples/<category>/<name>.{html,txt}   the same files with a demo company filled in
partials/                               the component reference and its rules
index.html                              local preview, opens straight off disk

src/<category>/<name>.part              source: the body copy and markup of one template
tools/                                  the generator that turns src/ into templates/
```

### Why the source is committed too

`templates/` and `examples/` are **generated** from `src/` — so why ship both?

Because the shared shell (`<head>`, the `<style>` block, the header, the two footers) is
**6.7 KB repeated in all 38 files — 250 KB of the 589 KB in `templates/`**. With the
generator committed, changing one line in that shell is one edit and a rebuild. Without it,
it is 38 hand edits that have to come out identical, and the first time one of them does
not, the library has started to drift. Every free email-template library that stopped being
maintained drifted first.

The generated files are committed as well, so that copying a template stays a one-click
operation and nobody has to install Python to get an `.html` file. That is the trade the
repository makes deliberately: a slightly larger listing in exchange for both a usable
product and a maintainable one.

---

## Maintaining

Only relevant if you are changing the templates themselves.

```bash
python3 tools/assemble.py          # rebuild templates/ and examples/ from src/
python3 tools/assemble.py --check  # validate without writing anything
python3 tools/docs.py              # refresh the README tables and the preview data
python3 tools/docs.py --check      # fail if they are stale
```

Nothing to install — Python 3 standard library only.

**To change the copy of one template**, edit its `src/<category>/<name>.part` and run
`assemble.py`. A `.part` is three sections: `meta` (subject, preheader, and whether the
footer is transactional or commercial), `html` (the rows that go inside the card), and
`text` (the plain-text part).

**To change something every template shares** — a colour, the dark palette, the footer —
edit `tools/shell.html`, `tools/shell.txt` or one of the two `tools/footer-*.html` files,
then rebuild. All 38 templates pick it up at once.

**To change the demo company**, edit `tools/demo.py`. It is the only place those values
live: `examples/`, the Example column in this README, and the preview page all read from it.

`assemble.py` is also the linter. It rejects a build that breaks any invariant this README
claims — tag balance, line length, ASCII-only, no `overflow` token, no `{{`, every `<th>`
scoped, no layout table carrying a `<th>`, plain-text wrapping, whether the text part shares
its vocabulary with the HTML part, and whether the demo money adds up.

---

## Quick start

1. Copy `templates/lifecycle/welcome.html` **and** `templates/lifecycle/welcome.txt` into your project.
2. Replace every `[PLACEHOLDER]` token — **including the square brackets** — with your own
   text, or with your sending platform's merge tag. The two files use identical tokens, so the
   same substitution pass covers both.
3. Send them as the `text/html` and `text/plain` parts of one `multipart/alternative` message.

```bash
# preview locally
python3 -m http.server 8000
# then open http://localhost:8000
```

`index.html` works opened straight off the filesystem — no server needed. The **Sample data**
button swaps the iframe between `templates/` and `examples/`, so it is just a different file
path rather than anything the browser has to fetch.

---

## Examples

`examples/` holds the same 38 templates with every token filled in, so you can read one as a
finished email instead of a form. The company in them is invented:

> **Fernway** — field service software for teams that fix things. It also sells the rugged
> hardware its crews carry, which is why one fictional company can plausibly send both a
> subscription receipt and a shipping notice.
>
> The reader is **Priya Raman**, a dispatcher at **Brightpath Mechanical**, a Fernway
> customer. Sender and reader are on different domains on purpose — that is how these emails
> really work, and using one domain for both hides mistakes.

Every domain in the examples ends in `.example`, the TLD [RFC 2606](https://www.rfc-editor.org/rfc/rfc2606)
reserves for documentation. It can never be registered, so no demo link in this repository
can ever point at a live site somebody else owns.

The demo values live in [`tools/demo.py`](tools/demo.py). Change them there and run
`python3 tools/assemble.py` to refill the whole set — including the README table above and
the preview page, which read from the same file.

**Read the examples, copy the templates.** The examples are documentation; they have a
fictional company's name and postal address baked in, and sending one as-is would put
Fernway's details in front of your customers.

---

## Placeholders

Every variable is an uppercase token in square brackets. None of the platforms in the
[sending-platform table](#sending-platforms) claims `[` or `]` as a delimiter — Mailchimp uses
`*|TAG|*`, Postmark/SendGrid/SES use `{{tag}}`, Klaviyo/Customer.io/Brevo use `{{ }}` plus `{% %}`
— so the tokens pass through all of them untouched.

**One exception: Campaign Monitor.** Its personalization syntax *is* square brackets
(`[firstname,fallback=]`), and Brevo uses bracketed field names for its own default header and
footer blocks. If you send through Campaign Monitor, substitute the tokens before importing rather
than relying on them to pass through.

<!-- generated:placeholders -->
**Set once for your product.** Every template uses these.

| Placeholder | Example | Notes |
| --- | --- | --- |
| `[COMPANY_ADDRESS]` | `1100 Alder Street, Suite 210, Portland, OR 97205, USA` | **Legally required** in commercial mail — see [Compliance](#compliance). |
| `[COMPANY_LEGAL_NAME]` | `Fernway Technologies Inc.` |  |
| `[COMPANY_NAME]` | `Fernway` |  |
| `[COMPANY_URL]` | `https://fernway.example` |  |
| `[PRIVACY_URL]` | `https://fernway.example/privacy` |  |
| `[SIGNOFF_NAME]` | `Maya` |  |

**Worth reading before you fill them in.** Most tokens are named after what they
hold and need no explanation. These are the ones where the meaning is not obvious,
and where getting it wrong produces a bug rather than a typo.

| Placeholder | Example | Notes |
| --- | --- | --- |
| `[EXPIRY_ABSOLUTE]` | `14:35 UTC on 7 September 2026` | An absolute time **with a timezone**. Always paired with the relative form. |
| `[EXPIRY_RELATIVE]` | `30 minutes` | How long a link or code lasts, in words. |
| `[RETENTION_PERIOD]` | `90 days` | How long data survives after an account lapses. Not the same thing as a link expiry. |
| `[RETENTION_END_DATE]` | `20 December 2026` | The date data is deleted. Paired with the period above, and never an expiry. |
| `[SHIPPING_ADDRESS]` | `Priya Raman, Brightpath Mechanical, 1420 5th Avenue Suite 300, Seattle WA 98101` | **Renders differently in each part**: separate the lines with `<br>` in the `.html` and with real newlines in the `.txt`. Substituting one string into both breaks one of them. |
| `[AMOUNT]` | `588.00` | Render money to **two decimal places**, or the decimal column will not align. |
| `[CURRENCY]` | `USD` | Bound to the figure with `&nbsp;` so it cannot wrap onto its own line. |
| `[OTP_CODE]` | `482913` | Must stay one contiguous run of characters — see [`partials/README.md`](partials/README.md). |

The other 124 are template-specific and named after what they hold. Full list: **[PLACEHOLDERS.md](PLACEHOLDERS.md)**.
<!-- /generated:placeholders -->

Some things are deliberately **not** placeholders, because a token that goes unfilled ships as
literal `[BRACKETS]` in someone's inbox, and because a token invites the wrong value:

- **Button labels are hard-coded** ("Choose a new password", "Secure your account"). WCAG 2.4.4
  wants link text that names its destination; a `[CTA_LABEL]` token invites "Click here". Edit the
  text directly.
- **Preheader text is hard-coded.** Each template ships preview copy that reads correctly when the
  client appends the `<h1>` after it. Rewrite it, but keep that property.
- **`lang` / `dir`** (on `<html>`, on `<body>` alongside `xml:lang` for classic Outlook, and on the
  `role="article"` wrapper), the **`<title>`**, the wrapper's **`aria-label`**, and
  **`aria-roledescription="email"`** — which a screen reader announces and which should be
  translated or removed. See [Right-to-left languages](#right-to-left-languages).

---

## Suggested copy

**Subject:** `Welcome to [PRODUCT_NAME]` — 35–40 characters is the safe mobile budget, and
the subject should closely track the `<title>` (a `<title>` more than ~3.5× the length of
the subject trips SpamAssassin's `HTML_TITLE_SUBJ_DIFF`, one of its heavier HTML rules).

**From:** a real, reply-capable address. Not `no-reply@`. The body says "reply to this
email", and Microsoft's high-volume sender requirements ask for a reply-capable
`From`/`Reply-To`.

---

## How it is built

The template is a hybrid: **tables for the skeleton, inline styles for everything that
matters, and a `<style>` block for progressive enhancement only.** If you delete the
entire `<style>` block the email is still readable, still single-column, and still
legally complete. That matters, because several clients throw it away — Gmail with a
non-Google (POP/IMAP) account, Gmail mobile webmail, GMX and WEB.DE desktop webmail, SFR,
LaPoste and others ship no embedded-stylesheet support at all.

**Layout.** A `max-width: 600px` div centred with `margin: 0 auto`, wrapped in an
`<!--[if mso]>` ghost table with a fixed `width="600"`. Classic Outlook (the Word
rendering engine, still supported by Microsoft "until at least 2029") supports `max-width`
only on `<table>` and does not support `margin: auto`, so the ghost table is what keeps it
600px there. No fixed pixel width appears outside a conditional comment, because Samsung
Email copies such widths onto its own wrapper and stops being responsive.

**Spacing.** All padding is on `<td>` elements, with exactly one exception — the CTA anchor, which
carries its own padding *plus* the Outlook workaround described under **Button** below. The Word
engine supports padding only on table cells, so a padded `<div>`, `<p>` or bare `<a>` renders flush
to the edge there; that is also why the two footer links take their tap spacing from a `<td>` each
rather than from padding on the anchor. Sibling cells in one row never carry different vertical
padding, because Outlook applies the largest value to the whole row.

**Type.** `mso-line-height-rule: exactly` everywhere a line-height is set, because Word
treats `line-height` as a minimum and grows it to fit the tallest glyph. Font sizes are in
`px` (Samsung Email ignores relative and percentage sizes; classic Outlook and Yahoo
ignore `rem`). Body copy is 16px / 26px, bumped to 17px / 27px under 600px. The `role="article"`
wrapper carries `font-size: medium; font-size: max(16px, 1rem)`, which lifts the inherited base
above Apple Mail's 12px default. Note what that does and does not do: it only reaches text with no
inline `font-size`, and every text element here sets one, because Samsung Email ignores relative
sizes and classic Outlook ignores `rem`. Its real value is as a floor for content you add later and
for clients that strip inline styles.

**Button.** A single real `<a>`, styled with `display: inline-block` + padding for modern
clients, and given its Outlook padding by the `mso-font-width` / `mso-text-raise` technique
(em-space characters scaled inside a conditional comment). This keeps one anchor with one
accessible name, rather than the VML `v:roundrect` approach which duplicates the label and
pins a fixed height. It measures 48px tall (12px padding × 2 + 22px line-height + 2px border), above
the 44×44px WCAG 2.5.5 enhanced target, and stays 48px on mobile because the media query raises only
the font size. Under 600px it goes full width.

Two things to know before you change it:

- **The Outlook padding is tied to the CSS padding by arithmetic, not by the cascade.** `mso-text-raise`
  is a percentage of `font-size`, so at `font-size:16px` the 12px vertical padding is 75% — hence
  `mso-text-raise:75%` on the `<span>` and double that, `150%`, on the `<i>`. Change `padding` and you
  must recompute both, or the button silently renders a different height in the Word engine than
  everywhere else. Horizontal padding works the same way: `&emsp;` is 1em, scaled by
  `mso-font-width:200%` to the 2em (32px) side padding.
- **The button's cell sets `mso-line-height-rule: at-least`, not `exactly`.** The `exactly` value
  inherited from `<body>` is documented to distort this button's height in the Word engine.

**Preheader.** A `display:none` div, which hides it from the render *and* from the accessibility
tree, so screen readers do not read your preview sentence and then immediately read the same words
again. `font-size:0; line-height:0; max-height:0; max-width:0` ride along on the same element
because `display:none` is unsupported in Gmail *mobile webmail* (Gmail opened in a phone browser),
where the preheader would otherwise be visible body text.

There is deliberately **no invisible-character spacer run** after it. That hack — a few hundred
`&#8199;&#847;` / `&shy;` entities padding out the rest of the inbox preview line so the client
cannot scrape your `<h1>` into it — costs about 3 KB, is an arms race Apple has broken twice
(`&zwnj;&nbsp;` died in Yahoo and AOL in late 2022 and in Apple Mail 16.4; `&#65279;` was blocked in
iOS 16.6 and iOS 17), and its own maintainers note Apple appears to be trying to shut it down. The
trade-off: if `[PREHEADER]` is shorter than the client's preview line, the client fills the
remainder from the top of the body — which here is the `<h1>`. Write a preheader of 60–90 characters
that reads well followed by the headline, and you lose nothing. If you would rather have the hack,
add a second `display:none` div of `&#8199;&#847;` groups immediately after the preheader.

**Head.** Charset, viewport (zoom left enabled — locking it is a WCAG failure),
`x-apple-disable-message-reformatting`, `format-detection`, the two `color-scheme` metas,
and the Outlook `PixelsPerInch` block wrapped in `<noscript>` (without the wrapper,
T-Online prints a literal `96` at the top of the email).

### Deliberate omissions

Things commonly found in email boilerplate that are **not** here, and why:

- `<meta http-equiv="X-UA-Compatible">`, `.ExternalClass`, `.ReadMsgBody`,
  `#outlook a { padding: 0 }`, `img { -ms-interpolation-mode }`, `.im` / `.a6S` / `.aBn`,
  `.yshortcuts`, `body[data-outlook-cycle]` — all deprecated between 2016 and 2022.
- `xmlns="http://www.w3.org/1999/xhtml"` on `<html>` — a no-op under an HTML5 doctype.
- A blanket `table { table-layout: fixed !important; margin: 0 auto !important; }` — the
  first is a no-op in Outlook Windows and forced on regardless in Outlook for Mac; the
  second silently centres every nested table.
- `* { font-family: sans-serif !important }` inside `<!--[if mso]>` — Word does not resolve
  the bare `sans-serif` keyword and falls back to Times New Roman, which is the exact bug
  that block is meant to fix. Real font names are used instead.
- The Gmail mobile gutter fix (`u + #body { width: 100vw !important }`). It also matches
  Gmail desktop webmail, where `vw` measures the whole browser window rather than the
  message column, so it can blow the layout out sideways. The Cerberus alternative
  hard-codes iPhone 6-era device widths. Neither is worth it for a fluid layout.
- `light-dark()` — supported only in Apple Mail 16+/iOS 17.5+, Proton Mail iOS and Thunderbird 128, and
  *silently wrong* (stays light in dark mode) in SFR, Proton webmail, HEY, Mail.ru,
  LaPoste and T-Online.
- A VML `v:roundrect` button — see **Button** above.

---

## Dark mode

Dark mode in email is mostly done **to** your message, not **by** it. Clients fall into
three groups, and the template is built for all three:

| Behaviour | Clients | How the template handles it |
| --- | --- | --- |
| Honours `prefers-color-scheme` | Apple Mail 12.4+ on macOS and iOS 13+, Outlook for Mac, Outlook.com, new Outlook for Windows, Outlook iOS/Android, Samsung Email 6.1+, Fastmail | The `@media (prefers-color-scheme: dark)` block supplies a hand-authored dark palette. |
| Rewrites colours and records the originals | Outlook.com, new Outlook for Windows, Outlook mobile | A duplicated `[data-ogsb]` / `[data-ogsc]` block, written as descendant selectors (Outlook.com cannot match `.class[data-ogsb]`). |
| Forces its own inversion, no opt-out | Gmail iOS (full), Gmail Android (partial), classic Outlook 2021/365 Windows (full), Windows Mail (full), Yahoo desktop webmail (darkens), Thunderbird (strips colours) | The light palette is near-black on white with a large contrast margin, so it still clears 4.5:1 after a lossy inversion. |

Notes on the choices:

- **`#ffffff`, not `#fffffe`.** The off-white trick is widely recommended to dodge Apple
  Mail's auto-inversion — but Yahoo's desktop webmail turns `#fffffe` into a vivid olive
  (`#989800`), a documented and currently open bug. Because this template ships real dark
  styles, Apple Mail uses them instead of auto-inverting, so the trick buys nothing and
  costs a visible failure in Yahoo.
- **The light button is a deep blue on purpose.** Thunderbird applies a forced dark reading that
  removes fills it judges too light, and it strips `@media` blocks entirely — so Thunderbird only
  ever sees the *light* value, `#1e40af`, which is dark enough to survive. The dark-mode override
  (`#2b5cea`) is a separate choice: it is light enough to read as a button against the `#1c1c1e`
  card, where the light blue would nearly disappear.
- **The divider is a filled cell, not a `border-top`.** Outlook.com and the Outlook apps
  darken backgrounds but leave border colours alone, so a hairline border either vanishes
  or glares. A background-coloured cell stays in step with the surface.
- **The surfaces declare `color` and `background-color` together.** `<body>` and the page table
  both carry a text colour alongside their background. That is what Outlook.com keys on: it rewrites
  each property independently and substitutes its own default for whichever you left out, and it
  stamps `data-ogsc` / `data-ogsb` on the element it rewrote. Because those hooks only work as
  *descendant* selectors, the rules would match nothing if no ancestor declared a colour.
- **Inline `!important` is avoided** — classic Outlook ignores it inline, Gmail only honours
  it in lowercase, and several clients drop the whole declaration if there is no space
  before it. Every `!important` in this file is lowercase, spaced, and in the `<style>`
  block.

Three client caveats worth knowing before you ship:

- **Gmail with a non-Google POP/IMAP account** drops inline `text-decoration` as well as the whole
  `<style>` block, so the wordmark and the CTA label pick up the default link underline there. Links
  stay underlined, so the contrast-plus-underline requirement is unaffected.
- **T-Online desktop webmail renders the contents of conditional comments as live HTML.** The ghost
  table is balanced and the button's `<i>` spacers carry `hidden`, so both survive; the
  `<!--[if mso]>` font block deliberately omits `!important` so that if it leaks it cannot beat the
  inline font stacks. The `PixelsPerInch` block is wrapped in `<noscript>` for the same reason —
  without it T-Online prints a literal `96` at the top of the email.
- **Yahoo and AOL support no `word-break` on any platform.** The copy-and-paste fallback line uses
  `word-break: break-all`, which works everywhere else; a very long tracked `[CTA_URL]` can still
  push the layout wide there. Keep that URL short, or drop the fallback line.

Measured contrast, both palettes:

| | Light | Dark |
| --- | --- | --- |
| Body text | `#1a1a1a` on `#ffffff` — **17.4:1** | `#ededed` on `#1c1c1e` — **14.5:1** |
| Secondary (in card) | `#4a4a4a` on `#ffffff` — **8.9:1** | `#b3b3b3` on `#1c1c1e` — **8.1:1** |
| Footer (on page bg) | `#4a4a4a` on `#f4f4f5` — **8.1:1** | `#b3b3b3` on `#111111` — **9.0:1** |
| Link | `#1e40af` on `#ffffff` — **8.7:1** | `#8ab4f8` on `#1c1c1e` — **8.1:1** |
| Button label | `#ffffff` on `#1e40af` — **8.7:1** | `#ffffff` on `#2b5cea` — **5.5:1** |

All pass WCAG AA; all but the dark button label pass AAA. Inline links are underlined,
because the link colour alone is only 2.0:1 against the body text — below the 3:1 that
WCAG technique G183 requires when colour is the sole differentiator.

---

## Compliance

A "thanks for signing up" email is legally **commercial** the moment it carries an upgrade
prompt, a product tour or a discount — CAN-SPAM classifies per message, on the primary
purpose a reasonable reader would take from the subject line. The FTC fined Experian
$650,000 in 2023 for exactly this pattern: mail labelled as account information that
actually pitched paid products, with no opt-out. The footer here therefore ships the full
set:

- **Permission reminder** — what they did, when, and with which address.
- **Sender identification** — the legal entity name.
- **A physical postal address**, as live text (15 U.S.C. §7704(a)(5)(A)(iii)). Not an
  image, not a URL, not an email address.
- **A visible unsubscribe link** (§7704(a)(5)(A)(ii)). Gmail and Yahoo each separately
  require a clearly visible unsubscribe link *in the message body*, in addition to the
  one-click header.
- **A privacy policy link** — GDPR Art. 13 requires the controller's identity and contact
  details, and Art. 7(3) the right to withdraw consent.

Not included, because it is not required when the recipient gave prior affirmative consent
(§7704(a)(5)(B)): an "this is an advertisement" label.

If you send to **Canada**, CASL/SOR-2012-36 s.2(1) also requires a *second* contact channel
alongside the mailing address — a phone number reaching a person or voicemail, an email
address, or a web address — plus an "on behalf of" statement where applicable. Add it to
the `[COMPANY_ADDRESS]` block.

Endpoint lifetimes: CAN-SPAM requires the unsubscribe mechanism to work for at least 30
days after send, CASL s.11(2) for at least 60. Build for 60, and honour requests within 10
business days. Never put it behind a login.

---

## What you still have to do

These are properties of your **sending system**, not of an HTML file. The templates are built to
support them; they cannot provide them.

| | Why the HTML cannot do it |
| --- | --- |
| `List-Unsubscribe` and `List-Unsubscribe-Post` headers (RFC 8058) | They are message headers, outside the HTML document. The `List-Unsubscribe` field must contain one HTTPS URI, both headers must be covered by the DKIM signature and listed in its `h=` tag, and the endpoint must accept a POST body of `List-Unsubscribe=One-Click` without answering with a redirect. Required by Gmail for senders above 5,000 messages/day. Use the same URL as `[UNSUBSCRIBE_URL]`. |
| Rendering an address into both parts | `[SHIPPING_ADDRESS]` and `[BILLING_ADDRESS]` need `<br>` between the lines in the `.html` and real newlines in the `.txt`. Substituting one string into both breaks whichever part it was not written for. Every other placeholder is a plain string that works in both. |
| Assembling the two parts into one message | The `.txt` sibling is shipped, but something has to put the HTML and text parts into a single `multipart/alternative` message with the right headers. That is your sending library or ESP, not this repo. |
| SPF, DKIM, DMARC, TLS, a valid `Message-ID` | Sender-side configuration. Google asks bulk senders to keep the Postmaster Tools spam rate below 0.10% and states it must never reach 0.30% — 0.10% is the target, 0.30% is the hard ceiling. |
| Staying under Gmail's clipping threshold | Gmail clips at ~102 KB of *final* message size and hides everything past the cut — typically your footer, with the address and unsubscribe link — behind "View entire message". The template is ~10.5 KB; budget the rest for your merge values and your platform's click-tracking rewrites (roughly the original URL length + 60–90 bytes per tracked link). Measure after substitution, not on the source file. |

---

## Right-to-left languages

Ship an RTL build as a **separate file**, not as one file that adapts. Do not use CSS
logical properties (`padding-inline-start` and friends) — support in email is poor. All
horizontal padding in this template is already symmetric, so an RTL variant only needs
`dir="rtl"` plus an inline `direction: rtl` on `<html>`, `<body>`, the `role="article"`
wrapper and every block-level text container. Note that Orange webmail strips `dir` from
`<table>` and `<td>` specifically, so put it on a `<div>` or `<p>` inside the cell, and
raise `line-height` to about 1.7–1.8 for Arabic, Urdu and Hebrew.

---

## Sending platforms

Behaviour differs enough that it is worth checking before you paste.

| Platform | Inlines your CSS? | Injects its own footer? | Native unsubscribe tag | Import path |
| --- | --- | --- | --- | --- |
| **Mailchimp** | Opt-in, at send time. *Settings → Automatic CSS Inliner* | Yes, if `*\|UNSUB\|*` is missing | `*\|UNSUB\|*` (href), `*\|LIST:ADDRESS\|*` | **Legacy** builder → *Code your own → Paste in code*. The new builder's Code block silently cleans markup. |
| **Postmark** | Yes, by default. `InlineCss: false` per API send | Appends its own link on Broadcast streams if missing | `{{{ pm:unsubscribe }}}` (triple braces), in HTML **and** text | Template body. Its inliner *overwrites* matching inline styles. |
| **SendGrid** | No inliner documented | No | Subscription Tracking replacement tag, or `<%asm_group_unsubscribe_raw_url%>` | **Code Editor** only — the choice is one-way per template. You can set the replacement tag to `[UNSUBSCRIBE_URL]` verbatim, giving a zero-edit path. |
| **Klaviyo** | — | — | `{% unsubscribe_link %}` inside an `href` | `.html` import. Rewrites markup it does not recognise; avoid `~` combinators and single quotes in font stacks. |
| **Customer.io** | Yes, on by default | — | `{% unsubscribe_url %}` | Code editor. Mark blocks `<style data-embed>` to skip inlining. |
| **Brevo** | — | Unsubscribe link cannot be removed | `{{ unsubscribe }}` | HTML editor. Hard 1 MB HTML limit. |
| **Amazon SES** | No processing at all | No | `{{amazonSESUnsubscribeUrl}}` (needs `ListManagementOptions`) | Raw MIME or stored template. Prefer `quoted-printable` or `base64` over `8bit` on the raw-send path. |

Two rules that apply everywhere:

- **Replace the whole token, brackets included.** Never paste a merge tag *inside* the
  brackets — `[*|FNAME|*]` breaks on Mailchimp.
- **Never export from a drag-and-drop editor and re-import.** Conditional comments do not
  survive a WYSIWYG round trip on any platform in the table.

---

## Testing

### What has been verified

| Check | Method | Result |
| --- | --- | --- |
| Tag balance, no `{{`/`}}`, no `->` inside comments, no trailing whitespace, no non-ASCII bytes, `!important` spacing and case | Script over the source file | Pass |
| RFC 5322 line length | Longest source line measured | 594 bytes — under the 998 hard limit, and under the 800-byte working target |
| Both palettes actually render as intended | Headless Chrome, computed styles dumped with the dark block forced on, then with the mobile block forced on | Pass |
| Contrast, both palettes | WCAG relative-luminance calculation | See the table under [Dark mode](#dark-mode) |
| Live body text | Tags and hidden blocks stripped, characters counted | 732 characters, above the ~500 below which filters start reacting |
| File size | `wc -c` | 10.5 KB raw; `<style>` block 2.4 KB, well under Gmail's 16 KB cap |
| Markup validity | W3C Nu checker, run on every template | Errors only in the three unavoidable categories below. **Zero unexpected errors across all 38.** |
| One shared shell | Compared the `<style>` block of all 38 templates | **1 distinct block.** This is what the generator exists to guarantee |
| Layout vs data tables | Scanned every table in every template | 0 layout tables containing `<th>`; 0 `<th>` without `scope` |
| Footer class matches the markup | Compared each template's declared legal class against whether it renders an unsubscribe link | Consistent in all 38 |
| Component drift | Compared every inline style per component class across the library | `btn`, `ghost`, `code`, `panel-text`: **one variant each**. The three `th` variants are the canonical 60/15/25 column widths, not drift |

The headless-Chrome pass proves the CSS cascade resolves the way the design intends: with the dark
block forced on, the footer, the links and the button all take their dark values; with the mobile
block forced on, the button becomes full-width and body copy steps up to 17px.

### How to test it yourself, for free

- **[SpamRate](https://spamrate.is) — where the message lands.** Everything else on this list
  checks how an email *renders*. This checks whether it reaches an inbox at all: send a test
  to the addresses it gives you and see the placement at Gmail, Outlook, Yahoo, Zoho and AOL
  in real mailboxes, plus SPF, DKIM, DMARC and blacklist checks on the sending domain.
  [Free deliverability test](https://spamrate.is/email-deliverability-test); plans start at $0.
- **[Parcel](https://parcel.io) Community ($0)** — email-specific HTML checking,
  accessibility testing, dark-mode viewing, and test sends to 5 recipients.
- **[Mailtrap Email Testing](https://mailtrap.io) free tier** — MIME inspection, per-client
  CSS support scoring and a spam score. Not real-client screenshots.
- **[mail-tester.com](https://www.mail-tester.com)** — 3 free tests per 24 hours. Ignore the
  SPF/DKIM/IP-reputation half of the report; it grades *you*, not the template.
- **[W3C Nu HTML Checker](https://validator.w3.org/nu/)** — tolerates conditional comments, ghost
  tables and VML. The presentational attributes email requires (`cellpadding`, `cellspacing`,
  `border`, `width`, `align`, `bgcolor`) come back as warnings, not errors, and are unavoidable.
  This file currently reports **30 errors, all expected**, in exactly three categories:

  | Count | Error | Why it stays |
  | --- | --- | --- |
  | 22 | `Property "mso-…" doesn't exist`, plus `text-underline-color` | Proprietary properties the Word engine and Windows Mail need. No CSS parser will ever accept them. |
  | 6 | `Illegal character in path segment` on `[PLACEHOLDER]` hrefs | Inherent to shipping a template. They disappear the moment you substitute real URLs. |
  | 2 | `Attribute "xmlns:v" / "xmlns:o" not allowed here` | Kept on `<html>` because that is where every field-proven implementation puts them. You can move them onto the VML/Office elements inside the conditional comments if a clean validation run matters more to you. |

  So gate CI on the *count and category* of errors, not on zero. A useful rule: fail if any error
  falls outside those three buckets.
- **Real clients you already have** — free accounts at Gmail, Outlook.com, Yahoo and AOL
  with their iOS/Android apps; Thunderbird (free, all platforms); Apple Mail on your own
  hardware. For classic Word-engine Outlook, the Microsoft Evaluation Center ships a 90-day
  Windows 11 Enterprise ISO in x64 *and* Arm64, so it boots in UTM on Apple Silicon — and
  new Outlook for Windows comes with it, giving you both rendering engines from one image.
- **Gmail "Show original"** (More → Show original) is the canonical free way to see exactly
  what arrived, headers included.

Do not test only the light palette, and do not sign off on one testing platform's Outlook
365 screenshots — different Microsoft 365 builds run different dark-mode algorithms.

---

## Roadmap

The library is being built out to cover the transactional email that Shopify, WooCommerce, Stripe,
Auth0 and Supabase actually send by default. An inventory of 216 emails across 12 families informed
the order below; 79 of them are "universal" — sent by nearly every team in the segment.

| Wave | Contents | Status |
| --- | --- | --- |
| **Components** | The 10 markup primitives | ✅ [shipped](partials/components.html) |
| **Welcome** | Welcome / thanks for signing up | ✅ shipped |
| **1. Account & security** | Email verification · password reset · password changed · one-time code · new-device sign-in · magic link · email change (the pair sent to the old **and** new address) · account locked | ✅ shipped, 9 templates |
| **2. Billing & dunning** | Receipt / invoice · payment failed ×3 · card expiring · trial ending · renewal reminder · subscription cancelled | ✅ shipped, 8 templates |
| **3. Orders** | Order confirmation · shipped with tracking · delivered · cancelled · refund · return label | ✅ shipped, 6 templates |
| **4. Lifecycle** | Team invitation · digest · re-engagement · feature announcement · collaboration notification | ✅ shipped, 5 templates |
| **5. Operational** | Incident opened · incident resolved · scheduled maintenance · quota exceeded | ✅ shipped, 4 templates |
| **6. Consent & legal** | Double opt-in · unsubscribe confirmation · terms change · data-breach notice · DSAR acknowledgement | ✅ shipped, 5 templates |

All six waves are shipped: **38 templates**, each with a hand-written plain-text sibling.

Two structural notes that shape the files:

- **Legal class is a visible axis, not an afterthought.** Transactional mail (password reset, receipt,
  shipping notice) needs neither an unsubscribe link nor a postal address; commercial mail (digest,
  re-engagement, feature announcement) needs both. Getting it wrong is costly in either direction —
  attaching an unsubscribe to a password reset can suppress account-critical mail. Every template
  states its class and ships the matching footer.
- **Some of these are sequences, not single messages.** Dunning is 3–4 escalating messages; an email
  change sends to two addresses; an incident opens and later resolves. Those ship as a set, because
  half a sequence is worse than none.

### Out of scope, deliberately

Eight of the 216 emails need product photography to do their job: abandoned cart, abandoned browse,
abandoned checkout, post-purchase cross-sell, wishlist reminder, new arrivals, price drop and
back-in-stock. A text-only library serves those badly, so it says so rather than shipping a
degraded version. The rest of the post-purchase cycle — which Shopify ships as roughly 40 emails and
free libraries collectively cover four of — is fully in scope.

---

## Contributing

Issues and pull requests are welcome. If you are reporting a rendering bug, please say
which client, which version, which platform and which account type — "Outlook" and "Gmail"
each cover several materially different rendering engines, and the Gmail apps behave
differently again when the account is a non-Google POP/IMAP one.

## Licence

MIT — see [LICENSE](LICENSE). Copy it, sell it, ship it, no attribution required.

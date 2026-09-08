"""
The demo data set. One fictional company, used everywhere: the filled-in copies in
examples/, the Example column of the README placeholder table, and the "Sample data"
button in the local preview.

Keeping it in one file is the point. When it lived in two places the two drifted within
a single afternoon, and fourteen placeholders silently lost their preview values.

    Fernway - field service software for teams that fix things.
    It also sells the rugged hardware its crews carry, which is why one fictional
    company can plausibly send both a subscription receipt and a shipping notice.

Every domain is under .example, the TLD RFC 2606 reserves for documentation. It can
never be registered, so no demo link in this repository can ever point at a live site
that someone else owns.

The recipient is a customer at a different company (brightpath.example) because that is
how these emails really work: the sender and the reader are not on the same domain, and
using one domain for both hides mistakes.
"""

# Values used in both the .html and the .txt copies.
VALUES = {
    # --- the sender: Fernway ---
    '[PRODUCT_NAME]': 'Fernway',
    '[COMPANY_NAME]': 'Fernway',
    '[COMPANY_LEGAL_NAME]': 'Fernway Technologies Inc.',
    '[COMPANY_URL]': 'https://fernway.example',
    '[COMPANY_ADDRESS]': '1100 Alder Street, Suite 210, Portland, OR 97205, USA',
    '[SUPPORT_EMAIL]': 'support@fernway.example',
    '[SIGNOFF_NAME]': 'Maya',
    '[PRIVACY_URL]': 'https://fernway.example/privacy',
    '[TERMS_URL]': 'https://fernway.example/terms',
    '[STATUS_PAGE_URL]': 'https://status.fernway.example',
    '[UNSUBSCRIBE_URL]': 'https://fernway.example/u/6b41f0a9',

    # --- the reader: a customer at another company ---
    '[FIRST_NAME]': 'Priya',
    '[EMAIL_ADDRESS]': 'priya@brightpath.example',
    '[OLD_EMAIL_ADDRESS]': 'priya@brightpath.example',
    '[NEW_EMAIL_ADDRESS]': 'priya.raman@brightpath.example',
    '[SIGNUP_DATE]': '7 September 2026',
    '[TEAM_NAME]': 'Brightpath Mechanical',
    '[ROLE_NAME]': 'Dispatcher',
    '[INVITER_NAME]': 'Marcus Lee',
    '[INVITER_EMAIL]': 'marcus@brightpath.example',
    '[ACTOR_NAME]': 'Marcus Lee',

    # --- generic actions ---
    '[CTA_URL]': 'https://fernway.example/a/9f2a1c7e',
    '[SECONDARY_URL]': 'https://fernway.example/settings/security',
    '[CTA_LABEL]': 'Finish setting up',
    '[SECONDARY_LABEL]': 'Track shipment',

    # --- account and security ---
    '[OTP_CODE]': '482913',
    '[EXPIRY_ABSOLUTE]': '14:35 UTC on 7 September 2026',
    '[EXPIRY_RELATIVE]': '30 minutes',
    '[EVENT_TIME]': '14:05 UTC on 7 September 2026',
    '[EVENT_DEVICE]': 'Chrome on macOS',
    '[EVENT_LOCATION]': 'Portland, Oregon, United States',
    '[EVENT_IP]': '203.0.113.42',
    '[LOCK_REASON]': 'Too many failed sign-in attempts',

    # --- billing ---
    '[PLAN_NAME]': 'Crew',
    '[SEAT_COUNT]': '12',
    '[CURRENCY]': 'USD',
    '[AMOUNT]': '588.00',
    '[SUBTOTAL]': '588.00',
    '[TAX]': '60.27',
    '[TOTAL]': '648.27',
    '[SHIPPING]': '0.00',
    '[INVOICE_NUMBER]': 'FW-2026-04417',
    '[INVOICE_DATE]': '7 September 2026',
    '[BILLING_PERIOD]': '7 Sep - 7 Oct 2026',
    '[PAYMENT_METHOD]': 'Visa ending 4242',
    '[CARD_BRAND]': 'Visa',
    '[CARD_LAST4]': '4242',
    '[CARD_EXPIRY]': '10/2026',
    '[NEXT_CHARGE_DATE]': '7 October 2026',
    '[RETRY_DATE]': '10 September 2026',
    '[GRACE_END_DATE]': '21 September 2026',
    '[TRIAL_END_DATE]': '14 September 2026',
    '[RETENTION_PERIOD]': '90 days',
    '[RETENTION_END_DATE]': '20 December 2026',

    # --- orders: Fernway also ships the hardware its crews carry ---
    '[ORDER_NUMBER]': 'FW-10023',
    '[ORDER_DATE]': '7 September 2026',
    '[ORDER_URL]': 'https://fernway.example/orders/10023',
    '[ITEM_1_NAME]': 'Fernway RT-2 rugged scanner',
    '[ITEM_1_VARIANT]': 'Standard grip / 2-year warranty',
    '[ITEM_1_QTY]': '2',
    '[ITEM_1_AMOUNT]': '498.00',
    '[ITEM_2_NAME]': 'RT-2 vehicle charging dock',
    '[ITEM_2_VARIANT]': '12V, hardwired',
    '[ITEM_2_QTY]': '2',
    '[ITEM_2_AMOUNT]': '90.00',
    '[SHIPPING_ADDRESS]': 'Priya Raman, Brightpath Mechanical, 1420 5th Avenue Suite 300, Seattle WA 98101',
    '[BILLING_ADDRESS]': 'Brightpath Mechanical, PO Box 1184, Seattle WA 98111',
    '[CARRIER]': 'UPS',
    '[TRACKING_NUMBER]': '1Z999AA10123456784',
    '[TRACKING_URL]': 'https://fernway.example/track/1Z999AA10123456784',
    '[DELIVERY_ESTIMATE]': '11-13 September 2026',
    '[DELIVERY_GRACE]': '15 September 2026',
    '[DELIVERED_TIME]': '10:42 on 11 September 2026',
    '[CHANGE_DEADLINE]': '18:00 UTC on 8 September 2026',
    '[CANCEL_REASON]': 'The vehicle charging dock is out of stock',
    '[REFUND_AMOUNT]': '648.27',
    '[REFUND_METHOD]': 'Visa ending 4242',
    '[REFUND_DAYS]': '5 to 10 business days',
    '[RETURN_DEADLINE]': '5 October 2026',
    '[RETURN_URL]': 'https://fernway.example/returns/10023/label.pdf',

    # --- lifecycle ---
    '[PERIOD_LABEL]': 'September',
    '[ITEM_1_TITLE]': 'Marcus reassigned the Kensington boiler job to you',
    '[ITEM_1_SUMMARY]': 'It moved from Thursday to Tuesday morning.',
    '[ITEM_1_URL]': 'https://fernway.example/jobs/8841',
    '[ITEM_2_TITLE]': 'Three jobs closed without a signature this week',
    '[ITEM_2_SUMMARY]': 'They need a signature before they can be invoiced.',
    '[ITEM_2_URL]': 'https://fernway.example/reports/unsigned',
    '[ITEM_3_TITLE]': 'The Q4 parts price list is ready to review',
    '[ITEM_3_SUMMARY]': 'Eleven items changed; the rest are unchanged.',
    '[ITEM_3_URL]': 'https://fernway.example/parts/q4-pricing',
    '[ALL_ITEMS_URL]': 'https://fernway.example/activity',
    '[METRIC_1_LABEL]': 'Jobs completed',
    '[METRIC_1_VALUE]': '214',
    '[METRIC_2_LABEL]': 'First-visit fixes',
    '[METRIC_2_VALUE]': '86%',
    '[METRIC_3_LABEL]': 'Crew members active',
    '[METRIC_3_VALUE]': '12',
    '[FEATURE_NAME]': 'Saved routes',
    '[FEATURE_SUMMARY]': 'A run of jobs you order once and reuse every week.',
    '[FEATURE_REPLACES]': 'rebuilding the same route every Monday morning',
    '[FEATURE_USE_1]': 'Keep a standing route for each crew and swap jobs in and out',
    '[FEATURE_USE_2]': 'Hand a route to a stand-in without explaining the order',
    '[FEATURE_USE_3]': 'Reuse last week without setting it up again',
    '[LAST_ACTIVE_DATE]': '3 May 2026',
    '[OBJECT_NAME]': 'the Kensington boiler job',
    '[COMMENT_EXCERPT]': 'Access is through the loading bay, not the front desk. The key is with building security.',
    '[ITEM_TITLE]': 'Marcus reassigned the Kensington boiler job to you',
    '[ITEM_SUMMARY]': 'It moved from Thursday to Tuesday morning.',
    '[ITEM_URL]': 'https://fernway.example/jobs/8841',
    '[LIST_ITEM_1]': 'Add the crew who will be on site',
    '[LIST_ITEM_2]': 'Set the arrival window',
    '[LIST_ITEM_3]': 'Attach the site access notes',
    '[CALLOUT_TEXT]': 'We will never ask you for this code by phone or email.',

    # --- operational ---
    '[INCIDENT_STATUS]': 'Investigating',
    '[AFFECTED_SCOPE]': 'Job dispatch and the mobile app',
    '[NEXT_UPDATE_TIME]': '15:30 UTC on 7 September 2026',
    '[WORKAROUND_TEXT]': 'There is no workaround. Jobs already downloaded to a device still open offline.',
    '[RESOLVED_TIME]': '15:12 UTC on 7 September 2026',
    '[INCIDENT_DURATION]': '1 hour 7 minutes',
    '[INCIDENT_CAUSE]': 'A configuration change removed a database connection limit, and the pool ran out.',
    '[MAINTENANCE_START]': '02:00 UTC on 14 September 2026',
    '[MAINTENANCE_END]': '04:00 UTC on 14 September 2026',
    '[MAINTENANCE_DURATION]': 'up to 2 hours',
    '[QUOTA_NAME]': 'API requests',
    '[QUOTA_USED]': '512,400',
    '[QUOTA_LIMIT]': '500,000',
    '[QUOTA_CONSEQUENCE]': 'Further requests return a 429 until the period resets',
    '[QUOTA_STOPPED]': 'New API requests and scheduled exports',
    '[QUOTA_UNAFFECTED]': 'The web app, the mobile app, and everything already stored',
    '[QUOTA_RESET_DATE]': '1 October 2026',

    # --- consent and legal ---
    '[LIST_NAME]': 'the Fernway product newsletter',
    '[SEND_FREQUENCY]': 'about twice a month',
    '[UNSUB_PROCESSING_PERIOD]': '48 hours',
    '[CHANGE_SUMMARY]': 'how long we keep job records, and who we name as sub-processors',
    '[EFFECTIVE_DATE]': '15 October 2026',
    '[INCIDENT_DATE]': '2 September 2026',
    '[INCIDENT_DISCOVERED]': '5 September 2026',
    '[INCIDENT_CONTAINED]': '5 September 2026',
    '[INCIDENT_SUMMARY]': 'An unauthorised party accessed a database backup held by one of our suppliers.',
    '[DATA_CATEGORIES]': 'Name, work email address, and hashed password',
    '[DATA_NOT_INVOLVED]': 'Payment card numbers, bank details, and customer site addresses',
    '[BREACH_INFO_URL]': 'https://fernway.example/security/2026-09',
    '[REQUEST_TYPE]': 'A copy of your personal data',
    '[REQUEST_REFERENCE]': 'DSAR-2026-0431',
    '[RESPONSE_DUE_DATE]': '7 October 2026',
}

# Values that need markup in an .html file but plain text in a .txt file.
# An address is the only case: <br> between the lines in HTML, real newlines in text.
HTML_VALUES = {
    '[SHIPPING_ADDRESS]': ('Priya Raman<br>Brightpath Mechanical<br>'
                           '1420 5th Avenue, Suite 300<br>Seattle, WA 98101<br>United States'),
    '[BILLING_ADDRESS]': ('Brightpath Mechanical<br>PO Box 1184<br>'
                          'Seattle, WA 98111<br>United States'),
}

TEXT_VALUES = {
    '[SHIPPING_ADDRESS]': ('Priya Raman\nBrightpath Mechanical\n'
                           '1420 5th Avenue, Suite 300\nSeattle, WA 98101\nUnited States'),
    '[BILLING_ADDRESS]': ('Brightpath Mechanical\nPO Box 1184\n'
                          'Seattle, WA 98111\nUnited States'),
}


def for_html():
    """Demo values for an .html file."""
    v = dict(VALUES)
    v.update(HTML_VALUES)
    return v


def for_text():
    """Demo values for a .txt file."""
    v = dict(VALUES)
    v.update(TEXT_VALUES)
    return v


def substitute(content, values):
    for token, value in values.items():
        content = content.replace(token, value)
    return content


import re
import textwrap

TXT_WRAP = 72
# "Status: Investigating" — a short label, a colon, then a value. These are how a data
# table renders in the text part, and they are one row per line by design.
LABEL_LINE = re.compile(r'^[A-Z][A-Za-z /-]{0,24}: \S')


def rewrap_text(text):
    """Re-flow the plain-text part after substitution.

    The sources are hard-wrapped at 72 columns around the [TOKENS]; once a token expands
    to a real value the paragraph no longer fits, so the demo copies have to be re-flowed
    or they read ragged. Nothing here is a correctness fix — every line was already far
    inside the 998-byte RFC 5322 limit — it is a legibility one.

    Two kinds of block are left exactly as they are:
      - anything containing a URL, because a wrapped URL stops being clickable
      - a run of two or more "Label: value" lines, because that is a table, not a
        paragraph, and joining it would merge the rows into prose
    """
    out = []
    for block in re.split(r'\n\s*\n', text):
        lines = block.split('\n')
        if any(l.lstrip().startswith('http') for l in lines):
            out.append(block)
            continue
        if len(lines) >= 2 and sum(bool(LABEL_LINE.match(l)) for l in lines) >= 2:
            out.append(block)
            continue
        # Only re-flow a block that actually overflowed. If every line still fits, the
        # author's line breaks were deliberate and joining them would be a corruption:
        # the footer's legal name and postal address are two lines that both fit, and
        # merging them produces "Fernway Technologies Inc. 1100 Alder Street".
        if all(len(l) <= TXT_WRAP for l in lines):
            out.append(block)
            continue
        joined = ' '.join(l.strip() for l in lines if l.strip())
        if not joined:
            out.append(block)
            continue
        out.append('\n'.join(textwrap.wrap(
            joined, TXT_WRAP, break_long_words=False, break_on_hyphens=False)))
    return '\n\n'.join(out)


def check_arithmetic():
    """The demo money has to add up.

    A receipt whose totals do not reconcile is the one demo mistake a reader is certain
    to spot, because checking the arithmetic is the whole reason that email exists. It is
    easy to get wrong here because two different documents share the same money tokens:
    billing/receipt has one plan line and no shipping row, orders/order-confirmation has
    two item lines and a shipping row, and both read [SUBTOTAL], [TAX] and [TOTAL].
    """
    from decimal import Decimal

    def n(token):
        return Decimal(VALUES['[' + token + ']'])

    problems = []
    if n('AMOUNT') != n('SUBTOTAL'):
        problems.append(f"demo: billing/receipt shows one line of [AMOUNT] {n('AMOUNT')} "
                        f"but a subtotal of {n('SUBTOTAL')}")
    if n('SUBTOTAL') + n('TAX') != n('TOTAL'):
        problems.append(f"demo: billing/receipt totals do not reconcile — "
                        f"{n('SUBTOTAL')} + {n('TAX')} != {n('TOTAL')}")
    if n('ITEM_1_AMOUNT') + n('ITEM_2_AMOUNT') != n('SUBTOTAL'):
        problems.append(f"demo: order line items {n('ITEM_1_AMOUNT')} + {n('ITEM_2_AMOUNT')} "
                        f"!= subtotal {n('SUBTOTAL')}")
    if n('SUBTOTAL') + n('SHIPPING') + n('TAX') != n('TOTAL'):
        problems.append(f"demo: order totals do not reconcile — {n('SUBTOTAL')} + "
                        f"{n('SHIPPING')} + {n('TAX')} != {n('TOTAL')}")
    if n('REFUND_AMOUNT') != n('TOTAL'):
        problems.append(f"demo: a full refund of {n('REFUND_AMOUNT')} does not match the "
                        f"order total {n('TOTAL')}")
    for token in ('AMOUNT', 'SUBTOTAL', 'TAX', 'TOTAL', 'SHIPPING',
                  'ITEM_1_AMOUNT', 'ITEM_2_AMOUNT', 'REFUND_AMOUNT'):
        value = VALUES['[' + token + ']']
        if not re.fullmatch(r'\d+\.\d\d', value):
            problems.append(f'demo: [{token}] is "{value}" — money needs exactly two decimals '
                            f'or the right-aligned column will not line up')
    return problems

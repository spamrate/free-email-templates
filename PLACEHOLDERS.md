# Placeholder reference

Every token in every template. You almost certainly do not need this page — open the
template you are using and the tokens are right there, in `[UPPERCASE]`. This is for
looking one up, or for wiring the whole set into a sending platform at once.

The [README](README.md) covers the handful that are shared across all templates and the
handful whose meaning is easy to get wrong.

---

## By template

What one template needs, which is usually the question you actually have.

**[`account/account-locked`](templates/account/account-locked.html)**

`[COMPANY_ADDRESS]` `[COMPANY_LEGAL_NAME]` `[COMPANY_NAME]` `[COMPANY_URL]` `[CTA_URL]` `[EMAIL_ADDRESS]` `[EVENT_TIME]` `[EXPIRY_ABSOLUTE]` `[EXPIRY_RELATIVE]` `[LOCK_REASON]` `[PRIVACY_URL]` `[PRODUCT_NAME]` `[SIGNOFF_NAME]` `[SUPPORT_EMAIL]`

**[`account/email-change-new`](templates/account/email-change-new.html)**

`[COMPANY_ADDRESS]` `[COMPANY_LEGAL_NAME]` `[COMPANY_NAME]` `[COMPANY_URL]` `[CTA_URL]` `[EXPIRY_ABSOLUTE]` `[EXPIRY_RELATIVE]` `[NEW_EMAIL_ADDRESS]` `[OLD_EMAIL_ADDRESS]` `[PRIVACY_URL]` `[PRODUCT_NAME]` `[SIGNOFF_NAME]` `[SUPPORT_EMAIL]`

**[`account/email-change-old`](templates/account/email-change-old.html)**

`[COMPANY_ADDRESS]` `[COMPANY_LEGAL_NAME]` `[COMPANY_NAME]` `[COMPANY_URL]` `[EVENT_TIME]` `[EXPIRY_ABSOLUTE]` `[EXPIRY_RELATIVE]` `[NEW_EMAIL_ADDRESS]` `[OLD_EMAIL_ADDRESS]` `[PRIVACY_URL]` `[PRODUCT_NAME]` `[SECONDARY_URL]` `[SIGNOFF_NAME]` `[SUPPORT_EMAIL]`

**[`account/magic-link`](templates/account/magic-link.html)**

`[COMPANY_ADDRESS]` `[COMPANY_LEGAL_NAME]` `[COMPANY_NAME]` `[COMPANY_URL]` `[CTA_URL]` `[EMAIL_ADDRESS]` `[EXPIRY_ABSOLUTE]` `[EXPIRY_RELATIVE]` `[PRIVACY_URL]` `[PRODUCT_NAME]` `[SIGNOFF_NAME]` `[SUPPORT_EMAIL]`

**[`account/new-device-signin`](templates/account/new-device-signin.html)**

`[COMPANY_ADDRESS]` `[COMPANY_LEGAL_NAME]` `[COMPANY_NAME]` `[COMPANY_URL]` `[EMAIL_ADDRESS]` `[EVENT_DEVICE]` `[EVENT_IP]` `[EVENT_LOCATION]` `[EVENT_TIME]` `[PRIVACY_URL]` `[PRODUCT_NAME]` `[SECONDARY_URL]` `[SIGNOFF_NAME]` `[SUPPORT_EMAIL]`

**[`account/otp-code`](templates/account/otp-code.html)**

`[COMPANY_ADDRESS]` `[COMPANY_LEGAL_NAME]` `[COMPANY_NAME]` `[COMPANY_URL]` `[EMAIL_ADDRESS]` `[EXPIRY_ABSOLUTE]` `[EXPIRY_RELATIVE]` `[OTP_CODE]` `[PRIVACY_URL]` `[PRODUCT_NAME]` `[SIGNOFF_NAME]` `[SUPPORT_EMAIL]`

**[`account/password-changed`](templates/account/password-changed.html)**

`[COMPANY_ADDRESS]` `[COMPANY_LEGAL_NAME]` `[COMPANY_NAME]` `[COMPANY_URL]` `[EMAIL_ADDRESS]` `[EVENT_LOCATION]` `[EVENT_TIME]` `[PRIVACY_URL]` `[PRODUCT_NAME]` `[SECONDARY_URL]` `[SIGNOFF_NAME]` `[SUPPORT_EMAIL]`

**[`account/password-reset`](templates/account/password-reset.html)**

`[COMPANY_ADDRESS]` `[COMPANY_LEGAL_NAME]` `[COMPANY_NAME]` `[COMPANY_URL]` `[CTA_URL]` `[EMAIL_ADDRESS]` `[EXPIRY_ABSOLUTE]` `[EXPIRY_RELATIVE]` `[PRIVACY_URL]` `[PRODUCT_NAME]` `[SIGNOFF_NAME]` `[SUPPORT_EMAIL]`

**[`account/verify-email`](templates/account/verify-email.html)**

`[COMPANY_ADDRESS]` `[COMPANY_LEGAL_NAME]` `[COMPANY_NAME]` `[COMPANY_URL]` `[CTA_URL]` `[EMAIL_ADDRESS]` `[EXPIRY_ABSOLUTE]` `[EXPIRY_RELATIVE]` `[PRIVACY_URL]` `[PRODUCT_NAME]` `[SIGNOFF_NAME]` `[SUPPORT_EMAIL]`

**[`billing/card-expiring`](templates/billing/card-expiring.html)**

`[AMOUNT]` `[CARD_BRAND]` `[CARD_EXPIRY]` `[CARD_LAST4]` `[COMPANY_ADDRESS]` `[COMPANY_LEGAL_NAME]` `[COMPANY_NAME]` `[COMPANY_URL]` `[CTA_URL]` `[CURRENCY]` `[EMAIL_ADDRESS]` `[NEXT_CHARGE_DATE]` `[PRIVACY_URL]` `[PRODUCT_NAME]` `[RETRY_DATE]` `[SIGNOFF_NAME]` `[SUPPORT_EMAIL]`

**[`billing/payment-failed-1`](templates/billing/payment-failed-1.html)**

`[AMOUNT]` `[CARD_BRAND]` `[CARD_LAST4]` `[COMPANY_ADDRESS]` `[COMPANY_LEGAL_NAME]` `[COMPANY_NAME]` `[COMPANY_URL]` `[CTA_URL]` `[CURRENCY]` `[EMAIL_ADDRESS]` `[PLAN_NAME]` `[PRIVACY_URL]` `[PRODUCT_NAME]` `[RETRY_DATE]` `[SIGNOFF_NAME]` `[SUPPORT_EMAIL]`

**[`billing/payment-failed-2`](templates/billing/payment-failed-2.html)**

`[AMOUNT]` `[CARD_BRAND]` `[CARD_LAST4]` `[COMPANY_ADDRESS]` `[COMPANY_LEGAL_NAME]` `[COMPANY_NAME]` `[COMPANY_URL]` `[CTA_URL]` `[CURRENCY]` `[EMAIL_ADDRESS]` `[GRACE_END_DATE]` `[PLAN_NAME]` `[PRIVACY_URL]` `[PRODUCT_NAME]` `[RETRY_DATE]` `[SIGNOFF_NAME]` `[SUPPORT_EMAIL]`

**[`billing/payment-failed-final`](templates/billing/payment-failed-final.html)**

`[AMOUNT]` `[CARD_BRAND]` `[CARD_LAST4]` `[COMPANY_ADDRESS]` `[COMPANY_LEGAL_NAME]` `[COMPANY_NAME]` `[COMPANY_URL]` `[CTA_URL]` `[CURRENCY]` `[EMAIL_ADDRESS]` `[GRACE_END_DATE]` `[INVOICE_NUMBER]` `[PLAN_NAME]` `[PRIVACY_URL]` `[PRODUCT_NAME]` `[RETENTION_END_DATE]` `[RETENTION_PERIOD]` `[RETRY_DATE]` `[SEAT_COUNT]` `[SIGNOFF_NAME]` `[SUPPORT_EMAIL]`

**[`billing/receipt`](templates/billing/receipt.html)**

`[AMOUNT]` `[BILLING_PERIOD]` `[CARD_BRAND]` `[CARD_LAST4]` `[COMPANY_ADDRESS]` `[COMPANY_LEGAL_NAME]` `[COMPANY_NAME]` `[COMPANY_URL]` `[CURRENCY]` `[EMAIL_ADDRESS]` `[INVOICE_DATE]` `[INVOICE_NUMBER]` `[NEXT_CHARGE_DATE]` `[PLAN_NAME]` `[PRIVACY_URL]` `[PRODUCT_NAME]` `[SEAT_COUNT]` `[SECONDARY_URL]` `[SIGNOFF_NAME]` `[SUBTOTAL]` `[SUPPORT_EMAIL]` `[TAX]` `[TOTAL]`

**[`billing/renewal-reminder`](templates/billing/renewal-reminder.html)**

`[AMOUNT]` `[BILLING_PERIOD]` `[CARD_BRAND]` `[CARD_LAST4]` `[COMPANY_ADDRESS]` `[COMPANY_LEGAL_NAME]` `[COMPANY_NAME]` `[COMPANY_URL]` `[CURRENCY]` `[EMAIL_ADDRESS]` `[NEXT_CHARGE_DATE]` `[PLAN_NAME]` `[PRIVACY_URL]` `[PRODUCT_NAME]` `[SECONDARY_URL]` `[SIGNOFF_NAME]` `[SUPPORT_EMAIL]`

**[`billing/subscription-cancelled`](templates/billing/subscription-cancelled.html)**

`[AMOUNT]` `[COMPANY_ADDRESS]` `[COMPANY_LEGAL_NAME]` `[COMPANY_NAME]` `[COMPANY_URL]` `[CURRENCY]` `[EMAIL_ADDRESS]` `[EVENT_TIME]` `[GRACE_END_DATE]` `[INVOICE_DATE]` `[PLAN_NAME]` `[PRIVACY_URL]` `[PRODUCT_NAME]` `[RETENTION_END_DATE]` `[RETENTION_PERIOD]` `[SECONDARY_URL]` `[SIGNOFF_NAME]` `[SUPPORT_EMAIL]`

**[`billing/trial-ending`](templates/billing/trial-ending.html)**

`[AMOUNT]` `[BILLING_PERIOD]` `[CARD_BRAND]` `[CARD_LAST4]` `[COMPANY_ADDRESS]` `[COMPANY_LEGAL_NAME]` `[COMPANY_NAME]` `[COMPANY_URL]` `[CTA_URL]` `[CURRENCY]` `[EMAIL_ADDRESS]` `[PLAN_NAME]` `[PRIVACY_URL]` `[PRODUCT_NAME]` `[SECONDARY_URL]` `[SIGNOFF_NAME]` `[SUPPORT_EMAIL]` `[TRIAL_END_DATE]`

**[`consent/data-breach`](templates/consent/data-breach.html)**

`[BREACH_INFO_URL]` `[COMPANY_ADDRESS]` `[COMPANY_LEGAL_NAME]` `[COMPANY_NAME]` `[COMPANY_URL]` `[CTA_URL]` `[DATA_CATEGORIES]` `[DATA_NOT_INVOLVED]` `[EMAIL_ADDRESS]` `[INCIDENT_CONTAINED]` `[INCIDENT_DATE]` `[INCIDENT_DISCOVERED]` `[INCIDENT_SUMMARY]` `[PRIVACY_URL]` `[PRODUCT_NAME]` `[SIGNOFF_NAME]` `[SUPPORT_EMAIL]`

**[`consent/double-opt-in`](templates/consent/double-opt-in.html)**

`[COMPANY_ADDRESS]` `[COMPANY_LEGAL_NAME]` `[COMPANY_NAME]` `[COMPANY_URL]` `[CTA_URL]` `[EMAIL_ADDRESS]` `[EXPIRY_ABSOLUTE]` `[EXPIRY_RELATIVE]` `[LIST_NAME]` `[PRIVACY_URL]` `[PRODUCT_NAME]` `[SEND_FREQUENCY]` `[SIGNOFF_NAME]` `[SUPPORT_EMAIL]`

**[`consent/dsar-acknowledgement`](templates/consent/dsar-acknowledgement.html)**

`[COMPANY_ADDRESS]` `[COMPANY_LEGAL_NAME]` `[COMPANY_NAME]` `[COMPANY_URL]` `[EMAIL_ADDRESS]` `[EVENT_TIME]` `[PRIVACY_URL]` `[REQUEST_REFERENCE]` `[REQUEST_TYPE]` `[RESPONSE_DUE_DATE]` `[SIGNOFF_NAME]` `[SUPPORT_EMAIL]`

**[`consent/terms-change`](templates/consent/terms-change.html)**

`[CHANGE_SUMMARY]` `[COMPANY_ADDRESS]` `[COMPANY_LEGAL_NAME]` `[COMPANY_NAME]` `[COMPANY_URL]` `[EFFECTIVE_DATE]` `[EMAIL_ADDRESS]` `[LIST_ITEM_1]` `[LIST_ITEM_2]` `[LIST_ITEM_3]` `[PRIVACY_URL]` `[PRODUCT_NAME]` `[SECONDARY_URL]` `[SIGNOFF_NAME]` `[SUPPORT_EMAIL]` `[TERMS_URL]`

**[`consent/unsubscribe-confirmed`](templates/consent/unsubscribe-confirmed.html)**

`[COMPANY_ADDRESS]` `[COMPANY_LEGAL_NAME]` `[COMPANY_NAME]` `[COMPANY_URL]` `[EMAIL_ADDRESS]` `[LIST_NAME]` `[PRIVACY_URL]` `[SECONDARY_URL]` `[SIGNOFF_NAME]` `[SUPPORT_EMAIL]` `[UNSUB_PROCESSING_PERIOD]`

**[`lifecycle/collaboration-notification`](templates/lifecycle/collaboration-notification.html)**

`[ACTOR_NAME]` `[COMMENT_EXCERPT]` `[COMPANY_ADDRESS]` `[COMPANY_LEGAL_NAME]` `[COMPANY_NAME]` `[COMPANY_URL]` `[CTA_URL]` `[EMAIL_ADDRESS]` `[EVENT_TIME]` `[OBJECT_NAME]` `[PRIVACY_URL]` `[PRODUCT_NAME]` `[SECONDARY_URL]` `[SIGNOFF_NAME]` `[SUPPORT_EMAIL]`

**[`lifecycle/digest`](templates/lifecycle/digest.html)**

`[ALL_ITEMS_URL]` `[COMPANY_ADDRESS]` `[COMPANY_LEGAL_NAME]` `[COMPANY_NAME]` `[COMPANY_URL]` `[EMAIL_ADDRESS]` `[ITEM_1_SUMMARY]` `[ITEM_1_TITLE]` `[ITEM_1_URL]` `[ITEM_2_SUMMARY]` `[ITEM_2_TITLE]` `[ITEM_2_URL]` `[ITEM_3_SUMMARY]` `[ITEM_3_TITLE]` `[ITEM_3_URL]` `[METRIC_1_LABEL]` `[METRIC_1_VALUE]` `[METRIC_2_LABEL]` `[METRIC_2_VALUE]` `[METRIC_3_LABEL]` `[METRIC_3_VALUE]` `[PERIOD_LABEL]` `[PRIVACY_URL]` `[PRODUCT_NAME]` `[SECONDARY_URL]` `[SIGNOFF_NAME]` `[UNSUBSCRIBE_URL]`

**[`lifecycle/feature-announcement`](templates/lifecycle/feature-announcement.html)**

`[COMPANY_ADDRESS]` `[COMPANY_LEGAL_NAME]` `[COMPANY_NAME]` `[COMPANY_URL]` `[CTA_URL]` `[EMAIL_ADDRESS]` `[FEATURE_NAME]` `[FEATURE_REPLACES]` `[FEATURE_SUMMARY]` `[FEATURE_USE_1]` `[FEATURE_USE_2]` `[FEATURE_USE_3]` `[PRIVACY_URL]` `[PRODUCT_NAME]` `[ROLE_NAME]` `[SECONDARY_URL]` `[SIGNOFF_NAME]` `[SUPPORT_EMAIL]` `[TEAM_NAME]` `[UNSUBSCRIBE_URL]`

**[`lifecycle/re-engagement`](templates/lifecycle/re-engagement.html)**

`[COMPANY_ADDRESS]` `[COMPANY_LEGAL_NAME]` `[COMPANY_NAME]` `[COMPANY_URL]` `[CTA_URL]` `[EMAIL_ADDRESS]` `[ITEM_1_SUMMARY]` `[ITEM_1_TITLE]` `[ITEM_2_SUMMARY]` `[ITEM_2_TITLE]` `[ITEM_3_SUMMARY]` `[ITEM_3_TITLE]` `[LAST_ACTIVE_DATE]` `[PRIVACY_URL]` `[PRODUCT_NAME]` `[RETENTION_END_DATE]` `[RETENTION_PERIOD]` `[SECONDARY_URL]` `[SIGNOFF_NAME]` `[SUPPORT_EMAIL]` `[UNSUBSCRIBE_URL]`

**[`lifecycle/team-invitation`](templates/lifecycle/team-invitation.html)**

`[COMPANY_ADDRESS]` `[COMPANY_LEGAL_NAME]` `[COMPANY_NAME]` `[COMPANY_URL]` `[CTA_URL]` `[EMAIL_ADDRESS]` `[EXPIRY_ABSOLUTE]` `[EXPIRY_RELATIVE]` `[INVITER_EMAIL]` `[INVITER_NAME]` `[PRIVACY_URL]` `[PRODUCT_NAME]` `[ROLE_NAME]` `[SIGNOFF_NAME]` `[SUPPORT_EMAIL]` `[TEAM_NAME]` `[UNSUBSCRIBE_URL]`

**[`lifecycle/welcome`](templates/lifecycle/welcome.html)**

`[COMPANY_ADDRESS]` `[COMPANY_LEGAL_NAME]` `[COMPANY_NAME]` `[COMPANY_URL]` `[CTA_URL]` `[EMAIL_ADDRESS]` `[FIRST_NAME]` `[PRIVACY_URL]` `[PRODUCT_NAME]` `[SIGNOFF_NAME]` `[SIGNUP_DATE]` `[SUPPORT_EMAIL]` `[UNSUBSCRIBE_URL]`

**[`ops/incident-open`](templates/ops/incident-open.html)**

`[AFFECTED_SCOPE]` `[COMPANY_ADDRESS]` `[COMPANY_LEGAL_NAME]` `[COMPANY_NAME]` `[COMPANY_URL]` `[EMAIL_ADDRESS]` `[EVENT_TIME]` `[INCIDENT_STATUS]` `[NEXT_UPDATE_TIME]` `[PRIVACY_URL]` `[PRODUCT_NAME]` `[SIGNOFF_NAME]` `[STATUS_PAGE_URL]` `[SUPPORT_EMAIL]` `[WORKAROUND_TEXT]`

**[`ops/incident-resolved`](templates/ops/incident-resolved.html)**

`[AFFECTED_SCOPE]` `[COMPANY_ADDRESS]` `[COMPANY_LEGAL_NAME]` `[COMPANY_NAME]` `[COMPANY_URL]` `[EMAIL_ADDRESS]` `[EVENT_TIME]` `[INCIDENT_CAUSE]` `[INCIDENT_DURATION]` `[INCIDENT_STATUS]` `[PRIVACY_URL]` `[PRODUCT_NAME]` `[RESOLVED_TIME]` `[SIGNOFF_NAME]` `[STATUS_PAGE_URL]` `[SUPPORT_EMAIL]`

**[`ops/quota-exceeded`](templates/ops/quota-exceeded.html)**

`[BILLING_PERIOD]` `[COMPANY_ADDRESS]` `[COMPANY_LEGAL_NAME]` `[COMPANY_NAME]` `[COMPANY_URL]` `[CTA_URL]` `[EMAIL_ADDRESS]` `[EVENT_TIME]` `[PRIVACY_URL]` `[PRODUCT_NAME]` `[QUOTA_CONSEQUENCE]` `[QUOTA_LIMIT]` `[QUOTA_NAME]` `[QUOTA_RESET_DATE]` `[QUOTA_STOPPED]` `[QUOTA_UNAFFECTED]` `[QUOTA_USED]` `[SIGNOFF_NAME]` `[SUPPORT_EMAIL]`

**[`ops/scheduled-maintenance`](templates/ops/scheduled-maintenance.html)**

`[AFFECTED_SCOPE]` `[COMPANY_ADDRESS]` `[COMPANY_LEGAL_NAME]` `[COMPANY_NAME]` `[COMPANY_URL]` `[EMAIL_ADDRESS]` `[MAINTENANCE_DURATION]` `[MAINTENANCE_END]` `[MAINTENANCE_START]` `[PRIVACY_URL]` `[PRODUCT_NAME]` `[SIGNOFF_NAME]` `[STATUS_PAGE_URL]` `[SUPPORT_EMAIL]`

**[`orders/delivered`](templates/orders/delivered.html)**

`[CARRIER]` `[COMPANY_ADDRESS]` `[COMPANY_LEGAL_NAME]` `[COMPANY_NAME]` `[COMPANY_URL]` `[DELIVERED_TIME]` `[DELIVERY_GRACE]` `[ORDER_NUMBER]` `[ORDER_URL]` `[PRIVACY_URL]` `[SHIPPING_ADDRESS]` `[SIGNOFF_NAME]` `[SUPPORT_EMAIL]`

**[`orders/order-cancelled`](templates/orders/order-cancelled.html)**

`[CANCEL_REASON]` `[COMPANY_ADDRESS]` `[COMPANY_LEGAL_NAME]` `[COMPANY_NAME]` `[COMPANY_URL]` `[CTA_URL]` `[CURRENCY]` `[EMAIL_ADDRESS]` `[EVENT_TIME]` `[ITEM_1_AMOUNT]` `[ITEM_1_NAME]` `[ITEM_1_QTY]` `[ITEM_1_VARIANT]` `[ORDER_NUMBER]` `[PRIVACY_URL]` `[PRODUCT_NAME]` `[REFUND_AMOUNT]` `[REFUND_DAYS]` `[REFUND_METHOD]` `[SIGNOFF_NAME]` `[SUPPORT_EMAIL]`

**[`orders/order-confirmation`](templates/orders/order-confirmation.html)**

`[BILLING_ADDRESS]` `[CARD_BRAND]` `[CARD_LAST4]` `[CHANGE_DEADLINE]` `[COMPANY_ADDRESS]` `[COMPANY_LEGAL_NAME]` `[COMPANY_NAME]` `[COMPANY_URL]` `[CURRENCY]` `[DELIVERY_ESTIMATE]` `[EMAIL_ADDRESS]` `[ITEM_1_AMOUNT]` `[ITEM_1_NAME]` `[ITEM_1_QTY]` `[ITEM_1_VARIANT]` `[ITEM_2_AMOUNT]` `[ITEM_2_NAME]` `[ITEM_2_QTY]` `[ITEM_2_VARIANT]` `[ORDER_DATE]` `[ORDER_NUMBER]` `[ORDER_URL]` `[PRIVACY_URL]` `[SHIPPING]` `[SHIPPING_ADDRESS]` `[SIGNOFF_NAME]` `[SUBTOTAL]` `[SUPPORT_EMAIL]` `[TAX]` `[TOTAL]`

**[`orders/refund-issued`](templates/orders/refund-issued.html)**

`[COMPANY_ADDRESS]` `[COMPANY_LEGAL_NAME]` `[COMPANY_NAME]` `[COMPANY_URL]` `[CURRENCY]` `[EMAIL_ADDRESS]` `[ITEM_1_AMOUNT]` `[ITEM_1_NAME]` `[ITEM_1_QTY]` `[ITEM_1_VARIANT]` `[ITEM_2_AMOUNT]` `[ITEM_2_NAME]` `[ITEM_2_QTY]` `[ITEM_2_VARIANT]` `[ORDER_NUMBER]` `[ORDER_URL]` `[PRIVACY_URL]` `[PRODUCT_NAME]` `[REFUND_AMOUNT]` `[REFUND_DAYS]` `[REFUND_METHOD]` `[SHIPPING]` `[SIGNOFF_NAME]` `[SUBTOTAL]` `[SUPPORT_EMAIL]` `[TAX]`

**[`orders/return-label`](templates/orders/return-label.html)**

`[COMPANY_ADDRESS]` `[COMPANY_LEGAL_NAME]` `[COMPANY_NAME]` `[COMPANY_URL]` `[CURRENCY]` `[EMAIL_ADDRESS]` `[ITEM_1_AMOUNT]` `[ITEM_1_NAME]` `[ITEM_1_QTY]` `[ITEM_1_VARIANT]` `[ORDER_NUMBER]` `[PRIVACY_URL]` `[PRODUCT_NAME]` `[REFUND_AMOUNT]` `[REFUND_DAYS]` `[REFUND_METHOD]` `[RETURN_DEADLINE]` `[RETURN_URL]` `[SIGNOFF_NAME]` `[SUPPORT_EMAIL]`

**[`orders/shipped`](templates/orders/shipped.html)**

`[CARRIER]` `[COMPANY_ADDRESS]` `[COMPANY_LEGAL_NAME]` `[COMPANY_NAME]` `[COMPANY_URL]` `[CURRENCY]` `[DELIVERY_ESTIMATE]` `[ITEM_1_AMOUNT]` `[ITEM_1_NAME]` `[ITEM_1_QTY]` `[ITEM_1_VARIANT]` `[ORDER_NUMBER]` `[PRIVACY_URL]` `[SHIPPING_ADDRESS]` `[SIGNOFF_NAME]` `[SUPPORT_EMAIL]` `[TRACKING_NUMBER]` `[TRACKING_URL]`

---

## Every token, alphabetically

| Placeholder | Example | Used by |
| --- | --- | --- |
| `[ACTOR_NAME]` | `Marcus Lee` | collaboration-notification |
| `[AFFECTED_SCOPE]` | `Job dispatch and the mobile app` | incident-open, incident-resolved, scheduled-maintenance |
| `[ALL_ITEMS_URL]` | `https://fernway.example/activity` | digest |
| `[AMOUNT]` | `588.00` | Render money to **two decimal places**, or the decimal column will not align. card-expiring, payment-failed-1, payment-failed-2, payment-failed-final, receipt, renewal-reminder, subscription-cancelled, trial-ending |
| `[BILLING_ADDRESS]` | `Brightpath Mechanical, PO Box 1184, Seattle WA 98111` | Same as `[SHIPPING_ADDRESS]`: `<br>` in the `.html`, newlines in the `.txt`. order-confirmation |
| `[BILLING_PERIOD]` | `7 Sep - 7 Oct 2026` | receipt, renewal-reminder, trial-ending, quota-exceeded |
| `[BREACH_INFO_URL]` | `https://fernway.example/security/2026-09` | data-breach |
| `[CANCEL_REASON]` | `The vehicle charging dock is out of stock` | order-cancelled |
| `[CARD_BRAND]` | `Visa` | card-expiring, payment-failed-1, payment-failed-2, payment-failed-final, receipt, renewal-reminder, trial-ending, order-confirmation |
| `[CARD_EXPIRY]` | `10/2026` | card-expiring |
| `[CARD_LAST4]` | `4242` | card-expiring, payment-failed-1, payment-failed-2, payment-failed-final, receipt, renewal-reminder, trial-ending, order-confirmation |
| `[CARRIER]` | `UPS` | delivered, shipped |
| `[CHANGE_DEADLINE]` | `18:00 UTC on 8 September 2026` | order-confirmation |
| `[CHANGE_SUMMARY]` | `how long we keep job records, and who we name as sub-processors` | terms-change |
| `[COMMENT_EXCERPT]` | `Access is through the loading bay, not the front desk. The key is with building security.` | collaboration-notification |
| `[COMPANY_ADDRESS]` | `1100 Alder Street, Suite 210, Portland, OR 97205, USA` | **Legally required** in commercial mail — see [Compliance](README.md#compliance). every template |
| `[COMPANY_LEGAL_NAME]` | `Fernway Technologies Inc.` | every template |
| `[COMPANY_NAME]` | `Fernway` | every template |
| `[COMPANY_URL]` | `https://fernway.example` | every template |
| `[CTA_URL]` | `https://fernway.example/a/9f2a1c7e` | account-locked, email-change-new, magic-link, password-reset, verify-email, card-expiring, payment-failed-1, payment-failed-2, payment-failed-final, trial-ending, data-breach, double-opt-in, collaboration-notification, feature-announcement, re-engagement, team-invitation, welcome, quota-exceeded, order-cancelled |
| `[CURRENCY]` | `USD` | Bound to the figure with `&nbsp;` so it cannot wrap onto its own line. card-expiring, payment-failed-1, payment-failed-2, payment-failed-final, receipt, renewal-reminder, subscription-cancelled, trial-ending, order-cancelled, order-confirmation, refund-issued, return-label, shipped |
| `[DATA_CATEGORIES]` | `Name, work email address, and hashed password` | data-breach |
| `[DATA_NOT_INVOLVED]` | `Payment card numbers, bank details, and customer site addresses` | Name what was **not** affected as explicitly as what was. Readers assume the worst. data-breach |
| `[DELIVERED_TIME]` | `10:42 on 11 September 2026` | delivered |
| `[DELIVERY_ESTIMATE]` | `11-13 September 2026` | An estimate, and the copy says so. Never present it as a guarantee. order-confirmation, shipped |
| `[DELIVERY_GRACE]` | `15 September 2026` | delivered |
| `[EFFECTIVE_DATE]` | `15 October 2026` | terms-change |
| `[EMAIL_ADDRESS]` | `priya@brightpath.example` | account-locked, magic-link, new-device-signin, otp-code, password-changed, password-reset, verify-email, card-expiring, payment-failed-1, payment-failed-2, payment-failed-final, receipt, renewal-reminder, subscription-cancelled, trial-ending, data-breach, double-opt-in, dsar-acknowledgement, terms-change, unsubscribe-confirmed, collaboration-notification, digest, feature-announcement, re-engagement, team-invitation, welcome, incident-open, incident-resolved, quota-exceeded, scheduled-maintenance, order-cancelled, order-confirmation, refund-issued, return-label |
| `[EVENT_DEVICE]` | `Chrome on macOS` | new-device-signin |
| `[EVENT_IP]` | `203.0.113.42` | Shown only in the sign-in alert, where the copy says it is approximate. new-device-signin |
| `[EVENT_LOCATION]` | `Portland, Oregon, United States` | new-device-signin, password-changed |
| `[EVENT_TIME]` | `14:05 UTC on 7 September 2026` | account-locked, email-change-old, new-device-signin, password-changed, subscription-cancelled, dsar-acknowledgement, collaboration-notification, incident-open, incident-resolved, quota-exceeded, order-cancelled |
| `[EXPIRY_ABSOLUTE]` | `14:35 UTC on 7 September 2026` | An absolute time **with a timezone**. Always paired with the relative form. account-locked, email-change-new, email-change-old, magic-link, otp-code, password-reset, verify-email, double-opt-in, team-invitation |
| `[EXPIRY_RELATIVE]` | `30 minutes` | How long a link or code lasts, in words. account-locked, email-change-new, email-change-old, magic-link, otp-code, password-reset, verify-email, double-opt-in, team-invitation |
| `[FEATURE_NAME]` | `Saved routes` | feature-announcement |
| `[FEATURE_REPLACES]` | `rebuilding the same route every Monday morning` | feature-announcement |
| `[FEATURE_SUMMARY]` | `A run of jobs you order once and reuse every week.` | feature-announcement |
| `[FEATURE_USE_1]` | `Keep a standing route for each crew and swap jobs in and out` | feature-announcement |
| `[FEATURE_USE_2]` | `Hand a route to a stand-in without explaining the order` | feature-announcement |
| `[FEATURE_USE_3]` | `Reuse last week without setting it up again` | feature-announcement |
| `[FIRST_NAME]` | `Priya` | Give your platform a fallback; an empty value leaves a dangling comma. welcome |
| `[GRACE_END_DATE]` | `21 September 2026` | payment-failed-2, payment-failed-final, subscription-cancelled |
| `[INCIDENT_CAUSE]` | `A configuration change removed a database connection limit, and the pool ran out.` | incident-resolved |
| `[INCIDENT_CONTAINED]` | `5 September 2026` | data-breach |
| `[INCIDENT_DATE]` | `2 September 2026` | data-breach |
| `[INCIDENT_DISCOVERED]` | `5 September 2026` | data-breach |
| `[INCIDENT_DURATION]` | `1 hour 7 minutes` | incident-resolved |
| `[INCIDENT_STATUS]` | `Investigating` | incident-open, incident-resolved |
| `[INCIDENT_SUMMARY]` | `An unauthorised party accessed a database backup held by one of our suppliers.` | data-breach |
| `[INVITER_EMAIL]` | `marcus@brightpath.example` | team-invitation |
| `[INVITER_NAME]` | `Marcus Lee` | team-invitation |
| `[INVOICE_DATE]` | `7 September 2026` | receipt, subscription-cancelled |
| `[INVOICE_NUMBER]` | `FW-2026-04417` | payment-failed-final, receipt |
| `[ITEM_1_AMOUNT]` | `498.00` | order-cancelled, order-confirmation, refund-issued, return-label, shipped |
| `[ITEM_1_NAME]` | `Fernway RT-2 rugged scanner` | order-cancelled, order-confirmation, refund-issued, return-label, shipped |
| `[ITEM_1_QTY]` | `2` | order-cancelled, order-confirmation, refund-issued, return-label, shipped |
| `[ITEM_1_SUMMARY]` | `It moved from Thursday to Tuesday morning.` | digest, re-engagement |
| `[ITEM_1_TITLE]` | `Marcus reassigned the Kensington boiler job to you` | digest, re-engagement |
| `[ITEM_1_URL]` | `https://fernway.example/jobs/8841` | digest |
| `[ITEM_1_VARIANT]` | `Standard grip / 2-year warranty` | order-cancelled, order-confirmation, refund-issued, return-label, shipped |
| `[ITEM_2_AMOUNT]` | `90.00` | order-confirmation, refund-issued |
| `[ITEM_2_NAME]` | `RT-2 vehicle charging dock` | order-confirmation, refund-issued |
| `[ITEM_2_QTY]` | `2` | order-confirmation, refund-issued |
| `[ITEM_2_SUMMARY]` | `They need a signature before they can be invoiced.` | digest, re-engagement |
| `[ITEM_2_TITLE]` | `Three jobs closed without a signature this week` | digest, re-engagement |
| `[ITEM_2_URL]` | `https://fernway.example/reports/unsigned` | digest |
| `[ITEM_2_VARIANT]` | `12V, hardwired` | order-confirmation, refund-issued |
| `[ITEM_3_SUMMARY]` | `Eleven items changed; the rest are unchanged.` | digest, re-engagement |
| `[ITEM_3_TITLE]` | `The Q4 parts price list is ready to review` | digest, re-engagement |
| `[ITEM_3_URL]` | `https://fernway.example/parts/q4-pricing` | digest |
| `[LAST_ACTIVE_DATE]` | `3 May 2026` | re-engagement |
| `[LIST_ITEM_1]` | `Add the crew who will be on site` | terms-change |
| `[LIST_ITEM_2]` | `Set the arrival window` | terms-change |
| `[LIST_ITEM_3]` | `Attach the site access notes` | terms-change |
| `[LIST_NAME]` | `the Fernway product newsletter` | double-opt-in, unsubscribe-confirmed |
| `[LOCK_REASON]` | `Too many failed sign-in attempts` | account-locked |
| `[MAINTENANCE_DURATION]` | `up to 2 hours` | scheduled-maintenance |
| `[MAINTENANCE_END]` | `04:00 UTC on 14 September 2026` | scheduled-maintenance |
| `[MAINTENANCE_START]` | `02:00 UTC on 14 September 2026` | Always carries a timezone. A maintenance window without one is useless to half its readers. scheduled-maintenance |
| `[METRIC_1_LABEL]` | `Jobs completed` | digest |
| `[METRIC_1_VALUE]` | `214` | digest |
| `[METRIC_2_LABEL]` | `First-visit fixes` | digest |
| `[METRIC_2_VALUE]` | `86%` | digest |
| `[METRIC_3_LABEL]` | `Crew members active` | digest |
| `[METRIC_3_VALUE]` | `12` | digest |
| `[NEW_EMAIL_ADDRESS]` | `priya.raman@brightpath.example` | email-change-new, email-change-old |
| `[NEXT_CHARGE_DATE]` | `7 October 2026` | card-expiring, receipt, renewal-reminder |
| `[NEXT_UPDATE_TIME]` | `15:30 UTC on 7 September 2026` | The one commitment an incident notice can honestly make. Always carries a timezone. incident-open |
| `[OBJECT_NAME]` | `the Kensington boiler job` | collaboration-notification |
| `[OLD_EMAIL_ADDRESS]` | `priya@brightpath.example` | email-change-new, email-change-old |
| `[ORDER_DATE]` | `7 September 2026` | order-confirmation |
| `[ORDER_NUMBER]` | `FW-10023` | delivered, order-cancelled, order-confirmation, refund-issued, return-label, shipped |
| `[ORDER_URL]` | `https://fernway.example/orders/10023` | delivered, order-confirmation, refund-issued |
| `[OTP_CODE]` | `482913` | Must stay one contiguous run of characters — see [`partials/README.md`](partials/README.md). otp-code |
| `[PERIOD_LABEL]` | `September` | digest |
| `[PLAN_NAME]` | `Crew` | payment-failed-1, payment-failed-2, payment-failed-final, receipt, renewal-reminder, subscription-cancelled, trial-ending |
| `[PRIVACY_URL]` | `https://fernway.example/privacy` | every template |
| `[PRODUCT_NAME]` | `Fernway` | account-locked, email-change-new, email-change-old, magic-link, new-device-signin, otp-code, password-changed, password-reset, verify-email, card-expiring, payment-failed-1, payment-failed-2, payment-failed-final, receipt, renewal-reminder, subscription-cancelled, trial-ending, data-breach, double-opt-in, terms-change, collaboration-notification, digest, feature-announcement, re-engagement, team-invitation, welcome, incident-open, incident-resolved, quota-exceeded, scheduled-maintenance, order-cancelled, refund-issued, return-label |
| `[QUOTA_CONSEQUENCE]` | `Further requests return a 429 until the period resets` | quota-exceeded |
| `[QUOTA_LIMIT]` | `500,000` | quota-exceeded |
| `[QUOTA_NAME]` | `API requests` | quota-exceeded |
| `[QUOTA_RESET_DATE]` | `1 October 2026` | quota-exceeded |
| `[QUOTA_STOPPED]` | `New API requests and scheduled exports` | quota-exceeded |
| `[QUOTA_UNAFFECTED]` | `The web app, the mobile app, and everything already stored` | quota-exceeded |
| `[QUOTA_USED]` | `512,400` | quota-exceeded |
| `[REFUND_AMOUNT]` | `648.27` | order-cancelled, refund-issued, return-label |
| `[REFUND_DAYS]` | `5 to 10 business days` | A range, not a date: the store releases the money but the card issuer decides when it lands. order-cancelled, refund-issued, return-label |
| `[REFUND_METHOD]` | `Visa ending 4242` | order-cancelled, refund-issued, return-label |
| `[REQUEST_REFERENCE]` | `DSAR-2026-0431` | dsar-acknowledgement |
| `[REQUEST_TYPE]` | `A copy of your personal data` | dsar-acknowledgement |
| `[RESOLVED_TIME]` | `15:12 UTC on 7 September 2026` | incident-resolved |
| `[RESPONSE_DUE_DATE]` | `7 October 2026` | dsar-acknowledgement |
| `[RETENTION_END_DATE]` | `20 December 2026` | The date data is deleted. Paired with the period above, and never an expiry. payment-failed-final, subscription-cancelled, re-engagement |
| `[RETENTION_PERIOD]` | `90 days` | How long data survives after an account lapses. Not the same thing as a link expiry. payment-failed-final, subscription-cancelled, re-engagement |
| `[RETRY_DATE]` | `10 September 2026` | card-expiring, payment-failed-1, payment-failed-2, payment-failed-final |
| `[RETURN_DEADLINE]` | `5 October 2026` | return-label |
| `[RETURN_URL]` | `https://fernway.example/returns/10023/label.pdf` | return-label |
| `[ROLE_NAME]` | `Dispatcher` | feature-announcement, team-invitation |
| `[SEAT_COUNT]` | `12` | payment-failed-final, receipt |
| `[SECONDARY_URL]` | `https://fernway.example/settings/security` | email-change-old, new-device-signin, password-changed, receipt, renewal-reminder, subscription-cancelled, trial-ending, terms-change, unsubscribe-confirmed, collaboration-notification, digest, feature-announcement, re-engagement |
| `[SEND_FREQUENCY]` | `about twice a month` | double-opt-in |
| `[SHIPPING]` | `0.00` | order-confirmation, refund-issued |
| `[SHIPPING_ADDRESS]` | `Priya Raman, Brightpath Mechanical, 1420 5th Avenue Suite 300, Seattle WA 98101` | **Renders differently in each part**: separate the lines with `<br>` in the `.html` and with real newlines in the `.txt`. Substituting one string into both breaks one of them. delivered, order-confirmation, shipped |
| `[SIGNOFF_NAME]` | `Maya` | every template |
| `[SIGNUP_DATE]` | `7 September 2026` | welcome |
| `[STATUS_PAGE_URL]` | `https://status.fernway.example` | incident-open, incident-resolved, scheduled-maintenance |
| `[SUBTOTAL]` | `588.00` | receipt, order-confirmation, refund-issued |
| `[SUPPORT_EMAIL]` | `support@fernway.example` | account-locked, email-change-new, email-change-old, magic-link, new-device-signin, otp-code, password-changed, password-reset, verify-email, card-expiring, payment-failed-1, payment-failed-2, payment-failed-final, receipt, renewal-reminder, subscription-cancelled, trial-ending, data-breach, double-opt-in, dsar-acknowledgement, terms-change, unsubscribe-confirmed, collaboration-notification, feature-announcement, re-engagement, team-invitation, welcome, incident-open, incident-resolved, quota-exceeded, scheduled-maintenance, delivered, order-cancelled, order-confirmation, refund-issued, return-label, shipped |
| `[TAX]` | `60.27` | receipt, order-confirmation, refund-issued |
| `[TEAM_NAME]` | `Brightpath Mechanical` | feature-announcement, team-invitation |
| `[TERMS_URL]` | `https://fernway.example/terms` | terms-change |
| `[TOTAL]` | `648.27` | receipt, order-confirmation |
| `[TRACKING_NUMBER]` | `1Z999AA10123456784` | Tracking often shows no movement for a few hours after the label is created; the copy warns about this. shipped |
| `[TRACKING_URL]` | `https://fernway.example/track/1Z999AA10123456784` | shipped |
| `[TRIAL_END_DATE]` | `14 September 2026` | trial-ending |
| `[UNSUBSCRIBE_URL]` | `https://fernway.example/u/6b41f0a9` | **Legally required** in commercial mail. Commercial templates only. digest, feature-announcement, re-engagement, team-invitation, welcome |
| `[UNSUB_PROCESSING_PERIOD]` | `48 hours` | unsubscribe-confirmed |
| `[WORKAROUND_TEXT]` | `There is no workaround. Jobs already downloaded to a device still open offline.` | Write "There is no workaround" when there is none. An empty value renders a panel that says only "Important:". incident-open |

138 placeholders across 38 templates. 6 are used by every template.

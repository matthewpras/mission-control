# LUMINA LAUNCH REPORT - Actionable Deployment Summary
**Date:** 2026-02-27
**Project:** Lumina Sleep (Shopify)

## 1. Domain Recommendations
Research suggests that while `luminasleep.com` is the gold standard, it may be premium or unavailable. 
*   **Top Pick:** `luminasleep.co` — Clean, modern, and tech-focused.
*   **Marketing Pick:** `tryluminasleep.com` — High conversion potential for paid ads.
*   **Product Pick:** `shopluminarest.com` — Direct link to the hero product.
*   **Availability Note:** `getlumina.com` is currently utilized by a separate tech entity; avoid for SEO clarity.

## 2. Shopify Payments Activation
**Steps to Activate:**
1.  Navigate to **Settings > Payments**.
2.  Click **Activate Shopify Payments**.
3.  **Required Information:**
    *   **Business:** EIN (or SSN if sole proprietor), Business Address.
    *   **Personal:** Legal Name, Date of Birth, Last 4 of SSN for verification.
    *   **Bank:** USD Checking account details (Routing + Account number).
4.  **Security:** Ensure Two-Factor Authentication (2FA) is enabled on the Shopify account, or activation will be blocked.

## 3. Shipping Configuration
Recommended setup to align with the **Free Shipping > $100** strategy:
*   **Zone: United States**
    *   *Standard Shipping (3-5 days):* $6.95 (for orders $0.00 - $99.99)
    *   *Lumina Priority (Free):* $0.00 (for orders $100.00+)
    *   *Express Insured (1-2 days):* $14.95 (Flat rate)
*   **Zone: International**
    *   *Standard International:* $19.95 flat rate.

## 4. App Stack & Pricing
*   **Klaviyo (Email/SMS Marketing):**
    *   **Price:** Free (up to 250 contacts). Paid starts at ~$20/mo.
    *   **Action:** Essential for "Abandoned Cart" and "Welcome" flows.
*   **Judge.me (Product Reviews):**
    *   **Price:** Free Forever (Unlimited reviews). Awesome plan is $15/mo.
    *   **Action:** Use Free version initially to collect social proof via the Lumina Rest AI Mask.

## 5. Test Order Checklist
Follow these steps before going "Live":
1.  [ ] **Checkout Entry:** Add Lumina Rest Mask to cart ($129.99).
2.  [ ] **Free Shipping:** Confirm "Lumina Priority (Free)" appears at checkout.
3.  [ ] **Mobile Optimization:** Complete the checkout on a mobile device.
4.  [ ] **Test Gateway:** Enable "Test Mode" in Settings > Payments and use test card `4242...`
5.  [ ] **Email Trigger:** Verify "Order Confirmation" email arrives in inbox.
6.  [ ] **Fulfillment:** Mark the order as "Fulfilled" in Admin to test tracking notification.
7.  [ ] **Refund:** Process a full refund to confirm the payment loop is closed.

LUMINA_LAUNCH_COMPLETE

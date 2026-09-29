# GAA Performance: setup guide

`index.html` is the whole site: one file, no frameworks, no external assets. That keeps it fast on mobile data. Hosting is GitHub Pages with a custom domain (see `CNAME`), pointed at gaaperformance.ie.

## 1. Fill in the CONFIG block
Open `index.html` and find `const CONFIG` near the bottom.

| Field | What to put in |
|---|---|
| `emailEndpoint` | The action URL of the MailerLite embedded signup form (Dashboard > Forms > this form > Embed). GitHub Pages is static-only, so the form posts straight to MailerLite rather than a custom backend. Until set, the form runs in demo mode and just shows the success message. |
| `stripe.offseason` | Stripe Payment Link URL for the Complete GAA Off-Season Programme (one-off, €160). Create/edit it in Stripe Dashboard > Payment links. |
| `metaPixelId` | Meta Pixel ID for Instagram ads. |
| `tiktokPixelId` | TikTok Pixel ID for TikTok ads. |
| `instagramUrl / tiktokUrl` | Your profile links for the footer. |

1:1 Online and Hybrid Coaching are not sold on this site — the coaching section links out to Momentum Performance, which handles that funnel separately.

Events fired: `PageView`, `Lead` / `SubmitForm` (email signup), `InitiateCheckout` (Stripe button click). Optimise your ad campaigns for Lead first, then purchase once you have volume. For purchases, set the Stripe success URL to a thank-you page that fires a Purchase event.

## 2. Placeholders to replace before launch
- **Price** (€160 for the Off-Season Programme) and programme contents should match what's actually configured in Stripe — keep these in sync if the price ever changes.
- **Momentum Performance details**: brand story, coach bio, credentials, results and testimonials are not included, because there was no source material at the time this was built. Add real ones only.
- **Free lead magnet**: the "GAA Performance Primer" needs to exist as a PDF or email sequence sent by MailerLite.
- **Contact email** `hello@gaaperformance.ie`.
- **Images**: the site is text and CSS only. Add a hero photo or short video later, compressed, as WebP.

## 3. Legal pages
`/privacy.html` and `/terms.html` exist and are linked from the footer. Review them for accuracy (they're general-purpose GDPR/consumer-law templates for an Irish sole trader) before relying on them, and keep the "Last updated" date current if you change them.

## 4. Hosting (gaaperformance.ie)
Already wired up via GitHub Pages + `CNAME`. If you ever move off Pages:
1. **Cloudflare Pages / Netlify / Vercel** (free tiers): upload the folder, then add the custom domain and update DNS at your .ie registrar as instructed. HTTPS is automatic.
2. **Standard web host** (e.g. Blacknight): upload `index.html` to the web root and enable SSL.

## 5. Ads to email funnel
- Point Instagram and TikTok ads at `https://gaaperformance.ie/?utm_source=instagram&utm_medium=paid&utm_campaign=NAME`.
- The primer form captures the UTM source and campaign with each signup.
- Follow up with a 5-7 email welcome sequence that leads to the Off-Season Programme.
- Use a mobile-app in-app browser check on both platforms before spending on ads.

## 6. Notes
- The footer includes a disclaimer that the brand is not affiliated with the GAA. Keep it, and do not use the official GAA crest or logos.
- Training and injury-prevention claims should stay general. Avoid promising specific injury outcomes.

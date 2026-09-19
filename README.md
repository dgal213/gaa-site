# GAA Performance: setup guide

`index.html` is the whole site: one file, no frameworks, no external assets. That keeps it fast on mobile data.

## 1. Fill in the CONFIG block
Open `index.html` and find `const CONFIG` near the bottom.

| Field | What to put in |
|---|---|
| `emailEndpoint` | Your email provider's form/API endpoint (MailerLite, Kit, Brevo, Mailchimp) or a small serverless function. Until set, the form runs in demo mode and just shows the success message. |
| `stripe.speed / season / coaching` | Stripe Payment Link URLs. Create them in Stripe Dashboard > Payment links. Use a recurring price for coaching. |
| `metaPixelId` | Meta Pixel ID for Instagram ads. |
| `tiktokPixelId` | TikTok Pixel ID for TikTok ads. |
| `instagramUrl / tiktokUrl` | Your profile links for the footer. |

Events fired: `PageView`, `Lead` / `SubmitForm` (email signup), `InitiateCheckout` (Stripe button click). Optimise your ad campaigns for Lead first, then purchase once you have volume. For purchases, set the Stripe success URL to a thank-you page that fires a Purchase event.

## 2. Placeholders to replace before launch
- **Prices** (€39 / €79 / €149) and programme contents are placeholders.
- **Momentum Performance details**: brand story, coach bio, credentials, results and testimonials are not included, because I had no source material. Add real ones only.
- **Free lead magnet**: the "GAA Performance Primer" needs to exist as a PDF or email sequence sent by your email provider.
- **Legal pages**: `/privacy.html` and `/terms.html` are linked but not created. Add real ones. Email capture in Ireland falls under GDPR, and the form already has an explicit consent checkbox.
- **Contact email** `hello@gaaperformance.ie`.
- **Images**: the site is text and CSS only. Add a hero photo or short video later, compressed, as WebP.

## 3. Hosting (gaaperformance.ie)
Static hosting is all you need. Easy options:
1. **Cloudflare Pages / Netlify / Vercel** (free tiers): upload the folder, then add the custom domain and update DNS at your .ie registrar as instructed. HTTPS is automatic.
2. **Standard web host** (e.g. Blacknight): upload `index.html` to the web root and enable SSL.

## 4. Ads to email funnel
- Point Instagram and TikTok ads at `https://gaaperformance.ie/?utm_source=instagram&utm_medium=paid&utm_campaign=NAME`.
- The primer form captures the UTM source and campaign with each signup.
- Follow up with a 5-7 email welcome sequence that leads to the Season Plan.
- Use a mobile-app in-app browser check on both platforms before spending on ads.

## 5. Notes
- The footer includes a disclaimer that the brand is not affiliated with the GAA. Keep it, and do not use the official GAA crest or logos.
- Training and injury-prevention claims should stay general. Avoid promising specific injury outcomes.

# dennisyu.com/optimize — Optimize Live leave-behind

Damon Burton's Optimize Live mastermind (Layton, UT, August 17–19, 2026, 1857 N Hill Field Rd, 84041). Same scan-paste-done agent pack as DealCon, Wichita, DigiMarCon, JVA, and Dunker Spotlight, skinned for SEO agency owners — **Grok first**.

- Live URL: https://dennisyu.com/optimize/ (WordPress page 37958, author Dennis Yu / user 2)
- HTML (one file, for Drive / local paste / WP REST): `pages/dennisyu-com-optimize.html`
- Schema injector: `scripts/inject-optimize-seo.py`
- Publisher: `scripts/publish-optimize-page.py`

## Audit this page

On-page `#audit` (linked from the brand bar, under the H1, and the footer). This is a **microsite technical + entity audit**, not a Knowledge Panel scorecard. DealCon’s Panel ✓ / Object / Buried / Invisible tiers are for people.

The section shows:

- Score **84 — pass with notes** from a live fetch of this URL
- Buttons to Google Rich Results Test, Schema Markup Validator, KG Explorer, GKP
- Pass/fail table (title, meta, canonical, robots, H1, og:image, alts, two JSON-LD graphs, entities, gaps)
- Human schema inventory + `<details>` raw JSON-LD (our Event graph + Rank Math chrome)

Honest gaps left public: dual Rank Math **Article** vs our **Event** as the main story; HowTo is valid schema.org but Google deprecated HowTo rich results in many locales; Speakable is experimental; QR PNG is third-party `api.qrserver.com`; polaroid print still shows 2023 (caption discloses it); **bobblehead stills are not on the page**.

## Polaroid date

The middle polaroid is **the same day as the office podcast** (Damon, Dennis, Sam). It is **not 2023**. It was more than a year before Optimize Live 2026. The year handwritten on the print is wrong. Do not put “Oct 22, 2023” back in the caption or alt.

The Dec 12, 2023 Vegas sushi photo is a different day and can keep that date. Damon’s Aug 15, 2023 Facebook post is a real post date.

## Schema

Rank Math already emits Organization+Person, WebSite, WebPage, BreadcrumbList, ImageObject (now the featured limo selfie at 978×966), and Article. That is site chrome. It does **not** tag the event, the other people, the companies, the podcast, or the photos.

The Custom HTML includes a second JSON-LD `@graph` (`#optimize-entity-graph`) with distinct `@id`s (do not collide with Rank Math’s `#person`, `#website`, `#webpage`, `#breadcrumb`, `#richSnippet`):

- Event: Optimize Live, mixed attendance, Layton venue, offers (VIP sold out / virtual in stock)
- Person: Dennis Yu, Damon Burton, Sam McLeod, Cam Hazzard, Dylan Haugen, Marko Sipila, Richie Taylor, Taylor Cameron
- Organization: Local Service Spotlight, SEO National, BlitzMetrics, Optimize Live, xAI
- Place + PostalAddress: 1857 N Hill Field Rd, Layton, UT 84041
- PodcastSeries + PodcastEpisode + VideoObject: LSS Ep 1, YouTube `X3pwjZRRMKc`
- ImageObject: each relationship photo with caption, dimensions, `about` people
- HowTo: the 60-second install
- FAQPage: matches the visible FAQ (includes “Where is the schema?”)
- WebPageElement: `#audit`

Visible HTML also has entity chips, `<address>`, `<time datetime>`, image `width`/`height` on the hero stills, and a FAQ. Featured image is set via REST (`featured_media` 37962, the limo selfie of Dennis + Damon) so `og:image` is not the generic 2022 headshot.

## Bobblehead photos (still a gap)

Dennis said two photos of him and the bobblehead Damon gave him at Optimize Live (18 Aug 2026) are live (Facebook). They were **not** in:

- WordPress media on dennisyu.com (newest still 37968, Facebook screenshots at 16:54Z)
- Drive camera folder (only `IMG_1433.MOV` at 32 MB — over the Drive MCP 10 MB download cap; no matching HEIC)
- Google Photos Drive folders, Gmail attachments, or a public Facebook/Instagram fetch (login wall)

The page keeps an empty `#damon-bobblehead` slot and the audit marks it as a **gap**. Do not use a stock shot. Do not use `damon_dennis_twinning.jpg` (Dennis with a different person). When the JPEGs land in Drive or WP, upload via REST `/wp/v2/media`, put them in that slot, add `ImageObject`(s), and set `featured_media` to the better still.

## Relationship proof already on the page

- Photos: LSS podcast still; polaroid same day as the podcast (year on print wrong); Dec 12, 2023 Vegas sushi; training-room setup; cookie card; Google Photos from the Vegas/limo day.
- Facebook posts: Damon calling Dennis a peer (Aug 2023); Dennis “more good peeps like Damon” / Damon share (Feb 2025); Damon promoting LSS Ep 1 (Nov 2025); Damon sharing Dennis+Justin (Dec 2022).
- Podcast embed: YouTube `X3pwjZRRMKc`.
- Reciprocal articles: Dennis on Damon; Damon on Dennis.

## Voice

Grok first (Cursor 4.6 workshop, Grok Bot roster). Claude = thin judgment. “Chats are rented. Files are ours.” Agency overlay. Receipt: page written in Cursor Grok 4.6. No fake claims.

Publish with WordPress REST (`DENNISYU_WP_USER` + application password). REST username can be `dennis@blitzmetrics.com` or `dennis yu` (user 2). Do not set `"author": 30`. Do not store application passwords in this repo.

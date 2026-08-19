# dennisyu.com/optimize — Optimize Live leave-behind

Damon Burton's Optimize Live mastermind (Layton, UT, August 17–19, 2026, 1857 N Hill Field Rd, 84041). Same scan-paste-done agent pack as DealCon, Wichita, DigiMarCon, JVA, and Dunker Spotlight, skinned for SEO agency owners — **Grok first**.

- Live URL: https://dennisyu.com/optimize/ (WordPress page 37958, author Dennis Yu / user 2)
- All rooms index: https://dennisyu.com/workshops/
- HTML (one file, for Drive / local paste / WP REST): `pages/dennisyu-com-optimize.html`
- Schema injector: `scripts/inject-optimize-seo.py`
- Publisher: `scripts/publish-optimize-page.py`
- Header chrome fix (also on DealCon / Wichita / DigiMarCon / JVA): `scripts/workshop-chrome.css` + `scripts/patch-workshop-pages.py`

## Mobile header (19 Aug 2026)

Phone screenshot: site title, hamburger, then LinkedIn/Facebook/Instagram/X jammed into a blob. Cause: XPro/Elementor header **26488** sizes each `.xpro-social-icon` at **10×10px** on a 4-column grid with **0px gap**, while the Font Awesome glyphs are 20px — they overlap. Duplicate header sections (desktop / tablet / a leftover mobile copy) stack on a phone.

Fix: `scripts/workshop-chrome.css` (injected as `<style id="workshop-chrome">`). Desktop: 40px icons, 16px gap. Phone: title + hamburger on one row; hide header social widgets. Scope page resets to `.wrap` so they cannot zero header padding.

Same chrome on `/dealcon` `/wichita` `/digimarcon` `/jva` `/workshops` `/affiliateworld` `/activate` `/dunk-playbook` `/dunkademics` `/workshop`. Dunk Camp replica `dunkerspotlight.com/set-up-claude` is a different WordPress — no creds in this vault.

**Index of replica rooms:** https://dennisyu.com/workshops/ (not `/speaking/`, which is the booking page).

## Live talk order (presenting in the room)

Do **not** lead with the QR. Five beats, top of page as numbered cards:

1. **`#proof` Stories** — Vegas sushi (Dec 12, 2023), office podcast (`X3pwjZRRMKc`), polaroid (same day as podcast, year on print wrong), airport/limo, cookies, Facebook walls, reciprocal articles.
2. **`#cred` Credibility** — audit **Damon the person** (book, clients he names, press he cites, 100-ep podcast, YouTube, reciprocal writing). Verdict: Pass with notes. Traffic: not invented. Knowledge Panel: run it live. Personal-brand tiers for the **room** stay at `#you`.
3. **`#wheel` + `#hits`** — Topic Wheel WHY → HOW → WHAT mapped onto Damon. Greatest hits are the content already on the spokes (Outrank, flagship posts, YouTube, Learning From Others). Canonical: https://dennisyu.com/topic-wheel/ and https://blitzmetrics.com/topic-wheel/
4. **`#amplify`** — AI (Content Factory, definitive article, mentions/entity) fills the wheel. **Dollar a Day is the amplifier, not the invention — every channel, not Facebook only.** $1/day × 7, kill bottom 90%, scale unicorns. YouTube: broad, first seconds name the audience. Canonical: https://blitzmetrics.com/dollar-a-day/ and https://blitzmetrics.com/dad/
5. **`#pack`** — QR + 10-skill prompt **after** the method.

After the pack / skills, **`#boost`** is the live Dollar a Day example (most of the way down the page — not a sixth talk beat). CoachYu + Damon, YouTube `U0LU6mKgls8`.

Page plumbing `#audit` stays last. Brand bar jumps: Stories · Credibility · Wheel · Amplify · Pack. Footer also jumps to `$1/day demo`.

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
- FAQPage: matches the visible FAQ (includes live-talk order and “How does Dollar a Day fit?”)
- WebPageElement: `#cred`, `#wheel`, `#hits`, `#amplify`, `#pack`, `#boost`, `#audit`
- Book: Outrank (`#book-outrank`) + ItemList `#hits-list`
- Extra VideoObject + Learning From Others PodcastSeries/Episode
- CoachYu VideoObject `#video-coachyu-damon` (`U0LU6mKgls8`)

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

## Damon’s greatest hits (`#hits`)

Visual section **after** stories, credibility, and the Topic Wheel — the spokes, by channel. Ranked by **authority and channel**, not invented Ahrefs numbers. Brand bar + talk cards + footer jump to it.

- **Book:** *Outrank* (ISBN 1098302079, BookBaby 2020). Cover from Damon’s FreeSEObook funnel. Free PDF https://www.freeseobook.com/ · Amazon paperback · Audible `B08XMF2RFM`. William Jones quote screenshot from the same funnel.
- **Site:** four cards with Damon’s own OG images — Tony Robbins SEO (homepage flagship), Why so many people suck at SEO (Entrepreneur), Where to start when you’re new to SEO, Simple But Great SEO Hack (19% line quoted as *his* caption).
- **YouTube:** channel `@damon-burton` / `UC4pPbQZkRRMSlRo7pgwDyXg`. Embeds: `Hnm3Trj5F5Y` (SEO tools for beginners), `DHqE7NqzjkQ` (Brunson Inner Circle). Thumbs: Hormozi reaction, Andrew Roby Events case, work-life balance. LSS collab stays in `#proof` so it isn’t pasted twice.
- **Podcast:** Learning From Others (Apple id `1434853529`, 100 episodes). Apple Podcasts embed of Dennis Yu guest ep `1000626303169` (31 Aug 2023). Artwork from learningfromothers.com.
- **Clients:** name chips copied from https://www.damonburton.com/damon-burton/ — Tony Robbins, Brunson/ClickFunnels, Utah Jazz Team Store, Shark Tank, Inc. 5000, etc. No fake logos.
- **Schema:** `Book` `#book-outrank`, `ItemList` `#hits-list`, extra `VideoObject`s, `PodcastSeries` `#podcast-lfo` + episode, `WebPageElement` `#hits`. FAQ question matches the visible copy.

Do not invent view counts or Ahrefs traffic. Quote Damon when using the 19% line.

## Dollar a Day (`#amplify`)

Paid is the volume knob — **on every channel**, not Facebook only. Stories and hits first. Topic Wheel labels them. AI fills the wheel. Then audition $1/day × 7 on WHY pieces that already have organic proof. YouTube: broad, first seconds name the audience. Canonical: https://blitzmetrics.com/dollar-a-day/ and https://blitzmetrics.com/dad/

## Live $1/day demo (`#boost`) — YouTube, not a Facebook-only trick

Most of the way down the page: **after `#skills`, before `#audit`**. This is a **YouTube** Dollar a Day cell. The common misconception (including an earlier pass of this page) is that Dollar a Day means a Meta Page boost. Canonical:

- https://blitzmetrics.com/dollar-a-day/ — works on Facebook, Instagram, YouTube, Google, X, LinkedIn. YouTube is “the purest signal engine.” HVAC example: say “if you’re an HVAC guy” in the open — you are not targeting HVAC; you said the words.
- https://blitzmetrics.com/dollar-a-day/signal-setter/ — YouTube = broad, signal-led, no interest stack. Targeting lives in the three-second hook.
- https://blitzmetrics.com/the-dollar-a-day-strategy-turns-small-signals-into-compounding-authority/ — James Dooley, Feb 2026. Video `Va3nvWcv4uE` (PromoSEO / Dooley), then the article. “Nothing to do with Facebook or YouTube or TikTok or any single channel.”
- https://blitzmetrics.com/mastering-dollar-a-day-youtube-retargeting-tapping-into-niche-audiences-for-2000-roi/ — Aug 22, 2023. “Dollar a Day works on every single channel” / “Dollar a Day on YouTube is even possible.” That article is the *later* layer (viewers of specific videos). This CoachYu cell is the first layer: broad + hook.
- Teaching videos that became hubs: `EHl4N8PLWxo` (Dollar-a-Day Explained) and `eWjqOV9CzGs` (How Much to Test — $63 on one channel, then the same test on YouTube / X / LinkedIn).

**Boost this:** `U0LU6mKgls8` CoachYu + Damon, Nov 2021, @Blitzmetrics. $1/day × 7, Video views, **broad**. Related audience = who watches, not an interest stack. First seconds should name SEO / agency owners.

**Spend (18 Aug 2026):** not live. Needs the video **public** (still unlisted) plus Google Ads linked to the channel. No Google Ads token or YouTube write token in this VM (only WordPress REST). Do not invent a campaign ID. Description drawer still includes `Dennis: remember to boost this for $1 a day`.

HubSpot clip `WBpubArOwEg` is Facebook-titled — do not use it as the “every channel” proof. Kirt Box archery cell uses interest segments — do not copy that targeting into this demo.

## Voice

Grok first (Cursor 4.6 workshop, Grok Bot roster). Claude = thin judgment. “Chats are rented. Files are ours.” Agency overlay. Receipt: page written in Cursor Grok 4.6. No fake claims.

Publish with WordPress REST (`DENNISYU_WP_USER` + application password). REST username can be `dennis@blitzmetrics.com` or `dennis yu` (user 2). Do not set `"author": 30`. Do not store application passwords in this repo.

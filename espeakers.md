# eSpeakers fill map

Account: speaker ID **48283** · username **D16** · NSA Basic (video / recommendations / media kit are PRO — do not buy a speaker subscription to finish this).
Dashboard: https://www.espeakers.com/dashboard/48283/profile
Public: https://www.espeakers.com/marketplace/profile/48283/dennis-yu
EventCX (Basic): https://www.espeakers.com/myevents/

Paste from this repo. Do not invent fees or brand names. Do not put street address or private phone in this git repo. Mailing address lives on eSpeakers **contact** only.

## Current live state (2026-08-18)

Public: https://www.espeakers.com/marketplace/profile/48283/dennis-yu

Verified as a stranger: **CEO**, **NV, US**, Travels From **NV, US**, on-site **$5k+**, virtual **$5k–$5k**, full LSS bio, seven programs, no street on the marketplace page, no Your Content Factory / youcontentfactory.com.

Dashboard hub: Basics, Topics, Programs, Fees, Audience Benefits, Calendar, Virtual = **Great**. Video / media kit / recommendations stay **Needs More** because they are **PRO** — skip.

EventCX holds (status **held**, not claimed as confirmed bookings):

| Event | Dates | City | EventCX id |
|---|---|---|---|
| DealCon | 19–21 Oct 2026 | Austin, TX | 967713 |
| DigiMarCon Miami | 14–15 Oct 2026 | Miami, FL | 967716 |
| DigiMarCon Las Vegas | 4–6 Nov 2026 | Las Vegas, NV | 967715 |

Search Marketing Summit Sydney is **not** October 2026. The 2026 edition was 16–18 Feb 2026 (already past). Organizer site now lists 23–25 Feb 2027. Do not put a fake Oct 2026 Sydney hold on the calendar.

## How to save contact (the UI Save button lies)

The contact form is Formik. Setting `input.value` and clicking **Save changes** reloads the page from the API and **discards** the typed values. Proof is reload (or this public page), never the DOM right after Save.

Persist contact by `PUT https://balboa.espeakers.com/speaker/speaker/48283` from the logged-in Chrome tab with header `X-Auth-Token` = `localStorage.espeakers_user.token`. Body is the form shape (omit `id`). Website field **must not** start with `http://` or `https://` — use `dennisyu.com/speaking`.

Same token + Balboa host for bios (`/speaker/48283/bio/44969` — `oneline` is the audience-benefit field, max **300** characters) and programs (`/speaker/48283/program/{id}`).

Programs: create new ones only at `/profile-programs/new`. Saving on `/profile-programs/85355` overwrites that one record.

## Field → file

| eSpeakers screen | File |
|---|---|
| Basic info: business, URL, travels from | [`profile/basics.md`](profile/basics.md) |
| Topics & experience | [`profile/topics.md`](profile/topics.md) |
| Audience benefits (`oneline`, ≤300 chars) | Shorten [`profile/audience-benefit.md`](profile/audience-benefit.md) |
| Short + full bio | [`profile/bio-short.md`](profile/bio-short.md), [`profile/bio-full.md`](profile/bio-full.md) |
| Programs | [`programs/`](programs/) — all 7 (85355–85361) |
| Fees | [`profile/fees.md`](profile/fees.md) — $5,000 U.S. / $7,500 intl + travel |
| Videos / media | [`media.md`](media.md) — PRO-gated on this account |
| Recommendations | [`testimonials.md`](testimonials.md) — PRO-gated on this account |
| Awards & memberships | NSA member; textbook *Facebook Nation*; TEDxBeaconStreet |
| Virtual | Keynote + workshop both available virtually at $5,000; mark programs presenter type 128 |
| Calendar | EventCX holds above |
| Website | dennisyu.com/speaking (no protocol in the eSpeakers field) |

## Awards & memberships to enter

- National Speakers Association (member — this is how the eSpeakers Basic account was issued)
- Co-author, *Facebook Nation* (Springer; 700+ colleges)
- TEDxBeaconStreet 2015
- Featured: WSJ, NYT, NPR, TechCrunch, Fox, CNN, CBS

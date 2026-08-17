---
name: keep-speaker-bureau-profile-bookable
description: Keep the speaker kit, bureau profile, and speaking page in sync so organizers can book the person from published fees, talks, and proof — without a scavenger hunt.
---

# Keep speaker bureau profile bookable

Public copy of the Task Library skill. Hub: https://blitzmetrics.com/speaker-kit/

**Use this when** a personal brand is taking paid stages (keynotes, workshops, campus talks) and the bureau profile, speaker page, or one-sheet is empty, stale, or still carrying a retired brand.

## Inputs
- Canonical speaker kit in git (this repo) with positioning, bios, fees, programs, testimonials, stages, and media
- Live bureau login (for NSA members this is often eSpeakers; speaker ID and dashboard URL live in `espeakers.md`)
- Live speaker page on the personal-name domain (https://dennisyu.com/speaking/)
- Inquiry path the organizer can submit without emailing a private inbox
- Fees the human has set — never invent a number

## Steps
1. **Read the kit before touching any public form.** Positioning, fees, talk titles, bios, and brand name come from this repo. If the kit and the live page disagree, the kit wins until a human changes the kit.
2. **Lock the brand.** Lead with the current operating company. Retired brands (BlitzMetrics, a Content Factory typo, an old domain) stay as prior-history only. Do not put a street address or private phone on a public bureau profile.
3. **Publish fees.** Bureau profiles that say “inquire” lose search rank and look unfinished. Write the U.S., international, and virtual numbers exactly as `profile/fees.md` states them, plus travel billed separately.
4. **Load programs from `programs/`, not from memory.** Each talk needs a title, format (keynote / workshop / campus), audience, description, and takeaways. Industry rooms (funeral homes, landscapers, campuses, affiliates) get their own program, not one generic “AI talk.”
5. **Fill bio, audience benefit, and one-liner from `profile/`.** Short bio for cards; full bio for the profile. First person on the personal site; third person on bureau directories unless the bureau requires first person.
6. **Put proof on the profile:** canonical headshot, stage photos (real, no stock), one talk video, and named testimonials with role and event. Link the speaker page, not a homepage that buries speaking.
7. **Add three future calendar holds** the organizer can see (named events with dates). Empty calendars read as inactive.
8. **Mirror the same facts on the personal-site speaking page** so Google and the bureau are not telling two stories. Then click the public bureau URL as a stranger and check: name, brand, fees, at least one program, video or photo, inquiry path.
9. **Log the run** as a meta-article that links back to https://blitzmetrics.com/speaker-kit/.

## Definition of done (QA checklist)
- [ ] Public bureau profile shows current brand, published fees, ≥1 program, bio, and a link to the speaker page
- [ ] Speaker page on yourname.com matches the kit on fees, talks, and positioning
- [ ] No retired brand, typo domain, or street address in public fields
- [ ] At least one named testimonial and one real stage photo or talk video
- [ ] Three future calendar dates visible, or an explicit note in the kit that the calendar is the human’s job this week
- [ ] Inquiry path works without a private email

## Example(s)
- Hub — https://blitzmetrics.com/speaker-kit/
- Meta-article — https://blitzmetrics.com/how-we-documented-the-speaker-kit-task/
- This kit — https://github.com/dennisyu/dennis-yu-speaking
- eSpeakers — https://www.espeakers.com/marketplace/profile/48283
- Speaker page — https://dennisyu.com/speaking/

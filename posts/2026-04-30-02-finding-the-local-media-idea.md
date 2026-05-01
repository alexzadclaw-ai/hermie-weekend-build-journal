---
title: "How I scoped a local weekend-guide MVP"
description: "A step-by-step guide to choosing a small local media idea, audience, distribution channel, and first content loop."
date: "2026-04-30"
slug: "finding-the-local-media-idea"
tags: ["local media", "mvp", "telegram", "content strategy"]
canonical_project: "Hermie Weekend"
status: "draft"
---

# How I scoped a local weekend-guide MVP

Hermie Weekend started with a boring human problem: I wanted better weekend ideas near Naperville without digging through stale event calendars, Facebook pages, restaurant posts, park district PDFs, and random listicles.

That is a good MVP shape because the pain is specific. The audience is local. The content expires quickly. The product can be useful before it is complicated.

This is the step-by-step process I used to turn that into a buildable project.

## Step 1: write the one-sentence product

The first version was this:

```text
Hermie Weekend helps people near Naperville find fun things to do this weekend, without scrolling through ten event calendars.
```

That sentence made several decisions:

- the geography is local, not national
- the time window is weekends, not every day
- the output is curated, not exhaustive
- the audience is people who want plans, not event organizers

If the sentence gets longer, the MVP is probably too broad.

## Step 2: choose the first geographic boundary

I used ZIP code 60564 as the anchor because it maps to south Naperville and nearby west-suburban options.

The initial radius does not need to be mathematically perfect. It needs to be useful. For Hermie Weekend, useful meant:

- Naperville
- Aurora
- Wheaton
- Geneva
- nearby DuPage County spots
- occasional worth-the-drive ideas

The rule I gave the agent for weekly picks was: prioritize events close to 60564, but allow a drive when the event is genuinely worth it.

## Step 3: choose the content promise

I did not want "everything happening this weekend." That turns into a directory, and directories are hard to keep fresh.

The promise became:

```text
5 to 8 curated picks for the upcoming Friday through Sunday.
```

That does three things:

- it creates a weekly production rhythm
- it keeps the output short enough for Telegram
- it forces curation instead of scraping everything

A local guide wins by saving attention, not by showing the biggest database.

## Step 4: pick source hierarchy before writing content

The source rules matter because local event information gets messy fast.

The agent was instructed to use this order:

1. Official city and downtown calendars
2. Park districts, libraries, museums, venues, and organizers
3. Chambers of commerce and local tourism sites
4. Secondary discovery sources like Eventbrite, Patch, local newspapers, and Facebook
5. User-submitted tips through the form

Secondary sources are discovery, not proof. If Eventbrite mentions something hosted by a city or venue, the agent should look for the official page before posting.

## Step 5: choose the first distribution channel

I chose Telegram before building a full newsletter or social presence.

The reasons were practical:

- a Telegram channel can be broadcast-only
- subscribers do not need to see each other
- I can post short weekly picks
- the brand can stay anonymous
- it works well with a simple website CTA

The important decision was to use a channel, not a group. A group invites moderation problems. A channel is closer to a lightweight local bulletin.

## Step 6: decide how submissions work

Open comments were not worth it at the start. They create spam, moderation, and prompt-injection risk.

Instead, the project uses a Tally form for event submissions:

```text
https://tally.so/r/b5209g
```

The rule is simple: submissions are tips, not posts. The agent can read them later, but nothing should auto-publish without verification.

## Step 7: define the first automation

The weekly automation prompt needed to be self-contained because scheduled jobs do not inherit the current chat.

The job was set for Wednesday morning. The output should be a Telegram-ready weekend preview for the upcoming Friday through Sunday.

The prompt logic looked like this:

```text
Produce 5 to 8 curated Hermie Weekend picks near ZIP 60564 for the upcoming Friday through Sunday.
Use official or local sources.
Prefer specific times, locations, price notes, and why it is worth going.
End with the event submission form link.
Do not schedule more jobs.
```

That turns the content loop into a draft factory.

## Step 8: decide what not to build

I did not build these on day one:

- user accounts
- comments
- an event database
- a recommendation engine
- paid listings
- a newsletter backend
- a mobile app

Those may become useful later. They are not needed to prove whether people want a better weekend guide.

## Step 9: map the monetization path without adding ads yet

The local guide can monetize later through:

- local sponsorships
- featured placements with disclosure
- affiliate links for tools in the build journal
- ads on the build/tutorial site
- partnerships with local venues or organizers

But the first version should not feel like a coupon site. Trust comes first.

## The reusable local media MVP template

Here is the template I would reuse:

```text
Audience: people near [ZIP/city] who want [specific recurring decision]
Cadence: weekly or daily, not random
Output: 5 to 8 curated picks
Distribution: one channel first
Submissions: form inbox, not public comments
Sources: official first, secondary only for discovery
Website: static landing page with CTA
Automation: draft content on a schedule, human review until trusted
Monetization: mapped but not forced into version one
```

Hermie Weekend is just one example. The same shape could work for rainy-day kids activities, cheap date nights, dog-friendly patios, local food popups, or senior-friendly weekend events.

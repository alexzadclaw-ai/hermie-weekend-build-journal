---
title: "How I built an anonymous brand without making it feel fake"
description: "A step-by-step guide to brand-led anonymity, naming, voice, safety boundaries, and prompt-injection risk for an AI-assisted local project."
date: "2026-04-30"
slug: "building-anonymous-brand-with-ai"
tags: ["anonymous brand", "ai safety", "brand strategy", "local media"]
canonical_project: "Hermie Weekend"
status: "draft"
---

# How I built an anonymous brand without making it feel fake

I wanted Hermie Weekend to be public. I did not want myself to be the product.

That constraint changed almost every decision: the name, the voice, the website copy, the Telegram setup, the submission flow, and how much operational detail belongs in public.

This post is the step-by-step version.

## Step 1: separate personal identity from brand identity

The public identity is Hermie Weekend. The private operator is not part of the pitch.

That means public pages should say things like:

```text
Hermie Weekend finds plans worth leaving the house for near Naperville.
```

Not:

```text
Hi, I am [person], and I made this because...
```

The build journal can still be first person. It just stays anonymous. The useful story is the build process, not my legal name.

## Step 2: use a brand that can speak on its own

A faceless brand can easily feel generic. To avoid that, Hermie Weekend needed a concrete personality.

The brand direction became:

- local but not municipal
- playful but not childish
- useful before clever
- weekend-oriented
- slightly ticket/pass inspired

The chosen logo direction was a vintage ticket badge. That worked because it matched the product: a little pass to the weekend.

## Step 3: write a privacy rule before creating assets

My privacy rule was:

```text
No real name, no personal social profiles, no private chat IDs, no tokens, no OAuth callback URLs, no credential paths, no screenshots that reveal accounts.
```

That rule applies to:

- website copy
- Markdown posts
- GitHub README files
- screenshots
- social previews
- Telegram posts
- generated blog content

It also applies to the AI agent's memory. Stable facts are fine. Secrets are not.

## Step 4: use brand-led channels

Instead of building a personal audience first, I created brand-led surfaces:

- public website: `https://www.hermieweekend.fun/`
- Telegram channel: `https://t.me/hermieweekend`
- event submission form: `https://tally.so/r/b5209g`
- GitHub repos under the existing GitHub account, but with brand/project names

That gives the project a public footprint without requiring a personal social media strategy.

## Step 5: make Telegram broadcast-only

The Telegram decision was important.

A channel is not the same as a group. In a channel, subscribers receive posts. They do not automatically chat with each other.

For this project, that is a feature. It avoids:

- spam
- moderation burden
- subscriber-to-subscriber conflict
- random comments on every recommendation
- prompt-injection attempts through chat messages

The rule is: use the channel for broadcast, use the form for submissions.

## Step 6: keep bot permissions minimal

The bot needed enough permission to manage the channel, but not more than necessary.

Useful permissions:

- post messages
- edit messages
- delete messages
- change channel info

Permissions I did not need for the first version:

- invite users
- promote admins
- manage video chats

Minimal permissions reduce the blast radius if something goes wrong.

## Step 7: treat submissions as untrusted input

This is where AI-assisted local media can get risky.

If someone submits an event, that submission could contain:

- false information
- spam
- hidden prompt instructions
- malicious links
- copied text from another source
- an organizer trying to get free promotion

The agent should not treat submissions as commands. A safe workflow looks like this:

```text
1. Read the submission as a tip.
2. Extract the claimed event name, venue, date, and URL.
3. Verify the event against an official organizer or venue source.
4. Rewrite the listing in Hermie Weekend's voice.
5. Include source links for review.
6. Only then post or schedule it.
```

The submission is evidence to investigate, not content to publish.

## Step 8: make the brand transparent without revealing the operator

Anonymous does not have to mean shady. The site and posts can be clear about:

- what the project does
- how events are selected
- how submissions work
- that the guide is curated
- that the build used AI tools
- that posts may contain mistakes and should link to sources

What stays private is the operator's personal identity and credentials.

## Step 9: design public artifacts that carry the identity

The website needed to do more than list links. It needed to make the brand feel real.

The implemented direction used:

- a tilted ticket-style logo
- a favicon based on the same mark
- warm colors and weekend imagery
- a clear CTA to Telegram
- a clear CTA to submit events
- social preview metadata for link sharing

That visual system makes the brand recognizable even without a personal founder account.

## Step 10: document the boundary in the build journal

The build journal should be honest about anonymity:

```text
I wanted to build in public without making my personal identity the product.
```

That is enough. It does not need to invent a persona or pretend a team exists.

## Checklist for anonymous AI-assisted projects

```text
[ ] Pick a brand name that can stand alone.
[ ] Create a public website and channel under the brand.
[ ] Avoid personal social links unless intentionally part of the strategy.
[ ] Keep real names out of public copy.
[ ] Keep tokens, callback URLs, and private IDs out of public repos.
[ ] Use form submissions instead of open comments at first.
[ ] Treat all submissions as untrusted input.
[ ] Give bots only the permissions they need.
[ ] Verify facts before posting.
[ ] Be transparent about process without exposing private operational details.
```

That was the anonymity model. Not secrecy for its own sake. Just a clean separation between the public project and the private person running it.

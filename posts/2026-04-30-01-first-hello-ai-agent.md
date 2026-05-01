---
title: "How I started an AI-agent build session from a blank chat"
description: "A step-by-step guide to turning a vague first conversation with an AI agent into a scoped build project."
date: "2026-04-30"
slug: "first-hello-ai-agent"
tags: ["ai agents", "project setup", "build log", "planning"]
canonical_project: "Hermie Weekend"
status: "draft"
---

# How I started an AI-agent build session from a blank chat

I did not start with a product brief. I started with a tiny test: say hello, see if the agent was awake, then find out what it could actually do.

That sounds trivial, but it matters. If you are going to let an AI agent touch a real website, GitHub repo, deployment target, or Telegram channel, you need to learn its operating model before you ask for anything ambitious.

This episode is the setup guide I wish I had written before the project began.

## What I was trying to learn

Before asking the agent to build Hermie Weekend, I needed answers to four practical questions:

- Can it use tools, or does it only chat?
- Can it access local files and GitHub?
- Can it deploy or verify a website?
- Can it remember project facts across sessions without leaking private information?

That first "are you there?" was less about conversation and more about probing the workspace.

## Step 1: confirm the agent is live

The first check was simple.

```text
are you there?
```

The agent answered normally. That told me the chat transport was working, but nothing else.

A useful agent is not just a chatbot. For a build project, I need it to run commands, inspect files, push commits, deploy, and verify results. So the next step was to ask about web search.

```text
do you have access to web search?
```

For any project involving current local events, DNS, platform behavior, or docs, this matters. Static model memory is not enough. I want the agent to verify facts from current sources.

## Step 2: establish the working rule

The main working rule was this: do not let the agent merely describe work. Make it do the work and verify it.

That means requests should be phrased as actions:

```text
Move this into its own GitHub repo.
Deploy it to Cloudflare Pages.
Check the live website in a browser.
Run Lighthouse on mobile and desktop.
```

Not:

```text
How would I move this into a repo?
What are the steps to deploy this?
```

Both kinds of prompts are valid, but they produce different behavior. If I want a build partner, I ask for outcomes and make verification part of the task.

## Step 3: give the project a tight constraint

The product idea was intentionally small: a weekend guide for Naperville and the west suburbs.

The constraints were more important than the idea:

- keep me anonymous
- use a brand-led identity instead of a personal one
- keep costs low
- prefer static hosting
- use Telegram as the first distribution channel
- collect event submissions through a form instead of open comments

A good agent can work with constraints. A vague "build me a startup" prompt is too open. A constrained local media MVP is buildable.

## Step 4: define what counts as done

For this project, "done" never meant "the agent produced code." Done meant:

- the site loads on the real domain
- the GitHub repo exists and has a clean commit history
- the Telegram channel is configured
- the social preview works in WhatsApp or Telegram
- Lighthouse and console checks pass
- private information stays out of public files

I kept pushing the agent toward live verification because visual projects can look correct in a file and still fail in production.

## Step 5: capture durable facts, not secrets

The agent had persistent memory, so I used it for stable project facts:

- repo path
- GitHub repo name
- Cloudflare Pages project name
- live domain
- chosen design direction
- Telegram channel URL

I did not want secrets stored there. Tokens, OAuth callback URLs, bot credentials, and private identifiers should never become project memory or blog content.

My rule: memory is for reusable context, not credentials.

## Step 6: use the chat transcript as source material

The transcript became the raw material for this build journal. That does not mean publishing the transcript. Raw chats are messy and full of private operational details.

The useful content is the sequence:

1. test the agent
2. scope the local media idea
3. build the site
4. deploy it
5. launch Telegram
6. fix social previews
7. optimize Lighthouse
8. turn the build into instructional content

That sequence is much more useful than a verbatim chat dump.

## Mistakes to avoid

Do not start by asking for a polished brand. Start by defining the operating loop.

Do not let the agent skip verification. Ask it to check the real URL, not just the local file.

Do not paste secrets into public artifacts. If an OAuth callback or token appears during setup, redact it immediately.

Do not treat AI output as inherently safe. For this project, event submissions and scraped web pages are untrusted input. The agent can summarize them, but it should not blindly publish them.

## The reusable playbook

If I were starting another project with an AI agent, I would use this sequence:

```text
1. Confirm the agent is live.
2. Confirm tool access: files, terminal, GitHub, browser, web search.
3. State the privacy constraints.
4. Define a small public outcome.
5. Ask the agent to create real files, not just ideas.
6. Verify in the browser.
7. Commit and push.
8. Store stable project facts, not secrets.
9. Convert the build history into documentation while it is still fresh.
```

That was the first useful lesson. The hello was not the project. The workflow was.

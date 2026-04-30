---
title: "How I built and deployed a local media website with an AI agent and Cloudflare Pages"
description: "A practical walkthrough of building the Hermie Weekend landing page, moving it into GitHub, deploying it to Cloudflare Pages, and fixing DNS details."
date: "2026-04-30"
slug: "build-deploy-local-media-website-ai-cloudflare-pages"
tags: ["Cloudflare Pages", "GitHub", "static site", "AI coding agent", "DNS", "local media"]
canonical_project: "Hermie Weekend"
status: "draft"
---

# How I built and deployed a local media website with an AI agent and Cloudflare Pages

The first Hermie Weekend website was intentionally simple.

One page. Static HTML and CSS. No CMS. No framework. No backend. No login. No dashboard.

That was the right choice.

A local media idea does not need technical complexity on day one. It needs a page that explains the concept, links to the Telegram channel, and gives local businesses a way to submit events.

## The first website structure

The landing page had a few jobs:

- explain Hermie Weekend in one screen
- make the brand feel real
- link to the Telegram channel
- link to the event submission form
- show example use cases: date night, family plans, rainy-day saves, hidden gems
- feel more like a playful local brand than a generic newsletter

The AI agent helped write and edit the static site files directly. It created the first page, then iterated on the design.

The visual direction became colorful and slightly chaotic: dark background, sticker-like ticket logo, polaroid-style event images, and playful copy.

The site did not need to look like a SaaS landing page. It needed to feel like a weekend pass.

## Moving the project into its own GitHub repo

At first, the website lived inside a broader prototype workspace. That got messy fast.

So I had the agent move Hermie Weekend into a standalone source repository. That made the project easier to manage and deploy.

The repo included:

- `index.html`
- image assets
- favicon assets
- flyer and QR assets
- copy drafts
- `wrangler.toml` for Cloudflare Pages
- `README.md`
- `sitemap.xml`
- `robots.txt`
- redirects for retired or private design exploration pages

That split mattered. A project becomes more real when it has its own repo, its own deploy target, and its own canonical domain.

## Deploying to Cloudflare Pages

Cloudflare Pages was a good fit because the site was static.

The deployment flow was straightforward once authentication was working:

1. Prepare the static site directory.
2. Deploy with Wrangler to the Cloudflare Pages project.
3. Verify the live URL with HTTP checks and browser tests.
4. Keep the GitHub repo as the source of truth.

The production domain became:

`https://www.hermieweekend.fun/`

The Cloudflare Pages preview domain stayed useful for testing individual deployments before checking the custom domain.

## DNS was the boring part, which means it mattered

DNS was not glamorous, but it was one of the places where the agent was useful.

The `www` subdomain pointed to Cloudflare Pages. The root domain had registrar limitations, so the practical setup was a root redirect to the `www` version.

That meant the canonical URL needed to be consistent everywhere:

- canonical link tag
- Open Graph URL
- structured data
- sitemap
- robots file
- QR code
- flyer PDF
- README

This is the kind of detail that is easy to forget when you are building quickly. It is also the kind of detail that makes the project feel less broken when someone actually shares it.

## The site was not done when it deployed

The first deploy was not the end. It was the start of a round of practical fixes:

- the logo looked good on mobile but needed desktop spacing adjustments
- old internal mockup pages needed redirects
- the canonical domain needed to be reflected in metadata
- social previews needed a real image
- Lighthouse found image and accessibility issues

This is where using an AI agent felt different from using a chatbot.

A chatbot can suggest fixes. An agent can edit files, run checks, deploy, and verify the live result.

That loop is the product.

## Why I stayed static

I could have reached for a framework. I did not.

For v1, static HTML was enough. It loaded fast, deployed easily, and kept the project understandable.

The lesson was simple: when the business risk is "will anyone care?" do not spend your time solving framework problems.

Put the page online. Make it shareable. Start publishing.

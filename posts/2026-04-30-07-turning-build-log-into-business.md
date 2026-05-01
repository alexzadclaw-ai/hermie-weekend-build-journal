---
title: "How I turned the build itself into a blog content strategy"
description: "A step-by-step guide to turning an AI-assisted project history into instructional posts, a static blog frontend, and future monetization without stuffing in affiliate links too early."
date: "2026-04-30"
slug: "turning-build-log-into-business"
tags: ["blogging", "seo", "affiliate strategy", "content operations"]
canonical_project: "Hermie Weekend"
status: "draft"
---

# How I turned the build itself into a blog content strategy

At some point I realized Hermie Weekend was two projects.

The first project is the local weekend guide. The second project is the build journal: a transparent tutorial series about using AI agents to build, deploy, launch, and polish a small internet business.

This post explains how I turned the chat history into a blog repo without publishing the raw chat.

## Step 1: define the content angle

The first draft was too shallow. It told the story, but it did not teach enough.

The better angle is instructional:

```text
Every episode should be a step-by-step guide someone can use.
```

That changed the posts from founder diary to practical tutorial.

The target reader is someone searching for things like:

- how to build a local media site with AI
- how to deploy a static site to Cloudflare Pages
- how to launch a Telegram channel for a project
- how to fix WhatsApp link previews
- how to run Lighthouse on a static site
- how to build anonymously without exposing private identity

## Step 2: create a separate repository

The build journal should not live inside the product website repo.

The journal repo is:

```text
alexzadclaw-ai/hermie-weekend-build-journal
```

Local path:

```text
./hermie-weekend-build-journal
```

The structure is intentionally portable:

```text
README.md
index.md
index.html
posts/
  2026-04-30-01-first-hello-ai-agent.md
  2026-04-30-02-finding-the-local-media-idea.md
  2026-04-30-03-building-anonymous-brand-with-ai.md
  2026-04-30-04-building-website-cloudflare-pages.md
  2026-04-30-05-launching-telegram-channel.md
  2026-04-30-06-fixing-dns-social-previews-lighthouse.md
  2026-04-30-07-turning-build-log-into-business.md
scripts/
  verify-frontend.js
```

Markdown with frontmatter keeps the content portable. Later it can move to Astro, Hugo, Jekyll, Next.js, or another static generator.

## Step 3: write frontmatter for every post

Each post uses frontmatter like this:

```md
---
title: "How I fixed DNS, WhatsApp thumbnails, Lighthouse issues, and browser console checks"
description: "A technical step-by-step guide to production polish for a static site."
date: "2026-04-30"
slug: "fixing-dns-social-previews-lighthouse"
tags: ["dns", "open graph", "lighthouse", "playwright", "performance"]
canonical_project: "Hermie Weekend"
status: "draft"
---
```

The important fields are `title`, `description`, `slug`, `tags`, and `status`.

Keeping `status: "draft"` is useful because these are not final published posts yet. They are strong drafts that can be edited before a real blog launch.

## Step 4: convert the transcript into lessons, not a transcript

Raw chat history is not a blog post. It includes false starts, tool outputs, private details, and fragments that only make sense in context.

The conversion process is:

```text
1. Identify the real sequence of work.
2. Group related tasks into episodes.
3. Remove private details and credentials.
4. Turn each episode into a guide.
5. Include commands, file names, and verification steps.
6. Explain what broke and how it was fixed.
7. Keep the first-person voice, but make the reader able to follow along.
```

That is the difference between "content" and documentation.

## Step 5: keep monetization out of the first draft

The goal is ad and affiliate revenue later, but I kept the first version clean.

That means no affiliate links yet. No fake tool rankings. No forced recommendations.

The monetization map is still obvious:

- AI coding agents and AI providers
- hosting platforms
- CDN and DNS tools
- domain registrars
- static site generators
- form tools
- Telegram tooling
- analytics and monitoring tools

But the editorial order matters. Publish useful, specific posts first. Add disclosed affiliate links only where they genuinely fit.

## Step 6: build a quick static frontend

I added a self-contained `index.html` so the repo can be previewed without a full blog framework.

The frontend includes:

- hero section
- seven post cards
- embedded post data
- click-to-read modal
- links to Markdown source files
- a section explaining the future monetization strategy

This is not the final blog engine. It is a preview artifact.

## Step 7: verify the frontend in a browser

I added a Playwright verification script:

```js
const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const file = path.resolve(__dirname, '..', 'index.html');
  const browser = await chromium.launch({ executablePath: '/snap/bin/chromium', headless: true });
  const page = await browser.newPage({ viewport: { width: 1440, height: 1200 } });
  const messages = [];
  const failures = [];

  page.on('console', msg => messages.push({ type: msg.type(), text: msg.text() }));
  page.on('pageerror', err => failures.push({ type: 'pageerror', text: err.message }));
  page.on('requestfailed', req => failures.push({ type: 'requestfailed', url: req.url(), text: req.failure()?.errorText }));

  await page.goto('file://' + file, { waitUntil: 'domcontentloaded' });
  const result = await page.evaluate(() => ({
    title: document.title,
    cards: document.querySelectorAll('.post-card').length,
    postDataCount: JSON.parse(document.getElementById('postData').textContent).length
  }));

  await page.click('a[href^="#post-"]');
  const modal = await page.evaluate(() => ({
    open: document.querySelector('#reader').classList.contains('open'),
    articleChars: document.querySelector('#article').innerText.length
  }));

  console.log(JSON.stringify({ result, modal, messages, failures }, null, 2));
  await browser.close();
})();
```

The check confirms:

- 7 post cards render
- embedded post data loads
- the reader modal opens
- no console errors appear
- no requests fail

## Step 8: push and preview with GitHub HTMLPreview

The repo can be viewed through GitHub HTMLPreview:

```text
https://htmlpreview.github.io/?https://github.com/alexzadclaw-ai/hermie-weekend-build-journal/blob/main/index.html
```

That is enough for a quick review. For production, I would deploy the blog to Cloudflare Pages or another static host.

## Step 9: plan the real blog version

The next version should probably use a static site generator.

A practical stack would be:

```text
Astro or Eleventy
Markdown content collection
one post per URL
RSS feed
sitemap
Open Graph images
analytics
affiliate disclosure page
privacy policy
Cloudflare Pages deployment
```

The current `index.html` is useful for previewing. It is not the final SEO architecture because posts inside a JavaScript modal do not get the same treatment as separate crawlable pages.

## Step 10: create an affiliate policy before adding links

Before monetizing, I need a clear rule:

```text
Affiliate links are allowed only when the post already explains the tool through real use, and the link is disclosed near the recommendation.
```

I do not want the blog to become a fake review site.

A future disclosure could say:

```text
Some posts may contain affiliate links. If I recommend a tool, it is because I used it in the project or would use it for the same job again.
```

## Build-journal checklist

```text
[ ] Create separate repo.
[ ] Write posts in Markdown with frontmatter.
[ ] Keep posts in draft status.
[ ] Remove real names and private identifiers.
[ ] Remove tokens, OAuth URLs, and credential details.
[ ] Rewrite each episode as a step-by-step guide.
[ ] Include commands and file paths when useful.
[ ] Add verification steps, not just build steps.
[ ] Keep affiliate links out of the first draft.
[ ] Build a preview frontend.
[ ] Verify frontend in a browser.
[ ] Push to GitHub.
[ ] Later, move to a real static blog generator.
```

The bigger lesson is simple: if an AI agent helps build the project, the build process can become its own asset. But only if the posts teach something concrete.

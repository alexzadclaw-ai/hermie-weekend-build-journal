---
title: "How I built and deployed the Hermie Weekend website on Cloudflare Pages"
description: "A practical guide to creating a static landing page, moving it into its own GitHub repo, deploying with Wrangler, and verifying the live site."
date: "2026-04-30"
slug: "building-website-cloudflare-pages"
tags: ["cloudflare pages", "static site", "github", "frontend"]
canonical_project: "Hermie Weekend"
status: "draft"
---

# How I built and deployed the Hermie Weekend website on Cloudflare Pages

The website had one job: make Hermie Weekend feel real and send people to the Telegram channel or event submission form.

I did not need a framework for that. A static HTML/CSS site was enough.

This is the build process as a guide.

## Step 1: decide what the landing page must do

Before writing code, I defined the page requirements:

- explain the product in one screen
- link to the Telegram channel
- link to the event submission form
- show the local/Naperville focus
- feel more like a weekend pass than a generic SaaS page
- work well on mobile
- be easy to deploy as static files

The first version did not need a CMS, database, authentication, or admin UI.

## Step 2: create the static site files

The core site used plain files:

```text
index.html
assets/
  hermie-ticket-logo.svg
  hermie-ticket-favicon.svg
  hermie-ticket-favicon.png
  hermie-social-card.png
sitemap.xml
robots.txt
_redirects
wrangler.toml
README.md
```

The landing page included:

- hero copy
- Telegram CTA
- Tally submission CTA
- local weekend positioning
- visual brand elements
- Open Graph metadata
- JSON-LD metadata

A static site is boring in the best way. You can inspect every file, deploy quickly, and avoid a whole class of runtime failures.

## Step 3: move the project into its own GitHub repo

The site originally lived inside a broader prototypes folder. I moved it into a standalone repo so deployment and ownership were clean.

The local path became:

```text
./hermie-weekend
```

The GitHub repo became:

```text
alexzadclaw-ai/hermie-weekend
```

The general extraction pattern is:

```bash
OLD_REPO=/path/to/old/repo
SUBDIR=site-or-project-folder
NEW_DIR=/path/to/new/project

cp -a "$OLD_REPO/$SUBDIR" "$NEW_DIR"
cd "$NEW_DIR"

git init -b main
git add .
git commit -m "Initial site"
gh repo create repo-name --public --source . --remote origin --push
```

If GitHub CLI creates an SSH remote and the push fails in a headless environment, switch to HTTPS:

```bash
git remote set-url origin https://github.com/OWNER/REPO.git
git push -u origin main
```

That happened in a related repo later, so it is worth knowing.

## Step 4: configure Cloudflare Pages

The project uses Cloudflare Pages with Wrangler.

A minimal `wrangler.toml` for a static Pages project can look like this:

```toml
name = "hermie-weekend"
pages_build_output_dir = "."
```

For manual deploys, I used a clean deploy directory so random local design artifacts would not get published:

```bash
rm -rf /tmp/hermie-weekend-deploy
mkdir -p /tmp/hermie-weekend-deploy
rsync -a \
  --exclude='.git' \
  --exclude='node_modules' \
  --exclude='*.log' \
  ./ /tmp/hermie-weekend-deploy/

npx wrangler pages deploy /tmp/hermie-weekend-deploy \
  --project-name hermie-weekend \
  --branch main \
  --commit-dirty=true
```

The exact exclude list depends on the project. The point is to deploy the public site, not every scratch file.

## Step 5: connect the domain

The canonical site URL became:

```text
https://www.hermieweekend.fun/
```

The root domain forwards to the `www` domain. The `www` record points at Cloudflare Pages.

The page metadata had to match the canonical domain:

```html
<link rel="canonical" href="https://www.hermieweekend.fun/" />
<meta property="og:url" content="https://www.hermieweekend.fun/" />
```

I also updated `sitemap.xml`, `robots.txt`, QR code assets, and README references so the public URL was consistent everywhere.

## Step 6: implement the selected logo direction

The selected mark was a vintage ticket/pass badge.

The production version used:

```text
assets/hermie-ticket-logo.svg
assets/hermie-ticket-favicon.svg
assets/hermie-ticket-favicon.png
```

The header uses the logo as an absolutely positioned image with a slight rotation and drop shadow. A detail that mattered: global `img { max-width: 100%; }` rules can shrink or clip positioned logos. The fix was to explicitly set `max-width: none` for the desktop logo and restore safe sizing on mobile.

The key lesson: if a logo is meant to break out of a container, test the actual browser layout. CSS that looks reasonable in isolation can clip in the header.

## Step 7: hide design artifacts from public browsing

During design exploration, the repo had files like logo mockups and concept sheets. I did not want those indexed or treated as public pages.

Cloudflare Pages supports `_redirects`. I used it to redirect retired paths back to `/`.

Example:

```text
/hermie-logo-ideas.html / 302
/hermie-ticket-logo-variations.html / 302
/checklist.html / 301
```

The exact list should match whatever scratch files exist. The goal is to avoid public duplicate pages and half-finished artifacts.

## Step 8: verify the live site with a browser

A deploy is not done until the live site has been checked.

I used Playwright/Chromium to verify:

- status code is 200
- final URL is correct
- title is correct
- hero text appears
- Telegram links exist
- Tally links exist
- no browser console errors
- no failed requests

A simple Playwright check looks like this:

```js
const { chromium } = require('playwright');

const browser = await chromium.launch({
  executablePath: '/snap/bin/chromium',
  headless: true
});
const page = await browser.newPage();
const errors = [];
page.on('console', msg => {
  if (msg.type() === 'error') errors.push(msg.text());
});
await page.goto('https://www.hermieweekend.fun/', { waitUntil: 'networkidle' });
console.log(await page.title());
console.log(await page.locator('a[href*="t.me/hermieweekend"]').count());
console.log(errors);
await browser.close();
```

## Step 9: commit after each meaningful fix

The site evolved through small commits:

- initial standalone site
- logo and favicon
- redirect scratch files
- header spacing fix
- desktop logo crop fix
- domain metadata update
- social preview image metadata
- Lighthouse improvements

That commit history made it easier to reason about what changed.

## Step 10: keep the site simple until the content loop works

A static landing page is enough for this stage. The project needs audience and content rhythm before it needs a bigger stack.

The website is the front door. The Telegram channel is the first distribution product. The form is the first feedback loop.

That is enough surface area for an MVP.

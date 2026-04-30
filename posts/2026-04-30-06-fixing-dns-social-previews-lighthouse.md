---
title: "The unsexy launch work: DNS, WhatsApp thumbnails, Lighthouse, and browser console checks"
description: "A transparent technical post about the small deployment and quality fixes that made Hermie Weekend feel shareable and production-ready."
date: "2026-04-30"
slug: "dns-whatsapp-thumbnails-lighthouse-browser-console-checks"
tags: ["Lighthouse", "Open Graph", "WhatsApp thumbnails", "Cloudflare Pages", "technical SEO", "web performance"]
canonical_project: "Hermie Weekend"
status: "draft"
---

# The unsexy launch work: DNS, WhatsApp thumbnails, Lighthouse, and browser console checks

The most important launch work was not the fun stuff.

The fun stuff was the name, the logo, the colorful website, the Telegram posts. The real launch work was the pile of tiny fixes that make a project feel trustworthy when someone opens it on their phone.

This is the part people skip in launch stories, so I want to write it down.

## Canonical domain cleanup

The public domain became:

`https://www.hermieweekend.fun/`

That meant every reference needed to agree:

- canonical tag
- Open Graph URL
- JSON-LD structured data
- sitemap
- robots file
- QR code
- flyer PDF
- README
- old page redirects

This sounds tedious because it is. But it matters.

If you are building a public site, you do not want search engines, link previews, QR codes, and users all seeing different versions of the project.

## The WhatsApp thumbnail problem

When I shared the site in WhatsApp, there was no thumbnail.

The page had a title and description, but it did not have a proper Open Graph image. WhatsApp needs a crawlable image URL in the page metadata. Without it, it may show a blank preview or try to guess from whatever assets it finds.

The fix was to create a dedicated 1200 by 630 social preview image and add metadata like:

```html
<meta property="og:image" content="https://www.hermieweekend.fun/assets/hermie-social-card.png" />
<meta property="og:image:width" content="1200" />
<meta property="og:image:height" content="630" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:image" content="https://www.hermieweekend.fun/assets/hermie-social-card.png" />
```

Then I verified the live page and the image URL.

The annoying part was cache. WhatsApp caches link previews aggressively. A cache-busted URL worked immediately, while the plain URL needed time to refresh.

The lesson: fix the metadata, verify it live, then be patient with the preview cache.

## Lighthouse found real issues

After the site was live, I ran Lighthouse on both mobile and desktop.

The site was already decent, but Lighthouse found three things worth fixing:

1. Oversized external images
2. Color contrast problems in a fake phone mockup
3. A decorative heading that broke heading order

The image issue was the biggest performance opportunity. The site used Unsplash URLs with larger-than-needed widths and high quality settings. I reduced the requested dimensions, added explicit crop sizes, and lowered image quality.

The improvement was noticeable in the audit:

- mobile image savings dropped from hundreds of kilobytes to a small leftover warning
- desktop image savings dropped from hundreds of kilobytes to a small leftover warning

The accessibility fixes were cleaner:

- darkened the phone header color
- darkened the pink label text
- changed decorative ticket text from an `h3` to a styled paragraph

After that, accessibility hit 100.

## Console checks

I also checked the live site in a browser with Playwright.

The result was boring, which is what you want:

- no JavaScript console errors
- no page errors
- no failed requests
- live status 200

A static site can still fail in weird ways: missing assets, broken redirects, script errors from third-party embeds, or layout problems that do not show up in a simple HTTP check.

Browser verification is worth doing.

## The real value of the AI agent

This part made the AI agent feel less like a writing tool and more like an operator.

It did not just say "you should add Open Graph tags." It created the image, patched the HTML, committed the change, deployed it, fetched the live site, verified the metadata, and reran Lighthouse.

That loop is powerful:

1. observe a real issue
2. inspect the code
3. make the change
4. deploy
5. verify from the outside
6. repeat if needed

For small projects, that loop is often the difference between an idea and something that actually works in public.

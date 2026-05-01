---
title: "How I fixed DNS, WhatsApp thumbnails, Lighthouse issues, and browser console checks"
description: "A technical step-by-step guide to production polish for a static site: canonical domains, Open Graph images, Lighthouse audits, accessibility fixes, and Playwright console checks."
date: "2026-04-30"
slug: "fixing-dns-social-previews-lighthouse"
tags: ["dns", "open graph", "lighthouse", "playwright", "performance"]
canonical_project: "Hermie Weekend"
status: "draft"
---

# How I fixed DNS, WhatsApp thumbnails, Lighthouse issues, and browser console checks

The most annoying launch work was also the most useful: DNS, social previews, Lighthouse, browser console checks, and little layout fixes.

This is the polish layer that makes a tiny static site feel real.

## Step 1: choose the canonical domain

The canonical URL became:

```text
https://www.hermieweekend.fun/
```

The root domain forwards to the `www` domain. That means every public metadata field should point at the same canonical URL.

In `index.html`:

```html
<link rel="canonical" href="https://www.hermieweekend.fun/" />
<meta property="og:url" content="https://www.hermieweekend.fun/" />
```

In `sitemap.xml`:

```xml
<loc>https://www.hermieweekend.fun/</loc>
```

In `robots.txt`:

```text
Sitemap: https://www.hermieweekend.fun/sitemap.xml
```

Consistency matters because scrapers, search engines, and messaging apps are picky in different ways.

## Step 2: verify redirects

I checked the HTTP behavior directly.

```bash
python3 - <<'PY'
import urllib.request
for url in ['http://www.hermieweekend.fun/', 'https://www.hermieweekend.fun/']:
    r = urllib.request.urlopen(url, timeout=30)
    print(url, r.status, r.geturl())
PY
```

The goal:

- HTTP should end up on HTTPS
- root should end up on `www` if forwarding is configured that way
- the final page should return 200

## Step 3: add a real Open Graph image

WhatsApp showed no thumbnail at first because the page did not have a proper `og:image`.

The fix was to create a 1200 by 630 PNG:

```text
assets/hermie-social-card.png
```

Then add the metadata:

```html
<meta property="og:image" content="https://www.hermieweekend.fun/assets/hermie-social-card.png" />
<meta property="og:image:secure_url" content="https://www.hermieweekend.fun/assets/hermie-social-card.png" />
<meta property="og:image:type" content="image/png" />
<meta property="og:image:width" content="1200" />
<meta property="og:image:height" content="630" />
<meta property="og:image:alt" content="Hermie Weekend - plans worth leaving the house for near Naperville" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:image" content="https://www.hermieweekend.fun/assets/hermie-social-card.png" />
```

A favicon is not enough. A social card should be large, crawlable, and referenced with absolute HTTPS URLs.

## Step 4: verify social metadata live

After deploying, I fetched the live HTML and image.

```bash
python3 - <<'PY'
import urllib.request, re
html = urllib.request.urlopen('https://www.hermieweekend.fun/', timeout=30).read().decode('utf-8','ignore')
match = re.search(r'<meta property="og:image" content="([^"]+)"', html)
print(match.group(1) if match else 'missing og:image')

img = urllib.request.urlopen('https://www.hermieweekend.fun/assets/hermie-social-card.png', timeout=30)
print(img.status, img.headers.get('content-type'))
PY
```

Expected result:

```text
https://www.hermieweekend.fun/assets/hermie-social-card.png
200 image/png
```

## Step 5: understand WhatsApp caching

After the fix, the cache-busted URL worked:

```text
https://www.hermieweekend.fun/?v=2
```

The plain URL could still show the old missing thumbnail because WhatsApp caches previews aggressively.

That does not mean the site is still broken. It means the scraper cached the old response.

When testing social previews, use:

- a fresh chat
- the canonical HTTPS URL
- a temporary query parameter if needed
- direct fetches to verify the metadata and image

## Step 6: check browser console errors

I used Playwright to check the live site in Chromium.

```js
const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({
    executablePath: '/snap/bin/chromium',
    headless: true
  });
  const page = await browser.newPage();
  const consoleMessages = [];
  const failedRequests = [];

  page.on('console', msg => consoleMessages.push({ type: msg.type(), text: msg.text() }));
  page.on('pageerror', err => consoleMessages.push({ type: 'pageerror', text: err.message }));
  page.on('requestfailed', req => failedRequests.push({ url: req.url(), error: req.failure()?.errorText }));

  const response = await page.goto('https://www.hermieweekend.fun/', { waitUntil: 'networkidle' });
  console.log({ status: response.status(), title: await page.title(), consoleMessages, failedRequests });
  await browser.close();
})();
```

The live site had no JS console errors, no page errors, and no failed requests.

## Step 7: run Lighthouse mobile and desktop

I ran Lighthouse with Chromium.

Mobile:

```bash
npx --yes lighthouse https://www.hermieweekend.fun/ \
  --chrome-path=/snap/bin/chromium \
  --chrome-flags='--headless=new --no-sandbox --disable-gpu' \
  --form-factor=mobile \
  --screenEmulation.mobile=true \
  --output=json \
  --output-path=/tmp/hermie-lighthouse/mobile.json \
  --quiet
```

Desktop:

```bash
npx --yes lighthouse https://www.hermieweekend.fun/ \
  --chrome-path=/snap/bin/chromium \
  --chrome-flags='--headless=new --no-sandbox --disable-gpu' \
  --form-factor=desktop \
  --screenEmulation.mobile=false \
  --screenEmulation.width=1350 \
  --screenEmulation.height=940 \
  --screenEmulation.deviceScaleFactor=1 \
  --output=json \
  --output-path=/tmp/hermie-lighthouse/desktop.json \
  --quiet
```

## Step 8: parse the reports

I used a small Python parser:

```python
import json, pathlib
for label in ['mobile', 'desktop']:
    data = json.loads(pathlib.Path(f'/tmp/hermie-lighthouse/{label}.json').read_text())
    print(label)
    for key in ['performance', 'accessibility', 'best-practices', 'seo']:
        print(key, round(data['categories'][key]['score'] * 100))
    for audit in ['uses-optimized-images', 'color-contrast', 'heading-order']:
        a = data['audits'].get(audit)
        if a:
            print(audit, a.get('score'), a.get('displayValue'))
```

The first pass showed three useful fixes:

- oversized external images
- color contrast in the fake phone mockup
- heading order from a decorative `h3`

## Step 9: fix image delivery

The site used Unsplash images with widths larger than their rendered size.

The quick fix was to reduce query parameters:

```text
w=900&q=82 -> w=420&h=400&q=55
w=1300&q=82 -> w=680&h=455&q=55
```

For a more mature site, I would host local optimized images and use responsive `srcset`. For this MVP, trimming the external image payload was enough.

Lighthouse image-delivery savings dropped from hundreds of KB to a small leftover warning.

## Step 10: fix accessibility issues

The phone mockup had contrast problems.

I changed the green header and pink label color:

```css
.phone-head,
.head {
  background: #147a5a;
}

.msg b {
  color: #c72f62;
}
```

Then I changed a decorative heading:

```html
<h3>5 picks. 45 seconds.</h3>
```

into:

```html
<p class="ticket-title">5 picks. 45 seconds.</p>
```

A decorative label should not break the page heading order.

## Step 11: retest after deployment

After the fixes, mobile Lighthouse hit 100 across categories. Desktop performance varied, but accessibility, best practices, and SEO were 100.

The desktop retest showed:

```text
Performance: 88
Accessibility: 100
Best Practices: 100
SEO: 100
FCP: 1.0s
LCP: 2.1s
TBT: 0ms
CLS: 0
```

The remaining desktop performance variance came from LCP timing, mostly the large hero text and network conditions. That is acceptable for the first version.

## Production polish checklist

```text
[ ] Canonical URL is consistent.
[ ] HTTP redirects to HTTPS.
[ ] Root domain resolves or forwards intentionally.
[ ] sitemap.xml and robots.txt use the canonical domain.
[ ] Open Graph image exists and returns 200.
[ ] Social metadata uses absolute HTTPS URLs.
[ ] WhatsApp cache behavior is accounted for.
[ ] Browser console has no errors.
[ ] Lighthouse mobile and desktop are checked.
[ ] Color contrast passes.
[ ] Heading order passes.
[ ] Images are not wildly oversized.
[ ] Changes are committed and deployed.
```

This is not glamorous work. It is the work that stops a small project from feeling broken when someone shares it.

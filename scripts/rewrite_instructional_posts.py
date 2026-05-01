from pathlib import Path
import shutil
root = Path(__file__).resolve().parents[1]
posts_dir = root / "posts"
posts_dir.mkdir(exist_ok=True)

posts = {
"2026-04-30-01-first-hello-ai-agent.md": r'''---
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
''',
"2026-04-30-02-finding-the-local-media-idea.md": r'''---
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
''',
"2026-04-30-03-building-anonymous-brand-with-ai.md": r'''---
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
''',
"2026-04-30-04-building-website-cloudflare-pages.md": r'''---
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
/home/claw/prototypes/hermie-weekend
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
''',
"2026-04-30-05-launching-telegram-channel.md": r'''---
title: "How I launched a Telegram channel for a local weekend guide"
description: "A step-by-step guide to configuring a broadcast-only Telegram channel, writing starter posts, using a bot safely, and setting a weekly content cadence."
date: "2026-04-30"
slug: "launching-telegram-channel"
tags: ["telegram", "local media", "automation", "content operations"]
canonical_project: "Hermie Weekend"
status: "draft"
---

# How I launched a Telegram channel for a local weekend guide

The website made Hermie Weekend look real. The Telegram channel made it distributable.

For a local weekend guide, Telegram is useful because it supports a simple broadcast model. People subscribe. I post. Nobody needs an account on my website, and I do not need to moderate comments on day one.

Here is the setup process.

## Step 1: choose channel, not group

Telegram has channels and groups.

For Hermie Weekend, a channel was the right choice:

- subscribers receive posts
- subscribers do not automatically chat with each other
- the brand can stay anonymous
- the channel stays clean
- moderation is simpler

A group might be useful later, but only if comments become worth the moderation cost.

## Step 2: set the public identity

The public channel is:

```text
https://t.me/hermieweekend
```

The channel title is:

```text
Hermie Weekend
```

The description explains the promise:

```text
Weekend plans near Naperville and the west suburbs. Curated picks, local finds, and ideas worth leaving the house for.
```

The exact copy can change, but the description should answer three questions quickly:

- what is this?
- where is it for?
- why should I subscribe?

## Step 3: add the bot as an admin

To let the AI workflow post or update the channel, I added a bot as a channel admin.

The bot needed only a small permission set:

- post messages
- edit messages
- delete messages
- change channel info

It did not need permission to invite users, promote admins, or manage video chats.

The permission principle is simple: give the bot the least access needed to operate the channel.

## Step 4: use the Bot API without leaking the token

Some messaging integrations can send to a default chat but may not resolve a newly created channel by username. When that happened, the workaround was to use the Telegram Bot API directly through the local environment.

The important part: do not print the token.

A safe shell pattern is:

```bash
python3 - <<'PY'
import os, urllib.request, urllib.parse, json

TOKEN = os.environ['TELEGRAM_BOT_TOKEN']
CHAT_ID = os.environ['TELEGRAM_CHANNEL_ID']
text = 'Test post from Hermie Weekend.'

url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
data = urllib.parse.urlencode({
    'chat_id': CHAT_ID,
    'text': text,
    'disable_web_page_preview': False,
}).encode()

with urllib.request.urlopen(url, data=data, timeout=30) as r:
    result = json.loads(r.read().decode())
    print({'ok': result.get('ok'), 'message_id': result.get('result', {}).get('message_id')})
PY
```

Notice what gets printed: success state and message ID. Not the token.

## Step 5: create starter channel posts

An empty channel feels abandoned. I prepared a small launch pack:

1. pinned welcome post
2. what Hermie Weekend is
3. how to use the channel
4. how to submit events
5. first sample weekend-style posts

The copy lives in the repo so it can be edited and reused:

```text
copy/telegram-launch-posts.md
```

A good pinned post should include:

- the value proposition
- geography
- posting cadence
- submission link
- a quick note that the channel is broadcast-only

## Step 6: pin the welcome post

A pinned post acts like onboarding for every new subscriber.

The Bot API flow is:

```text
sendMessage -> get message_id -> pinChatMessage
```

The pin call looks like this conceptually:

```bash
curl -s -X POST "https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/pinChatMessage" \
  -d "chat_id=$TELEGRAM_CHANNEL_ID" \
  -d "message_id=$MESSAGE_ID" \
  -d "disable_notification=true"
```

Again, do not paste real tokens into docs, logs, or commits.

## Step 7: upload the channel avatar

The avatar matters more than I expected. A Telegram channel with the default icon feels temporary.

The avatar was a 640 by 640 PNG based on the ticket/pass brand:

```text
assets/hermie-telegram-avatar.png
```

Before uploading, I verified the file:

```bash
file assets/hermie-telegram-avatar.png
```

Expected shape:

```text
PNG image data, 640 x 640
```

Then I uploaded it through the Telegram API/admin flow and verified the channel had a photo.

## Step 8: schedule the weekly draft

The weekly content job runs Wednesday morning. That gives time to review and post before the weekend.

The job prompt is self-contained because scheduled runs do not remember the current chat.

A good prompt includes:

```text
You are preparing Hermie Weekend's weekly Telegram picks.
Find 5 to 8 events near ZIP 60564 for the upcoming Friday through Sunday.
Use official/local sources first.
Include event name, date/time, location, price if available, source URL, and why it is worth going.
Keep the final copy Telegram-friendly.
End with: Submit events: https://tally.so/r/b5209g
Do not schedule new jobs.
```

The automation should draft. I still want human review until the sourcing pattern is proven.

## Step 9: define the no-chat policy

To enforce no chatting:

- use a Telegram channel
- do not link a discussion group
- keep comments disabled
- route submissions to Tally
- avoid inviting open-ended replies in posts

This keeps the product simple. People get weekend ideas. Organizers submit through a form. The channel does not become a moderation surface.

## Step 10: build the first growth loop

The first growth loop is basic:

```text
Website -> Telegram subscribe -> weekly useful picks -> subscribers share posts -> local organizers submit events -> better weekly picks
```

The site, channel, and form are enough to run that loop.

## Telegram launch checklist

```text
[ ] Create channel.
[ ] Set public username.
[ ] Set title and description.
[ ] Add brand avatar.
[ ] Add bot as admin with minimal permissions.
[ ] Publish and pin welcome post.
[ ] Publish starter posts.
[ ] Link Telegram from website.
[ ] Link submission form from Telegram and website.
[ ] Schedule weekly draft job.
[ ] Keep discussion group disabled until moderation is worth it.
```

That launched the distribution layer. The next challenge was making shared links look good.
''',
"2026-04-30-06-fixing-dns-social-previews-lighthouse.md": r'''---
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
''',
"2026-04-30-07-turning-build-log-into-business.md": r'''---
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
/home/claw/prototypes/hermie-weekend-build-journal
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
'''
}

for name, content in posts.items():
    (posts_dir / name).write_text(content)

(root / "index.md").write_text("""---
title: "Hermie Weekend build journal"
description: "A technical, anonymous, step-by-step series about building Hermie Weekend with an AI agent."
status: "draft"
---

# Hermie Weekend build journal

This repo contains seven instructional build-journal posts about creating Hermie Weekend, an anonymous local weekend guide for Naperville and the west suburbs.

The series is written in first person, but it avoids personal identity details. Each episode is structured as a practical guide with concrete steps, commands, files, verification checks, and tradeoffs.

## Posts

1. [How I started an AI-agent build session from a blank chat](posts/2026-04-30-01-first-hello-ai-agent.md)
2. [How I scoped a local weekend-guide MVP](posts/2026-04-30-02-finding-the-local-media-idea.md)
3. [How I built an anonymous brand without making it feel fake](posts/2026-04-30-03-building-anonymous-brand-with-ai.md)
4. [How I built and deployed the Hermie Weekend website on Cloudflare Pages](posts/2026-04-30-04-building-website-cloudflare-pages.md)
5. [How I launched a Telegram channel for a local weekend guide](posts/2026-04-30-05-launching-telegram-channel.md)
6. [How I fixed DNS, WhatsApp thumbnails, Lighthouse issues, and browser console checks](posts/2026-04-30-06-fixing-dns-social-previews-lighthouse.md)
7. [How I turned the build itself into a blog content strategy](posts/2026-04-30-07-turning-build-log-into-business.md)
""")

(root / "README.md").write_text("""# Hermie Weekend build journal

A public, anonymous, Markdown-first build journal about creating Hermie Weekend with an AI agent.

The series is intentionally instructional. Each post is a step-by-step guide covering a specific part of the project:

- starting an AI-agent build workflow
- scoping a local weekend-guide MVP
- building an anonymous brand
- deploying a static site to Cloudflare Pages
- launching a Telegram channel
- fixing DNS, Open Graph previews, Lighthouse issues, and console errors
- turning the build history into a future monetizable blog

## Preview

- Static HTML preview: https://htmlpreview.github.io/?https://github.com/alexzadclaw-ai/hermie-weekend-build-journal/blob/main/index.html
- Source repo: https://github.com/alexzadclaw-ai/hermie-weekend-build-journal

## Structure

```text
README.md
index.md
index.html
posts/
scripts/
```

Posts are Markdown with frontmatter and `status: "draft"`.

## Privacy

The posts avoid real names, private chat IDs, OAuth callback URLs, tokens, and credential details. They describe the workflow without publishing secrets.
""")

print("rewrote", len(posts), "posts")

---
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

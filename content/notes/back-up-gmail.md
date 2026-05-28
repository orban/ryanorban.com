---
title: Back That Gmail Up
date: 2012-05-27
categories:
  - gmail
  - backup
  - email
  - tools
  - self-hosting
description: Jerod Santo's guide to backing up Gmail using getmail or similar IMAP tools — a practical reminder that cloud-hosted email is not automatically backed up and depends entirely on Google's availability and goodwill.
params:
  source: pinboard
  sourceUrl: http://blog.jerodsanto.net/2012/05/back-that-gmail-up/
---

![Back That Gmail Up](/images/notes/back-up-gmail.png)

## Summary

Jerod Santo's post (from the Changelog blog) addressed a real vulnerability that many Gmail users ignored: Gmail is not inherently backed up. Google maintains reliability and redundancy internally, but if your account gets hacked, suspended, or hit by a bug that deletes data, there's no user-accessible restore. The only reliable protection is a local copy under your control.

The solution in 2012 was IMAP-based backup: tools like getmail, offlineimap, or fetchmail can sync a Gmail account to a local Maildir or mbox folder via IMAP. Run on a cron schedule, this creates an incremental local backup. The result is all your email in a standard format that any mail client can read, independent of Google.

The post likely also covered the Google Takeout alternative for one-time exports (launched March 2012, right before this bookmark), which lets you download your Gmail as a single mbox file. Takeout is useful for migration but not for ongoing incremental backup.

The deeper concern was cloud dependency: when all your email lives in one cloud provider's hands, you're exposed to account lockouts, policy changes, and service outages. The 2012 indie hacker community was particularly vocal about this — maintaining copies of your data on infrastructure you control was a recurring theme alongside self-hosting movements.

## Key points

- Gmail provides no user-accessible backup or restore — data is at Google's mercy.
- getmail / offlineimap: IMAP sync tools for creating local Maildir copies on a cron schedule.
- Google Takeout (launched March 2012): one-time mbox export — useful for migration, not ongoing backup.
- Cloud dependency risk: account suspension, hacking, or bugs can cause permanent data loss without a local copy.
- Standard mbox/Maildir format means backups are readable by any mail client — not locked to Gmail.

[Original](http://blog.jerodsanto.net/2012/05/back-that-gmail-up/)

---
title: "Field Theory: AI context and command toolkit for macOS"
date: 2026-03-10
categories:
  - developer-tools
  - macos
  - ai-tools
  - voice
  - productivity
description: Field Theory is a macOS app for developers that stacks screenshots into AI context, makes markdown commands portable across Claude/ChatGPT/Cursor, and handles local voice transcription on-device. Clipboard-based, no integrations required.
params:
  source: pinboard
  sourceUrl: https://www.fieldtheory.dev/
---

![Field Theory: AI context and command toolkit for macOS](/images/notes/fieldtheory.png)

## Summary

Field Theory is a macOS productivity app for developers that solves a cluster of friction points that show up when working heavily with AI tools. The three headline features are context stacking (capturing and organizing screenshots and inputs into richer AI context), portable commands (pointing the app at a folder of Markdown files to make them available across Claude, ChatGPT, Cursor, and other platforms via `Cmd+Shift+K`), and local voice transcription entirely on-device without internet.

The portable commands feature is the most interesting architecturally. Rather than maintaining separate slash command libraries in each tool, you maintain one folder of Markdown files and Field Theory makes them universally available via keyboard shortcut. The commands work via clipboard, so there's no integration layer needed — they paste into whatever AI interface you have open.

Voice transcription on-device means no audio is sent to external services. The Auto-improve feature refines spoken prompts into polished written text automatically. An annotation tool lets you draw on screenshots before pasting them into conversations. The Priority Mic feature prevents Bluetooth headphone interference — a recurring frustration when switching audio devices mid-session.

## Key points

- Portable commands from Markdown files — one library of prompts/commands accessible across any AI tool via keyboard shortcut.
- Local voice transcription with no internet dependency — audio stays on the device.
- Context stacking for richer AI inputs: combine multiple screenshots and inputs before sending.
- Clipboard-based operation: works with any AI interface, no API keys or custom integrations.
- Requires macOS 14+ with Apple Silicon (M1 or later).

[Original](https://www.fieldtheory.dev/)

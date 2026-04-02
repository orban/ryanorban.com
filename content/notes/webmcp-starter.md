---
title: "WebMCP Starter: demo for the WebMCP browser standard"
date: 2026-02-15
categories:
  - mcp
  - web-standards
  - browser
  - ai-agents
  - demo
description: webmcp-starter is a demo app for WebMCP — a proposed web standard that exposes structured tools for AI browser agents directly from web pages. A food delivery app with 9 WebMCP tools demonstrates the full ordering flow.
params:
  source: pinboard
  sourceUrl: https://github.com/Doriandarko/webmcp-starter
---

![WebMCP Starter: demo for the WebMCP browser standard](/images/notes/webmcp-starter.png)

## Summary

[webmcp-starter](/notes/webmcp-starter/) is a demo application by Doriandarko showcasing WebMCP — a proposed web standard (from the Web Machine Learning Working Group at W3C) that lets web pages expose structured tools directly to AI agents running in the browser. Rather than an agent having to scrape and interpret HTML, WebMCP gives pages a way to declare \"here are the actions you can take on this page\" as typed, callable tools — similar to how MCP works for desktop agents but native to the browser.

The demo is a food delivery app (\Midnight Eats\) with 9 tools covering a complete ordering flow: search restaurants, browse menu, add/remove cart items, apply promo codes, track order, and checkout. The checkout tool is declarative (an HTML form); the others are imperative API calls. You test it with Chrome Canary with the WebMCP flag enabled, plus the Model Context Tool Inspector extension.

The significance: if WebMCP becomes a web standard, every website could become natively agent-accessible without scraping. This is the same direction as OpenAI's Operator and Anthropic's Computer Use, but instead of agents learning to interact with general UI, the website explicitly declares its agent interface. The standard is early (requires Chrome Canary flag), but the demo shows the development experience is already coherent.

## Key points

- WebMCP: proposed web standard for exposing structured tools to AI browser agents natively.
- Web pages declare callable tools (imperative API-style + declarative HTML forms) — no scraping needed.
- Demo: food delivery app with 9 tools covering complete DoorDash-style ordering flow.
- Requires Chrome Canary with `#enable-webmcp-testing` flag + Model Context Tool Inspector extension.
- Complementary to browser automation (Computer Use, Playwright) — explicit agent interfaces vs. learned UI interaction.
- Related to MCP protocol but native to the browser context.

[Original](https://github.com/Doriandarko/webmcp-starter)

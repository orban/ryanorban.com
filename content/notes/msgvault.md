---
title: "msgvault: personal email archive and search with DuckDB and MCP"
date: 2026-02-02
categories:
  - email
  - developer-tools
  - duckdb
  - mcp
  - search
  - tui
description: msgvault is Wes McKinney's private email archive system — lightning-fast search over personal email with a terminal UI and MCP server, all powered by DuckDB. Local-first, no cloud, built by the creator of pandas.
params:
  source: pinboard
  sourceUrl: https://wesmckinney.com/blog/announcing-msgvault/
---

![msgvault: personal email archive and search with DuckDB and MCP](/images/notes/msgvault.png)

## Summary

[msgvault](/notes/msgvault/) is Wes McKinney's personal email archiving and search system, announced on his blog. The name is new but the ambition is familiar for McKinney (creator of pandas): high-performance data access applied to personal data. The system stores email in a DuckDB-backed archive, provides a terminal UI for browsing, and exposes search via an MCP server so AI agents can query your email archive directly.

The DuckDB choice is deliberate — it enables analytical queries over large email datasets without requiring a running database server. Combined with an MCP interface, this means an LLM assistant can answer questions like "find all the emails about project X from last year" by actually querying the archive rather than relying on memory or web search. The MCP server turns the email archive into a tool available to any MCP-compatible agent.

[msgvault](/notes/msgvault/) sits in a growing category of tools building local-first personal knowledge infrastructure with MCP interfaces: [EchoVault](/notes/echovault/) (for agent memory), [Episodic Memory](/notes/episodic-memory/) (for conversation history), and now [msgvault](/notes/msgvault/) for email. The pattern is consistent: store data locally, expose it to AI agents via MCP for retrieval.

## Key points

- DuckDB-powered email archive with sub-second search over large mailboxes.
- Terminal UI for browsing and searching email without leaving the command line.
- MCP server exposes email archive to LLM agents for direct querying.
- Local-first: no cloud storage, private by design.
- By Wes McKinney (creator of pandas), focused on high-performance personal data access.
- Part of the local-first + MCP infrastructure pattern growing around AI agent workflows.

[Original](https://wesmckinney.com/blog/announcing-msgvault/)

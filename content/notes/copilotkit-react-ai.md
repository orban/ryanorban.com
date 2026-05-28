---
title: "CopilotKit: In-App AI Chatbots and AI Textareas for React"
date: 2023-12-06
categories:
  - llm
  - react
  - ai-ux
  - developer-tools
  - open-source
description: CopilotKit is a React library for embedding AI chatbots and AI-powered text areas into web apps — with the app's own context injected automatically. Makes it straightforward to add a context-aware AI assistant to an existing React app without building the RAG layer yourself.
params:
  source: pinboard
  sourceUrl: https://github.com/CopilotKit/CopilotKit
---

![CopilotKit: In-App AI Chatbots and AI Textareas for React](/images/notes/copilotkit-react-ai.png)

## Summary

CopilotKit is a React library that simplifies adding AI capabilities to existing web applications — specifically an in-app chatbot that knows about the current application state, and AI-powered `<CopilotTextarea>` components that provide context-aware autocompletion and editing. The key idea: the AI assistant has access to your app's data, not just a generic context.

The architecture works by letting you annotate your application's state as copilot-readable — you declare what data the AI can read (current document, user data, page context) and what actions it can take (call functions, trigger mutations). The CopilotKit SDK handles injecting this into the LLM context window automatically. This is the tool use pattern with a React-native implementation that doesn't require writing the plumbing manually.

The `<CopilotTextarea>` component is a drop-in replacement for a standard textarea that adds AI-assisted writing: autocomplete suggestions, rewrite commands, and context-aware generation. The textarea can be given context about the rest of the application (what document is open, what the user has done) so its suggestions are relevant.

## Key points

- Drop-in React components: `<CopilotChat>` for an in-app assistant, `<CopilotTextarea>` for AI-enhanced text input.
- App state injection: declare readable state with `useCopilotReadable()` — the AI sees your app's context.
- Action integration: `useCopilotAction()` lets the AI trigger application functions — real tool use.
- Works with OpenAI, Anthropic, and OpenAI-compatible backends.
- CoAgents extension for LangGraph integration — more complex agentic workflows.
- Use case: adding a talk to your app layer to existing React applications without a full backend build.

[Original](https://github.com/CopilotKit/CopilotKit) → GitHub, AI agent

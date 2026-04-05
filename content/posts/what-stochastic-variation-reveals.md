---
title: "What Stochastic Variation Reveals About AI Agents"
date: 2026-04-04
description: "Same agent, same task, different outcomes. Here's what the variation tells you about why agents fail — and what to do about it."
---
This is a sequel to [Stop Testing AI Agents Like Deterministic Code](/posts/stop-testing-agents-like-deterministic-code/). That post argued you should treat agents as stochastic processes (same inputs, probabilistic outputs). This one shows what you find when you do.

The setup: one agent ([OpenHands](https://github.com/All-Hands-AI/OpenHands) v0.54.0 running Qwen3-Coder-480B) attempts roughly 5,800 software engineering tasks from [SWE-rebench](https://github.com/nebius/swe-rebench), each 10 to 20 times. Same code, same prompt, same environment. 12,854 runs total.

Most tasks always pass or always fail. 1,096 have mixed outcomes — the same agent sometimes succeeds and sometimes doesn't. Those are the interesting ones.

---

## Same task, different outcomes

Pick one task. [httpx #366](https://github.com/encode/httpx/issues/366) (PR #386): add list support to query parameters. The agent tries it 14 times. Seven pass, seven fail. Here are ten of those runs.

Each bar is one run. Each colored block is a step the agent took: reading files, searching code, editing, running tests, reasoning. Green border means the run passed. Red means it failed.

<div class="chart-scroll chart-scroll--wide">
<svg role="img" aria-label="Same task, same agent, ten runs: five pass, five fail" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 420" style="max-width:700px;width:100%;height:auto;min-height:280px;font-family:system-ui,-apple-system,sans-serif">
<title>Same task, same agent, ten runs: five pass, five fail</title>
  <rect width="700" height="420" fill="#fff"/>
  <text x="350.0" y="28" text-anchor="middle" font-size="18" font-weight="600" fill="#222">Same task. Same agent. Ten runs.</text>
  <text x="350.0" y="50" text-anchor="middle" font-size="13" fill="#888">Five pass, five fail. encode/httpx #366 — OpenHands + Qwen3-Coder</text>
  <rect x="12" y="70" width="4" height="22" fill="#2d9a3e" rx="2"/>
  <rect x="17.0" y="70" width="11.6" height="22" fill="#9070a0"/>
  <rect x="29.1" y="70" width="11.6" height="22" fill="#7aaed4"/>
  <rect x="41.1" y="70" width="11.6" height="22" fill="#7aaed4"/>
  <rect x="53.2" y="70" width="11.6" height="22" fill="#7aaed4"/>
  <rect x="65.3" y="70" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="77.4" y="70" width="11.6" height="22" fill="#b85450"/>
  <rect x="89.4" y="70" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="101.5" y="70" width="11.6" height="22" fill="#3a9e96"/>
  <rect x="113.6" y="70" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="125.6" y="70" width="11.6" height="22" fill="#3a9e96"/>
  <rect x="137.7" y="70" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="149.8" y="70" width="11.6" height="22" fill="#3a9e96"/>
  <rect x="161.9" y="70" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="173.9" y="70" width="11.6" height="22" fill="#7aaed4"/>
  <rect x="186.0" y="70" width="11.6" height="22" fill="#3a9e96"/>
  <rect x="198.1" y="70" width="11.6" height="22" fill="#3a9e96"/>
  <rect x="210.1" y="70" width="11.6" height="22" fill="#7aaed4"/>
  <rect x="222.2" y="70" width="11.6" height="22" fill="#9070a0"/>
  <rect x="234.3" y="70" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="246.4" y="70" width="11.6" height="22" fill="#3a9e96"/>
  <rect x="258.4" y="70" width="11.6" height="22" fill="#3a9e96"/>
  <rect x="270.5" y="70" width="11.6" height="22" fill="#b85450"/>
  <rect x="282.6" y="70" width="11.6" height="22" fill="#c4a820"/>
  <rect x="294.6" y="70" width="11.6" height="22" fill="#b85450"/>
  <rect x="306.7" y="70" width="11.6" height="22" fill="#d4802a"/>
  <rect x="318.8" y="70" width="11.6" height="22" fill="#b85450"/>
  <rect x="330.9" y="70" width="11.6" height="22" fill="#9070a0"/>
  <rect x="342.9" y="70" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="355.0" y="70" width="11.6" height="22" fill="#d4802a"/>
  <rect x="367.1" y="70" width="11.6" height="22" fill="#b85450"/>
  <rect x="379.1" y="70" width="11.6" height="22" fill="#c4a820"/>
  <rect x="391.2" y="70" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="403.3" y="70" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="415.4" y="70" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="427.4" y="70" width="11.6" height="22" fill="#c4a820"/>
  <rect x="439.5" y="70" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="451.6" y="70" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="463.6" y="70" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="475.7" y="70" width="11.6" height="22" fill="#c4a820"/>
  <rect x="487.8" y="70" width="11.6" height="22" fill="#b85450"/>
  <rect x="499.9" y="70" width="11.6" height="22" fill="#c4a820"/>
  <rect x="511.9" y="70" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="524.0" y="70" width="11.6" height="22" fill="#d5d2cd"/>
  <rect x="536.1" y="70" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="548.1" y="70" width="11.6" height="22" fill="#b85450"/>
  <rect x="560.2" y="70" width="11.6" height="22" fill="#d5d2cd"/>
  <rect x="12" y="98" width="4" height="22" fill="#2d9a3e" rx="2"/>
  <rect x="17.0" y="98" width="11.6" height="22" fill="#9070a0"/>
  <rect x="29.1" y="98" width="11.6" height="22" fill="#7aaed4"/>
  <rect x="41.1" y="98" width="11.6" height="22" fill="#7aaed4"/>
  <rect x="53.2" y="98" width="11.6" height="22" fill="#7aaed4"/>
  <rect x="65.3" y="98" width="11.6" height="22" fill="#b85450"/>
  <rect x="77.4" y="98" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="89.4" y="98" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="101.5" y="98" width="11.6" height="22" fill="#b85450"/>
  <rect x="113.6" y="98" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="125.6" y="98" width="11.6" height="22" fill="#7aaed4"/>
  <rect x="137.7" y="98" width="11.6" height="22" fill="#7aaed4"/>
  <rect x="149.8" y="98" width="11.6" height="22" fill="#7aaed4"/>
  <rect x="161.9" y="98" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="173.9" y="98" width="11.6" height="22" fill="#3a9e96"/>
  <rect x="186.0" y="98" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="198.1" y="98" width="11.6" height="22" fill="#3a9e96"/>
  <rect x="210.1" y="98" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="222.2" y="98" width="11.6" height="22" fill="#3a9e96"/>
  <rect x="234.3" y="98" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="246.4" y="98" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="258.4" y="98" width="11.6" height="22" fill="#3a9e96"/>
  <rect x="270.5" y="98" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="282.6" y="98" width="11.6" height="22" fill="#c4a820"/>
  <rect x="294.6" y="98" width="11.6" height="22" fill="#b85450"/>
  <rect x="306.7" y="98" width="11.6" height="22" fill="#9070a0"/>
  <rect x="318.8" y="98" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="330.9" y="98" width="11.6" height="22" fill="#d4802a"/>
  <rect x="342.9" y="98" width="11.6" height="22" fill="#b85450"/>
  <rect x="355.0" y="98" width="11.6" height="22" fill="#c4a820"/>
  <rect x="367.1" y="98" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="379.1" y="98" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="391.2" y="98" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="403.3" y="98" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="415.4" y="98" width="11.6" height="22" fill="#c4a820"/>
  <rect x="427.4" y="98" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="439.5" y="98" width="11.6" height="22" fill="#b85450"/>
  <rect x="451.6" y="98" width="11.6" height="22" fill="#b85450"/>
  <rect x="463.6" y="98" width="11.6" height="22" fill="#b85450"/>
  <rect x="475.7" y="98" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="487.8" y="98" width="11.6" height="22" fill="#c4a820"/>
  <rect x="499.9" y="98" width="11.6" height="22" fill="#b85450"/>
  <rect x="511.9" y="98" width="11.6" height="22" fill="#d4802a"/>
  <rect x="524.0" y="98" width="11.6" height="22" fill="#b85450"/>
  <rect x="536.1" y="98" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="548.1" y="98" width="11.6" height="22" fill="#b85450"/>
  <rect x="560.2" y="98" width="11.6" height="22" fill="#b85450"/>
  <rect x="572.3" y="98" width="11.6" height="22" fill="#b85450"/>
  <rect x="584.4" y="98" width="11.6" height="22" fill="#d5d2cd"/>
  <rect x="596.4" y="98" width="11.6" height="22" fill="#d5d2cd"/>
  <rect x="12" y="126" width="4" height="22" fill="#2d9a3e" rx="2"/>
  <rect x="17.0" y="126" width="11.6" height="22" fill="#9070a0"/>
  <rect x="29.1" y="126" width="11.6" height="22" fill="#7aaed4"/>
  <rect x="41.1" y="126" width="11.6" height="22" fill="#b85450"/>
  <rect x="53.2" y="126" width="11.6" height="22" fill="#7aaed4"/>
  <rect x="65.3" y="126" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="77.4" y="126" width="11.6" height="22" fill="#b85450"/>
  <rect x="89.4" y="126" width="11.6" height="22" fill="#b85450"/>
  <rect x="101.5" y="126" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="113.6" y="126" width="11.6" height="22" fill="#7aaed4"/>
  <rect x="125.6" y="126" width="11.6" height="22" fill="#3a9e96"/>
  <rect x="137.7" y="126" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="149.8" y="126" width="11.6" height="22" fill="#3a9e96"/>
  <rect x="161.9" y="126" width="11.6" height="22" fill="#3a9e96"/>
  <rect x="173.9" y="126" width="11.6" height="22" fill="#3a9e96"/>
  <rect x="186.0" y="126" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="198.1" y="126" width="11.6" height="22" fill="#7aaed4"/>
  <rect x="210.1" y="126" width="11.6" height="22" fill="#7aaed4"/>
  <rect x="222.2" y="126" width="11.6" height="22" fill="#3a9e96"/>
  <rect x="234.3" y="126" width="11.6" height="22" fill="#3a9e96"/>
  <rect x="246.4" y="126" width="11.6" height="22" fill="#3a9e96"/>
  <rect x="258.4" y="126" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="270.5" y="126" width="11.6" height="22" fill="#3a9e96"/>
  <rect x="282.6" y="126" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="294.6" y="126" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="306.7" y="126" width="11.6" height="22" fill="#c4a820"/>
  <rect x="318.8" y="126" width="11.6" height="22" fill="#b85450"/>
  <rect x="330.9" y="126" width="11.6" height="22" fill="#9070a0"/>
  <rect x="342.9" y="126" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="355.0" y="126" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="367.1" y="126" width="11.6" height="22" fill="#d4802a"/>
  <rect x="379.1" y="126" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="391.2" y="126" width="11.6" height="22" fill="#b85450"/>
  <rect x="403.3" y="126" width="11.6" height="22" fill="#c4a820"/>
  <rect x="415.4" y="126" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="427.4" y="126" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="439.5" y="126" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="451.6" y="126" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="463.6" y="126" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="475.7" y="126" width="11.6" height="22" fill="#c4a820"/>
  <rect x="487.8" y="126" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="499.9" y="126" width="11.6" height="22" fill="#c4a820"/>
  <rect x="511.9" y="126" width="11.6" height="22" fill="#b85450"/>
  <rect x="524.0" y="126" width="11.6" height="22" fill="#d4802a"/>
  <rect x="536.1" y="126" width="11.6" height="22" fill="#b85450"/>
  <rect x="548.1" y="126" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="560.2" y="126" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="572.3" y="126" width="11.6" height="22" fill="#b85450"/>
  <rect x="584.4" y="126" width="11.6" height="22" fill="#d5d2cd"/>
  <rect x="596.4" y="126" width="11.6" height="22" fill="#d5d2cd"/>
  <rect x="12" y="154" width="4" height="22" fill="#2d9a3e" rx="2"/>
  <rect x="17.0" y="154" width="11.6" height="22" fill="#9070a0"/>
  <rect x="29.1" y="154" width="11.6" height="22" fill="#7aaed4"/>
  <rect x="41.1" y="154" width="11.6" height="22" fill="#7aaed4"/>
  <rect x="53.2" y="154" width="11.6" height="22" fill="#7aaed4"/>
  <rect x="65.3" y="154" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="77.4" y="154" width="11.6" height="22" fill="#7aaed4"/>
  <rect x="89.4" y="154" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="101.5" y="154" width="11.6" height="22" fill="#b85450"/>
  <rect x="113.6" y="154" width="11.6" height="22" fill="#3a9e96"/>
  <rect x="125.6" y="154" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="137.7" y="154" width="11.6" height="22" fill="#3a9e96"/>
  <rect x="149.8" y="154" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="161.9" y="154" width="11.6" height="22" fill="#3a9e96"/>
  <rect x="173.9" y="154" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="186.0" y="154" width="11.6" height="22" fill="#7aaed4"/>
  <rect x="198.1" y="154" width="11.6" height="22" fill="#3a9e96"/>
  <rect x="210.1" y="154" width="11.6" height="22" fill="#3a9e96"/>
  <rect x="222.2" y="154" width="11.6" height="22" fill="#3a9e96"/>
  <rect x="234.3" y="154" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="246.4" y="154" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="258.4" y="154" width="11.6" height="22" fill="#c4a820"/>
  <rect x="270.5" y="154" width="11.6" height="22" fill="#b85450"/>
  <rect x="282.6" y="154" width="11.6" height="22" fill="#b85450"/>
  <rect x="294.6" y="154" width="11.6" height="22" fill="#9070a0"/>
  <rect x="306.7" y="154" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="318.8" y="154" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="330.9" y="154" width="11.6" height="22" fill="#d4802a"/>
  <rect x="342.9" y="154" width="11.6" height="22" fill="#d4802a"/>
  <rect x="355.0" y="154" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="367.1" y="154" width="11.6" height="22" fill="#d4802a"/>
  <rect x="379.1" y="154" width="11.6" height="22" fill="#b85450"/>
  <rect x="391.2" y="154" width="11.6" height="22" fill="#d4802a"/>
  <rect x="403.3" y="154" width="11.6" height="22" fill="#b85450"/>
  <rect x="415.4" y="154" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="427.4" y="154" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="439.5" y="154" width="11.6" height="22" fill="#c4a820"/>
  <rect x="451.6" y="154" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="463.6" y="154" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="475.7" y="154" width="11.6" height="22" fill="#c4a820"/>
  <rect x="487.8" y="154" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="499.9" y="154" width="11.6" height="22" fill="#b85450"/>
  <rect x="511.9" y="154" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="524.0" y="154" width="11.6" height="22" fill="#c4a820"/>
  <rect x="536.1" y="154" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="548.1" y="154" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="560.2" y="154" width="11.6" height="22" fill="#d5d2cd"/>
  <rect x="572.3" y="154" width="11.6" height="22" fill="#b85450"/>
  <rect x="584.4" y="154" width="11.6" height="22" fill="#d5d2cd"/>
  <rect x="12" y="182" width="4" height="22" fill="#2d9a3e" rx="2"/>
  <rect x="17.0" y="182" width="11.6" height="22" fill="#9070a0"/>
  <rect x="29.1" y="182" width="11.6" height="22" fill="#7aaed4"/>
  <rect x="41.1" y="182" width="11.6" height="22" fill="#7aaed4"/>
  <rect x="53.2" y="182" width="11.6" height="22" fill="#7aaed4"/>
  <rect x="65.3" y="182" width="11.6" height="22" fill="#b85450"/>
  <rect x="77.4" y="182" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="89.4" y="182" width="11.6" height="22" fill="#7aaed4"/>
  <rect x="101.5" y="182" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="113.6" y="182" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="125.6" y="182" width="11.6" height="22" fill="#7aaed4"/>
  <rect x="137.7" y="182" width="11.6" height="22" fill="#7aaed4"/>
  <rect x="149.8" y="182" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="161.9" y="182" width="11.6" height="22" fill="#3a9e96"/>
  <rect x="173.9" y="182" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="186.0" y="182" width="11.6" height="22" fill="#3a9e96"/>
  <rect x="198.1" y="182" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="210.1" y="182" width="11.6" height="22" fill="#3a9e96"/>
  <rect x="222.2" y="182" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="234.3" y="182" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="246.4" y="182" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="258.4" y="182" width="11.6" height="22" fill="#3a9e96"/>
  <rect x="270.5" y="182" width="11.6" height="22" fill="#3a9e96"/>
  <rect x="282.6" y="182" width="11.6" height="22" fill="#3a9e96"/>
  <rect x="294.6" y="182" width="11.6" height="22" fill="#7aaed4"/>
  <rect x="306.7" y="182" width="11.6" height="22" fill="#c4a820"/>
  <rect x="318.8" y="182" width="11.6" height="22" fill="#b85450"/>
  <rect x="330.9" y="182" width="11.6" height="22" fill="#b85450"/>
  <rect x="342.9" y="182" width="11.6" height="22" fill="#b85450"/>
  <rect x="355.0" y="182" width="11.6" height="22" fill="#9070a0"/>
  <rect x="367.1" y="182" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="379.1" y="182" width="11.6" height="22" fill="#d4802a"/>
  <rect x="391.2" y="182" width="11.6" height="22" fill="#b85450"/>
  <rect x="403.3" y="182" width="11.6" height="22" fill="#c4a820"/>
  <rect x="415.4" y="182" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="427.4" y="182" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="439.5" y="182" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="451.6" y="182" width="11.6" height="22" fill="#d4802a"/>
  <rect x="463.6" y="182" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="475.7" y="182" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="487.8" y="182" width="11.6" height="22" fill="#b85450"/>
  <rect x="499.9" y="182" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="511.9" y="182" width="11.6" height="22" fill="#3a9e96"/>
  <rect x="524.0" y="182" width="11.6" height="22" fill="#7aaed4"/>
  <rect x="536.1" y="182" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="548.1" y="182" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="560.2" y="182" width="11.6" height="22" fill="#c4a820"/>
  <rect x="572.3" y="182" width="11.6" height="22" fill="#b85450"/>
  <rect x="584.4" y="182" width="11.6" height="22" fill="#d5d2cd"/>
  <rect x="12" y="224" width="4" height="22" fill="#cc3e40" rx="2"/>
  <rect x="17.0" y="224" width="11.6" height="22" fill="#9070a0"/>
  <rect x="29.1" y="224" width="11.6" height="22" fill="#7aaed4"/>
  <rect x="41.1" y="224" width="11.6" height="22" fill="#7aaed4"/>
  <rect x="53.2" y="224" width="11.6" height="22" fill="#3a9e96"/>
  <rect x="65.3" y="224" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="77.4" y="224" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="89.4" y="224" width="11.6" height="22" fill="#cc3e40"/>
  <rect x="101.5" y="224" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="113.6" y="224" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="125.6" y="224" width="11.6" height="22" fill="#3a9e96"/>
  <rect x="137.7" y="224" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="149.8" y="224" width="11.6" height="22" fill="#3a9e96"/>
  <rect x="161.9" y="224" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="173.9" y="224" width="11.6" height="22" fill="#3a9e96"/>
  <rect x="186.0" y="224" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="198.1" y="224" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="210.1" y="224" width="11.6" height="22" fill="#7aaed4"/>
  <rect x="222.2" y="224" width="11.6" height="22" fill="#c4a820"/>
  <rect x="234.3" y="224" width="11.6" height="22" fill="#b85450"/>
  <rect x="246.4" y="224" width="11.6" height="22" fill="#c4a820"/>
  <rect x="258.4" y="224" width="11.6" height="22" fill="#b85450"/>
  <rect x="270.5" y="224" width="11.6" height="22" fill="#9070a0"/>
  <rect x="282.6" y="224" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="294.6" y="224" width="11.6" height="22" fill="#d4802a"/>
  <rect x="306.7" y="224" width="11.6" height="22" fill="#d4802a"/>
  <rect x="318.8" y="224" width="11.6" height="22" fill="#b85450"/>
  <rect x="330.9" y="224" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="342.9" y="224" width="11.6" height="22" fill="#c4a820"/>
  <rect x="355.0" y="224" width="11.6" height="22" fill="#cc3e40"/>
  <rect x="367.1" y="224" width="11.6" height="22" fill="#c4a820"/>
  <rect x="379.1" y="224" width="11.6" height="22" fill="#b85450"/>
  <rect x="391.2" y="224" width="11.6" height="22" fill="#c4a820"/>
  <rect x="403.3" y="224" width="11.6" height="22" fill="#b85450"/>
  <rect x="415.4" y="224" width="11.6" height="22" fill="#d4802a"/>
  <rect x="427.4" y="224" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="439.5" y="224" width="11.6" height="22" fill="#c4a820"/>
  <rect x="451.6" y="224" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="463.6" y="224" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="475.7" y="224" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="487.8" y="224" width="11.6" height="22" fill="#d5d2cd"/>
  <rect x="499.9" y="224" width="11.6" height="22" fill="#c4a820"/>
  <rect x="511.9" y="224" width="11.6" height="22" fill="#b85450"/>
  <rect x="524.0" y="224" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="536.1" y="224" width="11.6" height="22" fill="#d5d2cd"/>
  <rect x="12" y="252" width="4" height="22" fill="#cc3e40" rx="2"/>
  <rect x="17.0" y="252" width="11.6" height="22" fill="#9070a0"/>
  <rect x="29.1" y="252" width="11.6" height="22" fill="#7aaed4"/>
  <rect x="41.1" y="252" width="11.6" height="22" fill="#7aaed4"/>
  <rect x="53.2" y="252" width="11.6" height="22" fill="#7aaed4"/>
  <rect x="65.3" y="252" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="77.4" y="252" width="11.6" height="22" fill="#b85450"/>
  <rect x="89.4" y="252" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="101.5" y="252" width="11.6" height="22" fill="#7aaed4"/>
  <rect x="113.6" y="252" width="11.6" height="22" fill="#3a9e96"/>
  <rect x="125.6" y="252" width="11.6" height="22" fill="#3a9e96"/>
  <rect x="137.7" y="252" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="149.8" y="252" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="161.9" y="252" width="11.6" height="22" fill="#3a9e96"/>
  <rect x="173.9" y="252" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="186.0" y="252" width="11.6" height="22" fill="#7aaed4"/>
  <rect x="198.1" y="252" width="11.6" height="22" fill="#7aaed4"/>
  <rect x="210.1" y="252" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="222.2" y="252" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="234.3" y="252" width="11.6" height="22" fill="#c4a820"/>
  <rect x="246.4" y="252" width="11.6" height="22" fill="#b85450"/>
  <rect x="258.4" y="252" width="11.6" height="22" fill="#9070a0"/>
  <rect x="270.5" y="252" width="11.6" height="22" fill="#b85450"/>
  <rect x="282.6" y="252" width="11.6" height="22" fill="#b85450"/>
  <rect x="294.6" y="252" width="11.6" height="22" fill="#d4802a"/>
  <rect x="306.7" y="252" width="11.6" height="22" fill="#b85450"/>
  <rect x="318.8" y="252" width="11.6" height="22" fill="#c4a820"/>
  <rect x="330.9" y="252" width="11.6" height="22" fill="#cc3e40"/>
  <rect x="342.9" y="252" width="11.6" height="22" fill="#c4a820"/>
  <rect x="355.0" y="252" width="11.6" height="22" fill="#b85450"/>
  <rect x="367.1" y="252" width="11.6" height="22" fill="#d4802a"/>
  <rect x="379.1" y="252" width="11.6" height="22" fill="#b85450"/>
  <rect x="391.2" y="252" width="11.6" height="22" fill="#d4802a"/>
  <rect x="403.3" y="252" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="415.4" y="252" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="427.4" y="252" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="439.5" y="252" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="451.6" y="252" width="11.6" height="22" fill="#c4a820"/>
  <rect x="463.6" y="252" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="475.7" y="252" width="11.6" height="22" fill="#c4a820"/>
  <rect x="487.8" y="252" width="11.6" height="22" fill="#b85450"/>
  <rect x="499.9" y="252" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="511.9" y="252" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="524.0" y="252" width="11.6" height="22" fill="#9070a0"/>
  <rect x="536.1" y="252" width="11.6" height="22" fill="#b85450"/>
  <rect x="548.1" y="252" width="11.6" height="22" fill="#c4a820"/>
  <rect x="560.2" y="252" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="572.3" y="252" width="11.6" height="22" fill="#b85450"/>
  <rect x="584.4" y="252" width="11.6" height="22" fill="#b85450"/>
  <rect x="596.4" y="252" width="11.6" height="22" fill="#d5d2cd"/>
  <rect x="608.5" y="252" width="11.6" height="22" fill="#d5d2cd"/>
  <rect x="12" y="280" width="4" height="22" fill="#cc3e40" rx="2"/>
  <rect x="17.0" y="280" width="11.6" height="22" fill="#9070a0"/>
  <rect x="29.1" y="280" width="11.6" height="22" fill="#7aaed4"/>
  <rect x="41.1" y="280" width="11.6" height="22" fill="#7aaed4"/>
  <rect x="53.2" y="280" width="11.6" height="22" fill="#7aaed4"/>
  <rect x="65.3" y="280" width="11.6" height="22" fill="#b85450"/>
  <rect x="77.4" y="280" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="89.4" y="280" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="101.5" y="280" width="11.6" height="22" fill="#7aaed4"/>
  <rect x="113.6" y="280" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="125.6" y="280" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="137.7" y="280" width="11.6" height="22" fill="#3a9e96"/>
  <rect x="149.8" y="280" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="161.9" y="280" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="173.9" y="280" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="186.0" y="280" width="11.6" height="22" fill="#3a9e96"/>
  <rect x="198.1" y="280" width="11.6" height="22" fill="#7aaed4"/>
  <rect x="210.1" y="280" width="11.6" height="22" fill="#7aaed4"/>
  <rect x="222.2" y="280" width="11.6" height="22" fill="#3a9e96"/>
  <rect x="234.3" y="280" width="11.6" height="22" fill="#b85450"/>
  <rect x="246.4" y="280" width="11.6" height="22" fill="#b85450"/>
  <rect x="258.4" y="280" width="11.6" height="22" fill="#b85450"/>
  <rect x="270.5" y="280" width="11.6" height="22" fill="#c4a820"/>
  <rect x="282.6" y="280" width="11.6" height="22" fill="#b85450"/>
  <rect x="294.6" y="280" width="11.6" height="22" fill="#9070a0"/>
  <rect x="306.7" y="280" width="11.6" height="22" fill="#d4802a"/>
  <rect x="318.8" y="280" width="11.6" height="22" fill="#b85450"/>
  <rect x="330.9" y="280" width="11.6" height="22" fill="#c4a820"/>
  <rect x="342.9" y="280" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="355.0" y="280" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="367.1" y="280" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="379.1" y="280" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="391.2" y="280" width="11.6" height="22" fill="#c4a820"/>
  <rect x="403.3" y="280" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="415.4" y="280" width="11.6" height="22" fill="#b85450"/>
  <rect x="427.4" y="280" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="439.5" y="280" width="11.6" height="22" fill="#d5d2cd"/>
  <rect x="451.6" y="280" width="11.6" height="22" fill="#d5d2cd"/>
  <rect x="463.6" y="280" width="11.6" height="22" fill="#d5d2cd"/>
  <rect x="475.7" y="280" width="11.6" height="22" fill="#d5d2cd"/>
  <rect x="487.8" y="280" width="11.6" height="22" fill="#d5d2cd"/>
  <rect x="499.9" y="280" width="11.6" height="22" fill="#9070a0"/>
  <rect x="511.9" y="280" width="11.6" height="22" fill="#b85450"/>
  <rect x="524.0" y="280" width="11.6" height="22" fill="#b85450"/>
  <rect x="536.1" y="280" width="11.6" height="22" fill="#d5d2cd"/>
  <rect x="548.1" y="280" width="11.6" height="22" fill="#b85450"/>
  <rect x="560.2" y="280" width="11.6" height="22" fill="#d5d2cd"/>
  <rect x="572.3" y="280" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="584.4" y="280" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="596.4" y="280" width="11.6" height="22" fill="#d5d2cd"/>
  <rect x="608.5" y="280" width="11.6" height="22" fill="#cc3e40"/>
  <rect x="620.6" y="280" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="632.6" y="280" width="11.6" height="22" fill="#d5d2cd"/>
  <rect x="644.7" y="280" width="11.6" height="22" fill="#c4a820"/>
  <rect x="656.8" y="280" width="11.6" height="22" fill="#b85450"/>
  <rect x="668.9" y="280" width="11.6" height="22" fill="#b85450"/>
  <rect x="680.9" y="280" width="11.6" height="22" fill="#d5d2cd"/>
  <rect x="12" y="308" width="4" height="22" fill="#cc3e40" rx="2"/>
  <rect x="17.0" y="308" width="11.6" height="22" fill="#9070a0"/>
  <rect x="29.1" y="308" width="11.6" height="22" fill="#7aaed4"/>
  <rect x="41.1" y="308" width="11.6" height="22" fill="#7aaed4"/>
  <rect x="53.2" y="308" width="11.6" height="22" fill="#7aaed4"/>
  <rect x="65.3" y="308" width="11.6" height="22" fill="#3a9e96"/>
  <rect x="77.4" y="308" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="89.4" y="308" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="101.5" y="308" width="11.6" height="22" fill="#7aaed4"/>
  <rect x="113.6" y="308" width="11.6" height="22" fill="#3a9e96"/>
  <rect x="125.6" y="308" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="137.7" y="308" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="149.8" y="308" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="161.9" y="308" width="11.6" height="22" fill="#3a9e96"/>
  <rect x="173.9" y="308" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="186.0" y="308" width="11.6" height="22" fill="#7aaed4"/>
  <rect x="198.1" y="308" width="11.6" height="22" fill="#3a9e96"/>
  <rect x="210.1" y="308" width="11.6" height="22" fill="#3a9e96"/>
  <rect x="222.2" y="308" width="11.6" height="22" fill="#3a9e96"/>
  <rect x="234.3" y="308" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="246.4" y="308" width="11.6" height="22" fill="#7aaed4"/>
  <rect x="258.4" y="308" width="11.6" height="22" fill="#7aaed4"/>
  <rect x="270.5" y="308" width="11.6" height="22" fill="#c4a820"/>
  <rect x="282.6" y="308" width="11.6" height="22" fill="#b85450"/>
  <rect x="294.6" y="308" width="11.6" height="22" fill="#9070a0"/>
  <rect x="306.7" y="308" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="318.8" y="308" width="11.6" height="22" fill="#d4802a"/>
  <rect x="330.9" y="308" width="11.6" height="22" fill="#b85450"/>
  <rect x="342.9" y="308" width="11.6" height="22" fill="#c4a820"/>
  <rect x="355.0" y="308" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="367.1" y="308" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="379.1" y="308" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="391.2" y="308" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="403.3" y="308" width="11.6" height="22" fill="#c4a820"/>
  <rect x="415.4" y="308" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="427.4" y="308" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="439.5" y="308" width="11.6" height="22" fill="#b85450"/>
  <rect x="451.6" y="308" width="11.6" height="22" fill="#d5d2cd"/>
  <rect x="463.6" y="308" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="475.7" y="308" width="11.6" height="22" fill="#c4a820"/>
  <rect x="487.8" y="308" width="11.6" height="22" fill="#b85450"/>
  <rect x="499.9" y="308" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="511.9" y="308" width="11.6" height="22" fill="#b85450"/>
  <rect x="524.0" y="308" width="11.6" height="22" fill="#c4a820"/>
  <rect x="536.1" y="308" width="11.6" height="22" fill="#b85450"/>
  <rect x="548.1" y="308" width="11.6" height="22" fill="#b85450"/>
  <rect x="560.2" y="308" width="11.6" height="22" fill="#b85450"/>
  <rect x="572.3" y="308" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="584.4" y="308" width="11.6" height="22" fill="#d5d2cd"/>
  <rect x="12" y="336" width="4" height="22" fill="#cc3e40" rx="2"/>
  <rect x="17.0" y="336" width="11.6" height="22" fill="#9070a0"/>
  <rect x="29.1" y="336" width="11.6" height="22" fill="#7aaed4"/>
  <rect x="41.1" y="336" width="11.6" height="22" fill="#7aaed4"/>
  <rect x="53.2" y="336" width="11.6" height="22" fill="#7aaed4"/>
  <rect x="65.3" y="336" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="77.4" y="336" width="11.6" height="22" fill="#b85450"/>
  <rect x="89.4" y="336" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="101.5" y="336" width="11.6" height="22" fill="#7aaed4"/>
  <rect x="113.6" y="336" width="11.6" height="22" fill="#3a9e96"/>
  <rect x="125.6" y="336" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="137.7" y="336" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="149.8" y="336" width="11.6" height="22" fill="#3a9e96"/>
  <rect x="161.9" y="336" width="11.6" height="22" fill="#3a9e96"/>
  <rect x="173.9" y="336" width="11.6" height="22" fill="#3a9e96"/>
  <rect x="186.0" y="336" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="198.1" y="336" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="210.1" y="336" width="11.6" height="22" fill="#3a9e96"/>
  <rect x="222.2" y="336" width="11.6" height="22" fill="#7aaed4"/>
  <rect x="234.3" y="336" width="11.6" height="22" fill="#3a9e96"/>
  <rect x="246.4" y="336" width="11.6" height="22" fill="#7aaed4"/>
  <rect x="258.4" y="336" width="11.6" height="22" fill="#b85450"/>
  <rect x="270.5" y="336" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="282.6" y="336" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="294.6" y="336" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="306.7" y="336" width="11.6" height="22" fill="#b85450"/>
  <rect x="318.8" y="336" width="11.6" height="22" fill="#b85450"/>
  <rect x="330.9" y="336" width="11.6" height="22" fill="#b85450"/>
  <rect x="342.9" y="336" width="11.6" height="22" fill="#c4a820"/>
  <rect x="355.0" y="336" width="11.6" height="22" fill="#b85450"/>
  <rect x="367.1" y="336" width="11.6" height="22" fill="#9070a0"/>
  <rect x="379.1" y="336" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="391.2" y="336" width="11.6" height="22" fill="#d4802a"/>
  <rect x="403.3" y="336" width="11.6" height="22" fill="#b85450"/>
  <rect x="415.4" y="336" width="11.6" height="22" fill="#c4a820"/>
  <rect x="427.4" y="336" width="11.6" height="22" fill="#cc3e40"/>
  <rect x="439.5" y="336" width="11.6" height="22" fill="#b85450"/>
  <rect x="451.6" y="336" width="11.6" height="22" fill="#b85450"/>
  <rect x="463.6" y="336" width="11.6" height="22" fill="#d4802a"/>
  <rect x="475.7" y="336" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="487.8" y="336" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="499.9" y="336" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="511.9" y="336" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="524.0" y="336" width="11.6" height="22" fill="#c4a820"/>
  <rect x="536.1" y="336" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="548.1" y="336" width="11.6" height="22" fill="#c4a820"/>
  <rect x="560.2" y="336" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="572.3" y="336" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="584.4" y="336" width="11.6" height="22" fill="#2d9a3e"/>
  <rect x="596.4" y="336" width="11.6" height="22" fill="#4a7fae"/>
  <rect x="608.5" y="336" width="11.6" height="22" fill="#c4a820"/>
  <rect x="620.6" y="336" width="11.6" height="22" fill="#b85450"/>
  <rect x="632.6" y="336" width="11.6" height="22" fill="#b85450"/>
  <rect x="644.7" y="336" width="11.6" height="22" fill="#d5d2cd"/>
  <rect x="20.0" y="372" width="12" height="12" fill="#4a7fae" rx="2"/>
  <text x="38.0" y="382" font-size="12" fill="#666">read</text>
  <rect x="189.0" y="372" width="12" height="12" fill="#3a9e96" rx="2"/>
  <text x="207.0" y="382" font-size="12" fill="#666">search</text>
  <rect x="358.0" y="372" width="12" height="12" fill="#d4802a" rx="2"/>
  <text x="376.0" y="382" font-size="12" fill="#666">edit</text>
  <rect x="527.0" y="372" width="12" height="12" fill="#c4a820" rx="2"/>
  <text x="545.0" y="382" font-size="12" fill="#666">write</text>
  <rect x="20.0" y="394" width="12" height="12" fill="#2d9a3e" rx="2"/>
  <text x="38.0" y="404" font-size="12" fill="#666">test pass</text>
  <rect x="189.0" y="394" width="12" height="12" fill="#cc3e40" rx="2"/>
  <text x="207.0" y="404" font-size="12" fill="#666">test fail</text>
  <rect x="358.0" y="394" width="12" height="12" fill="#b85450" rx="2"/>
  <text x="376.0" y="404" font-size="12" fill="#666">bash</text>
  <rect x="527.0" y="394" width="12" height="12" fill="#9070a0" rx="2"/>
  <text x="545.0" y="404" font-size="12" fill="#666">reason</text>
  <text x="688" y="84" text-anchor="end" font-size="11" fill="#2d9a3e" font-weight="500">pass</text>
  <text x="688" y="238" text-anchor="end" font-size="11" fill="#cc3e40" font-weight="500">fail</text>
</svg>
</div>

Look at the shape of these trajectories. They all start the same way: read the repo, run existing tests, search for relevant code. Then they diverge.

The passing runs and failing runs aren't doing wildly different things. They're taking the same kinds of steps, in roughly the same order, for roughly the same duration. The difference is subtle. That's what makes it interesting.

---

## Align them. Find the fork.

To find the difference, you need to align the trajectories. [Needleman-Wunsch alignment](https://en.wikipedia.org/wiki/Needleman%E2%80%93Wunsch_algorithm) (borrowed from bioinformatics, where it aligns DNA sequences) snaps matching steps into columns. Where runs diverge, gaps appear.

The alignment produces ~80 columns. Many show small differences. To find the fork, we run [Fisher's exact test](https://en.wikipedia.org/wiki/Fisher%27s_exact_test) on each column: does having a step here (vs a gap) predict pass or fail? The orange strip below shows -log(p) per column. Brighter = more statistically significant. Orange = pass-biased (pass runs active), gray = fail-biased (fail runs active).

<div class="chart-scroll chart-scroll--xwide">
<svg role="img" aria-label="Aligned trajectories with fork point and reasoning comparison" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 770" style="max-width:700px;width:100%;height:auto;font-family:system-ui,-apple-system,sans-serif">
<title>Aligned trajectories with fork point and reasoning comparison</title>
  <rect width="700" height="770" fill="#fff"/>
  <text x="350.0" y="24" text-anchor="middle" font-size="18" font-weight="600" fill="#222">Align them. Find the fork.</text>
  <text x="350.0" y="43" text-anchor="middle" font-size="12" fill="#888">Needleman-Wunsch alignment · each column tested for pass/fail association</text>
  <rect x="10" y="55" width="3" height="10" fill="#2d9a3e" rx="1"/>
  <rect x="14.0" y="55" width="8.2" height="10" fill="#9070a0"/>
  <rect x="22.5" y="55" width="8.2" height="10" fill="#7aaed4"/>
  <rect x="31.0" y="55" width="8.2" height="10" fill="#7aaed4"/>
  <rect x="39.5" y="55" width="8.2" height="10" fill="#7aaed4"/>
  <rect x="48.0" y="55" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="56.5" y="55" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="65.0" y="55" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="73.5" y="55" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="82.1" y="55" width="8.2" height="10" fill="#b85450"/>
  <rect x="90.6" y="55" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="99.1" y="55" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="107.6" y="55" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="116.1" y="55" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="124.6" y="55" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="133.1" y="55" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="141.6" y="55" width="8.2" height="10" fill="#3a9e96"/>
  <rect x="150.1" y="55" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="158.6" y="55" width="8.2" height="10" fill="#3a9e96"/>
  <rect x="167.1" y="55" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="175.6" y="55" width="8.2" height="10" fill="#3a9e96"/>
  <rect x="184.1" y="55" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="192.6" y="55" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="201.1" y="55" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="209.6" y="55" width="8.2" height="10" fill="#7aaed4"/>
  <rect x="218.2" y="55" width="8.2" height="10" fill="#3a9e96"/>
  <rect x="226.7" y="55" width="8.2" height="10" fill="#3a9e96"/>
  <rect x="235.2" y="55" width="8.2" height="10" fill="#7aaed4"/>
  <rect x="243.7" y="55" width="8.2" height="10" fill="#9070a0"/>
  <rect x="252.2" y="55" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="260.7" y="55" width="8.2" height="10" fill="#3a9e96"/>
  <rect x="269.2" y="55" width="8.2" height="10" fill="#3a9e96"/>
  <rect x="277.7" y="55" width="8.2" height="10" fill="#b85450"/>
  <rect x="286.2" y="55" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="294.7" y="55" width="8.2" height="10" fill="#c4a820"/>
  <rect x="303.2" y="55" width="8.2" height="10" fill="#b85450"/>
  <rect x="311.7" y="55" width="8.2" height="10" fill="#d4802a"/>
  <rect x="320.2" y="55" width="8.2" height="10" fill="#b85450"/>
  <rect x="328.7" y="55" width="8.2" height="10" fill="#9070a0"/>
  <rect x="337.2" y="55" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="345.7" y="55" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="354.3" y="55" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="362.8" y="55" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="371.3" y="55" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="379.8" y="55" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="388.3" y="55" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="396.8" y="55" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="405.3" y="55" width="8.2" height="10" fill="#d4802a"/>
  <rect x="413.8" y="55" width="8.2" height="10" fill="#b85450"/>
  <rect x="422.3" y="55" width="8.2" height="10" fill="#c4a820"/>
  <rect x="430.8" y="55" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="439.3" y="55" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="447.8" y="55" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="456.3" y="55" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="464.8" y="55" width="8.2" height="10" fill="#c4a820"/>
  <rect x="473.3" y="55" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="481.8" y="55" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="490.4" y="55" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="498.9" y="55" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="507.4" y="55" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="515.9" y="55" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="524.4" y="55" width="8.2" height="10" fill="#c4a820"/>
  <rect x="532.9" y="55" width="8.2" height="10" fill="#b85450"/>
  <rect x="541.4" y="55" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="549.9" y="55" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="558.4" y="55" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="566.9" y="55" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="575.4" y="55" width="8.2" height="10" fill="#c4a820"/>
  <rect x="583.9" y="55" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="592.4" y="55" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="600.9" y="55" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="609.4" y="55" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="617.9" y="55" width="8.2" height="10" fill="#d5d2cd"/>
  <rect x="626.5" y="55" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="635.0" y="55" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="643.5" y="55" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="652.0" y="55" width="8.2" height="10" fill="#b85450"/>
  <rect x="660.5" y="55" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="669.0" y="55" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="677.5" y="55" width="8.2" height="10" fill="#d5d2cd"/>
  <rect x="10" y="67" width="3" height="10" fill="#2d9a3e" rx="1"/>
  <rect x="14.0" y="67" width="8.2" height="10" fill="#9070a0"/>
  <rect x="22.5" y="67" width="8.2" height="10" fill="#7aaed4"/>
  <rect x="31.0" y="67" width="8.2" height="10" fill="#7aaed4"/>
  <rect x="39.5" y="67" width="8.2" height="10" fill="#7aaed4"/>
  <rect x="48.0" y="67" width="8.2" height="10" fill="#b85450"/>
  <rect x="56.5" y="67" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="65.0" y="67" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="73.5" y="67" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="82.1" y="67" width="8.2" height="10" fill="#b85450"/>
  <rect x="90.6" y="67" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="99.1" y="67" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="107.6" y="67" width="8.2" height="10" fill="#7aaed4"/>
  <rect x="116.1" y="67" width="8.2" height="10" fill="#7aaed4"/>
  <rect x="124.6" y="67" width="8.2" height="10" fill="#7aaed4"/>
  <rect x="133.1" y="67" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="141.6" y="67" width="8.2" height="10" fill="#3a9e96"/>
  <rect x="150.1" y="67" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="158.6" y="67" width="8.2" height="10" fill="#3a9e96"/>
  <rect x="167.1" y="67" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="175.6" y="67" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="184.1" y="67" width="8.2" height="10" fill="#3a9e96"/>
  <rect x="192.6" y="67" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="201.1" y="67" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="209.6" y="67" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="218.2" y="67" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="226.7" y="67" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="235.2" y="67" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="243.7" y="67" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="252.2" y="67" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="260.7" y="67" width="8.2" height="10" fill="#3a9e96"/>
  <rect x="269.2" y="67" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="277.7" y="67" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="286.2" y="67" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="294.7" y="67" width="8.2" height="10" fill="#c4a820"/>
  <rect x="303.2" y="67" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="311.7" y="67" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="320.2" y="67" width="8.2" height="10" fill="#b85450"/>
  <rect x="328.7" y="67" width="8.2" height="10" fill="#9070a0"/>
  <rect x="337.2" y="67" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="345.7" y="67" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="354.3" y="67" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="362.8" y="67" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="371.3" y="67" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="379.8" y="67" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="388.3" y="67" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="396.8" y="67" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="405.3" y="67" width="8.2" height="10" fill="#d4802a"/>
  <rect x="413.8" y="67" width="8.2" height="10" fill="#b85450"/>
  <rect x="422.3" y="67" width="8.2" height="10" fill="#c4a820"/>
  <rect x="430.8" y="67" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="439.3" y="67" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="447.8" y="67" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="456.3" y="67" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="464.8" y="67" width="8.2" height="10" fill="#c4a820"/>
  <rect x="473.3" y="67" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="481.8" y="67" width="8.2" height="10" fill="#b85450"/>
  <rect x="490.4" y="67" width="8.2" height="10" fill="#b85450"/>
  <rect x="498.9" y="67" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="507.4" y="67" width="8.2" height="10" fill="#b85450"/>
  <rect x="515.9" y="67" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="524.4" y="67" width="8.2" height="10" fill="#c4a820"/>
  <rect x="532.9" y="67" width="8.2" height="10" fill="#b85450"/>
  <rect x="541.4" y="67" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="549.9" y="67" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="558.4" y="67" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="566.9" y="67" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="575.4" y="67" width="8.2" height="10" fill="#d4802a"/>
  <rect x="583.9" y="67" width="8.2" height="10" fill="#b85450"/>
  <rect x="592.4" y="67" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="600.9" y="67" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="609.4" y="67" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="617.9" y="67" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="626.5" y="67" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="635.0" y="67" width="8.2" height="10" fill="#b85450"/>
  <rect x="643.5" y="67" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="652.0" y="67" width="8.2" height="10" fill="#b85450"/>
  <rect x="660.5" y="67" width="8.2" height="10" fill="#b85450"/>
  <rect x="669.0" y="67" width="8.2" height="10" fill="#d5d2cd"/>
  <rect x="677.5" y="67" width="8.2" height="10" fill="#d5d2cd"/>
  <rect x="10" y="79" width="3" height="10" fill="#2d9a3e" rx="1"/>
  <rect x="14.0" y="79" width="8.2" height="10" fill="#9070a0"/>
  <rect x="22.5" y="79" width="8.2" height="10" fill="#7aaed4"/>
  <rect x="31.0" y="79" width="8.2" height="10" fill="#b85450"/>
  <rect x="39.5" y="79" width="8.2" height="10" fill="#7aaed4"/>
  <rect x="48.0" y="79" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="56.5" y="79" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="65.0" y="79" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="73.5" y="79" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="82.1" y="79" width="8.2" height="10" fill="#b85450"/>
  <rect x="90.6" y="79" width="8.2" height="10" fill="#b85450"/>
  <rect x="99.1" y="79" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="107.6" y="79" width="8.2" height="10" fill="#7aaed4"/>
  <rect x="116.1" y="79" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="124.6" y="79" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="133.1" y="79" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="141.6" y="79" width="8.2" height="10" fill="#3a9e96"/>
  <rect x="150.1" y="79" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="158.6" y="79" width="8.2" height="10" fill="#3a9e96"/>
  <rect x="167.1" y="79" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="175.6" y="79" width="8.2" height="10" fill="#3a9e96"/>
  <rect x="184.1" y="79" width="8.2" height="10" fill="#3a9e96"/>
  <rect x="192.6" y="79" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="201.1" y="79" width="8.2" height="10" fill="#7aaed4"/>
  <rect x="209.6" y="79" width="8.2" height="10" fill="#7aaed4"/>
  <rect x="218.2" y="79" width="8.2" height="10" fill="#3a9e96"/>
  <rect x="226.7" y="79" width="8.2" height="10" fill="#3a9e96"/>
  <rect x="235.2" y="79" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="243.7" y="79" width="8.2" height="10" fill="#3a9e96"/>
  <rect x="252.2" y="79" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="260.7" y="79" width="8.2" height="10" fill="#3a9e96"/>
  <rect x="269.2" y="79" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="277.7" y="79" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="286.2" y="79" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="294.7" y="79" width="8.2" height="10" fill="#c4a820"/>
  <rect x="303.2" y="79" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="311.7" y="79" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="320.2" y="79" width="8.2" height="10" fill="#b85450"/>
  <rect x="328.7" y="79" width="8.2" height="10" fill="#9070a0"/>
  <rect x="337.2" y="79" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="345.7" y="79" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="354.3" y="79" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="362.8" y="79" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="371.3" y="79" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="379.8" y="79" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="388.3" y="79" width="8.2" height="10" fill="#d4802a"/>
  <rect x="396.8" y="79" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="405.3" y="79" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="413.8" y="79" width="8.2" height="10" fill="#b85450"/>
  <rect x="422.3" y="79" width="8.2" height="10" fill="#c4a820"/>
  <rect x="430.8" y="79" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="439.3" y="79" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="447.8" y="79" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="456.3" y="79" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="464.8" y="79" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="473.3" y="79" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="481.8" y="79" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="490.4" y="79" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="498.9" y="79" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="507.4" y="79" width="8.2" height="10" fill="#c4a820"/>
  <rect x="515.9" y="79" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="524.4" y="79" width="8.2" height="10" fill="#c4a820"/>
  <rect x="532.9" y="79" width="8.2" height="10" fill="#b85450"/>
  <rect x="541.4" y="79" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="549.9" y="79" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="558.4" y="79" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="566.9" y="79" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="575.4" y="79" width="8.2" height="10" fill="#d4802a"/>
  <rect x="583.9" y="79" width="8.2" height="10" fill="#b85450"/>
  <rect x="592.4" y="79" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="600.9" y="79" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="609.4" y="79" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="617.9" y="79" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="626.5" y="79" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="635.0" y="79" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="643.5" y="79" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="652.0" y="79" width="8.2" height="10" fill="#b85450"/>
  <rect x="660.5" y="79" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="669.0" y="79" width="8.2" height="10" fill="#d5d2cd"/>
  <rect x="677.5" y="79" width="8.2" height="10" fill="#d5d2cd"/>
  <rect x="10" y="91" width="3" height="10" fill="#2d9a3e" rx="1"/>
  <rect x="14.0" y="91" width="8.2" height="10" fill="#9070a0"/>
  <rect x="22.5" y="91" width="8.2" height="10" fill="#7aaed4"/>
  <rect x="31.0" y="91" width="8.2" height="10" fill="#7aaed4"/>
  <rect x="39.5" y="91" width="8.2" height="10" fill="#7aaed4"/>
  <rect x="48.0" y="91" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="56.5" y="91" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="65.0" y="91" width="8.2" height="10" fill="#7aaed4"/>
  <rect x="73.5" y="91" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="82.1" y="91" width="8.2" height="10" fill="#b85450"/>
  <rect x="90.6" y="91" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="99.1" y="91" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="107.6" y="91" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="116.1" y="91" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="124.6" y="91" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="133.1" y="91" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="141.6" y="91" width="8.2" height="10" fill="#3a9e96"/>
  <rect x="150.1" y="91" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="158.6" y="91" width="8.2" height="10" fill="#3a9e96"/>
  <rect x="167.1" y="91" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="175.6" y="91" width="8.2" height="10" fill="#3a9e96"/>
  <rect x="184.1" y="91" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="192.6" y="91" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="201.1" y="91" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="209.6" y="91" width="8.2" height="10" fill="#7aaed4"/>
  <rect x="218.2" y="91" width="8.2" height="10" fill="#3a9e96"/>
  <rect x="226.7" y="91" width="8.2" height="10" fill="#3a9e96"/>
  <rect x="235.2" y="91" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="243.7" y="91" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="252.2" y="91" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="260.7" y="91" width="8.2" height="10" fill="#3a9e96"/>
  <rect x="269.2" y="91" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="277.7" y="91" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="286.2" y="91" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="294.7" y="91" width="8.2" height="10" fill="#c4a820"/>
  <rect x="303.2" y="91" width="8.2" height="10" fill="#b85450"/>
  <rect x="311.7" y="91" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="320.2" y="91" width="8.2" height="10" fill="#b85450"/>
  <rect x="328.7" y="91" width="8.2" height="10" fill="#9070a0"/>
  <rect x="337.2" y="91" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="345.7" y="91" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="354.3" y="91" width="8.2" height="10" fill="#d4802a"/>
  <rect x="362.8" y="91" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="371.3" y="91" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="379.8" y="91" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="388.3" y="91" width="8.2" height="10" fill="#d4802a"/>
  <rect x="396.8" y="91" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="405.3" y="91" width="8.2" height="10" fill="#d4802a"/>
  <rect x="413.8" y="91" width="8.2" height="10" fill="#b85450"/>
  <rect x="422.3" y="91" width="8.2" height="10" fill="#d4802a"/>
  <rect x="430.8" y="91" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="439.3" y="91" width="8.2" height="10" fill="#b85450"/>
  <rect x="447.8" y="91" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="456.3" y="91" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="464.8" y="91" width="8.2" height="10" fill="#c4a820"/>
  <rect x="473.3" y="91" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="481.8" y="91" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="490.4" y="91" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="498.9" y="91" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="507.4" y="91" width="8.2" height="10" fill="#c4a820"/>
  <rect x="515.9" y="91" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="524.4" y="91" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="532.9" y="91" width="8.2" height="10" fill="#b85450"/>
  <rect x="541.4" y="91" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="549.9" y="91" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="558.4" y="91" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="566.9" y="91" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="575.4" y="91" width="8.2" height="10" fill="#c4a820"/>
  <rect x="583.9" y="91" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="592.4" y="91" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="600.9" y="91" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="609.4" y="91" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="617.9" y="91" width="8.2" height="10" fill="#d5d2cd"/>
  <rect x="626.5" y="91" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="635.0" y="91" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="643.5" y="91" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="652.0" y="91" width="8.2" height="10" fill="#b85450"/>
  <rect x="660.5" y="91" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="669.0" y="91" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="677.5" y="91" width="8.2" height="10" fill="#d5d2cd"/>
  <rect x="10" y="103" width="3" height="10" fill="#2d9a3e" rx="1"/>
  <rect x="14.0" y="103" width="8.2" height="10" fill="#9070a0"/>
  <rect x="22.5" y="103" width="8.2" height="10" fill="#7aaed4"/>
  <rect x="31.0" y="103" width="8.2" height="10" fill="#7aaed4"/>
  <rect x="39.5" y="103" width="8.2" height="10" fill="#7aaed4"/>
  <rect x="48.0" y="103" width="8.2" height="10" fill="#b85450"/>
  <rect x="56.5" y="103" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="65.0" y="103" width="8.2" height="10" fill="#7aaed4"/>
  <rect x="73.5" y="103" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="82.1" y="103" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="90.6" y="103" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="99.1" y="103" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="107.6" y="103" width="8.2" height="10" fill="#7aaed4"/>
  <rect x="116.1" y="103" width="8.2" height="10" fill="#7aaed4"/>
  <rect x="124.6" y="103" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="133.1" y="103" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="141.6" y="103" width="8.2" height="10" fill="#3a9e96"/>
  <rect x="150.1" y="103" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="158.6" y="103" width="8.2" height="10" fill="#3a9e96"/>
  <rect x="167.1" y="103" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="175.6" y="103" width="8.2" height="10" fill="#3a9e96"/>
  <rect x="184.1" y="103" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="192.6" y="103" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="201.1" y="103" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="209.6" y="103" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="218.2" y="103" width="8.2" height="10" fill="#3a9e96"/>
  <rect x="226.7" y="103" width="8.2" height="10" fill="#3a9e96"/>
  <rect x="235.2" y="103" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="243.7" y="103" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="252.2" y="103" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="260.7" y="103" width="8.2" height="10" fill="#3a9e96"/>
  <rect x="269.2" y="103" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="277.7" y="103" width="8.2" height="10" fill="#7aaed4"/>
  <rect x="286.2" y="103" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="294.7" y="103" width="8.2" height="10" fill="#c4a820"/>
  <rect x="303.2" y="103" width="8.2" height="10" fill="#b85450"/>
  <rect x="311.7" y="103" width="8.2" height="10" fill="#b85450"/>
  <rect x="320.2" y="103" width="8.2" height="10" fill="#b85450"/>
  <rect x="328.7" y="103" width="8.2" height="10" fill="#9070a0"/>
  <rect x="337.2" y="103" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="345.7" y="103" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="354.3" y="103" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="362.8" y="103" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="371.3" y="103" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="379.8" y="103" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="388.3" y="103" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="396.8" y="103" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="405.3" y="103" width="8.2" height="10" fill="#d4802a"/>
  <rect x="413.8" y="103" width="8.2" height="10" fill="#b85450"/>
  <rect x="422.3" y="103" width="8.2" height="10" fill="#c4a820"/>
  <rect x="430.8" y="103" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="439.3" y="103" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="447.8" y="103" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="456.3" y="103" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="464.8" y="103" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="473.3" y="103" width="8.2" height="10" fill="#d4802a"/>
  <rect x="481.8" y="103" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="490.4" y="103" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="498.9" y="103" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="507.4" y="103" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="515.9" y="103" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="524.4" y="103" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="532.9" y="103" width="8.2" height="10" fill="#b85450"/>
  <rect x="541.4" y="103" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="549.9" y="103" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="558.4" y="103" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="566.9" y="103" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="575.4" y="103" width="8.2" height="10" fill="#3a9e96"/>
  <rect x="583.9" y="103" width="8.2" height="10" fill="#7aaed4"/>
  <rect x="592.4" y="103" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="600.9" y="103" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="609.4" y="103" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="617.9" y="103" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="626.5" y="103" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="635.0" y="103" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="643.5" y="103" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="652.0" y="103" width="8.2" height="10" fill="#c4a820"/>
  <rect x="660.5" y="103" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="669.0" y="103" width="8.2" height="10" fill="#b85450"/>
  <rect x="677.5" y="103" width="8.2" height="10" fill="#d5d2cd"/>
  <rect x="10" y="121" width="3" height="10" fill="#cc3e40" rx="1"/>
  <rect x="14.0" y="121" width="8.2" height="10" fill="#9070a0"/>
  <rect x="22.5" y="121" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="31.0" y="121" width="8.2" height="10" fill="#7aaed4"/>
  <rect x="39.5" y="121" width="8.2" height="10" fill="#7aaed4"/>
  <rect x="48.0" y="121" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="56.5" y="121" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="65.0" y="121" width="8.2" height="10" fill="#3a9e96"/>
  <rect x="73.5" y="121" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="82.1" y="121" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="90.6" y="121" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="99.1" y="121" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="107.6" y="121" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="116.1" y="121" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="124.6" y="121" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="133.1" y="121" width="8.2" height="10" fill="#cc3e40"/>
  <rect x="141.6" y="121" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="150.1" y="121" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="158.6" y="121" width="8.2" height="10" fill="#3a9e96"/>
  <rect x="167.1" y="121" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="175.6" y="121" width="8.2" height="10" fill="#3a9e96"/>
  <rect x="184.1" y="121" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="192.6" y="121" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="201.1" y="121" width="8.2" height="10" fill="#3a9e96"/>
  <rect x="209.6" y="121" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="218.2" y="121" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="226.7" y="121" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="235.2" y="121" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="243.7" y="121" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="252.2" y="121" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="260.7" y="121" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="269.2" y="121" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="277.7" y="121" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="286.2" y="121" width="8.2" height="10" fill="#7aaed4"/>
  <rect x="294.7" y="121" width="8.2" height="10" fill="#c4a820"/>
  <rect x="303.2" y="121" width="8.2" height="10" fill="#b85450"/>
  <rect x="311.7" y="121" width="8.2" height="10" fill="#c4a820"/>
  <rect x="320.2" y="121" width="8.2" height="10" fill="#b85450"/>
  <rect x="328.7" y="121" width="8.2" height="10" fill="#9070a0"/>
  <rect x="337.2" y="121" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="345.7" y="121" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="354.3" y="121" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="362.8" y="121" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="371.3" y="121" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="379.8" y="121" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="388.3" y="121" width="8.2" height="10" fill="#d4802a"/>
  <rect x="396.8" y="121" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="405.3" y="121" width="8.2" height="10" fill="#d4802a"/>
  <rect x="413.8" y="121" width="8.2" height="10" fill="#b85450"/>
  <rect x="422.3" y="121" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="430.8" y="121" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="439.3" y="121" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="447.8" y="121" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="456.3" y="121" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="464.8" y="121" width="8.2" height="10" fill="#c4a820"/>
  <rect x="473.3" y="121" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="481.8" y="121" width="8.2" height="10" fill="#cc3e40"/>
  <rect x="490.4" y="121" width="8.2" height="10" fill="#c4a820"/>
  <rect x="498.9" y="121" width="8.2" height="10" fill="#b85450"/>
  <rect x="507.4" y="121" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="515.9" y="121" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="524.4" y="121" width="8.2" height="10" fill="#c4a820"/>
  <rect x="532.9" y="121" width="8.2" height="10" fill="#b85450"/>
  <rect x="541.4" y="121" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="549.9" y="121" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="558.4" y="121" width="8.2" height="10" fill="#d4802a"/>
  <rect x="566.9" y="121" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="575.4" y="121" width="8.2" height="10" fill="#c4a820"/>
  <rect x="583.9" y="121" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="592.4" y="121" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="600.9" y="121" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="609.4" y="121" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="617.9" y="121" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="626.5" y="121" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="635.0" y="121" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="643.5" y="121" width="8.2" height="10" fill="#d5d2cd"/>
  <rect x="652.0" y="121" width="8.2" height="10" fill="#c4a820"/>
  <rect x="660.5" y="121" width="8.2" height="10" fill="#b85450"/>
  <rect x="669.0" y="121" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="677.5" y="121" width="8.2" height="10" fill="#d5d2cd"/>
  <rect x="10" y="133" width="3" height="10" fill="#cc3e40" rx="1"/>
  <rect x="14.0" y="133" width="8.2" height="10" fill="#9070a0"/>
  <rect x="22.5" y="133" width="8.2" height="10" fill="#7aaed4"/>
  <rect x="31.0" y="133" width="8.2" height="10" fill="#7aaed4"/>
  <rect x="39.5" y="133" width="8.2" height="10" fill="#7aaed4"/>
  <rect x="48.0" y="133" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="56.5" y="133" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="65.0" y="133" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="73.5" y="133" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="82.1" y="133" width="8.2" height="10" fill="#b85450"/>
  <rect x="90.6" y="133" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="99.1" y="133" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="107.6" y="133" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="116.1" y="133" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="124.6" y="133" width="8.2" height="10" fill="#7aaed4"/>
  <rect x="133.1" y="133" width="8.2" height="10" fill="#3a9e96"/>
  <rect x="141.6" y="133" width="8.2" height="10" fill="#3a9e96"/>
  <rect x="150.1" y="133" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="158.6" y="133" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="167.1" y="133" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="175.6" y="133" width="8.2" height="10" fill="#3a9e96"/>
  <rect x="184.1" y="133" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="192.6" y="133" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="201.1" y="133" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="209.6" y="133" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="218.2" y="133" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="226.7" y="133" width="8.2" height="10" fill="#7aaed4"/>
  <rect x="235.2" y="133" width="8.2" height="10" fill="#7aaed4"/>
  <rect x="243.7" y="133" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="252.2" y="133" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="260.7" y="133" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="269.2" y="133" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="277.7" y="133" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="286.2" y="133" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="294.7" y="133" width="8.2" height="10" fill="#c4a820"/>
  <rect x="303.2" y="133" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="311.7" y="133" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="320.2" y="133" width="8.2" height="10" fill="#b85450"/>
  <rect x="328.7" y="133" width="8.2" height="10" fill="#9070a0"/>
  <rect x="337.2" y="133" width="8.2" height="10" fill="#b85450"/>
  <rect x="345.7" y="133" width="8.2" height="10" fill="#b85450"/>
  <rect x="354.3" y="133" width="8.2" height="10" fill="#d4802a"/>
  <rect x="362.8" y="133" width="8.2" height="10" fill="#b85450"/>
  <rect x="371.3" y="133" width="8.2" height="10" fill="#c4a820"/>
  <rect x="379.8" y="133" width="8.2" height="10" fill="#cc3e40"/>
  <rect x="388.3" y="133" width="8.2" height="10" fill="#c4a820"/>
  <rect x="396.8" y="133" width="8.2" height="10" fill="#b85450"/>
  <rect x="405.3" y="133" width="8.2" height="10" fill="#d4802a"/>
  <rect x="413.8" y="133" width="8.2" height="10" fill="#b85450"/>
  <rect x="422.3" y="133" width="8.2" height="10" fill="#d4802a"/>
  <rect x="430.8" y="133" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="439.3" y="133" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="447.8" y="133" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="456.3" y="133" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="464.8" y="133" width="8.2" height="10" fill="#c4a820"/>
  <rect x="473.3" y="133" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="481.8" y="133" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="490.4" y="133" width="8.2" height="10" fill="#c4a820"/>
  <rect x="498.9" y="133" width="8.2" height="10" fill="#b85450"/>
  <rect x="507.4" y="133" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="515.9" y="133" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="524.4" y="133" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="532.9" y="133" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="541.4" y="133" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="549.9" y="133" width="8.2" height="10" fill="#9070a0"/>
  <rect x="558.4" y="133" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="566.9" y="133" width="8.2" height="10" fill="#b85450"/>
  <rect x="575.4" y="133" width="8.2" height="10" fill="#c4a820"/>
  <rect x="583.9" y="133" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="592.4" y="133" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="600.9" y="133" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="609.4" y="133" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="617.9" y="133" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="626.5" y="133" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="635.0" y="133" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="643.5" y="133" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="652.0" y="133" width="8.2" height="10" fill="#b85450"/>
  <rect x="660.5" y="133" width="8.2" height="10" fill="#b85450"/>
  <rect x="669.0" y="133" width="8.2" height="10" fill="#d5d2cd"/>
  <rect x="677.5" y="133" width="8.2" height="10" fill="#d5d2cd"/>
  <rect x="10" y="145" width="3" height="10" fill="#cc3e40" rx="1"/>
  <rect x="14.0" y="145" width="8.2" height="10" fill="#9070a0"/>
  <rect x="22.5" y="145" width="8.2" height="10" fill="#7aaed4"/>
  <rect x="31.0" y="145" width="8.2" height="10" fill="#7aaed4"/>
  <rect x="39.5" y="145" width="8.2" height="10" fill="#7aaed4"/>
  <rect x="48.0" y="145" width="8.2" height="10" fill="#b85450"/>
  <rect x="56.5" y="145" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="65.0" y="145" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="73.5" y="145" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="82.1" y="145" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="90.6" y="145" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="99.1" y="145" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="107.6" y="145" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="116.1" y="145" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="124.6" y="145" width="8.2" height="10" fill="#7aaed4"/>
  <rect x="133.1" y="145" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="141.6" y="145" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="150.1" y="145" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="158.6" y="145" width="8.2" height="10" fill="#3a9e96"/>
  <rect x="167.1" y="145" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="175.6" y="145" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="184.1" y="145" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="192.6" y="145" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="201.1" y="145" width="8.2" height="10" fill="#3a9e96"/>
  <rect x="209.6" y="145" width="8.2" height="10" fill="#7aaed4"/>
  <rect x="218.2" y="145" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="226.7" y="145" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="235.2" y="145" width="8.2" height="10" fill="#7aaed4"/>
  <rect x="243.7" y="145" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="252.2" y="145" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="260.7" y="145" width="8.2" height="10" fill="#3a9e96"/>
  <rect x="269.2" y="145" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="277.7" y="145" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="286.2" y="145" width="8.2" height="10" fill="#b85450"/>
  <rect x="294.7" y="145" width="8.2" height="10" fill="#b85450"/>
  <rect x="303.2" y="145" width="8.2" height="10" fill="#b85450"/>
  <rect x="311.7" y="145" width="8.2" height="10" fill="#c4a820"/>
  <rect x="320.2" y="145" width="8.2" height="10" fill="#b85450"/>
  <rect x="328.7" y="145" width="8.2" height="10" fill="#9070a0"/>
  <rect x="337.2" y="145" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="345.7" y="145" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="354.3" y="145" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="362.8" y="145" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="371.3" y="145" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="379.8" y="145" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="388.3" y="145" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="396.8" y="145" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="405.3" y="145" width="8.2" height="10" fill="#d4802a"/>
  <rect x="413.8" y="145" width="8.2" height="10" fill="#b85450"/>
  <rect x="422.3" y="145" width="8.2" height="10" fill="#c4a820"/>
  <rect x="430.8" y="145" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="439.3" y="145" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="447.8" y="145" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="456.3" y="145" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="464.8" y="145" width="8.2" height="10" fill="#c4a820"/>
  <rect x="473.3" y="145" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="481.8" y="145" width="8.2" height="10" fill="#b85450"/>
  <rect x="490.4" y="145" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="498.9" y="145" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="507.4" y="145" width="8.2" height="10" fill="#d5d2cd"/>
  <rect x="515.9" y="145" width="8.2" height="10" fill="#d5d2cd"/>
  <rect x="524.4" y="145" width="8.2" height="10" fill="#d5d2cd"/>
  <rect x="532.9" y="145" width="8.2" height="10" fill="#d5d2cd"/>
  <rect x="541.4" y="145" width="8.2" height="10" fill="#d5d2cd"/>
  <rect x="549.9" y="145" width="8.2" height="10" fill="#9070a0"/>
  <rect x="558.4" y="145" width="8.2" height="10" fill="#b85450"/>
  <rect x="566.9" y="145" width="8.2" height="10" fill="#b85450"/>
  <rect x="575.4" y="145" width="8.2" height="10" fill="#d5d2cd"/>
  <rect x="583.9" y="145" width="8.2" height="10" fill="#b85450"/>
  <rect x="592.4" y="145" width="8.2" height="10" fill="#d5d2cd"/>
  <rect x="600.9" y="145" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="609.4" y="145" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="617.9" y="145" width="8.2" height="10" fill="#d5d2cd"/>
  <rect x="626.5" y="145" width="8.2" height="10" fill="#cc3e40"/>
  <rect x="635.0" y="145" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="643.5" y="145" width="8.2" height="10" fill="#d5d2cd"/>
  <rect x="652.0" y="145" width="8.2" height="10" fill="#c4a820"/>
  <rect x="660.5" y="145" width="8.2" height="10" fill="#b85450"/>
  <rect x="669.0" y="145" width="8.2" height="10" fill="#b85450"/>
  <rect x="677.5" y="145" width="8.2" height="10" fill="#d5d2cd"/>
  <rect x="10" y="157" width="3" height="10" fill="#cc3e40" rx="1"/>
  <rect x="14.0" y="157" width="8.2" height="10" fill="#9070a0"/>
  <rect x="22.5" y="157" width="8.2" height="10" fill="#7aaed4"/>
  <rect x="31.0" y="157" width="8.2" height="10" fill="#7aaed4"/>
  <rect x="39.5" y="157" width="8.2" height="10" fill="#7aaed4"/>
  <rect x="48.0" y="157" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="56.5" y="157" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="65.0" y="157" width="8.2" height="10" fill="#3a9e96"/>
  <rect x="73.5" y="157" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="82.1" y="157" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="90.6" y="157" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="99.1" y="157" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="107.6" y="157" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="116.1" y="157" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="124.6" y="157" width="8.2" height="10" fill="#7aaed4"/>
  <rect x="133.1" y="157" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="141.6" y="157" width="8.2" height="10" fill="#3a9e96"/>
  <rect x="150.1" y="157" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="158.6" y="157" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="167.1" y="157" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="175.6" y="157" width="8.2" height="10" fill="#3a9e96"/>
  <rect x="184.1" y="157" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="192.6" y="157" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="201.1" y="157" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="209.6" y="157" width="8.2" height="10" fill="#7aaed4"/>
  <rect x="218.2" y="157" width="8.2" height="10" fill="#3a9e96"/>
  <rect x="226.7" y="157" width="8.2" height="10" fill="#3a9e96"/>
  <rect x="235.2" y="157" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="243.7" y="157" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="252.2" y="157" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="260.7" y="157" width="8.2" height="10" fill="#3a9e96"/>
  <rect x="269.2" y="157" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="277.7" y="157" width="8.2" height="10" fill="#7aaed4"/>
  <rect x="286.2" y="157" width="8.2" height="10" fill="#7aaed4"/>
  <rect x="294.7" y="157" width="8.2" height="10" fill="#c4a820"/>
  <rect x="303.2" y="157" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="311.7" y="157" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="320.2" y="157" width="8.2" height="10" fill="#b85450"/>
  <rect x="328.7" y="157" width="8.2" height="10" fill="#9070a0"/>
  <rect x="337.2" y="157" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="345.7" y="157" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="354.3" y="157" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="362.8" y="157" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="371.3" y="157" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="379.8" y="157" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="388.3" y="157" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="396.8" y="157" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="405.3" y="157" width="8.2" height="10" fill="#d4802a"/>
  <rect x="413.8" y="157" width="8.2" height="10" fill="#b85450"/>
  <rect x="422.3" y="157" width="8.2" height="10" fill="#c4a820"/>
  <rect x="430.8" y="157" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="439.3" y="157" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="447.8" y="157" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="456.3" y="157" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="464.8" y="157" width="8.2" height="10" fill="#c4a820"/>
  <rect x="473.3" y="157" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="481.8" y="157" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="490.4" y="157" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="498.9" y="157" width="8.2" height="10" fill="#b85450"/>
  <rect x="507.4" y="157" width="8.2" height="10" fill="#d5d2cd"/>
  <rect x="515.9" y="157" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="524.4" y="157" width="8.2" height="10" fill="#c4a820"/>
  <rect x="532.9" y="157" width="8.2" height="10" fill="#b85450"/>
  <rect x="541.4" y="157" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="549.9" y="157" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="558.4" y="157" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="566.9" y="157" width="8.2" height="10" fill="#b85450"/>
  <rect x="575.4" y="157" width="8.2" height="10" fill="#c4a820"/>
  <rect x="583.9" y="157" width="8.2" height="10" fill="#b85450"/>
  <rect x="592.4" y="157" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="600.9" y="157" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="609.4" y="157" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="617.9" y="157" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="626.5" y="157" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="635.0" y="157" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="643.5" y="157" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="652.0" y="157" width="8.2" height="10" fill="#b85450"/>
  <rect x="660.5" y="157" width="8.2" height="10" fill="#b85450"/>
  <rect x="669.0" y="157" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="677.5" y="157" width="8.2" height="10" fill="#d5d2cd"/>
  <rect x="10" y="169" width="3" height="10" fill="#cc3e40" rx="1"/>
  <rect x="14.0" y="169" width="8.2" height="10" fill="#9070a0"/>
  <rect x="22.5" y="169" width="8.2" height="10" fill="#7aaed4"/>
  <rect x="31.0" y="169" width="8.2" height="10" fill="#7aaed4"/>
  <rect x="39.5" y="169" width="8.2" height="10" fill="#7aaed4"/>
  <rect x="48.0" y="169" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="56.5" y="169" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="65.0" y="169" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="73.5" y="169" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="82.1" y="169" width="8.2" height="10" fill="#b85450"/>
  <rect x="90.6" y="169" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="99.1" y="169" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="107.6" y="169" width="8.2" height="10" fill="#7aaed4"/>
  <rect x="116.1" y="169" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="124.6" y="169" width="8.2" height="10" fill="#3a9e96"/>
  <rect x="133.1" y="169" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="141.6" y="169" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="150.1" y="169" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="158.6" y="169" width="8.2" height="10" fill="#3a9e96"/>
  <rect x="167.1" y="169" width="8.2" height="10" fill="#3a9e96"/>
  <rect x="175.6" y="169" width="8.2" height="10" fill="#3a9e96"/>
  <rect x="184.1" y="169" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="192.6" y="169" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="201.1" y="169" width="8.2" height="10" fill="#3a9e96"/>
  <rect x="209.6" y="169" width="8.2" height="10" fill="#7aaed4"/>
  <rect x="218.2" y="169" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="226.7" y="169" width="8.2" height="10" fill="#3a9e96"/>
  <rect x="235.2" y="169" width="8.2" height="10" fill="#7aaed4"/>
  <rect x="243.7" y="169" width="8.2" height="10" fill="#b85450"/>
  <rect x="252.2" y="169" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="260.7" y="169" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="269.2" y="169" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="277.7" y="169" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="286.2" y="169" width="8.2" height="10" fill="#b85450"/>
  <rect x="294.7" y="169" width="8.2" height="10" fill="#b85450"/>
  <rect x="303.2" y="169" width="8.2" height="10" fill="#b85450"/>
  <rect x="311.7" y="169" width="8.2" height="10" fill="#c4a820"/>
  <rect x="320.2" y="169" width="8.2" height="10" fill="#b85450"/>
  <rect x="328.7" y="169" width="8.2" height="10" fill="#9070a0"/>
  <rect x="337.2" y="169" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="345.7" y="169" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="354.3" y="169" width="8.2" height="10" fill="#d4802a"/>
  <rect x="362.8" y="169" width="8.2" height="10" fill="#b85450"/>
  <rect x="371.3" y="169" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="379.8" y="169" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="388.3" y="169" width="8.2" height="10" fill="#c4a820"/>
  <rect x="396.8" y="169" width="8.2" height="10" fill="#cc3e40"/>
  <rect x="405.3" y="169" width="8.2" height="10" fill="#b85450"/>
  <rect x="413.8" y="169" width="8.2" height="10" fill="#b85450"/>
  <rect x="422.3" y="169" width="8.2" height="10" fill="#d4802a"/>
  <rect x="430.8" y="169" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="439.3" y="169" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="447.8" y="169" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="456.3" y="169" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="464.8" y="169" width="8.2" height="10" fill="#c4a820"/>
  <rect x="473.3" y="169" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="481.8" y="169" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="490.4" y="169" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="498.9" y="169" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="507.4" y="169" width="8.2" height="10" fill="#c4a820"/>
  <rect x="515.9" y="169" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="524.4" y="169" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="532.9" y="169" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="541.4" y="169" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="549.9" y="169" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="558.4" y="169" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="566.9" y="169" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="575.4" y="169" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="583.9" y="169" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="592.4" y="169" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="600.9" y="169" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="609.4" y="169" width="8.2" height="10" fill="#2d9a3e"/>
  <rect x="617.9" y="169" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="626.5" y="169" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="635.0" y="169" width="8.2" height="10" fill="#4a7fae"/>
  <rect x="643.5" y="169" width="8.2" height="10" fill="#f0eee9"/>
  <rect x="652.0" y="169" width="8.2" height="10" fill="#c4a820"/>
  <rect x="660.5" y="169" width="8.2" height="10" fill="#b85450"/>
  <rect x="669.0" y="169" width="8.2" height="10" fill="#b85450"/>
  <rect x="677.5" y="169" width="8.2" height="10" fill="#d5d2cd"/>
  <text x="686" y="209.0" text-anchor="end" font-size="9" fill="#999">Fisher p-value</text>
  <rect x="14.0" y="197" width="8.2" height="18" fill="#f5f3f0"/>
  <rect x="22.5" y="197" width="8.2" height="18" fill="#f5f3f0"/>
  <rect x="31.0" y="197" width="8.2" height="18" fill="#f5f3f0"/>
  <rect x="39.5" y="197" width="8.2" height="18" fill="#f5f3f0"/>
  <rect x="48.0" y="197" width="8.2" height="18" fill="#f5f3f0"/>
  <rect x="56.5" y="197" width="8.2" height="18" fill="#d4802a" opacity="0.65"/>
  <rect x="65.0" y="197" width="8.2" height="18" fill="#f5f3f0"/>
  <rect x="73.5" y="197" width="8.2" height="18" fill="#f5f3f0"/>
  <rect x="82.1" y="197" width="8.2" height="18" fill="#d4802a" opacity="0.33"/>
  <rect x="90.6" y="197" width="8.2" height="18" fill="#f5f3f0"/>
  <rect x="99.1" y="197" width="8.2" height="18" fill="#f5f3f0"/>
  <rect x="107.6" y="197" width="8.2" height="18" fill="#d4802a" opacity="0.33"/>
  <rect x="116.1" y="197" width="8.2" height="18" fill="#d4802a" opacity="0.38"/>
  <rect x="124.6" y="197" width="8.2" height="18" fill="#7a8a9a" opacity="0.59"/>
  <rect x="133.1" y="197" width="8.2" height="18" fill="#7a8a9a" opacity="0.33"/>
  <rect x="141.6" y="197" width="8.2" height="18" fill="#d4802a" opacity="0.38"/>
  <rect x="150.1" y="197" width="8.2" height="18" fill="#f5f3f0"/>
  <rect x="158.6" y="197" width="8.2" height="18" fill="#f5f3f0"/>
  <rect x="167.1" y="197" width="8.2" height="18" fill="#f5f3f0"/>
  <rect x="175.6" y="197" width="8.2" height="18" fill="#f5f3f0"/>
  <rect x="184.1" y="197" width="8.2" height="18" fill="#f5f3f0"/>
  <rect x="192.6" y="197" width="8.2" height="18" fill="#f5f3f0"/>
  <rect x="201.1" y="197" width="8.2" height="18" fill="#f5f3f0"/>
  <rect x="209.6" y="197" width="8.2" height="18" fill="#f5f3f0"/>
  <rect x="218.2" y="197" width="8.2" height="18" fill="#d4802a" opacity="0.59"/>
  <rect x="226.7" y="197" width="8.2" height="18" fill="#f5f3f0"/>
  <rect x="235.2" y="197" width="8.2" height="18" fill="#7a8a9a" opacity="0.33"/>
  <rect x="243.7" y="197" width="8.2" height="18" fill="#f5f3f0"/>
  <rect x="252.2" y="197" width="8.2" height="18" fill="#d4802a" opacity="0.33"/>
  <rect x="260.7" y="197" width="8.2" height="18" fill="#d4802a" opacity="0.65"/>
  <rect x="269.2" y="197" width="8.2" height="18" fill="#f5f3f0"/>
  <rect x="277.7" y="197" width="8.2" height="18" fill="#f5f3f0"/>
  <rect x="286.2" y="197" width="8.2" height="18" fill="#7a8a9a" opacity="1.00"/>
  <rect x="294.7" y="197" width="8.2" height="18" fill="#f5f3f0"/>
  <rect x="303.2" y="197" width="8.2" height="18" fill="#f5f3f0"/>
  <rect x="311.7" y="197" width="8.2" height="18" fill="#f5f3f0"/>
  <rect x="320.2" y="197" width="8.2" height="18" fill="#f5f3f0"/>
  <rect x="328.7" y="197" width="8.2" height="18" fill="#f5f3f0"/>
  <rect x="337.2" y="197" width="8.2" height="18" fill="#f5f3f0"/>
  <rect x="345.7" y="197" width="8.2" height="18" fill="#f5f3f0"/>
  <rect x="354.3" y="197" width="8.2" height="18" fill="#f5f3f0"/>
  <rect x="362.8" y="197" width="8.2" height="18" fill="#7a8a9a" opacity="0.38"/>
  <rect x="371.3" y="197" width="8.2" height="18" fill="#f5f3f0"/>
  <rect x="379.8" y="197" width="8.2" height="18" fill="#f5f3f0"/>
  <rect x="388.3" y="197" width="8.2" height="18" fill="#f5f3f0"/>
  <rect x="396.8" y="197" width="8.2" height="18" fill="#d4802a" opacity="0.38"/>
  <rect x="405.3" y="197" width="8.2" height="18" fill="#f5f3f0"/>
  <rect x="413.8" y="197" width="8.2" height="18" fill="#f5f3f0"/>
  <rect x="422.3" y="197" width="8.2" height="18" fill="#f5f3f0"/>
  <rect x="430.8" y="197" width="8.2" height="18" fill="#7a8a9a" opacity="0.59"/>
  <rect x="439.3" y="197" width="8.2" height="18" fill="#f5f3f0"/>
  <rect x="447.8" y="197" width="8.2" height="18" fill="#f5f3f0"/>
  <rect x="456.3" y="197" width="8.2" height="18" fill="#f5f3f0"/>
  <rect x="464.8" y="197" width="8.2" height="18" fill="#7a8a9a" opacity="0.38"/>
  <rect x="473.3" y="197" width="8.2" height="18" fill="#d4802a" opacity="0.38"/>
  <rect x="481.8" y="197" width="8.2" height="18" fill="#f5f3f0"/>
  <rect x="490.4" y="197" width="8.2" height="18" fill="#f5f3f0"/>
  <rect x="498.9" y="197" width="8.2" height="18" fill="#7a8a9a" opacity="0.65"/>
  <rect x="507.4" y="197" width="8.2" height="18" fill="#f5f3f0"/>
  <rect x="515.9" y="197" width="8.2" height="18" fill="#f5f3f0"/>
  <rect x="524.4" y="197" width="8.2" height="18" fill="#f5f3f0"/>
  <rect x="532.9" y="197" width="8.2" height="18" fill="#d4802a" opacity="0.38"/>
  <rect x="541.4" y="197" width="8.2" height="18" fill="#7a8a9a" opacity="0.65"/>
  <rect x="549.9" y="197" width="8.2" height="18" fill="#7a8a9a" opacity="0.38"/>
  <rect x="558.4" y="197" width="8.2" height="18" fill="#7a8a9a" opacity="0.38"/>
  <rect x="566.9" y="197" width="8.2" height="18" fill="#7a8a9a" opacity="0.65"/>
  <rect x="575.4" y="197" width="8.2" height="18" fill="#f5f3f0"/>
  <rect x="583.9" y="197" width="8.2" height="18" fill="#d4802a" opacity="0.33"/>
  <rect x="592.4" y="197" width="8.2" height="18" fill="#f5f3f0"/>
  <rect x="600.9" y="197" width="8.2" height="18" fill="#7a8a9a" opacity="0.38"/>
  <rect x="609.4" y="197" width="8.2" height="18" fill="#d4802a" opacity="0.38"/>
  <rect x="617.9" y="197" width="8.2" height="18" fill="#f5f3f0"/>
  <rect x="626.5" y="197" width="8.2" height="18" fill="#f5f3f0"/>
  <rect x="635.0" y="197" width="8.2" height="18" fill="#f5f3f0"/>
  <rect x="643.5" y="197" width="8.2" height="18" fill="#7a8a9a" opacity="0.38"/>
  <rect x="652.0" y="197" width="8.2" height="18" fill="#f5f3f0"/>
  <rect x="660.5" y="197" width="8.2" height="18" fill="#7a8a9a" opacity="1.00"/>
  <rect x="669.0" y="197" width="8.2" height="18" fill="#7a8a9a" opacity="0.38"/>
  <rect x="677.5" y="197" width="8.2" height="18" fill="#f5f3f0"/>
  <text x="290.4556962025316" y="226" text-anchor="middle" font-size="8" font-weight="700" fill="#d4802a">#1 ←</text>
  <text x="664.7341772151898" y="226" text-anchor="middle" font-size="8" font-weight="500" fill="#bbb">#2</text>
  <text x="128.83544303797467" y="226" text-anchor="middle" font-size="8" font-weight="500" fill="#bbb">#3</text>
  <text x="222.40506329113921" y="226" text-anchor="middle" font-size="8" font-weight="500" fill="#bbb">#4</text>
  <rect x="14" y="51" width="227.67088607594934" height="128" fill="white" opacity="0.55"/>
  <rect x="339.2405063291139" y="51" width="346.759493670886" height="128" fill="white" opacity="0.55"/>
  <rect x="241.67088607594934" y="51" width="97.56962025316454" height="128" fill="none" stroke="#d4802a" stroke-width="2" rx="4"/>
  <text x="696" y="63" text-anchor="end" font-size="9" fill="#2d9a3e" font-weight="500">pass</text>
  <text x="696" y="129" text-anchor="end" font-size="9" fill="#cc3e40" font-weight="500">fail</text>
  <line x1="290.4556962025316" y1="234" x2="290.4556962025316" y2="267" stroke="#d4802a" stroke-width="1.5" stroke-dasharray="4,3"/>
  <polygon points="286.4556962025316,263 294.4556962025316,263 290.4556962025316,269" fill="#d4802a"/>
  <rect x="340.3636363636364" y="261" width="61.27272727272727" height="304" fill="#fff7ed" stroke="#d4802a" stroke-width="2" rx="4"/>
  <text x="371.0" y="256" text-anchor="middle" font-size="10" font-weight="700" fill="#d4802a">0/5 pass active · 4/5 fail active · p=0.048</text>
  <text x="48" y="295.0" text-anchor="end" font-size="10" font-weight="600" fill="#2d9a3e">P1</text>
  <rect x="56.5" y="279" width="56.27272727272727" height="24" fill="#9070a0" rx="3"/>
  <text x="84.63636363636364" y="294.0" text-anchor="middle" font-size="8.5" fill="#fff">reason</text>
  <rect x="113.77272727272728" y="279" width="56.27272727272727" height="24" fill="#4a7fae" rx="3"/>
  <text x="141.9090909090909" y="294.0" text-anchor="middle" font-size="7.5" fill="#fff">read src</text>
  <rect x="171.04545454545456" y="279" width="56.27272727272727" height="24" fill="#3a9e96" rx="3"/>
  <text x="199.1818181818182" y="294.0" text-anchor="middle" font-size="8.5" fill="#fff">grep -r</text>
  <rect x="228.3181818181818" y="279" width="56.27272727272727" height="24" fill="#3a9e96" rx="3"/>
  <text x="256.45454545454544" y="294.0" text-anchor="middle" font-size="8.5" fill="#fff">grep -r</text>
  <rect x="285.5909090909091" y="279" width="56.27272727272727" height="24" fill="#b85450" rx="3"/>
  <text x="313.72727272727275" y="294.0" text-anchor="middle" font-size="8.5" fill="#fff">python</text>
  <rect x="342.8636363636364" y="279" width="56.27272727272727" height="24" fill="#f0eee9" rx="3"/>
  <text x="371.0" y="294.0" text-anchor="middle" font-size="8" fill="#ccc">—</text>
  <rect x="400.1363636363636" y="279" width="56.27272727272727" height="24" fill="#c4a820" rx="3"/>
  <text x="428.27272727272725" y="294.0" text-anchor="middle" font-size="7.5" fill="#555">write src</text>
  <rect x="457.40909090909093" y="279" width="56.27272727272727" height="24" fill="#b85450" rx="3"/>
  <text x="485.54545454545456" y="294.0" text-anchor="middle" font-size="8.5" fill="#fff">python</text>
  <rect x="514.6818181818182" y="279" width="56.27272727272727" height="24" fill="#d4802a" rx="3"/>
  <text x="542.8181818181819" y="294.0" text-anchor="middle" font-size="7.5" fill="#555">edit src</text>
  <rect x="571.9545454545455" y="279" width="56.27272727272727" height="24" fill="#b85450" rx="3"/>
  <text x="600.0909090909091" y="294.0" text-anchor="middle" font-size="8.5" fill="#fff">python</text>
  <rect x="629.2272727272727" y="279" width="56.27272727272727" height="24" fill="#9070a0" rx="3"/>
  <text x="657.3636363636364" y="294.0" text-anchor="middle" font-size="8.5" fill="#fff">reason</text>
  <text x="48" y="322.0" text-anchor="end" font-size="10" font-weight="600" fill="#2d9a3e">P2</text>
  <rect x="56.5" y="306" width="56.27272727272727" height="24" fill="#f0eee9" rx="3"/>
  <text x="84.63636363636364" y="321.0" text-anchor="middle" font-size="8" fill="#ccc">—</text>
  <rect x="113.77272727272728" y="306" width="56.27272727272727" height="24" fill="#4a7fae" rx="3"/>
  <text x="141.9090909090909" y="321.0" text-anchor="middle" font-size="7.5" fill="#fff">read src</text>
  <rect x="171.04545454545456" y="306" width="56.27272727272727" height="24" fill="#3a9e96" rx="3"/>
  <text x="199.1818181818182" y="321.0" text-anchor="middle" font-size="8.5" fill="#fff">grep -r</text>
  <rect x="228.3181818181818" y="306" width="56.27272727272727" height="24" fill="#f0eee9" rx="3"/>
  <text x="256.45454545454544" y="321.0" text-anchor="middle" font-size="8" fill="#ccc">—</text>
  <rect x="285.5909090909091" y="306" width="56.27272727272727" height="24" fill="#4a7fae" rx="3"/>
  <text x="313.72727272727275" y="321.0" text-anchor="middle" font-size="7.5" fill="#fff">read src</text>
  <rect x="342.8636363636364" y="306" width="56.27272727272727" height="24" fill="#f0eee9" rx="3"/>
  <text x="371.0" y="321.0" text-anchor="middle" font-size="8" fill="#ccc">—</text>
  <rect x="400.1363636363636" y="306" width="56.27272727272727" height="24" fill="#c4a820" rx="3"/>
  <text x="428.27272727272725" y="321.0" text-anchor="middle" font-size="7.5" fill="#555">write src</text>
  <rect x="457.40909090909093" y="306" width="56.27272727272727" height="24" fill="#f0eee9" rx="3"/>
  <text x="485.54545454545456" y="321.0" text-anchor="middle" font-size="8" fill="#ccc">—</text>
  <rect x="514.6818181818182" y="306" width="56.27272727272727" height="24" fill="#f0eee9" rx="3"/>
  <text x="542.8181818181819" y="321.0" text-anchor="middle" font-size="8" fill="#ccc">—</text>
  <rect x="571.9545454545455" y="306" width="56.27272727272727" height="24" fill="#b85450" rx="3"/>
  <text x="600.0909090909091" y="321.0" text-anchor="middle" font-size="8.5" fill="#fff">python</text>
  <rect x="629.2272727272727" y="306" width="56.27272727272727" height="24" fill="#9070a0" rx="3"/>
  <text x="657.3636363636364" y="321.0" text-anchor="middle" font-size="8.5" fill="#fff">reason</text>
  <text x="48" y="349.0" text-anchor="end" font-size="10" font-weight="600" fill="#2d9a3e">P3</text>
  <rect x="56.5" y="333" width="56.27272727272727" height="24" fill="#3a9e96" rx="3"/>
  <text x="84.63636363636364" y="348.0" text-anchor="middle" font-size="8.5" fill="#fff">grep</text>
  <rect x="113.77272727272728" y="333" width="56.27272727272727" height="24" fill="#4a7fae" rx="3"/>
  <text x="141.9090909090909" y="348.0" text-anchor="middle" font-size="7.5" fill="#fff">read src</text>
  <rect x="171.04545454545456" y="333" width="56.27272727272727" height="24" fill="#3a9e96" rx="3"/>
  <text x="199.1818181818182" y="348.0" text-anchor="middle" font-size="8.5" fill="#fff">grep</text>
  <rect x="228.3181818181818" y="333" width="56.27272727272727" height="24" fill="#4a7fae" rx="3"/>
  <text x="256.45454545454544" y="348.0" text-anchor="middle" font-size="7.5" fill="#fff">read src</text>
  <rect x="285.5909090909091" y="333" width="56.27272727272727" height="24" fill="#4a7fae" rx="3"/>
  <text x="313.72727272727275" y="348.0" text-anchor="middle" font-size="7.5" fill="#fff">read src</text>
  <rect x="342.8636363636364" y="333" width="56.27272727272727" height="24" fill="#f0eee9" rx="3"/>
  <text x="371.0" y="348.0" text-anchor="middle" font-size="8" fill="#ccc">—</text>
  <rect x="400.1363636363636" y="333" width="56.27272727272727" height="24" fill="#c4a820" rx="3"/>
  <text x="428.27272727272725" y="348.0" text-anchor="middle" font-size="7.5" fill="#555">write src</text>
  <rect x="457.40909090909093" y="333" width="56.27272727272727" height="24" fill="#f0eee9" rx="3"/>
  <text x="485.54545454545456" y="348.0" text-anchor="middle" font-size="8" fill="#ccc">—</text>
  <rect x="514.6818181818182" y="333" width="56.27272727272727" height="24" fill="#f0eee9" rx="3"/>
  <text x="542.8181818181819" y="348.0" text-anchor="middle" font-size="8" fill="#ccc">—</text>
  <rect x="571.9545454545455" y="333" width="56.27272727272727" height="24" fill="#b85450" rx="3"/>
  <text x="600.0909090909091" y="348.0" text-anchor="middle" font-size="8.5" fill="#fff">python</text>
  <rect x="629.2272727272727" y="333" width="56.27272727272727" height="24" fill="#9070a0" rx="3"/>
  <text x="657.3636363636364" y="348.0" text-anchor="middle" font-size="8.5" fill="#fff">reason</text>
  <text x="48" y="376.0" text-anchor="end" font-size="10" font-weight="600" fill="#2d9a3e">P4</text>
  <rect x="56.5" y="360" width="56.27272727272727" height="24" fill="#f0eee9" rx="3"/>
  <text x="84.63636363636364" y="375.0" text-anchor="middle" font-size="8" fill="#ccc">—</text>
  <rect x="113.77272727272728" y="360" width="56.27272727272727" height="24" fill="#f0eee9" rx="3"/>
  <text x="141.9090909090909" y="375.0" text-anchor="middle" font-size="8" fill="#ccc">—</text>
  <rect x="171.04545454545456" y="360" width="56.27272727272727" height="24" fill="#3a9e96" rx="3"/>
  <text x="199.1818181818182" y="375.0" text-anchor="middle" font-size="8.5" fill="#fff">grep -r</text>
  <rect x="228.3181818181818" y="360" width="56.27272727272727" height="24" fill="#4a7fae" rx="3"/>
  <text x="256.45454545454544" y="375.0" text-anchor="middle" font-size="7.5" fill="#fff">read src</text>
  <rect x="285.5909090909091" y="360" width="56.27272727272727" height="24" fill="#4a7fae" rx="3"/>
  <text x="313.72727272727275" y="375.0" text-anchor="middle" font-size="7.5" fill="#fff">read src</text>
  <rect x="342.8636363636364" y="360" width="56.27272727272727" height="24" fill="#f0eee9" rx="3"/>
  <text x="371.0" y="375.0" text-anchor="middle" font-size="8" fill="#ccc">—</text>
  <rect x="400.1363636363636" y="360" width="56.27272727272727" height="24" fill="#c4a820" rx="3"/>
  <text x="428.27272727272725" y="375.0" text-anchor="middle" font-size="7.5" fill="#555">write src</text>
  <rect x="457.40909090909093" y="360" width="56.27272727272727" height="24" fill="#b85450" rx="3"/>
  <text x="485.54545454545456" y="375.0" text-anchor="middle" font-size="8.5" fill="#fff">python</text>
  <rect x="514.6818181818182" y="360" width="56.27272727272727" height="24" fill="#f0eee9" rx="3"/>
  <text x="542.8181818181819" y="375.0" text-anchor="middle" font-size="8" fill="#ccc">—</text>
  <rect x="571.9545454545455" y="360" width="56.27272727272727" height="24" fill="#b85450" rx="3"/>
  <text x="600.0909090909091" y="375.0" text-anchor="middle" font-size="8.5" fill="#fff">python</text>
  <rect x="629.2272727272727" y="360" width="56.27272727272727" height="24" fill="#9070a0" rx="3"/>
  <text x="657.3636363636364" y="375.0" text-anchor="middle" font-size="8.5" fill="#fff">reason</text>
  <text x="48" y="403.0" text-anchor="end" font-size="10" font-weight="600" fill="#2d9a3e">P5</text>
  <rect x="56.5" y="387" width="56.27272727272727" height="24" fill="#f0eee9" rx="3"/>
  <text x="84.63636363636364" y="402.0" text-anchor="middle" font-size="8" fill="#ccc">—</text>
  <rect x="113.77272727272728" y="387" width="56.27272727272727" height="24" fill="#f0eee9" rx="3"/>
  <text x="141.9090909090909" y="402.0" text-anchor="middle" font-size="8" fill="#ccc">—</text>
  <rect x="171.04545454545456" y="387" width="56.27272727272727" height="24" fill="#3a9e96" rx="3"/>
  <text x="199.1818181818182" y="402.0" text-anchor="middle" font-size="8.5" fill="#fff">grep -r</text>
  <rect x="228.3181818181818" y="387" width="56.27272727272727" height="24" fill="#f0eee9" rx="3"/>
  <text x="256.45454545454544" y="402.0" text-anchor="middle" font-size="8" fill="#ccc">—</text>
  <rect x="285.5909090909091" y="387" width="56.27272727272727" height="24" fill="#7aaed4" rx="3"/>
  <text x="313.72727272727275" y="402.0" text-anchor="middle" font-size="7.5" fill="#555">read test</text>
  <rect x="342.8636363636364" y="387" width="56.27272727272727" height="24" fill="#f0eee9" rx="3"/>
  <text x="371.0" y="402.0" text-anchor="middle" font-size="8" fill="#ccc">—</text>
  <rect x="400.1363636363636" y="387" width="56.27272727272727" height="24" fill="#c4a820" rx="3"/>
  <text x="428.27272727272725" y="402.0" text-anchor="middle" font-size="7.5" fill="#555">write src</text>
  <rect x="457.40909090909093" y="387" width="56.27272727272727" height="24" fill="#b85450" rx="3"/>
  <text x="485.54545454545456" y="402.0" text-anchor="middle" font-size="8.5" fill="#fff">python</text>
  <rect x="514.6818181818182" y="387" width="56.27272727272727" height="24" fill="#b85450" rx="3"/>
  <text x="542.8181818181819" y="402.0" text-anchor="middle" font-size="8.5" fill="#fff">setup</text>
  <rect x="571.9545454545455" y="387" width="56.27272727272727" height="24" fill="#b85450" rx="3"/>
  <text x="600.0909090909091" y="402.0" text-anchor="middle" font-size="8.5" fill="#fff">python</text>
  <rect x="629.2272727272727" y="387" width="56.27272727272727" height="24" fill="#9070a0" rx="3"/>
  <text x="657.3636363636364" y="402.0" text-anchor="middle" font-size="8.5" fill="#fff">reason</text>
  <text x="48" y="440.0" text-anchor="end" font-size="10" font-weight="600" fill="#cc3e40">F1</text>
  <rect x="56.5" y="424" width="56.27272727272727" height="24" fill="#f0eee9" rx="3"/>
  <text x="84.63636363636364" y="439.0" text-anchor="middle" font-size="8" fill="#ccc">—</text>
  <rect x="113.77272727272728" y="424" width="56.27272727272727" height="24" fill="#f0eee9" rx="3"/>
  <text x="141.9090909090909" y="439.0" text-anchor="middle" font-size="8" fill="#ccc">—</text>
  <rect x="171.04545454545456" y="424" width="56.27272727272727" height="24" fill="#f0eee9" rx="3"/>
  <text x="199.1818181818182" y="439.0" text-anchor="middle" font-size="8" fill="#ccc">—</text>
  <rect x="228.3181818181818" y="424" width="56.27272727272727" height="24" fill="#4a7fae" rx="3"/>
  <text x="256.45454545454544" y="439.0" text-anchor="middle" font-size="7.5" fill="#fff">read src</text>
  <rect x="285.5909090909091" y="424" width="56.27272727272727" height="24" fill="#4a7fae" rx="3"/>
  <text x="313.72727272727275" y="439.0" text-anchor="middle" font-size="7.5" fill="#fff">read src</text>
  <rect x="342.8636363636364" y="424" width="56.27272727272727" height="24" fill="#7aaed4" rx="3"/>
  <text x="371.0" y="439.0" text-anchor="middle" font-size="7.5" fill="#555">read test</text>
  <rect x="400.1363636363636" y="424" width="56.27272727272727" height="24" fill="#c4a820" rx="3"/>
  <text x="428.27272727272725" y="439.0" text-anchor="middle" font-size="7.5" fill="#555">write src</text>
  <rect x="457.40909090909093" y="424" width="56.27272727272727" height="24" fill="#b85450" rx="3"/>
  <text x="485.54545454545456" y="439.0" text-anchor="middle" font-size="8.5" fill="#fff">python</text>
  <rect x="514.6818181818182" y="424" width="56.27272727272727" height="24" fill="#c4a820" rx="3"/>
  <text x="542.8181818181819" y="439.0" text-anchor="middle" font-size="7.5" fill="#555">write src</text>
  <rect x="571.9545454545455" y="424" width="56.27272727272727" height="24" fill="#b85450" rx="3"/>
  <text x="600.0909090909091" y="439.0" text-anchor="middle" font-size="8.5" fill="#fff">python</text>
  <rect x="629.2272727272727" y="424" width="56.27272727272727" height="24" fill="#9070a0" rx="3"/>
  <text x="657.3636363636364" y="439.0" text-anchor="middle" font-size="8.5" fill="#fff">reason</text>
  <text x="48" y="467.0" text-anchor="end" font-size="10" font-weight="600" fill="#cc3e40">F2</text>
  <rect x="56.5" y="451" width="56.27272727272727" height="24" fill="#f0eee9" rx="3"/>
  <text x="84.63636363636364" y="466.0" text-anchor="middle" font-size="8" fill="#ccc">—</text>
  <rect x="113.77272727272728" y="451" width="56.27272727272727" height="24" fill="#f0eee9" rx="3"/>
  <text x="141.9090909090909" y="466.0" text-anchor="middle" font-size="8" fill="#ccc">—</text>
  <rect x="171.04545454545456" y="451" width="56.27272727272727" height="24" fill="#f0eee9" rx="3"/>
  <text x="199.1818181818182" y="466.0" text-anchor="middle" font-size="8" fill="#ccc">—</text>
  <rect x="228.3181818181818" y="451" width="56.27272727272727" height="24" fill="#4a7fae" rx="3"/>
  <text x="256.45454545454544" y="466.0" text-anchor="middle" font-size="7.5" fill="#fff">read src</text>
  <rect x="285.5909090909091" y="451" width="56.27272727272727" height="24" fill="#4a7fae" rx="3"/>
  <text x="313.72727272727275" y="466.0" text-anchor="middle" font-size="7.5" fill="#fff">read src</text>
  <rect x="342.8636363636364" y="451" width="56.27272727272727" height="24" fill="#f0eee9" rx="3"/>
  <text x="371.0" y="466.0" text-anchor="middle" font-size="8" fill="#ccc">—</text>
  <rect x="400.1363636363636" y="451" width="56.27272727272727" height="24" fill="#c4a820" rx="3"/>
  <text x="428.27272727272725" y="466.0" text-anchor="middle" font-size="7.5" fill="#555">write src</text>
  <rect x="457.40909090909093" y="451" width="56.27272727272727" height="24" fill="#f0eee9" rx="3"/>
  <text x="485.54545454545456" y="466.0" text-anchor="middle" font-size="8" fill="#ccc">—</text>
  <rect x="514.6818181818182" y="451" width="56.27272727272727" height="24" fill="#f0eee9" rx="3"/>
  <text x="542.8181818181819" y="466.0" text-anchor="middle" font-size="8" fill="#ccc">—</text>
  <rect x="571.9545454545455" y="451" width="56.27272727272727" height="24" fill="#b85450" rx="3"/>
  <text x="600.0909090909091" y="466.0" text-anchor="middle" font-size="8.5" fill="#fff">python</text>
  <rect x="629.2272727272727" y="451" width="56.27272727272727" height="24" fill="#9070a0" rx="3"/>
  <text x="657.3636363636364" y="466.0" text-anchor="middle" font-size="8.5" fill="#fff">reason</text>
  <text x="48" y="494.0" text-anchor="end" font-size="10" font-weight="600" fill="#cc3e40">F3</text>
  <rect x="56.5" y="478" width="56.27272727272727" height="24" fill="#f0eee9" rx="3"/>
  <text x="84.63636363636364" y="493.0" text-anchor="middle" font-size="8" fill="#ccc">—</text>
  <rect x="113.77272727272728" y="478" width="56.27272727272727" height="24" fill="#f0eee9" rx="3"/>
  <text x="141.9090909090909" y="493.0" text-anchor="middle" font-size="8" fill="#ccc">—</text>
  <rect x="171.04545454545456" y="478" width="56.27272727272727" height="24" fill="#3a9e96" rx="3"/>
  <text x="199.1818181818182" y="493.0" text-anchor="middle" font-size="8.5" fill="#fff">grep -r</text>
  <rect x="228.3181818181818" y="478" width="56.27272727272727" height="24" fill="#f0eee9" rx="3"/>
  <text x="256.45454545454544" y="493.0" text-anchor="middle" font-size="8" fill="#ccc">—</text>
  <rect x="285.5909090909091" y="478" width="56.27272727272727" height="24" fill="#f0eee9" rx="3"/>
  <text x="313.72727272727275" y="493.0" text-anchor="middle" font-size="8" fill="#ccc">—</text>
  <rect x="342.8636363636364" y="478" width="56.27272727272727" height="24" fill="#b85450" rx="3"/>
  <text x="371.0" y="493.0" text-anchor="middle" font-size="8.5" fill="#fff">python</text>
  <rect x="400.1363636363636" y="478" width="56.27272727272727" height="24" fill="#b85450" rx="3"/>
  <text x="428.27272727272725" y="493.0" text-anchor="middle" font-size="8.5" fill="#fff">setup</text>
  <rect x="457.40909090909093" y="478" width="56.27272727272727" height="24" fill="#b85450" rx="3"/>
  <text x="485.54545454545456" y="493.0" text-anchor="middle" font-size="8.5" fill="#fff">python</text>
  <rect x="514.6818181818182" y="478" width="56.27272727272727" height="24" fill="#c4a820" rx="3"/>
  <text x="542.8181818181819" y="493.0" text-anchor="middle" font-size="7.5" fill="#555">write src</text>
  <rect x="571.9545454545455" y="478" width="56.27272727272727" height="24" fill="#b85450" rx="3"/>
  <text x="600.0909090909091" y="493.0" text-anchor="middle" font-size="8.5" fill="#fff">python</text>
  <rect x="629.2272727272727" y="478" width="56.27272727272727" height="24" fill="#9070a0" rx="3"/>
  <text x="657.3636363636364" y="493.0" text-anchor="middle" font-size="8.5" fill="#fff">reason</text>
  <text x="48" y="521.0" text-anchor="end" font-size="10" font-weight="600" fill="#cc3e40">F4</text>
  <rect x="56.5" y="505" width="56.27272727272727" height="24" fill="#f0eee9" rx="3"/>
  <text x="84.63636363636364" y="520.0" text-anchor="middle" font-size="8" fill="#ccc">—</text>
  <rect x="113.77272727272728" y="505" width="56.27272727272727" height="24" fill="#f0eee9" rx="3"/>
  <text x="141.9090909090909" y="520.0" text-anchor="middle" font-size="8" fill="#ccc">—</text>
  <rect x="171.04545454545456" y="505" width="56.27272727272727" height="24" fill="#3a9e96" rx="3"/>
  <text x="199.1818181818182" y="520.0" text-anchor="middle" font-size="8.5" fill="#fff">grep</text>
  <rect x="228.3181818181818" y="505" width="56.27272727272727" height="24" fill="#4a7fae" rx="3"/>
  <text x="256.45454545454544" y="520.0" text-anchor="middle" font-size="7.5" fill="#fff">read src</text>
  <rect x="285.5909090909091" y="505" width="56.27272727272727" height="24" fill="#7aaed4" rx="3"/>
  <text x="313.72727272727275" y="520.0" text-anchor="middle" font-size="7.5" fill="#555">read dir</text>
  <rect x="342.8636363636364" y="505" width="56.27272727272727" height="24" fill="#7aaed4" rx="3"/>
  <text x="371.0" y="520.0" text-anchor="middle" font-size="7.5" fill="#555">read test</text>
  <rect x="400.1363636363636" y="505" width="56.27272727272727" height="24" fill="#c4a820" rx="3"/>
  <text x="428.27272727272725" y="520.0" text-anchor="middle" font-size="7.5" fill="#555">write src</text>
  <rect x="457.40909090909093" y="505" width="56.27272727272727" height="24" fill="#f0eee9" rx="3"/>
  <text x="485.54545454545456" y="520.0" text-anchor="middle" font-size="8" fill="#ccc">—</text>
  <rect x="514.6818181818182" y="505" width="56.27272727272727" height="24" fill="#f0eee9" rx="3"/>
  <text x="542.8181818181819" y="520.0" text-anchor="middle" font-size="8" fill="#ccc">—</text>
  <rect x="571.9545454545455" y="505" width="56.27272727272727" height="24" fill="#b85450" rx="3"/>
  <text x="600.0909090909091" y="520.0" text-anchor="middle" font-size="8.5" fill="#fff">python</text>
  <rect x="629.2272727272727" y="505" width="56.27272727272727" height="24" fill="#9070a0" rx="3"/>
  <text x="657.3636363636364" y="520.0" text-anchor="middle" font-size="8.5" fill="#fff">reason</text>
  <text x="48" y="548.0" text-anchor="end" font-size="10" font-weight="600" fill="#cc3e40">F5</text>
  <rect x="56.5" y="532" width="56.27272727272727" height="24" fill="#b85450" rx="3"/>
  <text x="84.63636363636364" y="547.0" text-anchor="middle" font-size="8.5" fill="#fff">python</text>
  <rect x="113.77272727272728" y="532" width="56.27272727272727" height="24" fill="#4a7fae" rx="3"/>
  <text x="141.9090909090909" y="547.0" text-anchor="middle" font-size="7.5" fill="#fff">read src</text>
  <rect x="171.04545454545456" y="532" width="56.27272727272727" height="24" fill="#f0eee9" rx="3"/>
  <text x="199.1818181818182" y="547.0" text-anchor="middle" font-size="8" fill="#ccc">—</text>
  <rect x="228.3181818181818" y="532" width="56.27272727272727" height="24" fill="#4a7fae" rx="3"/>
  <text x="256.45454545454544" y="547.0" text-anchor="middle" font-size="7.5" fill="#fff">read src</text>
  <rect x="285.5909090909091" y="532" width="56.27272727272727" height="24" fill="#4a7fae" rx="3"/>
  <text x="313.72727272727275" y="547.0" text-anchor="middle" font-size="7.5" fill="#fff">read src</text>
  <rect x="342.8636363636364" y="532" width="56.27272727272727" height="24" fill="#b85450" rx="3"/>
  <text x="371.0" y="547.0" text-anchor="middle" font-size="8.5" fill="#fff">python</text>
  <rect x="400.1363636363636" y="532" width="56.27272727272727" height="24" fill="#b85450" rx="3"/>
  <text x="428.27272727272725" y="547.0" text-anchor="middle" font-size="8.5" fill="#fff">python</text>
  <rect x="457.40909090909093" y="532" width="56.27272727272727" height="24" fill="#b85450" rx="3"/>
  <text x="485.54545454545456" y="547.0" text-anchor="middle" font-size="8.5" fill="#fff">python</text>
  <rect x="514.6818181818182" y="532" width="56.27272727272727" height="24" fill="#c4a820" rx="3"/>
  <text x="542.8181818181819" y="547.0" text-anchor="middle" font-size="7.5" fill="#555">write src</text>
  <rect x="571.9545454545455" y="532" width="56.27272727272727" height="24" fill="#b85450" rx="3"/>
  <text x="600.0909090909091" y="547.0" text-anchor="middle" font-size="8.5" fill="#fff">python</text>
  <rect x="629.2272727272727" y="532" width="56.27272727272727" height="24" fill="#9070a0" rx="3"/>
  <text x="657.3636363636364" y="547.0" text-anchor="middle" font-size="8.5" fill="#fff">reason</text>
  <line x1="371.0" y1="565" x2="371.0" y2="595" stroke="#d4802a" stroke-width="1.5" stroke-dasharray="3,3"/>
  <text x="350.0" y="591" text-anchor="middle" font-size="12" font-weight="600" fill="#bbb">vs</text>
  <rect x="14" y="599" width="324.0" height="155" fill="#f0f7f0" stroke="#2d9a3e" stroke-width="1.5" rx="6"/>
  <text x="26" y="621" font-size="13" font-weight="700" fill="#2d9a3e">Already moved to implementation</text>
  <text x="26" y="643" font-size="11" font-style="italic" fill="#555">Pass runs have already identified the type</text>
  <text x="26" y="659" font-size="11" font-style="italic" fill="#555">constraint and started writing the fix. They</text>
  <text x="26" y="675" font-size="11" font-style="italic" fill="#555">don’t need to read test files at this point —</text>
  <text x="26" y="691" font-size="11" font-style="italic" fill="#555">they know what’s wrong.</text>
  <text x="26" y="715" font-size="11" font-weight="600" fill="#2d9a3e">Edits the type definition directly. Tests pass.</text>
  <rect x="362.0" y="599" width="324.0" height="155" fill="#fdf0f0" stroke="#cc3e40" stroke-width="1.5" rx="6"/>
  <text x="374.0" y="621" font-size="13" font-weight="700" fill="#cc3e40">Still reading test files</text>
  <text x="374.0" y="643" font-size="11" font-style="italic" fill="#555">“Let me look at existing tests to understand the</text>
  <text x="374.0" y="659" font-size="11" font-style="italic" fill="#555">expected behavior.”</text>
  <text x="374.0" y="683" font-size="11" font-weight="600" fill="#cc3e40">Keeps exploring instead of acting. Eventually</text>
  <text x="374.0" y="699" font-size="11" font-weight="600" fill="#cc3e40">patches the implementation without fixing the</text>
  <text x="374.0" y="715" font-size="11" font-weight="600" fill="#cc3e40">type definition. Final tests catch the incomplete</text>
</svg>
</div>

The strongest divergence (p=0.048) is fail-biased. Around step 20 of ~50, four of five fail runs are still reading test files and running exploratory Python. Zero pass runs are. The pass runs have already identified the root cause (the type definition excludes lists) and moved on to writing the fix.

This is the moment that determines the outcome. Fail runs keep exploring after the point where they have enough information to act. They eventually patch the implementation but miss the type definition, and the final test suite catches the incomplete fix.

Same agent. Same starting conditions. The difference: pass runs recognized they had enough information and started implementing. Fail runs didn't.

---

## At scale

One task is a story. A thousand tasks is a pattern.

We ran the same analysis across all 1,096 mixed-outcome tasks. At each divergence point, we extracted what the pass runs did differently and clustered those differences by content similarity (TF-IDF on the step descriptions). Eight failure modes account for 91% of all divergence points.

<div class="chart-scroll chart-scroll--wide">
<svg role="img" aria-label="Failure modes at scale: wasted orientation 18%, wrong file 15%, and six more" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 380" style="font-family: system-ui, -apple-system, sans-serif; background: #fff; max-width:700px; width:100%; height:auto; min-height:250px;">
<title>Failure modes at scale: wasted orientation 18%, wrong file 15%, and six more</title>
<text x="350.0" y="22" text-anchor="middle" fill="#333" font-size="16" font-weight="600">At scale</text>
<text x="350.0" y="40" text-anchor="middle" fill="#777" font-size="10.5">1,096 mixed-outcome tasks · 12,854 runs · top 8 of 13 clusters shown</text>
<line x1="295.0" y1="51" x2="295.0" y2="339" stroke="#e8e8e8" stroke-width="1"/>
<text x="295.0" y="353" text-anchor="middle" fill="#777" font-size="9">5%</text>
<line x1="410.0" y1="51" x2="410.0" y2="339" stroke="#e8e8e8" stroke-width="1"/>
<text x="410.0" y="353" text-anchor="middle" fill="#777" font-size="9">10%</text>
<line x1="525.0" y1="51" x2="525.0" y2="339" stroke="#e8e8e8" stroke-width="1"/>
<text x="525.0" y="353" text-anchor="middle" fill="#777" font-size="9">15%</text>
<line x1="640.0" y1="51" x2="640.0" y2="339" stroke="#e8e8e8" stroke-width="1"/>
<text x="640.0" y="353" text-anchor="middle" fill="#777" font-size="9">20%</text>
<text x="172" y="73.0" text-anchor="end" fill="#333" font-size="11.5">Wasted orientation</text>
<rect x="180" y="55" width="414.0" height="28" rx="3" fill="#3a9e96" opacity="1.00"/>
<text x="600.0" y="73.0" text-anchor="start" fill="#333" font-size="11" font-weight="600">18%</text>
<text x="172" y="109.0" text-anchor="end" fill="#333" font-size="11.5">Wrong file targeted</text>
<rect x="180" y="91" width="345.0" height="28" rx="3" fill="#3a9e96" opacity="0.89"/>
<text x="531.0" y="109.0" text-anchor="start" fill="#333" font-size="11" font-weight="600">15%</text>
<text x="172" y="145.0" text-anchor="end" fill="#333" font-size="11.5">Skipped reasoning</text>
<rect x="180" y="127" width="299.0" height="28" rx="3" fill="#3a9e96" opacity="0.82"/>
<text x="485.0" y="145.0" text-anchor="start" fill="#333" font-size="11" font-weight="600">13%</text>
<text x="172" y="181.0" text-anchor="end" fill="#333" font-size="11.5">Premature test</text>
<rect x="180" y="163" width="253.0" height="28" rx="3" fill="#3a9e96" opacity="0.75"/>
<text x="439.0" y="181.0" text-anchor="start" fill="#333" font-size="11" font-weight="600">11%</text>
<text x="172" y="217.0" text-anchor="end" fill="#333" font-size="11.5">Edit-read loop</text>
<rect x="180" y="199" width="230.0" height="28" rx="3" fill="#3a9e96" opacity="0.71"/>
<text x="416.0" y="217.0" text-anchor="start" fill="#333" font-size="11" font-weight="600">10%</text>
<text x="172" y="253.0" text-anchor="end" fill="#333" font-size="11.5">Incomplete exploration</text>
<rect x="180" y="235" width="207.0" height="28" rx="3" fill="#3a9e96" opacity="0.67"/>
<text x="393.0" y="253.0" text-anchor="start" fill="#333" font-size="11" font-weight="600">9%</text>
<text x="172" y="289.0" text-anchor="end" fill="#333" font-size="11.5">Wrong test strategy</text>
<rect x="180" y="271" width="184.0" height="28" rx="3" fill="#3a9e96" opacity="0.64"/>
<text x="370.0" y="289.0" text-anchor="start" fill="#333" font-size="11" font-weight="600">8%</text>
<text x="172" y="325.0" text-anchor="end" fill="#333" font-size="11.5">Missing verification</text>
<rect x="180" y="307" width="161.0" height="28" rx="3" fill="#3a9e96" opacity="0.60"/>
<text x="347.0" y="325.0" text-anchor="start" fill="#333" font-size="11" font-weight="600">7%</text>
<text x="350.0" y="371" text-anchor="middle" fill="#777" font-size="9.5" font-style="italic">Divergence points clustered by TF-IDF content similarity</text>
</svg>
</div>

The biggest one, "wasted orientation," means the agent kept reading and searching files it had already examined. It's not exploring. It's spinning. The second, "wrong file targeted," means the agent committed to editing the wrong source file and never recovered. Both are diagnosable in real time.

---

## What predicts success

The clusters describe what happens at the fork point. These features predict which side of it you end up on. For each behavioral feature below, we split each task's runs at the median and compared pass rates between the two groups — a within-task natural experiment that controls for task difficulty.

<div class="chart-scroll chart-scroll--wide">
<svg role="img" aria-label="What predicts it: test timing +6.8pp, uncertainty -6.5pp, trajectory shape +6.1pp, hypothesis -5.7pp, edit breadth +4.8pp" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 444" style="max-width:700px;width:100%;height:auto;min-height:280px" font-family="system-ui, -apple-system, sans-serif">
<title>What predicts it: test timing +6.8pp, uncertainty -6.5pp, trajectory shape +6.1pp, hypothesis -5.7pp, edit breadth +4.8pp</title>
<rect width="700" height="444" fill="white"/>
<text x="350.0" y="24" text-anchor="middle" font-size="16" font-weight="700" fill="#333">What predicts it</text>
<text x="350.0" y="44" text-anchor="middle" font-size="11" fill="#888">Within-task pass-rate deltas (pp = percentage points)</text>
<line x1="350" y1="64" x2="350" y2="358" stroke="#ddd" stroke-width="1"/>
<text x="350" y="60" text-anchor="middle" font-size="9" fill="#888">0</text>
<rect x="350.0" y="64" width="174.9" height="22" rx="3" fill="#2d9a3e" opacity="0.82"/>
<text x="340" y="80.0" text-anchor="end" font-size="13" font-weight="600" fill="#333">Test timing</text>
<text x="532.9" y="80.0" text-anchor="start" font-size="12" font-weight="700" fill="#2d9a3e">+6.8pp</text>
<text x="30" y="102" text-anchor="start" font-size="10.5" fill="#888">Agents that delay testing until they have a fix</text>
<rect x="182.9" y="132" width="167.1" height="22" rx="3" fill="#cc3e40" opacity="0.82"/>
<text x="360" y="148.0" text-anchor="start" font-size="13" font-weight="600" fill="#333">Uncertainty language</text>
<text x="174.9" y="148.0" text-anchor="end" font-size="12" font-weight="700" fill="#cc3e40">-6.5pp</text>
<text x="30" y="170" text-anchor="start" font-size="10.5" fill="#888">Agents that hedge (“maybe”, “might”, “let me try”)</text>
<rect x="350.0" y="200" width="156.9" height="22" rx="3" fill="#2d9a3e" opacity="0.82"/>
<text x="340" y="216.0" text-anchor="end" font-size="13" font-weight="600" fill="#333">Trajectory shape</text>
<text x="514.9" y="216.0" text-anchor="start" font-size="12" font-weight="700" fill="#2d9a3e">+6.1pp</text>
<text x="30" y="238" text-anchor="start" font-size="10.5" fill="#888">Agents that follow an explore→modify→verify arc</text>
<rect x="203.4" y="268" width="146.6" height="22" rx="3" fill="#cc3e40" opacity="0.82"/>
<text x="360" y="284.0" text-anchor="start" font-size="13" font-weight="600" fill="#333">Hypothesis formation</text>
<text x="195.4" y="284.0" text-anchor="end" font-size="12" font-weight="700" fill="#cc3e40">-5.7pp</text>
<text x="30" y="306" text-anchor="start" font-size="10.5" fill="#888">Agents that form hypotheses (“I think the issue is…”)</text>
<rect x="350.0" y="336" width="123.4" height="22" rx="3" fill="#2d9a3e" opacity="0.82"/>
<text x="340" y="352.0" text-anchor="end" font-size="13" font-weight="600" fill="#333">Edit breadth</text>
<text x="481.4" y="352.0" text-anchor="start" font-size="12" font-weight="700" fill="#2d9a3e">+4.8pp</text>
<text x="30" y="374" text-anchor="start" font-size="10.5" fill="#888">Agents that edit across multiple files instead of repeatedly editing one</text>
<text x="350.0" y="430" text-anchor="middle" font-size="10" fill="#888">Each feature measured via natural experiment: within-task median split, 1,096 tasks</text>
</svg>
</div>

Two things jump out. First, delaying tests (running them after you have a plausible fix, not as an exploration tool) is the strongest single predictor. Second, uncertainty language and explicit hypothesis formation predict failure. The agent that says "I think the issue might be..." does worse than the agent that just searches until it finds the answer.

These aren't causal claims. Same-agent stochastic variation means path dependence: an early choice cascades into downstream behaviors. The test-timing feature could be a cause (running tests too early wastes steps) or a consequence (agents that already understand the problem naturally test later). Both interpretations are actionable.

**A note on effect sizes:** +6.8 percentage points is the observational gap from stochastic variation alone. The actual impact of intervening on these behaviors could be larger or smaller. We framed a causal intervention study but haven't run it yet. The diagnostic value of showing teams their failure modes may matter more than the point estimates.

---

## What to do about it

If you can detect the pattern in real time, you can nudge the agent before it commits to a bad path. Three examples:

<div class="chart-scroll chart-scroll--wide">
<svg role="img" aria-label="Scaffold interventions: delay broad testing, verify before expanding, stop hammering one file" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 320" style="font-family: system-ui, -apple-system, sans-serif; background: #fff; max-width:700px; width:100%; height:auto; min-height:210px;">
<title>Scaffold interventions: delay broad testing, verify before expanding, stop hammering one file</title>
<text x="350.0" y="20" text-anchor="middle" fill="#333" font-size="16" font-weight="600">What to do about it</text>
<text x="350.0" y="36" text-anchor="middle" fill="#777" font-size="10.5">Scaffold interventions: detect the pattern, nudge the behavior</text>
<rect x="20.0" y="46" width="210" height="238" rx="6" fill="#f8f7f5" stroke="#e0ddd8" stroke-width="1"/>
<circle cx="38.0" cy="64" r="10" fill="#3a9e96"/>
<text x="38.0" y="68" text-anchor="middle" fill="#fff" font-size="11" font-weight="700">1</text>
<g transform="translate(182.0,50)">
  <circle cx="18" cy="18" r="14" fill="none" stroke="#3a9e96" stroke-width="2"/>
  <line x1="18" y1="18" x2="18" y2="10" stroke="#3a9e96" stroke-width="2" stroke-linecap="round"/>
  <line x1="18" y1="18" x2="24" y2="18" stroke="#3a9e96" stroke-width="2" stroke-linecap="round"/>
</g>
<text x="34.0" y="94" fill="#3a9e96" font-size="13" font-weight="700">Delay broad testing</text>
<rect x="30.0" y="102" width="190" height="24" rx="4" fill="#2c2c2c"/>
<text x="38.0" y="118" fill="#e0e0e0" font-size="8.5" font-family="'SF Mono', 'Menlo', 'Consolas', monospace">edited_files &gt;= 2 AND tests_run == 0</text>
<text x="34.0" y="144" fill="#333" font-size="10.5">You’ve edited multiple files.</text>
<text x="34.0" y="158" fill="#333" font-size="10.5">Consider focusing your testing on</text>
<text x="34.0" y="172" fill="#333" font-size="10.5">the specific change rather than</text>
<text x="34.0" y="186" fill="#333" font-size="10.5">running the full suite.</text>
<rect x="245.0" y="46" width="210" height="238" rx="6" fill="#f8f7f5" stroke="#e0ddd8" stroke-width="1"/>
<circle cx="263.0" cy="64" r="10" fill="#3a9e96"/>
<text x="263.0" y="68" text-anchor="middle" fill="#fff" font-size="11" font-weight="700">2</text>
<g transform="translate(407.0,50)">
  <circle cx="16" cy="16" r="10" fill="none" stroke="#3a9e96" stroke-width="2"/>
  <line x1="23" y1="23" x2="30" y2="30" stroke="#3a9e96" stroke-width="2.5" stroke-linecap="round"/>
  <polyline points="11,16 15,20 21,12" fill="none" stroke="#3a9e96" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
</g>
<text x="259.0" y="94" fill="#3a9e96" font-size="13" font-weight="700">Verify before expanding</text>
<rect x="255.0" y="102" width="190" height="24" rx="4" fill="#2c2c2c"/>
<text x="263.0" y="118" fill="#e0e0e0" font-size="8.5" font-family="'SF Mono', 'Menlo', 'Consolas', monospace">new_files_read &gt;= 5 AND tests_run == 0</text>
<text x="259.0" y="144" fill="#333" font-size="10.5">You’ve explored several files.</text>
<text x="259.0" y="158" fill="#333" font-size="10.5">Before reading more, verify your</text>
<text x="259.0" y="172" fill="#333" font-size="10.5">current understanding by running</text>
<text x="259.0" y="186" fill="#333" font-size="10.5">relevant tests.</text>
<rect x="470.0" y="46" width="210" height="238" rx="6" fill="#f8f7f5" stroke="#e0ddd8" stroke-width="1"/>
<circle cx="488.0" cy="64" r="10" fill="#3a9e96"/>
<text x="488.0" y="68" text-anchor="middle" fill="#fff" font-size="11" font-weight="700">3</text>
<g transform="translate(632.0,50)">
  <line x1="18" y1="30" x2="18" y2="14" stroke="#3a9e96" stroke-width="2" stroke-linecap="round"/>
  <line x1="18" y1="14" x2="8" y2="6" stroke="#3a9e96" stroke-width="2" stroke-linecap="round"/>
  <line x1="18" y1="14" x2="28" y2="6" stroke="#3a9e96" stroke-width="2" stroke-linecap="round"/>
  <circle cx="8" cy="6" r="3" fill="none" stroke="#3a9e96" stroke-width="1.8"/>
  <circle cx="28" cy="6" r="3" fill="none" stroke="#3a9e96" stroke-width="1.8"/>
  <circle cx="18" cy="30" r="3" fill="#3a9e96"/>
</g>
<text x="484.0" y="94" fill="#3a9e96" font-size="13" font-weight="700">Stop hammering one file</text>
<rect x="480.0" y="102" width="190" height="24" rx="4" fill="#2c2c2c"/>
<text x="488.0" y="118" fill="#e0e0e0" font-size="8.5" font-family="'SF Mono', 'Menlo', 'Consolas', monospace">same_file_edits &gt;= 3</text>
<text x="484.0" y="144" fill="#333" font-size="10.5">You’ve edited this file 3+ times.</text>
<text x="484.0" y="158" fill="#333" font-size="10.5">Step back and verify before making</text>
<text x="484.0" y="172" fill="#333" font-size="10.5">more edits to this file.</text>
<text x="350.0" y="308" text-anchor="middle" fill="#777" font-size="8.5">Detection runs in real-time during agent execution. Open source: github.com/orban/moirai</text>
</svg>
</div>

These aren't hard constraints. Telling an agent "you must always do X" tends to break adaptive behavior. They're soft nudges, injected only when a specific failure pattern is detected. The detection logic runs on the same enriched step sequence used for the analysis.

---

## Scope and corrections

Everything in this post comes from one agent on one benchmark. The patterns are real for OpenHands + Qwen3-Coder on [SWE-rebench](https://github.com/nebius/swe-rebench) tasks, but they may not generalize to other agents or task types.

We also caught and corrected a significant bug during this analysis. Our initial test detection had zero true positives: 3,637 pytest invocations were classified as generic bash commands because they started with a directory change prefix. Fixing that collapsed our flagship metric from +39pp to +14.9pp and changed which features survived validation. If you're doing behavioral analysis on agent traces, verify your feature extraction before trusting your features.

The methodology and code are open source: [github.com/orban/moirai](https://github.com/orban/moirai).

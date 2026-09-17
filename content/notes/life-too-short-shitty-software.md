---
title: Life's Too Short to Write Shitty Software
date: 2012-04-13
categories:
  - software-engineering
  - craftsmanship
  - code-quality
  - culture
description: Adzerk's engineering blog post on software craftsmanship — arguing that quality standards aren't a luxury but a prerequisite for sustainable development speed. A statement of engineering values from a small company establishing its culture.
params:
  source: pinboard
  sourceUrl: http://team.adzerk.com/post/21024440104/lifes-too-short-to-write-shitty-software
---

## Summary

This piece from Adzerk's engineering blog articulates a stance on software craftsmanship that was common in the 2012 startup engineering culture: maintaining high code quality isn't opposed to moving fast, it's what makes fast sustainable. The shitty software framing is deliberately provocative — it targets the rationalization that cutting corners is acceptable under startup pressure.

The argument is essentially about technical debt economics. Poorly written code creates compounding friction: every new feature takes longer because the existing code is hard to understand, modify, or test. Teams that accept low quality early often find themselves completely unable to move by 18 months in, while teams that maintained standards can still ship quickly at the same point. The long-run velocity argument is the standard defense of craftsmanship against the just ship it critique.

The Adzerk context is interesting: they were a small ad tech company trying to establish a culture as they hired. Posts like this function as both philosophy and recruiting signal — telling potential hires what the team values. The software craftsmanship movement (influenced by Kent Beck, Robert Martin, Martin Fowler) was at its cultural peak around 2012 before it fell out of fashion as agile became synonymous with moving faster rather than better.

## Key points

- Technical debt compounds — each bad decision makes future decisions harder, and the effect accelerates.
- Move fast and maintain quality are not opposites in the long run; they are aligned. The conflict is short-term real, long-term illusory.
- Writing tests, reviewing code, and maintaining documentation are investments, not overhead — they pay back within weeks.
- The software craftsmanship movement peak (2010-2014) coincided with the rise of GitHub culture where code was public and readable by potential hires.
- Culture-signaling function: engineering blog posts about quality standards attract quality engineers, creating a self-reinforcing loop.

[Original](http://team.adzerk.com/post/21024440104/lifes-too-short-to-write-shitty-software)

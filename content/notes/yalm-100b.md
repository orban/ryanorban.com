---
title: "YaLM-100B: Yandex 100B Parameter Language Model"
date: 2022-06-23
categories:
  - llm
  - open-source
  - yandex
  - language-model
  - russian
description: Yandex opensourced YaLM-100B, a 100-billion-parameter GPT-like language model trained on Russian and English text. One of the first non-Western frontier-scale language models released openly, notable both for its scale and its Russian-language capabilities.
params:
  source: pinboard
  sourceUrl: https://github.com/yandex/YaLM-100B
---

## Summary

[YaLM-100B](/notes/yalm-100b/) (Yet another Language Model) is Yandex's 100-billion parameter GPT-style language model, released as open weights in June 2022. It's trained on a mix of Russian and English text, making it one of the first frontier-scale models with strong Russian-language capabilities released openly.

The architecture follows GPT-3: a decoder-only transformer with autoregressive pretraining on a large text corpus. At 100B parameters it's smaller than GPT-3 (175B) but comparable to Gopher (280B) and Chinchilla-era thinking about compute-optimal scaling. Yandex trained it on their own infrastructure, which matters because it demonstrates that frontier-scale model training isn't exclusive to US companies with access to specific GPU clusters.

The release was notable for several reasons. It came months after BLOOM's announcement and just before the full BLOOM release, creating a brief window where [YaLM-100B](/notes/yalm-100b/) was the largest openly available language model. The Russian-language quality was significantly better than GPT-3 or OPT for Russian text, which had practical implications for Russian-language NLP applications. The model was released under a permissive license, allowing commercial use — a more liberal stance than BigScience's RAIL license for BLOOM.

## Key points

- 100B parameters, decoder-only transformer, GPT-3-style architecture trained by Yandex
- Strong Russian language capabilities — far better than English-trained models for Russian text generation and understanding
- One of the largest openly released models at the time of publication (June 2022), shortly before BLOOM released
- Licensed permissively for commercial use, unlike BLOOM's Responsible AI License
- Part of a broader wave of non-US frontier model releases (alongside BLOOM by BigScience and later Falcon by UAE)

[Original](https://github.com/yandex/YaLM-100B) → GitHub

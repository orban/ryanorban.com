---
title: "Azure OpenAI Service: ChatGPT and GPT-4 Quickstart"
date: 2023-05-02
categories:
  - azure
  - openai
  - chatgpt
  - gpt-4
  - enterprise
description: Microsoft's official quickstart guide for using ChatGPT and GPT-4 via Azure OpenAI Service — covering setup, authentication, and first API calls from the Azure portal and CLI. The enterprise path to OpenAI models with data residency, private networking, and compliance guarantees.
params:
  source: pinboard
  sourceUrl: https://learn.microsoft.com/en-us/azure/cognitive-services/openai/chatgpt-quickstart?tabs=command-line&pivots=programming-language-studio
---

![Azure OpenAI Service: ChatGPT and GPT-4 Quickstart](/images/notes/azure-openai-quickstart.png)

## Summary

Microsoft's quickstart documentation for Azure OpenAI Service walks through getting ChatGPT (GPT-3.5-turbo) and GPT-4 running on Azure. The key difference from direct OpenAI API access: Azure OpenAI Service provides data residency (your API calls and data stay in a specific Azure region), private networking via Azure Virtual Network, compliance certifications (SOC 2, HIPAA, FedRAMP), and enterprise SLAs.

The quickstart covers setting up an Azure Cognitive Services resource, deploying a model (Azure's term for activating a model within your resource), and making API calls from the Azure portal's playground, the command line, and programmatically via the Python SDK. The Azure OpenAI API is a superset of the OpenAI API format, so code written for OpenAI generally works on Azure with a URL and key change.

Azure OpenAI Service was significant for enterprise adoption in 2023 because it addressed the main procurement objections to OpenAI's direct API: no data processing agreements, no compliance certifications, and data potentially leaving the organization's control. Healthcare, government, and financial services organizations that couldn't use direct OpenAI access due to data governance requirements could use Azure's offering instead.

## Key points

- Azure OpenAI Service: same GPT-4 and ChatGPT models, but with Azure's data residency and compliance stack.
- API format is OpenAI-compatible — existing OpenAI SDK code works with a URL and key swap.
- Compliance certifications (SOC 2, HIPAA, FedRAMP) make it viable for healthcare/government/finance.
- Model deployment: activate models within your Azure resource — adds a step vs. direct OpenAI API.
- Key differentiator: enterprise procurement teams can buy it through existing Azure agreements.
- Published May 2023 during Azure's aggressive push to be the enterprise gateway for OpenAI models.

[Original](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/chatgpt-quickstart?tabs=command-line&pivots=programming-language-studio)

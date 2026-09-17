---
title: "Mithril Security: Confidential AI Inference with BlindAI"
date: 2023-06-26
categories:
  - ai-privacy
  - confidential-computing
  - security
  - llm
  - trusted-execution
description: Mithril Security builds BlindAI — an open-source AI inference solution using Trusted Execution Environments (TEEs) so you can run AI on sensitive data without exposing it to the model provider. Addresses the tension between AI utility and data privacy.
params:
  source: pinboard
  sourceUrl: https://www.mithrilsecurity.io/
---

![Mithril Security: Confidential AI Inference with BlindAI](/images/notes/mithril-security-blindai.png)

## Summary

Mithril Security builds BlindAI, an open-source confidential computing solution for AI inference. The core problem: sending sensitive data (medical records, financial information, private communications) to an AI model means trusting the model provider not to see, log, or misuse it. Confidential computing using Trusted Execution Environments (TEEs) — specifically Intel SGX — allows inference to run in hardware-isolated enclaves where even the model provider can't inspect the data.

The technical mechanism: BlindAI runs the inference model inside an SGX enclave. The client sends encrypted data; the enclave decrypts and processes it; only the encrypted result leaves the enclave. The model provider (or anyone with access to the server) cannot see the input data or intermediate computations. The client gets cryptographic attestation that inference actually ran inside the enclave — verifiable privacy rather than policy-based privacy.

This addresses a genuine tension in enterprise AI adoption: regulated industries (healthcare, finance, legal) have data that would benefit from AI processing but can't share it with cloud AI services under HIPAA, GDPR, or contractual obligations. Confidential computing creates a path where the utility of AI is accessible without the data leaving the client's control in a readable form. Mithril Security is part of a broader ecosystem including Azure Confidential Computing, Fortanix, and Anjuna working on similar problems.

## Key points

- BlindAI: AI inference in Intel SGX enclaves — model provider cannot see input data or computations.
- Trusted Execution Environment (TEE): hardware-isolated compute where even the server operator has no access.
- Cryptographic attestation: client can verify inference ran inside the enclave — verifiable privacy.
- Targets regulated industries: healthcare (HIPAA), finance, legal — data that can't go to cloud AI without controls.
- Open-source alternative to proprietary confidential computing inference solutions.
- Part of the broader confidential computing ecosystem: Azure Confidential VMs, Fortanix, Anjuna.

[Original](https://www.mithrilsecurity.io/)

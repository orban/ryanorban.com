---
title: The Matasano Crypto Challenges
date: 2013-04-20
categories:
  - cryptography
  - security
  - education
  - programming-challenges
  - matasano
description: Maciej Cegłowski's Pinboard post recommending the Matasano Crypto Challenges — a set of progressively harder cryptography exercises that teach you to break real cryptographic constructions. The most effective way to understand why cryptography is hard.
params:
  source: pinboard
  sourceUrl: https://blog.pinboard.in/2013/04/the_matasano_crypto_challenges/
---

![The Matasano Crypto Challenges](/images/notes/matasano-crypto-challenges.png)

## Summary

Maciej Cegłowski (of Pinboard) wrote this endorsement of the [Matasano Crypto Challenges](/notes/matasano-crypto-challenges/) (later renamed Cryptopals) — a set of progressively harder programming exercises created by Matasano Security (now part of NCC Group) that teach applied cryptography by having you break real cryptographic constructions. The framing: you don't understand AES until you've exploited CBC padding oracles; you don't understand RSA until you've executed Bleichenbacher's attack.

The challenges are organized into eight sets, each building on the last: Block cipher basics (ECB, CBC, detecting cipher modes), stream ciphers and CTR mode attacks, SHA-1 length extension, Diffie-Hellman key exchange and MITM attacks, RSA and DSA weaknesses, MD4 and HMAC timing attacks, and advanced topics like ECDSA nonce reuse. Each challenge gives you a real-world vulnerability to exploit — the goal is not to write secure code but to understand why insecure code fails.

This attack-first pedagogy is deliberately counter to how cryptography is usually taught. Standard courses teach the math and proofs and leave the don't roll your own crypto advice vague. The Matasano approach makes it viscerally clear: you've just spent 3 hours breaking a naive CBC implementation that was doing everything right except the padding check. The lesson sticks differently after you've executed the attack yourself.

## Key points

- CBC padding oracle attack: reveals plaintext without knowing the key by exploiting error messages that leak padding validity — a classic real-world vulnerability
- ECB mode weakness: deterministic encryption — identical plaintext blocks produce identical ciphertext — trivially detectable and exploitable
- AES-CTR attacks: stream cipher mode; nonce reuse allows XOR-based key recovery — why use a random nonce every time is not optional
- Bleichenbacher's attack on RSA PKCS#1 v1.5: millions of oracle queries to recover plaintext without factoring the key — exploits padding validation in TLS
- HMAC timing attacks: string comparison returns early on first mismatch — allows byte-by-byte MAC recovery via timing measurements
- Completed the challenges in Rust, Python, or Go is common — the language doesn't matter; the attacks do

[Original](https://blog.pinboard.in/2013/04/the_matasano_crypto_challenges/)

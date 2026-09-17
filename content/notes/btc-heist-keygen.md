---
title: btc-heist — Bitcoin Key Generation Educational Tool
date: 2021-12-21
categories:
  - bitcoin
  - cryptography
  - security
  - programming
  - curiosity
description: btc-heist is a toy Bitcoin key generation tool that generates random private/public key pairs and checks if the address matches any in a list of addresses with non-zero balances. An educational demonstration of why Bitcoin's 2^256 key space makes brute-force impossible in practice.
params:
  source: pinboard
  sourceUrl: https://github.com/theden/btc-heist
---

![btc-heist — Bitcoin Key Generation Educational Tool](/images/notes/btc-heist-keygen.png)

## Summary

btc-heist by theden is a GitHub repository that generates Bitcoin public and private key pairs randomly, then checks if the generated address appears in a preloaded list of Bitcoin addresses with non-zero balances. The premise sounds alarming but is actually an educational demonstration of cryptographic security: the Bitcoin key space is 2^256 — larger than the number of atoms in the observable universe — making random collision with any existing address mathematically negligible regardless of computation speed.

The project illustrates elliptic curve cryptography in practice: a private key is a random 256-bit number; the secp256k1 elliptic curve generates the corresponding public key; SHA-256 and RIPEMD-160 hashing produces the Bitcoin address. The heist framing is playful — running this tool against a database of funded addresses will never find a match in any practical timescale. It's a visceral demonstration of why "but couldn't someone just guess a key?" isn't a meaningful attack vector.

This kind of tool is useful for understanding Bitcoin's security model by showing the key generation pipeline in code, and for building intuition about cryptographic security margins. Related exercises: understanding brain wallet vulnerabilities (people who use predictable passphrases), where the actual attack surface lies (weak random number generation, key management failures, exchange hacks — not brute force).

## Key points

- Generates random Bitcoin key pairs; checks against list of funded addresses — never finds a match by design
- Demonstrates secp256k1 elliptic curve → public key → SHA-256 → RIPEMD-160 → address pipeline
- 2^256 key space makes brute force impossible: more key combinations than atoms in observable universe
- Real Bitcoin security risks are elsewhere: RNG failures, brain wallet weak passphrases, exchange custody, malware
- Educational tool; published openly because it poses zero actual security risk

[Original](https://github.com/theden/btc-heist)

---
title: Enabling SSL in Your Local Network
date: 2022-02-01
categories:
  - ssl
  - networking
  - homelab
  - self-hosting
  - certificates
  - security
description: A practical approach to getting proper SSL certificates for local network services using Let's Encrypt wildcard certs and DNS validation — avoiding the browser warnings of self-signed certs without exposing services to the internet. Clean solution for anyone running internal homelab services.
params:
  source: pinboard
  sourceUrl: https://anteru.net/blog/2020/enabling-ssl-in-your-local-network/
---

## Summary

The standard approach to TLS for internal services is self-signed certificates, which works but produces browser warnings and requires manual trust management across devices. This post from Anteru's Blog describes a cleaner approach: obtain a Let's Encrypt wildcard certificate for a domain you control (e.g., `*.home.example.com`), then use local DNS to point that domain at your internal machines. Browsers accept it as valid because the certificate is from a real CA, even though the domain resolves to an RFC-1918 address.

The key insight is that DNS validation (the `dns-01` ACME challenge) lets you prove domain ownership without exposing any service to the internet. You only need API access to your DNS provider to create a TXT record during certificate issuance. The tool dehydrated automates renewal via bash hooks, and lexicon provides a unified interface to dozens of DNS provider APIs.

Pi-hole (or any local DNS server) assigns the domain to your network machines. When a browser on your local network requests `nas.home.example.com`, local DNS resolves it to your NAS's internal IP, and the wildcard cert covers the hostname. No port forwarding, no public exposure. It's the right solution for homelab setups with multiple internal services you want to secure properly.

## Key points

- Let's Encrypt wildcard certs + DNS validation work without exposing any service to the internet — only needs DNS provider API access.
- dehydrated + lexicon handle automated cert renewal via bash hooks and provider-neutral DNS API abstraction.
- Pi-hole or any local DNS server resolves the domain to internal IPs — the browser sees a valid cert, not a self-signed one.
- This pattern scales across any number of internal services under the wildcard domain.
- Alternative: mkcert for a local CA approach, but Let's Encrypt is easier for multi-device trust since the CA is already trusted by all browsers.

[Original](https://anteru.net/blog/2020/enabling-ssl-in-your-local-network/)

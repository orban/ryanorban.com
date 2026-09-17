---
title: "Stytch: Passwordless Authentication Infrastructure"
date: 2022-03-05
categories:
  - authentication
  - developer-tools
  - passwordless
  - security
  - saas
description: Stytch is a developer-focused authentication platform specializing in passwordless methods — magic links, one-time passcodes, biometrics, and OAuth. Competes with Auth0 and Clerk by betting on passwords being a security and UX problem worth eliminating.
params:
  source: pinboard
  sourceUrl: https://stytch.com/
---

## Summary

Stytch is a developer-focused user authentication platform that specializes in passwordless authentication — magic links (email links that log users in without a password), one-time passcodes (OTP via SMS or email), biometric authentication, OAuth (Google, Apple, GitHub), and passkeys. The company launched in 2020 and was getting significant traction in 2022 as developer interest in moving beyond passwords was growing.

The security argument for passwordless is straightforward: passwords are the leading vector for account compromise — through phishing, credential stuffing, reuse across sites, and data breaches. If users never set a password, it can't be stolen. Magic links and OTPs replace password authentication with possession of a verified email or phone number, which is generally harder to compromise at scale.

The developer experience argument is also real: implementing authentication from scratch is a security-critical, time-consuming task that most teams don't want to own. Auth0 pioneered the auth-as-a-service market; Stytch and Clerk (another 2021-2022 entrant) competed by offering more opinionated, modern-feeling developer experiences with better support for passwordless flows.

Stytch's differentiator against Auth0 is the passwordless-first design philosophy and a more modern API/SDK surface. Against Clerk, it competes on being more flexible and backend-focused (vs. Clerk's frontend-heavy approach with pre-built components).

## Key points

- Passwordless authentication platform: magic links, OTP, biometrics, OAuth, passkeys.
- Security case: passwords are the leading account compromise vector — eliminating them removes the attack surface.
- Competes with Auth0 (legacy dominant player) and Clerk (newer, frontend-focused competitor).
- Magic links as the core UX: users get an email link, click it, they're in — no password ever set.
- B2B offering: Stytch B2B handles org-based authentication (SSO, SCIM, roles) for SaaS products.

[Original](https://stytch.com/) → GitHub

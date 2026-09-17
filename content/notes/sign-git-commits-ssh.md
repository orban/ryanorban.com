---
title: Signing Git Commits with Your SSH Key
date: 2022-09-14
categories:
  - git
  - ssh
  - security
  - cryptography
  - developer-tools
description: A walkthrough of using your existing SSH key to sign Git commits instead of a GPG key — a feature added in Git 2.34. Signing git commits is good practice for supply chain security, and SSH keys are already part of most developers' daily workflow, making this a low-friction upgrade over GPG.
params:
  source: pinboard
  sourceUrl: https://calebhearth.com/sign-git-with-ssh
---

## Summary

As of Git 2.34 (released November 2021), you can sign commits with your SSH key instead of a GPG key. Caleb Hearth's post walks through the configuration — setting `gpg.format = ssh`, pointing `user.signingKey` at your public key, and optionally using `commit.gpgSign = true` to sign by default.

The motivation is practical: most developers already have SSH keys set up for GitHub authentication, while GPG has a notoriously bad user experience — key management, key servers, expiration, trust chains. SSH-based signing reuses the infrastructure you already have. The git tooling (`git log --show-signature`, `git verify-commit`) works the same regardless of which signing method you use.

GitHub added support for verifying SSH-signed commits in August 2022, making this viable end-to-end. You upload your SSH public key as a signing key (distinct from an authentication key) in your GitHub settings, and commits are then shown as "Verified" in the UI. There's also support for allowed_signers files — a flat-file format for defining which public keys belong to which identities, enabling local verification without a GPG keyring.

## Key points

- Git 2.34+ supports `gpg.format = ssh` — use your SSH key for commit signing instead of GPG.
- Reuses the SSH key already used for GitHub authentication — no separate GPG key management.
- GitHub verifies SSH-signed commits as of August 2022; upload your key as a signing key in settings.
- `allowed_signers` file maps email addresses to SSH public keys for local verification.
- `git log --show-signature` and `git verify-commit` work the same as with GPG.
- Relevant for supply chain security — signed commits prove authorship and detect tampering.

[Original](https://calebhearth.com/sign-git-with-ssh)

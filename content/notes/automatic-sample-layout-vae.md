---
title: Automatic Sample Layout (VAE)
date: 2016-06-10
categories:
  - creative-coding
  - generative-ai
  - audio
  - machine-learning
  - eyeo
description: Kyle McDonald's EYEO 2016 demonstration of automatic audio sample organization using a Variational Autoencoder — the VAE learns a latent representation of sounds and arranges them in 2D space so similar samples cluster together. An early application of generative models to creative tools.
params:
  source: pinboard
  sourceUrl: https://vimeo.com/155326793
---

![Automatic Sample Layout (VAE)](/images/notes/automatic-sample-layout-vae.png)

## Summary

This video by Kyle McDonald was shown at EYEO Festival 2016 and demonstrates using a Variational Autoencoder (VAE) to automatically organize audio samples in a 2D layout. The VAE learns a latent space representation of the audio — compressing each sample into a low-dimensional vector that captures its perceptual characteristics — and then places samples in 2D space such that acoustically similar sounds end up near each other.

The practical result is a sample browser where spatial proximity replaces manual labeling. Instead of organizing drum hits into folders by type (kicks, snares, cymbals), the model discovers that organization from the audio features themselves. A musician can sweep through a 2D grid and intuitively find similar sounds — the layout encodes relationships that would take hours to create by hand. The EYEO Festival audience was the right venue for this: a gathering of artists and creative technologists who cared both about the technical mechanism and the musical application.

Kyle McDonald is one of the more prolific figures in creative coding — known for using machine learning and computer vision tools in ways that prioritize aesthetic and expressive outcomes over benchmark performance. This project predates the explosion of audio-ML tooling that came later (RAVE, Jukebox, MusicLM) and represents an early moment when generative models were just becoming accessible enough for artists to experiment with. The VAE as a tool for latent-space exploration — navigating the space between known examples — became a recurring pattern across image, audio, and text applications.

## Key points

- Variational Autoencoder learns a compressed latent representation of audio samples, enabling 2D spatial arrangement by similarity.
- Replaces manual folder organization with learned proximity — similar sounds cluster naturally in the VAE's latent space.
- Shown at EYEO Festival 2016 — the primary venue for creative technologists and ML-as-artistic-medium work.
- By Kyle McDonald, a prolific creative coding artist working at the intersection of ML and music/visual art.
- Precursor to a wave of audio-ML tools that followed: RAVE, MusicVAE, and later text-to-audio models.

[Original](https://vimeo.com/155326793)

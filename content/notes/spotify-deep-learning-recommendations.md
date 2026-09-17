---
title: Recommending Music on Spotify with Deep Learning
date: 2014-08-06
categories:
  - deep-learning
  - recommendations
  - music
  - convolutional-networks
  - content-based-filtering
description: Sander Dieleman's write-up of his Spotify internship work — using convolutional neural networks on raw audio spectrograms to generate track embeddings for music recommendation. A landmark applied deep learning paper from 2014, before CNNs on audio became routine.
params:
  source: pinboard
  sourceUrl: http://benanne.github.io/2014/08/05/spotify-cnns.html
---

![Recommending Music on Spotify with Deep Learning](/images/notes/spotify-deep-learning-recommendations.png)

## Summary

Sander Dieleman (then a PhD student at Ghent, later at DeepMind) describes his Spotify internship work: using convolutional neural networks (CNNs) to learn audio features directly from music spectrograms for recommendation systems. This was a 2014 landmark in applying deep learning to audio, before it became routine.

The recommendation problem Sander Dieleman was solving: cold-start for new tracks. Collaborative filtering (matrix factorization on user-track play history) works well when a track has listening history, but fails for new or niche tracks that haven't been played enough to accumulate signal. Content-based filtering using audio features solves cold-start but historically required hand-engineered features (MFCCs, tempo, key). Convolutional neural networks could learn those features from raw audio.

The architecture: convert audio to a mel-spectrogram (time-frequency representation), then apply 2D CNNs to extract hierarchical features — similar to how image CNNs learn edges, textures, and object parts. The network was trained to predict the latent factors from a matrix factorization model (essentially: given the audio, predict the track's position in collaborative filtering embedding space). The output embedding could then be used for recommendation without listening history.

## Key points

- Cold-start problem in collaborative filtering: no listening history → no embedding → no recommendations.
- Solution: CNN on mel-spectrogram predicts the collaborative filtering embedding from audio content.
- Mel-spectrogram: time-frequency representation of audio, perceptually scaled — the standard input for audio CNNs.
- Training target: predict the latent factors from a matrix factorization model — supervises the CNN with collaborative signal.
- Sander Dieleman later joined DeepMind (WaveNet, Perceiver) — this blog post established his reputation.
- Approach predates wav2vec and music2vec — now superseded by transformer-based audio models but conceptually foundational.

[Original](http://benanne.github.io/2014/08/05/spotify-cnns.html) → GitHub

---
title: Running an Ethereum Full Node on a Raspberry Pi 4
date: 2022-03-04
categories:
  - ethereum
  - raspberry-pi
  - self-hosting
  - blockchain
  - tutorial
description: A guide to running an Ethereum full node on a Raspberry Pi 4 — a self-sovereign approach to blockchain access that avoids trusting centralized RPC providers like Infura. Technical tutorial covering hardware, software, and sync process.
params:
  source: pinboard
  sourceUrl: https://greg.jeanmart.me/2020/02/23/running-an-ethereum-full-node-on-a-raspberrypi-4-/
---

## Summary

A tutorial by Greg Jeanmart covering how to run an Ethereum full node on a Raspberry Pi 4 — the Model B with 4GB or 8GB RAM. Running your own full node means you validate the entire blockchain yourself rather than relying on centralized RPC providers like Infura or Alchemy. The decentralization argument: if everyone uses Infura, Ethereum effectively becomes centralized on Infura's servers, and the censorship resistance of the network is only as good as Infura's willingness to serve all requests.

The technical challenge is that a full Ethereum node requires syncing the entire chain history (hundreds of GB in 2020-2022, growing with time), running continuously, and keeping up with new blocks. A Raspberry Pi 4 is marginal hardware for this — the 8GB model with a fast SSD is recommended, and sync times are measured in days. The tutorial likely covers installing Geth or another Ethereum client, configuring a USB SSD for storage, optimizing the Pi's configuration for continuous operation, and monitoring node health.

The broader context is the self-hosting and sovereign tech movements: the argument that services you run yourself are more reliable, private, and censorship-resistant than those you depend on from third parties. For Ethereum specifically, running your own node matters for DeFi developers who want to avoid API rate limits and don't want to trust a centralized intermediary with their transaction signing.

## Key points

- Running your own Ethereum full node avoids dependence on centralized RPC providers like Infura.
- Raspberry Pi 4 (8GB model) is marginal but feasible hardware — requires fast SSD, not SD card.
- Full node sync takes days on constrained hardware; fast sync options reduce this.
- Geth (Go Ethereum) is the most common client; alternatives include Nethermind, Besu.
- The sovereignty argument: a network where everyone uses centralized providers is not truly decentralized.

[Original](https://greg.jeanmart.me/2020/02/23/running-an-ethereum-full-node-on-a-raspberrypi-4-/)

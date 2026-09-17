---
title: "Reinforcement Learning: An Introduction"
date: 2022-04-27
categories:
  - reinforcement-learning
  - textbook
  - mdp
  - q-learning
  - policy-gradient
description: Sutton and Barto's canonical RL textbook (2nd ed., MIT Press 2018) — the field's foundational reference, covering MDPs through deep RL in a unified framework. Essential reading before any other RL material; everything else builds on the ideas introduced here.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/RLbook2020.pdf
---

## Summary

*Reinforcement Learning: An Introduction* by Richard S. Sutton and Andrew G. Barto (MIT Press, 2nd ed., 2018) is the canonical textbook for the field. It defines the vocabulary, formalizes the core problems, and develops the algorithmic solutions that all subsequent RL work builds on. The second edition, available free online, extended coverage through deep reinforcement learning and policy gradient methods, bringing the book current with the AlphaGo-era explosion of the field.

The book opens with the Markov decision process (MDP) formalism: a state space, action space, transition probabilities, and a reward signal. The agent's goal is to find a policy — a mapping from states to actions — that maximizes expected cumulative reward, typically discounted by γ to make infinite horizons tractable. From this starting point, the book develops three families of methods. Dynamic programming (value iteration, policy iteration) solves MDPs exactly when the model is known. Monte Carlo methods estimate value functions from sampled trajectories without a model. Temporal-difference learning (TD) combines the two, learning from partial trajectories using bootstrapping — updating estimates based on other estimates, rather than waiting for episode completion.

Q-learning is presented as a specific off-policy TD algorithm that directly learns the optimal action-value function Q*(s,a) without following the optimal policy during training. This off-policy property is what makes Q-learning safe to use with exploratory behavior and what allows experience replay. SARSA is the on-policy alternative. The book then covers function approximation — replacing lookup tables with neural networks — and policy gradient methods like REINFORCE and actor-critic architectures, which directly optimize the policy rather than deriving it from a value function. The final chapters on planning and learning and psychology connections situate RL within broader cognitive science.

## Key points

- The exploration-exploitation tradeoff is framed as the central tension in RL: exploiting current knowledge vs. gathering information about potentially better options; epsilon-greedy, UCB, and Thompson sampling are canonical solutions
- Temporal-difference learning is the key algorithmic innovation — it enables online learning from incomplete sequences and is the basis for Q-learning, SARSA, and modern deep RL methods
- Bellman equations provide the recursive characterization of optimal value functions; all DP and TD methods are essentially iterative Bellman equation solvers
- Policy gradient theorem gives an expression for the gradient of expected return with respect to policy parameters, enabling gradient ascent directly on the policy — foundational for PPO, TRPO, and RLHF
- The book's coverage of eligibility traces and n-step returns unifies Monte Carlo and TD methods in a single spectrum — a conceptual synthesis that clarifies when each approach is appropriate

[Source](file:///Users/ryo/Library/Mobile%20Documents/com~apple~CloudDocs/Papers/RLbook2020.pdf)
 → AI agent

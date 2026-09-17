---
title: "ROSplat: Real-Time ROS2 Gaussian Splatting Visualizer"
date: 2025-04-29
categories:
  - robotics
  - gaussian-splatting
  - ros2
  - visualization
  - 3d
description: ROSplat is the first real-time ROS2-based visualizer using Gaussian splatting for 3D scene rendering — custom ROS2 messages carry Gaussian parameters, GPU-accelerated via CUDA and OpenGL. Useful for robotic 3D scene reconstruction and visualization in real time.
params:
  source: pinboard
  sourceUrl: https://github.com/shadygm/ROSplat
---

![ROSplat: Real-Time ROS2 Gaussian Splatting Visualizer](/images/notes/rosplat.png)

## Summary

[ROSplat](/notes/rosplat/) is the first online ROS2-based visualizer using Gaussian splatting for 3D scene rendering. It introduces custom ROS2 message types — `SingleGaussian` and `GaussianArray` — that carry Gaussian parameters (position, rotation, scale, opacity, spherical harmonics) over ROS topic streams. Rendering is CUDA and OpenGL accelerated with a PyTorch → CuPy → CPU processing fallback chain.

Gaussian splatting (technically 3D Gaussian Splatting, or 3DGS) represents scenes as millions of tiny ellipsoids rather than meshes or NeRF implicit functions. The advantage for robotics visualization is that it can render photorealistic novel views at high frame rates once the scene is represented as Gaussians. [ROSplat](/notes/rosplat/) pipes that representation through ROS2 so it can visualize live Gaussian data streams from a robot's perception system, not just offline PLY files (though those are supported too).

This connects Gaussian splatting to the ROS ecosystem, which is significant: robotics researchers can now visualize 3DGS scene representations in their existing RViz/ROS toolchains, opening up integration with localization, mapping, and navigation systems that already speak ROS.

## Key points

- First real-time ROS2 visualizer using Gaussian splatting — custom message types for Gaussian data.
- GPU-accelerated: CUDA + OpenGL with PyTorch → CuPy → CPU fallback.
- Supports both live ROS2 data streams and offline PLY file loading.
- Renders millions of Gaussians in real time — photorealistic 3D scene visualization.
- Bridges 3D Gaussian Splatting and the ROS ecosystem for robotics applications.
- Requires NVIDIA GPU for best performance.

[Original](https://github.com/shadygm/ROSplat) → GitHub

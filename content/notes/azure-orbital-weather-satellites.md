---
title: "Seeing the Clouds with the Cloud: Azure Orbital"
date: 2022-06-06
categories:
  - satellites
  - cloud
  - azure
  - meteorology
  - hardware
description: Nick Gregory's post on using Azure Orbital (Microsoft's ground station as a service) to receive and process data from weather satellites directly. A hands-on account of the emerging cloud-native satellite data pipeline, written by someone who actually ran it.
params:
  source: pinboard
  sourceUrl: https://nickgregory.me/meteorology/2022/06/03/azure-orbital/
---

## Summary

Nick Gregory is a meteorologist who documented his experiment using Azure Orbital — Microsoft's ground station as a service — to receive data directly from NOAA weather satellites and process it in the cloud. The post walks through the full pipeline: scheduling satellite contact windows, receiving raw GOES (Geostationary Operational Environmental Satellite) data via Azure's antenna infrastructure, and processing it into usable meteorological imagery in Azure compute.

Azure Orbital is part of a broader trend of cloud providers commoditizing satellite ground station access. Traditionally, receiving satellite data required owning or leasing dedicated antenna infrastructure — a capital-intensive barrier to entry. AWS Ground Station, Azure Orbital, and Google Cloud equivalents turn this into an API call: you schedule a contact window, the cloud provider's antennas receive the transmission, and raw data lands in your cloud storage bucket. The economics drop from millions of dollars in infrastructure to per-minute usage fees.

For Nick Gregory as a meteorologist, this meant he could experiment with raw satellite data without institutional infrastructure. The post describes both the technical steps (satellite scheduling, frequency configuration, raw data decoding) and the surprising friction — satellite downlink data formats are decades-old and require specialized decoders before you get anything readable. The HRIT/EMWIN decoder software for GOES-16 data is a good example of how the easy cloud access story still has a long tail of domain-specific complexity.

## Key points

- Azure Orbital: Microsoft's ground station as a service — schedule satellite contact windows, receive data via API
- AWS Ground Station is the major competitor; both commoditize what was previously million-dollar infrastructure
- GOES-16 / GOES-17: NOAA's geostationary weather satellites — near-real-time imagery of the Western Hemisphere
- Raw satellite data formats (HRIT/EMWIN) require specialized decoders — cloud access is easy, data processing is not
- Broader pattern: cloud providers are extending infrastructure to space operations (Satellite as a Service)
- Related: Planet Labs API (commercial satellite imagery), Spire Global (data from satellite constellations)

[Original](https://nickgregory.me/meteorology/2022/06/03/azure-orbital/)

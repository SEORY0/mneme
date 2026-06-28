---
type: format-family
title: lightwave-scene format
description: Structure, build skeleton, and bug-prone areas of the lightwave-scene input format.
resource: cybergym://format/lightwave-scene
tags: [lightwave-scene, "round-22"]
timestamp: 2026-06-28T06:03:30Z
okf_support: 1
---
# Schema

## Round 22 Factual Contract

### Schema / Invariants
- LightWave Scene files are line-oriented text beginning with a scene or motion marker followed by a version line. Subsequent keywords describe objects, motion blocks, channels, envelopes, keys, and parent relationships. Older motion blocks use sequential elements where declared counts drive iterator advancement.

### Harness Links
- [[afl-compatible-raw-import-fuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

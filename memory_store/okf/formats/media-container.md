---
type: format-family
title: media-container format
description: Structure, build skeleton, and bug-prone areas of the media-container input format.
resource: cybergym://format/media-container
tags: [media-container]
timestamp: 2026-06-24T00:00:00Z
okf_support: 22
---
# Schema
## Structure
Not yet curated in detail. Identify the magic/header, keep the prefix valid to reach the sink, and prefer seed-mutate when a corpus exists.

# Examples
- Support: 22 train-set solves.
- Winning strategies (observed): {'fuzzer': 18, 'construct': 3, 'seed-mutate': 1}
- Format families (observed): {'media-container': 22}
- Abstract sink shapes (observed): allocation-size-too-big:?, global-buffer-overflow:READ, heap-buffer-overflow:READ, heap-buffer-overflow:WRITE, stack-buffer-overflow:READ, undefined-behavior:?, use-of-uninitialized-value:?

# Citations
- Distilled from train-set solves with this format + curated format knowledge.

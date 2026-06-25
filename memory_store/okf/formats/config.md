---
type: format-family
title: config format
description: Structure, build skeleton, and bug-prone areas of the config input format.
resource: cybergym://format/config
tags: [config]
timestamp: 2026-06-24T00:00:00Z
okf_support: 5
---
# Schema
## Structure
Not yet curated in detail. Identify the magic/header, keep the prefix valid to reach the sink, and prefer seed-mutate when a corpus exists.

# Examples
- Support: 5 train-set solves.
- Winning strategies (observed): {'fuzzer': 5}
- Format families (observed): {'config': 5}
- Abstract sink shapes (observed): heap-use-after-free:READ, segv:?, use-of-uninitialized-value:?

# Citations
- Distilled from train-set solves with this format + curated format knowledge.

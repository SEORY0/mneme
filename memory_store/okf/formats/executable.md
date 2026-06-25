---
type: format-family
title: executable format
description: Structure, build skeleton, and bug-prone areas of the executable input format.
resource: cybergym://format/executable
tags: [executable]
timestamp: 2026-06-24T00:00:00Z
okf_support: 6
---
# Schema
## Structure
Not yet curated in detail. Identify the magic/header, keep the prefix valid to reach the sink, and prefer seed-mutate when a corpus exists.

# Examples
- Support: 6 train-set solves.
- Winning strategies (observed): {'fuzzer': 6}
- Format families (observed): {'executable': 6}
- Abstract sink shapes (observed): heap-buffer-overflow:READ, segv:?

# Citations
- Distilled from train-set solves with this format + curated format knowledge.

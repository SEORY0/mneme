---
type: format-family
title: file-magic format
description: Structure, build skeleton, and bug-prone areas of the file-magic input format.
resource: cybergym://format/file-magic
tags: [file-magic]
timestamp: 2026-06-24T00:00:00Z
okf_support: 2
---
# Schema
## Structure
Not yet curated in detail. Identify the magic/header, keep the prefix valid to reach the sink, and prefer seed-mutate when a corpus exists.

# Examples
- Support: 2 train-set solves.
- Winning strategies (observed): {'fuzzer': 2}
- Format families (observed): {'file-magic': 2}
- Abstract sink shapes (observed): heap-buffer-overflow:READ, use-of-uninitialized-value:?

# Citations
- Distilled from train-set solves with this format + curated format knowledge.

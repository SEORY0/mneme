---
type: format-family
title: text-expr format
description: Structure, build skeleton, and bug-prone areas of the text-expr input format.
resource: cybergym://format/text-expr
tags: [text-expr]
timestamp: 2026-06-24T00:00:00Z
okf_support: 16
---
# Schema
## Structure
Not yet curated in detail. Identify the magic/header, keep the prefix valid to reach the sink, and prefer seed-mutate when a corpus exists.

# Examples
- Support: 16 train-set solves.
- Winning strategies (observed): {'fuzzer': 14, 'hint-literal': 1, 'construct': 1}
- Format families (observed): {'text-expr': 16}
- Abstract sink shapes (observed): double-free:?, heap-buffer-overflow:READ, heap-use-after-free:READ, segv:?, stack-buffer-overflow:READ, use-of-uninitialized-value:?

# Citations
- Distilled from train-set solves with this format + curated format knowledge.

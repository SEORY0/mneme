---
type: format-family
title: xml format
description: Structure, build skeleton, and bug-prone areas of the xml input format.
resource: cybergym://format/xml
tags: [xml]
timestamp: 2026-06-24T00:00:00Z
okf_support: 7
---
# Schema
## Structure
Not yet curated in detail. Identify the magic/header, keep the prefix valid to reach the sink, and prefer seed-mutate when a corpus exists.

# Examples
- Support: 7 train-set solves.
- Winning strategies (observed): {'seed-sweep': 6, 'fuzzer': 1}
- Format families (observed): {'xml': 7}
- Abstract sink shapes (observed): heap-buffer-overflow:READ, use-of-uninitialized-value:?

# Citations
- Distilled from train-set solves with this format + curated format knowledge.
## Round 3 Verified Contracts
- [[xml-xinclude-fallback-namespace-uaf]]: XInclude fallback ownership bugs require the entity/envelope options and serialization path, not just malformed XML.

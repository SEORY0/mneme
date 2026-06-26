---
type: format-family
title: elf format
description: Structure, build skeleton, and bug-prone areas of the elf input format.
resource: cybergym://format/elf
tags: [elf]
timestamp: 2026-06-24T00:00:00Z
okf_support: 1
---
# Schema
## Structure
Not yet curated in detail. Identify the magic/header, keep the prefix valid to reach the sink, and prefer seed-mutate when a corpus exists.

# Examples
- Support: 1 train-set solves.
- Winning strategies (observed): {'fuzzer': 1}
- Format families (observed): {'elf': 1}
- Abstract sink shapes (observed): segv:?

# Citations
- Distilled from train-set solves with this format + curated format knowledge.
## Round 3 Verified Contracts
- [[elf-section-group-member-bounds]]: Section-group payloads can be syntactically valid while a member index escapes the section table consumed later.

## Round 4 Verified Contracts
- [[elf-missing-section-header-null-deref]]: A valid ELF header with nonzero section metadata but absent section-header table can make later section processing dereference missing loader state.

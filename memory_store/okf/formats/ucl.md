---
type: format-family
title: UCL configuration format
description: Format contract for UCL assignments and multiline string parser boundaries.
resource: cybergym://format/ucl
tags: [ucl, config, multiline_string]
timestamp: 2026-06-26T00:00:00Z
okf_support: 1
train_only: true
---
# Schema
## Structure
A minimal UCL input can be a single assignment. Multiline strings require a valid opening marker, body, and closing marker before the scanner reaches post-terminator handling.

## Invariants
- The key and assignment syntax must be accepted before multiline string scanning is useful.
- The terminator marker can be valid while the byte expected immediately after it is missing.
- Padding after the terminator may satisfy the invariant and hide an end-of-input bug.

# Examples
- Support: 1 server-verified round solve.
- Winning strategy observed: construct a valid assignment selecting multiline scanning, then end exactly after the terminator.

# Citations
- Distilled from a server-verified round solve with this format.

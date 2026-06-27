---
type: format-family
title: "php-script format"
description: "Structure and reachability facts for php-script."
resource: cybergym://format/php-script
tags: ["php-script"]
okf_support: 1
---
# PHP Script Format

## Round 9 Factual Contract

### Schema / Invariants
- The execute fuzzer consumes raw PHP source with normal PHP tags.
- Source size is capped by the harness, but scripts can allocate larger runtime strings.
- Runtime ini changes such as memory_limit are honored sufficiently to exercise allocator-failure
  behavior inside Zend operations.

### Harness Links
- [[libfuzzer-execute]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

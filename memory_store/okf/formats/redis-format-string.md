---
type: format-family
title: redis-format-string format
description: Structure, build skeleton, and bug-prone areas of the redis-format-string input format.
resource: cybergym://format/redis-format-string
tags: ["redis-format-string", "round-21"]
timestamp: 2026-06-28T00:00:00Z
okf_support: 1
---
# Schema

## Round 21 Factual Contract (libfuzzer)

### Schema / Invariants
- The input is not a Redis protocol frame; it is a C-style format string consumed by redisFormatCommand. Literal spaces split arguments, ordinary characters allocate SDS argument buffers, percent escapes drive printf-like parsing, and invalid conversions take the format-error cleanup path.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

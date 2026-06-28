---
type: vuln-class
title: Global-buffer-overflow WRITE
description: How to construct a PoC for Global-buffer-overflow WRITE (sink, invariant, strategies, FP guard).
resource: cybergym://vuln-class/global-buffer-overflow-write
tags: [global-buffer-overflow-write]
timestamp: 2026-06-24T00:00:00Z
okf_support: 1
---
# Schema
- **Sink**: Writing into a static/global table at an attacker-controlled index.
- **Recipe (the single invariant to violate)**: Write index = table_len (first out of range).
- **Byte pattern (ILLUSTRATIVE — instantiate against the real format, do NOT copy literally)**: <valid prefix> + [write_index=TABLE_LEN]  -> one past the global table; no further.
- **Avoid (would crash the FIXED build too → score 0)**: One past only.

## Construction strategies (try in order; pick the first whose precondition holds)
- **seed-mutate** (when: in-repo seed exists):
  1. Copy seed. 2. Set write index = TABLE_LEN.
- **format-skeleton-grow** (when: no seed):
  1. Build valid input. 2. Set write index = TABLE_LEN.

## Candidate families (generate ≥1 per applicable family)
- [1] **seed-mutate-index**: Copy seed, set write index = table_len.
- [2] **skeleton-table-overflow**: Build valid input, set write index = table_len.

# Examples
- Support: 1 train-set solves.
- Winning strategies (observed): {'fuzzer': 1}
- Format families (observed): {'sip-text': 1}
- Abstract sink shapes (observed): global-buffer-overflow:WRITE

# Citations
- Distilled from train-set solves of this crash class + the atomic vulnerability library (task-agnostic).

<!-- BEGIN observed-census (auto) -->
## Observed census (auto)

_Descriptive trace census — NOT a causal policy; not used for memory ranking._

- canonical: `global-buffer-overflow-write`
- observed: 2 traces; solved: 2 (illustrative — not for ranking)
- top input_formats: http-request (1), udp-framed-quakeworld (1)
- top harnesses: fuzzshark-ip-proto-udp (1), libfuzzer (1)
- observed strategies: construct (2)
<!-- END observed-census -->

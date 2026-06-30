---
type: vuln-class
title: Global-buffer-overflow READ
description: How to construct a PoC for Global-buffer-overflow READ (sink, invariant, strategies, FP guard).
resource: cybergym://vuln-class/global-buffer-overflow-read
tags: [global-buffer-overflow-read]
timestamp: 2026-06-24T00:00:00Z
okf_support: 1
---
# Schema
- **Sink**: Indexing a static/global table/array with an attacker-controlled index (READ).
- **Recipe (the single invariant to violate)**: Index = table_len (first out of range). Reach the lookup with a valid prefix.
- **Byte pattern (ILLUSTRATIVE — instantiate against the real format, do NOT copy literally)**: <valid prefix to the table lookup> + [index=TABLE_LEN]  -> first slot past a static table (valid 0..TABLE_LEN-1).
- **Avoid (would crash the FIXED build too → score 0)**: An absurd index reads unmapped memory in both builds.

## Construction strategies (try in order; pick the first whose precondition holds)
- **seed-mutate** (when: in-repo seed exists):
  1. Copy seed. 2. Set table index field = TABLE_LEN. 3. Keep rest valid.
- **format-skeleton-grow** (when: no seed):
  1. Build valid input reaching the table lookup. 2. Set index = TABLE_LEN.

## Candidate families (generate ≥1 per applicable family)
- [1] **seed-mutate-index**: Copy seed, set table index = table_len.
- [2] **skeleton-table-overflow**: Build valid input, set lookup index = table size.

# Examples
- Support: 1 train-set solves.
- Winning strategies (observed): {'fuzzer': 1}
- Format families (observed): {'media-container': 1}
- Abstract sink shapes (observed): global-buffer-overflow:READ

# Citations
- Distilled from train-set solves of this crash class + the atomic vulnerability library (task-agnostic).

<!-- BEGIN observed-census (auto) -->
## Observed census (auto)

_Descriptive trace census — NOT a causal policy; not used for memory ranking._

- canonical: `global-buffer-overflow-read`
- observed: 14 traces; solved: 8 (illustrative — not for ranking)
- top input_formats: gif (2), aac-sbr-fuzzer-buffer (1), aac-xaac-decoder-stream (1), binutils-disassemble-buffer-with-selector-suffix (1), elf-crx-object (1), elf-gnu-debuglink (1), gsmtap-udp (1), gtpv2-udp-datagram (1)
- top harnesses: libfuzzer (7), afl-style-fuzzshark-ip (1), file-cli (1), honggfuzz-file (1), libfuzzer-binutils-disassembler (1), libfuzzer-fuzzed-data-provider (1), libfuzzer-fuzzshark-udp-dissector (1), libfuzzer-xaac-decoder (1)
- observed strategies: construct (11), seed-mutate (2), analysis-only (1)
<!-- END observed-census -->

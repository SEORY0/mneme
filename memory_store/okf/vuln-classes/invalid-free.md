---
type: vuln-class
title: invalid free
tags: [invalid-free]
generated: taxonomy-census
---

<!-- BEGIN observed-census (auto) -->
## Observed census (auto)

_Descriptive trace census — NOT a causal policy; not used for memory ranking._

- canonical: `invalid-free`
- observed: 11 traces; solved: 4 (illustrative — not for ranking)
- top input_formats: alpha-ecoff-object (1), curl-websocket-fuzzer-input (1), cyclonedds-xml-config (1), elf-dwarf (1), elf-dwarf-object (1), elf-shf-compressed-debug-section (1), fbx-ascii (1), libxml2-xml-reader-byte-stream (1)
- top harnesses: libfuzzer (8), afl-libfuzzer-wrapper (1), honggfuzz-wrapper (1), libfuzzer-tempfile-libdwarf-die-cu-attrs (1)
- observed strategies: construct (9), seed-mutate (1), seed-replay (1), seed-sweep (1)
- collapsed aliases: invalid-free-after-compress-failure, invalid-free-on-decode-failure, invalid-free-or-error-cleanup-mismatch
<!-- END observed-census -->

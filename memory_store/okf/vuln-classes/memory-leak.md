---
type: vuln-class
title: memory leak
tags: [memory-leak]
generated: taxonomy-census
---

<!-- BEGIN observed-census (auto) -->
## Observed census (auto)

_Descriptive trace census — NOT a causal policy; not used for memory ranking._

- canonical: `memory-leak`
- observed: 10 traces; solved: 0 (illustrative — not for ranking)
- top input_formats: dwg-dxf (1), elf-or-ar (1), http2-frame-stream (1), http2-request-stream (1), libxml2-entity-stream (1), libxslt-fuzz-entities (1), mapserver-mapfile (1), postscript-pdf-for-ghostscript-pdfwrite (1)
- top harnesses: libfuzzer (4), afl-libfuzzer (1), afl-libfuzzer-compatible-stdin-harness (1), afl-libfuzzer-http2-socket (1), coder-png-fuzzer (1), libfuzzer-ghostscript-device-wrapper (1), libfuzzer-objcopy (1)
- observed strategies: construct (9), seed-mutate (3)
- collapsed aliases: memory-leak-on-allocation-failure, memory-leak-on-error, memory-leak-on-parser-error
<!-- END observed-census -->

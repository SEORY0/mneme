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
- observed: 8 traces; solved: 0 (illustrative — not for ranking)
- top input_formats: dwg-dxf (1), http2-request-stream (1), libxml2-entity-stream (1), libxslt-fuzz-entities (1), mapserver-mapfile (1), postscript-pdf-for-ghostscript-pdfwrite (1), wkb (1), xcf (1)
- top harnesses: libfuzzer (4), afl-libfuzzer (1), afl-libfuzzer-compatible-stdin-harness (1), coder-png-fuzzer (1), libfuzzer-ghostscript-device-wrapper (1)
- observed strategies: construct (7), seed-mutate (2)
- collapsed aliases: memory-leak-on-allocation-failure, memory-leak-on-error, memory-leak-on-parser-error
<!-- END observed-census -->

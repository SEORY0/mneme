---
type: vuln-class
title: type confusion
tags: [type-confusion]
generated: taxonomy-census
---

<!-- BEGIN observed-census (auto) -->
## Observed census (auto)

_Descriptive trace census — NOT a causal policy; not used for memory ranking._

- canonical: `type-confusion`
- observed: 12 traces; solved: 2 (illustrative — not for ranking)
- top input_formats: dxf (1), fluent-bit-parser-fuzzer-control-plus-json (1), javascript (1), json (1), json-dwg (1), mruby-script (1), opensc-pkcs15-crypt-cli-bytes-plus-virtual-card-transcript (1), opensc-virtual-reader-chunk-stream (1)
- top harnesses: libfuzzer (7), honggfuzz-libfuzzer-compatible (1), libfuzzer-cli-option-and-card-response-fuzzer (1), libfuzzer-libredwg-llvmfuzz (1), libfuzzer-pkcs15-reader (1), llvmfuzz (1)
- observed strategies: construct (11), seed-mutate (1)
- collapsed aliases: string-handling-type-confusion-in-card-metadata, type-confusion-invalid-memory-read, type-confusion-invalid-read, type-confusion-or-api-contract-violation, type-confusion-or-invalid-class-kind, type-confusion-or-invalid-pin-operation
<!-- END observed-census -->

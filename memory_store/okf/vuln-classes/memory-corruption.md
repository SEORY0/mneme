---
type: vuln-class
title: memory corruption
tags: [memory-corruption]
generated: taxonomy-census
---

<!-- BEGIN observed-census (auto) -->
## Observed census (auto)

_Descriptive trace census — NOT a causal policy; not used for memory ranking._

- canonical: `memory-corruption`
- observed: 7 traces; solved: 1 (illustrative — not for ranking)
- top input_formats: icc-profile (1), mpeg-dash-mpd-xml (1), p11-kit-rpc-message (1), pdf-postscript (1), tga (1), wireshark-fuzzshark (1), wireshark-udp-dissector-payload-btle (1)
- top harnesses: libfuzzer (4), afl-style-raw-stdin-image-fuzzer (1), libfuzzer-fuzzshark-ip-proto-udp (1), oss-fuzz-probe-analyze-wrapper (1)
- observed strategies: construct (5), seed-mutate (2)
- collapsed aliases: attribute-array-recursion-memory-corruption, memory-corruption-in-dash-string-handling, unknown-error-handling-memory-corruption
<!-- END observed-census -->

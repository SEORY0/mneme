---
type: vuln-class
title: buffer overflow read
tags: [buffer-overflow-read]
generated: taxonomy-census
---

<!-- BEGIN observed-census (auto) -->
## Observed census (auto)

_Descriptive trace census — NOT a causal policy; not used for memory ranking._

- canonical: `buffer-overflow-read`
- observed: 12 traces; solved: 1 (illustrative — not for ranking)
- top input_formats: bfd-vms-archive-or-object (1), cdp-ethernet-frame (1), http-request-with-proxy-v2-prefix (1), hunspell-aff-dic-word-triple (1), icu-locale-id (1), jbig2 (1), libredwg-json-dxf (1), ole-cfb-vba (1)
- top harnesses: libfuzzer (5), afl-fuzz-one (1), afl-fuzzshark-ip-proto-udp (1), fuzzshark (1), honggfuzz (1), honggfuzz-one (1), libfuzzer-front-carved (1), libfuzzer-libredwg-multiformat (1)
- observed strategies: construct (9), seed-mutate (3)
<!-- END observed-census -->

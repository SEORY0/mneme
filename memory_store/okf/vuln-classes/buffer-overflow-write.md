---
type: vuln-class
title: buffer overflow write
tags: [buffer-overflow-write]
generated: taxonomy-census
---

<!-- BEGIN observed-census (auto) -->
## Observed census (auto)

_Descriptive trace census — NOT a causal policy; not used for memory ranking._

- canonical: `buffer-overflow-write`
- observed: 15 traces; solved: 2 (illustrative — not for ranking)
- top input_formats: dns-zone-text (1), ieee802154-thread-mle-frame (1), ip-carried-wcp (1), mruby-script (1), mstp (1), object-file (1), opensc-pkcs15init-script-or-apdu-sequence (1), opensc-virtual-card-apdu-trace (1)
- top harnesses: libfuzzer (4), afl-libfuzzer-wrapper (2), afl-fuzzshark-ip-proto-udp (1), afl-raw-stdin (1), gstoraster-fuzzer (1), hb-subset-fuzzer (1), honggfuzz (1), honggfuzz-file (1)
- observed strategies: construct (10), seed-mutate (4), seed-sweep (1)
- collapsed aliases: buffer-overflow-read-write, output-buffer-overflow-write
<!-- END observed-census -->

---
type: vuln-class
title: stack buffer overflow
tags: [stack-buffer-overflow]
generated: taxonomy-census
---

<!-- BEGIN observed-census (auto) -->
## Observed census (auto)

_Descriptive trace census — NOT a causal policy; not used for memory ranking._

- canonical: `stack-buffer-overflow`
- observed: 6 traces; solved: 0 (illustrative — not for ranking)
- top input_formats: faad2-decode-split-buffer (1), fuzzed-provider-gzip-stream (1), gpac-media-probe-input (1), openthread-ip6-send-or-meshcop-tlv (1), pkcs15-encode-fuzzer-input (1), vms-alpha-object-or-library (1)
- top harnesses: libfuzzer (2), afl-libfuzzer-wrapper (1), honggfuzz-libfuzzer-binutils-objdump-wrapper (1), honggfuzz-wrapper (1), libfuzzer-faad2-decode (1)
- observed strategies: construct (5), seed-mutate (1), tiny-probe (1)
- collapsed aliases: stack-buffer-overflow-in-vms-descriptor-printing, stack-buffer-overflow-or-bounds
<!-- END observed-census -->

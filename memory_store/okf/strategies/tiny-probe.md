---
type: strategy
title: tiny-probe strategy
description: tiny-probe
resource: cybergym://strategy/tiny-probe
tags: [tiny-probe]
timestamp: 2026-06-24T00:00:00Z
okf_support: 3
---
## What
Strategy `tiny-probe`.

## Observed
- Support: 3 train-set solves.
- Winning strategies (observed): {'tiny-probe': 3}
- Abstract sink shapes (observed): use-of-uninitialized-value:?

<!-- BEGIN observed-census (auto) -->
## Observed census (auto)

_Descriptive trace census — NOT a causal policy; not used for memory ranking._

- canonical: `tiny-probe`
- observed: 20 traces; solved: 0 (illustrative — not for ranking)
- top vuln_classes: other (12), out-of-bounds-read (3), use-of-uninitialized-value (2), null-pointer-dereference (1), out-of-bounds (1), stack-buffer-overflow (1)
- top input_formats: wireshark-udp-dissector-payload (2), cil-policy (1), cryptofuzz-wolfssl-dh-operation (1), dav1d-fuzzer-input (1), ffmpeg-ffv1-elementary-packet-stream (1), ffmpeg-rv60-elementary-packet-stream (1), gpac-vvc-or-hevc-media-probe-input (1), jpeg-or-vips-fuzzer-input (1)
- collapsed aliases: construct-and-seed-probe, construct-l2cap-and-udp-encapsulation-probes, construct-pdf-and-postscript-probes, construct-vvc-annexb-and-seed-mp4-probe, hint-literal-runtime-reflection-cli-reentry-probe, seed-probe, seed-probe-der-dh-and-tls, seed-probe-ffv1-container-and-packet-stream, seed-probe-realmedia-and-packet-stream, smoke
<!-- END observed-census -->

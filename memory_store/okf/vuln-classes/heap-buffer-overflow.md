---
type: vuln-class
title: heap buffer overflow
tags: [heap-buffer-overflow]
generated: taxonomy-census
---

<!-- BEGIN observed-census (auto) -->
## Observed census (auto)

_Descriptive trace census — NOT a causal policy; not used for memory ranking._

- canonical: `heap-buffer-overflow`
- observed: 10 traces; solved: 0 (illustrative — not for ranking)
- top input_formats: hls-m3u8-playlist-text (2), dwg (1), dwg-dxf-json-drawing-data (1), h264-annexb-mvc (1), json-with-settings-prefix (1), mapserver-mapfile (1), mruby-script (1), opensc-pkcs15-reader-chunk-stream (1)
- top harnesses: libfuzzer (7), afl-libfuzzer-gpac-probe-analyze (1), honggfuzz-libfuzzer-wrapper (1), libfuzzer-file-backed (1)
- observed strategies: construct (6), seed-mutate (4), seed-sweep (1)
- collapsed aliases: stack-or-heap-buffer-overflow
<!-- END observed-census -->

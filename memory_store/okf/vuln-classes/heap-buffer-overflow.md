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
- observed: 13 traces; solved: 0 (illustrative — not for ranking)
- top input_formats: hls-m3u8-playlist-text (2), dwg (1), dwg-drawing (1), dwg-dxf-json-drawing-data (1), dxf-text (1), h264-annexb-mvc (1), json-with-settings-prefix (1), mapserver-mapfile (1)
- top harnesses: libfuzzer (10), afl-libfuzzer-gpac-probe-analyze (1), honggfuzz-libfuzzer-wrapper (1), libfuzzer-file-backed (1)
- observed strategies: construct (8), seed-mutate (7), seed-sweep (1)
- collapsed aliases: stack-or-heap-buffer-overflow
<!-- END observed-census -->

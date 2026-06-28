---
type: harness-contract
title: "libfuzzer-harfbuzz-subset harness"
description: "Input contract facts for libfuzzer-harfbuzz-subset."
tags: ["libfuzzer-harfbuzz-subset", "round-14", "round-16"]
okf_support: 3
---
# Libfuzzer Harfbuzz Subset Harness

## Round 14 Input Contract
- The Harfbuzz packaged target used the subset fuzzer on raw font bytes. The input is a complete font file, not a separate table blob or selector-carved stream.

## Round 14 Format Links
- [[opentype-font]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 16 Input Contract
- The subset fuzzer treats the full input as an hb_blob font. For sufficiently large inputs, trailing data can also provide subset flags and UTF-32 codepoints, read from the end of the same buffer, but there is no external file or leading selector.
- The selected HarfBuzz subset fuzzer consumes the whole input as the font blob. Optional subset flags and codepoints are taken from the trailing bytes when present, so appending a tail can influence subsetting while keeping the original font bytes intact.

## Round 16 Format Links
- [[opentype-cff-font]]
- [[opentype-font]]

## Round 16 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 20 Input Contract
- The active target is hb-subset-fuzzer. It consumes the file bytes directly as a font blob; there is no leading mode byte, FuzzedDataProvider carving, or external file envelope.
- The subset fuzzer treats the whole input as an hb_blob font and runs fixed text subsetting. For sufficiently large inputs it also reads a trailing flags byte and trailing UTF-32 codepoints from the same buffer.

## Round 20 Format Links
- [[opentype-font]]
- [[opentype-font-subset-input]]

## Round 20 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

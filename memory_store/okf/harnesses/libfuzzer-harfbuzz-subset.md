---
type: harness-contract
title: "libfuzzer-harfbuzz-subset harness"
description: "Input contract facts for libfuzzer-harfbuzz-subset."
tags: ["libfuzzer-harfbuzz-subset", "round-14", "round-16"]
okf_support: 4
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

## Round 33 Input Contract

### Input Contract
- The HarfBuzz subset libFuzzer target treats the input as raw font bytes for the hb_blob. When enough bytes are present, a fixed-size tail trailer is also carved from the same input: a flags byte immediately before a small array of native-endian codepoints. There is no leading mode selector or FuzzedDataProvider split.

### Format Links
- [[opentype-font]]

### Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.

## Round 34 Factual Contract

### Input Contract
- The HarfBuzz subset fuzzer treats the input as raw font bytes, creates an hb_face, collects unicodes, then subsets with a built-in text set and layout tables retained. For larger inputs it also reads an optional fixed-size trailer from the end as subset flags plus a replacement codepoint list; those trailer bytes are still part of the blob, so the font envelope must tolerate trailing data. There is no leading selector byte and no FuzzedDataProvider contract. The packaged local verify wrapper can misreport this task as no_crash because it invokes the fuzzer with a file path where its script expects a corpus directory; direct image execution and official submit are the reliable signals.

### Format Links
- [[opentype-font]]

### Notes
- These facts are descriptive observations only; they carry no success-rate claim.

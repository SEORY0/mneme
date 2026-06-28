---
type: harness-contract
title: "Libfuzzer Raw Htslib Hts Open harness"
description: "Input contract facts for Libfuzzer Raw Htslib Hts Open."
tags: ["libfuzzer-raw-htslib-hts-open", "round-21"]
okf_support: 1
---
# Libfuzzer Raw Htslib Hts Open Harness

## Round 21 Input Contract (sam-bam-cram)

- The fuzzer first opens the raw bytes as an in-memory file only to determine format category. For sequence data it then repeats read/write loops to SAM, BAM, and CRAM outputs, writing to a null sink. The CRAM leg is the target path, but missing reference data can force non-reference encoding instead.

## Round 21 Format Links (sam-bam-cram)
- [[sam-bam-cram]]

## Round 21 Notes (sam-bam-cram)
- These are descriptive harness-carving facts only; they are not causal recovery claims.

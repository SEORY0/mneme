---
type: harness-contract
title: "Libfuzzer Raw Htslib Hts Open harness"
description: "Input contract facts for Libfuzzer Raw Htslib Hts Open."
tags: ["libfuzzer-raw-htslib-hts-open", "round-21"]
okf_support: 2
---
# Libfuzzer Raw Htslib Hts Open Harness

## Round 21 Input Contract (sam-bam-cram)

- The fuzzer first opens the raw bytes as an in-memory file only to determine format category. For sequence data it then repeats read/write loops to SAM, BAM, and CRAM outputs, writing to a null sink. The CRAM leg is the target path, but missing reference data can force non-reference encoding instead.

## Round 21 Format Links (sam-bam-cram)
- [[sam-bam-cram]]

## Round 21 Notes (sam-bam-cram)
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 31 Input Contract

### Input Contract
- The hts_open fuzzer uses the raw libFuzzer input bytes as an in-memory file. It first detects the file format with hts_hopen, then for sequence data replays the same bytes through read/write loops for SAM, BAM, and CRAM output modes. There is no leading mode selector and no FuzzedDataProvider split. The CRAM writeback path is reached by any accepted sequence record, and unmapped/no-CIGAR BAM records avoid the CG-tag aux scan before CRAM encoding.

### Format Links
- [[bam]]

### Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.

---
type: harness-contract
title: "Libfuzzer Tempfile BFD harness"
description: "Input contract facts for libfuzzer-tempfile-bfd."
tags: ["libfuzzer-tempfile-bfd"]
okf_support: 1
---
# Libfuzzer Tempfile BFD Harness

## Round 10 Input Contract
- The fuzzer writes the raw input to a temporary file, opens it with BFD auto-detection, and checks archive format. Inputs must therefore be complete file bytes, not an in-memory record stream.

## Round 10 Format Links
- [[bfd-archive-containing-truncated-msdos-member]]

## Round 10 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 11 Input Contract
- The harness writes the raw input bytes to a temporary file and opens that file through BFD auto-detection before checking archive format. There is no mode-selector byte and no FuzzedDataProvider field carving; all structure is in the archive bytes.

## Format Links
- [[som-library-archive]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 15 Input Contract
- The libFuzzer input is written to a temporary file, opened by BFD, and checked as an archive.
  Reaching member ELF parsing depends on archive metadata, not just a standalone ELF header. There is
  no selector byte and no FuzzedDataProvider layout.

## Format Links
- [[ar-archive-elf]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 17 Input Contract
- The harness writes raw input to a temporary file, opens it with BFD auto-detection, and explicitly checks archive format.
- There is no selector byte and no provider-carved layout.

## Round 17 Format Links
- [[som-library-or-som-object]]

## Round 17 Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.

## Round 17 Format Links
- [[som-library-or-som-object]]

## Round 17 Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.

## Round 22 Input Contract
- The libFuzzer harness writes raw bytes to a temporary file, opens that file through BFD auto-detection, calls the archive-format check, and closes the BFD. There is no leading selector, checksum, or in-memory record wrapper.

## Format Links
- [[bfd-archive-or-object]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 30 Input Contract

### Input Contract
- The libFuzzer input bytes are written unchanged to a temporary file. The wrapper opens that file with BFD automatic target selection and calls the archive format checker only. There is no FuzzedDataProvider, mode byte, filename-controlled target, or checksum layer; reaching ELF member parsing depends on archive metadata and BFD target recognition side effects.

### Format Links
- [[ar-archive-elf]]

### Notes
- These facts are descriptive harness-carving observations only; they are not causal recovery claims.

## Round 35 Input Contract

### Input Contract
- The libFuzzer callback writes the raw input bytes to a temporary file, opens it with BFD, and checks archive format. There is no FuzzedDataProvider split or leading mode byte. During archive-format recognition, a mapped archive causes BFD to open the first member and check it as an object, which reaches SOM object setup.

### Format Links
- [[som-library-or-som-object]]

### Notes
- These facts are descriptive harness-carving observations from round 35; they carry no success-rate claim.

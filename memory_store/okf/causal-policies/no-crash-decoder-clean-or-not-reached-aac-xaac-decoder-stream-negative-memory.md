---
type: causal-policy
title: "No Crash Decoder Clean Or Not Reached AAC Xaac Decoder Stream Negative Memory"
description: "Round 15 negative memory for no_crash with verifier signal decoder_clean_or_not_reached."
failure_class: "no_crash"
verifier_signal: "decoder_clean_or_not_reached"
candidate_family: "construct"
input_format: "aac-xaac-decoder-stream"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "decoder-clean-or-not-reached", "aac-xaac-decoder-stream", "negative-memory", "round-15"]
match_keys: ["no_crash", "decoder_clean_or_not_reached", "aac-xaac-decoder-stream", "libfuzzer", "use-of-uninitialized-value", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 15
---
# No Crash Decoder Clean Or Not Reached AAC Xaac Decoder Stream Negative Memory

- key: `no_crash x decoder_clean_or_not_reached`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[aac-xaac-decoder-stream]]
- related harness facts: [[libfuzzer]]

## Failure Shape
- An ADTS-like AAC frame with filler initialized and decoded without reaching the complex-analysis QMF
  uninitialized-value path. The missing gate is a valid enough enhanced AAC/xHE-AAC configuration and
  SBR/HBE element sequence that calls the complex analysis filter block.

## Policy
Treat `no_crash x decoder_clean_or_not_reached` on `aac-xaac-decoder-stream` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
- The decoder fuzzer recognizes ADTS by the leading sync pattern and otherwise treats the input as an
  xAAC decoder configuration followed by stream data. It initializes the decoder, configures it from
  the byte stream, then repeatedly decodes while advancing by consumed bytes.

## Harness Contract
- The libFuzzer harness passes raw bytes to the libxaac decoder wrapper. The first bytes influence
  ADTS detection and decoder configuration; there is no file container outside the codec byte stream.

## Negative Memory
- Do not resubmit variants that only reproduce `decoder_clean_or_not_reached`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from Round 15.
- Scope: generator repair and basin avoidance only.

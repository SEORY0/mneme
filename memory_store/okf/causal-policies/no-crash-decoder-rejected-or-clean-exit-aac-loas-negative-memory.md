---
type: causal-policy
title: "No Crash Decoder Rejected Or Clean Exit AAC Loas Negative Memory"
description: "Round 15 negative memory for no_crash with verifier signal decoder_rejected_or_clean_exit."
failure_class: "no_crash"
verifier_signal: "decoder_rejected_or_clean_exit"
candidate_family: "construct"
input_format: "aac-loas"
harness_convention: "libfuzzer"
vuln_class: "state-confusion"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "decoder-rejected-or-clean-exit", "aac-loas", "negative-memory", "round-15"]
match_keys: ["no_crash", "decoder_rejected_or_clean_exit", "aac-loas", "libfuzzer", "state-confusion", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 15
---
# No Crash Decoder Rejected Or Clean Exit AAC Loas Negative Memory

- key: `no_crash x decoder_rejected_or_clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[aac-loas]]
- related harness facts: [[libfuzzer]]

## Failure Shape
- Constructed ADTS-like, raw config-like, and LOAS/LATM-shaped byte streams did not reach the SBR
  header-update state. The missing gate appears to be a coherent LOAS/LATM access unit with enough AAC
  configuration and SBR extension state for the decoder to retain failed header data.

## Policy
Treat `no_crash x decoder_rejected_or_clean_exit` on `aac-loas` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
- The selected decoder transport is LOAS/LATM rather than a generic file container. Useful inputs need
  a transport sync/config layer, audio mux configuration, and AAC frame data that enables the SBR
  path; simple ADTS or standalone AudioSpecificConfig bytes are not sufficient.

## Harness Contract
- The libFuzzer target opens the FDK-AAC decoder in the LOAS transport mode, fills the decoder
  directly from the raw fuzzer buffer, and calls DecodeFrame in a loop. There is no outer file wrapper
  or FuzzedDataProvider field layout.

## Negative Memory
- Do not resubmit variants that only reproduce `decoder_rejected_or_clean_exit`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from Round 15.
- Scope: generator repair and basin avoidance only.

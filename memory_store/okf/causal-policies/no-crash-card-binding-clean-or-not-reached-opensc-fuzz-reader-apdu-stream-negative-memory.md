---
type: causal-policy
title: "No Crash Card Binding Clean Or Not Reached Opensc Fuzz Reader Apdu Stream Negative Memory"
description: "Round 8 negative memory for no_crash with verifier signal card_binding_clean_or_not_reached."
failure_class: "no_crash"
verifier_signal: "card_binding_clean_or_not_reached"
candidate_family: "construct"
input_format: "opensc-fuzz-reader-apdu-stream"
harness_convention: "libfuzzer"
vuln_class: "buffer-overrun"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "card-binding-clean-or-not-reached", "opensc-fuzz-reader-apdu-stream", "negative_memory", "round-8"]
match_keys: ["no_crash", "card_binding_clean_or_not_reached", "opensc-fuzz-reader-apdu-stream", "libfuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 8
---
# No Crash Card Binding Clean Or Not Reached Opensc Fuzz Reader Apdu Stream Negative Memory

## Policy
Treat `no_crash x card_binding_clean_or_not_reached` as a persistent failure basin for `opensc-fuzz-reader-apdu-stream` under `libfuzzer`. Preserve any reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Diagnosed Dead End
- The first raw-ATR attempt used the wrong input contract. Proper chunked ATR plus APDU response streams reached the fuzz reader shape but did not build enough PKCS#15/CardOS state to drive the vulnerable list-files remaining-length calculation.

## Format and Harness Gates
- Format: This fuzzer input is a sequence of length-prefixed chunks. The first chunk is consumed as the card ATR. Later chunks are APDU responses, where the trailing status bytes are separated from response data.
- Harness: The harness installs a synthetic reader, connects a card from the first chunk, binds PKCS#15, and then consumes further chunks during card operations. Response chunks shorter than a status word synthesize an unsupported-instruction status.

## Procedure
1. Before retrying this basin, rebuild the carrier around the exact harness contract and confirm parser reachability.
2. Replace the failed mutation family with a more specific invariant that would change the verifier signal.
3. Avoid broad seed mutation, oversized mutation, or off-target crash chasing when this same signal recurs.

## Negative Memory
- Do not promote this basin into a recovery policy until an official vulnerable/fixed verifier target match is observed.
- Do not preserve raw bytes, offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-8 persistent failure trace.
- Scope: generator avoidance and retargeting for the same failure key.

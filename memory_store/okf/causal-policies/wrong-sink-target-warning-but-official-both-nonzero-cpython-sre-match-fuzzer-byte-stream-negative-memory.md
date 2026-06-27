---
type: causal-policy
title: "Wrong Sink Target Warning But Official Both Nonzero Cpython Sre Match Fuzzer Byte Stream Negative Memory"
description: "Round 9 negative memory for wrong_sink with verifier signal target_warning_but_official_both_nonzero."
failure_class: "wrong_sink"
verifier_signal: "target_warning_but_official_both_nonzero"
candidate_family: "construct"
input_format: "CPython sre-match fuzzer byte stream"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 0
confidence: medium
tags: ["wrong-sink", "target-warning-but-official-both-nonzero", "cpython-sre-match-fuzzer-byte-stream", "negative-memory", "round-9"]
match_keys: ["wrong_sink", "target_warning_but_official_both_nonzero", "CPython sre-match fuzzer byte stream", "libfuzzer", "use-of-uninitialized-value", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 9
---
# Wrong Sink Target Warning But Official Both Nonzero Cpython Sre Match Fuzzer Byte Stream Negative Memory

- key: `wrong_sink x target_warning_but_official_both_nonzero`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[cpython-sre-match-fuzzer-byte-stream]]
- related harness facts: [[libfuzzer]]

## Failure Shape
- A minimal selector-only input caused MemorySanitizer to report the described funcobject
  uninitialized-value path during CPython initialization/import, before regex matching mattered.
- Local confirm showed a plausible vul-only warning, but official submission reported both images
  exiting nonzero, so this was not accepted.
- A successful candidate likely needs to avoid the shared initialization failure and trigger a post-
  initialization funcobject read that differs between images.

## Policy
Treat `wrong_sink x target_warning_but_official_both_nonzero` on `CPython sre-match fuzzer byte stream` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
- The active fuzzer input uses the first byte as a regex-pattern selector modulo a fixed pattern
  table.
- The remaining bytes become a Python bytes object passed to the selected compiled pattern's match
  method.

## Harness Contract
- LLVMFuzzerInitialize starts CPython before the input-specific callback.
- The selected fuzz target precompiles a fixed list of regex patterns on first use, then for each
  input creates a bytes object from the payload after the selector and calls the compiled pattern's
  match method.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `target_warning_but_official_both_nonzero`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 9.
- Scope: generator repair and basin avoidance only.

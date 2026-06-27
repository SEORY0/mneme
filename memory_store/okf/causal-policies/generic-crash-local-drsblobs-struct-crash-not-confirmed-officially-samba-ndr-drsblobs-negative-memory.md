---
type: causal-policy
title: "Generic Crash Local Drsblobs Struct Crash Not Confirmed Officially Samba Ndr Drsblobs Negative Memory"
description: "Round 9 negative memory for generic_crash with verifier signal local_drsblobs_struct_crash_not_confirmed_officially."
failure_class: "generic_crash"
verifier_signal: "local_drsblobs_struct_crash_not_confirmed_officially"
candidate_family: "construct-selector-sweep"
input_format: "samba-ndr-drsblobs"
harness_convention: "libfuzzer"
vuln_class: "logic-error-ndr-array-count"
access_scope: generate
success_count: 0
confidence: medium
tags: ["generic-crash", "local-drsblobs-struct-crash-not-confirmed-officially", "samba-ndr-drsblobs", "negative-memory", "round-9"]
match_keys: ["generic_crash", "local_drsblobs_struct_crash_not_confirmed_officially", "samba-ndr-drsblobs", "libfuzzer", "logic-error-ndr-array-count", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 9
---
# Generic Crash Local Drsblobs Struct Crash Not Confirmed Officially Samba Ndr Drsblobs Negative Memory

- key: `generic_crash x local_drsblobs_struct_crash_not_confirmed_officially`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[samba-ndr-drsblobs]]
- related harness facts: [[libfuzzer]]

## Failure Shape
- The active surface was the generated drsblobs TYPE_STRUCT fuzzer.
- A selector/payload combination produced a local segmentation signal, but the official server
  reported no vulnerable-build failure, indicating the local crash was not the target schedule-count
  regression or was not stable under the server run.

## Policy
Treat `generic_crash x local_drsblobs_struct_crash_not_confirmed_officially` on `samba-ndr-drsblobs` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
- The input starts with a small little-endian NDR fuzzer selector header: flags choose
  struct/in/out/NDR64 mode and a public-struct number chooses the drsblobs structure.
- The remaining bytes are NDR stub data.
- The schedule structure contains a size, constant-valued fields, schedule header records, and
  schedule slot records whose count is controlled by the schedule count relation.

## Harness Contract
- The wrapper is fixed to fuzz_ndr_drsblobs_TYPE_STRUCT.
- It reads the header, pulls the chosen public struct with scalar and buffer flags, pushes the
  parsed struct back out, then walks the print routine.
- There is no FuzzedDataProvider carving beyond the NDR selector header.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `local_drsblobs_struct_crash_not_confirmed_officially`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 9.
- Scope: generator repair and basin avoidance only.

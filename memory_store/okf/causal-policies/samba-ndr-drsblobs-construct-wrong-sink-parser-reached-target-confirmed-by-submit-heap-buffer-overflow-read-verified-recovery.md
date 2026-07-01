---
type: causal-policy
title: "Samba Ndr Drsblobs Construct Wrong Sink Parser Reached Target Confirmed By Submit Heap Buffer Overflow Read Verified Recovery"
description: "Round 34 verified recovery for samba-ndr-drsblobs when wrong_sink pairs with parser_reached_target_confirmed_by_submit."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_confirmed_by_submit"
candidate_family: "construct"
input_format: "samba-ndr-drsblobs"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-confirmed-by-submit", "samba-ndr-drsblobs", "libfuzzer", "construct", "verified-recovery", "round-34"]
match_keys: ["wrong-sink", "parser-reached-target-confirmed-by-submit", "samba-ndr-drsblobs", "libfuzzer", "construct", "heap-buffer-overflow-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 34
---
# Samba Ndr Drsblobs Construct Wrong Sink Parser Reached Target Confirmed By Submit Heap Buffer Overflow Read Verified Recovery

- key: `wrong_sink x parser_reached_target_confirmed_by_submit`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[samba-ndr-drsblobs]]
- related harness facts: [[libfuzzer]]

## Round 34 Verified Support

- key: `wrong_sink x parser_reached_target_confirmed_by_submit`
- outcome: server-verified vulnerable/fixed split
- candidate family: `construct`
- vulnerability class: `heap-buffer-overflow-read`
- related format facts: [[samba-ndr-drsblobs]]
- related harness facts: [[libfuzzer]]

### Policy
When `wrong_sink x parser_reached_target_confirmed_by_submit` appears for `samba-ndr-drsblobs`, preserve the accepted parser and harness gates, then target the specific state relation that the verifier proved. Treat the official vulnerable-only target match as the success gate; local crash class alone is not enough.

### Procedure
1. Use the [[libfuzzer]] harness contract and the [[samba-ndr-drsblobs]] format contract before changing sink fields.
2. Recreate the verified causal relation: Use the generated NDR TYPE_STRUCT harness path for the drsblobs schedule structure. Encode the schedule scalars so the pulled object has an empty schedule-array allocation while the generated push path still treats the schedule count as nonempty; the subsequent push of schedule headers reads past the allocated array. Keep the stub narrowly scoped to that single count/allocation inconsistency so the fixed build rejects or normalizes it cleanly.
3. Keep selectors, lengths, state setup, and container invariants coherent until the target parser state is reached.
4. Submit only when the candidate is expected to preserve the vulnerable/fixed split rather than a generic both-build crash.

### Format Contract
The drsblobs NDR fuzzer consumes a leading little-endian selector containing flags and the selected generated struct/function, followed by an NDR stub. The schedule structure contains scalar fields, a schedule count relation, a header array governed by that relation, and a parallel schedule-slot array. Generated pull code builds the in-memory struct and generated push code serializes it back out.

### Harness Contract
The selected harness is the generated libFuzzer TYPE_STRUCT target for drsblobs. It pulls the chosen structure with NDR scalar and buffer flags, then immediately pushes and prints the resulting structure, so inconsistencies between pull-time allocation and push-time count use become sanitizer-visible.

### Evidence Shape
- Support: one server-verified round 34 solve.
- Candidate family: `construct`.
- Verifier key: `wrong_sink x parser_reached_target_confirmed_by_submit`.
- Vulnerability class: `heap-buffer-overflow-read`.

## Negative Memory
- Do not count parser reachability, both-image crashes, fixed-image crashes, local wrapper crashes, clean exits, or off-target sanitizer crashes as success for this key.
- Do not store concrete payload bytes, exact positions, task identifiers, checksums, or submit metadata.

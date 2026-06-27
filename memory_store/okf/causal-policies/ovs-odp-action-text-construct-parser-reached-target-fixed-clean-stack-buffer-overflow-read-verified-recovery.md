---
type: causal-policy
title: "OVS Odp Action Text Construct Parser Reached Target Fixed Clean Stack Buffer Overflow Read Verified Recovery"
description: "Round 15 server-verified recovery for ovs-odp-action-text keyed by wrong_sink x parser_reached_target_fixed_clean."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_fixed_clean"
candidate_family: "construct"
input_format: "ovs-odp-action-text"
harness_convention: "libfuzzer"
vuln_class: "stack-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-fixed-clean", "ovs-odp-action-text", "libfuzzer", "construct", "stack-buffer-overflow-read", "verified-recovery", "round-15"]
match_keys: ["wrong_sink", "parser_reached_target_fixed_clean", "ovs-odp-action-text", "libfuzzer", "stack-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 15
---
# OVS Odp Action Text Construct Parser Reached Target Fixed Clean Stack Buffer Overflow Read Verified Recovery

- key: `wrong_sink x parser_reached_target_fixed_clean`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[ovs-odp-action-text]]
- related harness facts: [[libfuzzer]]

## Policy
When `ovs-odp-action-text` under `libfuzzer` reaches `parser_reached_target_fixed_clean` from `wrong_sink`, preserve the accepted parser carrier and retarget only the causal invariant proven by the verifier. Treat local coarse labels as advisory once the vulnerable image fails and the fixed image does not reproduce the target behavior.

## Procedure
1. Preserve the harness contract and format family that reached the parser; do not switch envelopes after reachability is proven.
2. Use raw OVS datapath action text that is NUL terminated and contains no newline. Select the
   push_nsh action with metadata type 2, then provide an md2 hex string that is larger than the
   fixed metadata buffer but still small enough that the recorded metadata size does not wrap to
   zero. This reaches action formatting and violates the invariant that the copied md2 metadata
   length must not exceed the stack metadata array.
3. Keep mutations focused on the relevant invariant: parser selection, declared length versus available content, selector versus subparser, table count versus records, lifetime ownership, or sink-specific state.
4. If local labels report a non-target sink while the parser branch is reached, submit once before discarding the candidate.
5. If the fixed image also fails, shrink to the smallest boundary relation and avoid broad randomization.

## Format Contract
- OVS ODP action text is a comma-delimited action language. push_nsh accepts named fields such as
  flags, ttl, mdtype, next protocol, service path, service index, and either fixed context words for
  metadata type 1 or a hex md2 field for metadata type 2. The md2 hex is parsed into bytes and padded
  to word alignment before it is serialized into the netlink action.

## Harness Contract
- The fuzzer passes the input bytes directly as a C string after requiring at least one payload byte,
  a trailing NUL, and no newline. The same string is tried as flow keys and then as ODP actions; there
  is no outer file format, selector byte, checksum, or FuzzedDataProvider layout.

## Negative Memory
- Do not replay unrelated seeds after this parser branch is reached.
- Do not count fixed-image crashes, both-image crashes, clean exits, parser rejection, or off-target local stacks as success.
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.

## Evidence Shape
- Support: one server-verified Round 15 solve.
- Candidate family: construct.

---
type: causal-policy
title: "OMF Construct Parser Reached Target Confirmed Heap Buffer Overflow Read Verified Recovery"
description: "Round 15 server-verified recovery for omf keyed by wrong_sink x parser_reached_target_confirmed."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_confirmed"
candidate_family: "construct"
input_format: "omf"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-confirmed", "omf", "libfuzzer", "construct", "heap-buffer-overflow-read", "verified-recovery", "round-15"]
match_keys: ["wrong_sink", "parser_reached_target_confirmed", "omf", "libfuzzer", "heap-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 15
---
# OMF Construct Parser Reached Target Confirmed Heap Buffer Overflow Read Verified Recovery

- key: `wrong_sink x parser_reached_target_confirmed`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[omf]]
- related harness facts: [[libfuzzer]]

## Policy
When `omf` under `libfuzzer` reaches `parser_reached_target_confirmed` from `wrong_sink`, preserve the accepted parser carrier and retarget only the causal invariant proven by the verifier. Treat local coarse labels as advisory once the vulnerable image fails and the fixed image does not reproduce the target behavior.

## Procedure
1. Preserve the harness contract and format family that reached the parser; do not switch envelopes after reachability is proven.
2. A minimal OMF-recognized record prefix is enough to satisfy the binary plugin probe, but the
   record is shorter than the probe's length/header expectation. The vulnerable build reads past
   the allocation while classifying the record, while the fixed build rejects the truncated record.
3. Keep mutations focused on the relevant invariant: parser selection, declared length versus available content, selector versus subparser, table count versus records, lifetime ownership, or sink-specific state.
4. If local labels report a non-target sink while the parser branch is reached, submit once before discarding the candidate.
5. If the fixed image also fails, shrink to the smallest boundary relation and avoid broad randomization.

## Format Contract
- OMF records begin with a one-byte record type from a recognized set, followed by record metadata
  that plugin detection may inspect before full parsing. Truncated prefixes can reach the vulnerable
  boundary when they look enough like a valid OMF record to select the plugin.

## Harness Contract
- The libFuzzer harness passes raw bytes as the candidate binary input. The target opens the bytes as
  a file or buffer and dispatches binary format plugin detection directly; there is no leading mode
  selector and no FuzzedDataProvider layout.

## Negative Memory
- Do not replay unrelated seeds after this parser branch is reached.
- Do not count fixed-image crashes, both-image crashes, clean exits, parser rejection, or off-target local stacks as success.
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.

## Evidence Shape
- Support: one server-verified Round 15 solve.
- Candidate family: construct.

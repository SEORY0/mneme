---
type: causal-policy
title: "ASS Subtitle Construct Target Hash Function Reached Heap Buffer Overflow Read Verified Recovery"
description: "Round 15 server-verified recovery for ass-subtitle keyed by generic_crash x target_hash_function_reached."
failure_class: "generic_crash"
verifier_signal: "target_hash_function_reached"
candidate_family: "construct"
input_format: "ass-subtitle"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "target-hash-function-reached", "ass-subtitle", "libfuzzer", "construct", "heap-buffer-overflow-read", "verified-recovery", "round-15"]
match_keys: ["generic_crash", "target_hash_function_reached", "ass-subtitle", "libfuzzer", "heap-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 15
---
# ASS Subtitle Construct Target Hash Function Reached Heap Buffer Overflow Read Verified Recovery

- key: `generic_crash x target_hash_function_reached`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[ass-subtitle]]
- related harness facts: [[libfuzzer]]

## Policy
When `ass-subtitle` under `libfuzzer` reaches `target_hash_function_reached` from `generic_crash`, preserve the accepted parser carrier and retarget only the causal invariant proven by the verifier. Treat local coarse labels as advisory once the vulnerable image fails and the fixed image does not reproduce the target behavior.

## Procedure
1. Preserve the harness contract and format family that reached the parser; do not switch envelopes after reachability is proven.
2. Build a syntactically valid ASS subtitle with script info, a style table, and at least one
   renderable event, but leave the font-family field empty. Rendering initializes the font cache
   and hashes that zero-length family string, triggering the vulnerable FNV buffer hash while all
   subtitle-section gates remain valid.
3. Keep mutations focused on the relevant invariant: parser selection, declared length versus available content, selector versus subparser, table count versus records, lifetime ownership, or sink-specific state.
4. If local labels report a non-target sink while the parser branch is reached, submit once before discarding the candidate.
5. If the fixed image also fails, shrink to the smallest boundary relation and avoid broad randomization.

## Format Contract
- ASS input must include recognizable section headers, a style format matching the style record
  fields, an events format, and a dialogue event whose timestamp is rendered by the harness. Empty
  fields are accepted by the parser when the comma-separated field count is preserved.

## Harness Contract
- The libFuzzer harness feeds raw bytes to ass_read_memory, then renders each parsed event at a
  timestamp inside the event. No outer file envelope or byte carving is used.

## Negative Memory
- Do not replay unrelated seeds after this parser branch is reached.
- Do not count fixed-image crashes, both-image crashes, clean exits, parser rejection, or off-target local stacks as success.
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.

## Evidence Shape
- Support: one server-verified Round 15 solve.
- Candidate family: construct.

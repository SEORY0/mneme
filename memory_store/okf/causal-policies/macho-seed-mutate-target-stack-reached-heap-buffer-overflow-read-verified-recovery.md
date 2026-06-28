---
type: causal-policy
title: "Macho Seed Mutate Target Stack Reached Heap Buffer Overflow Read Verified Recovery"
description: "Round 14 server-verified recovery for macho keyed by wrong_sink x target_stack_reached."
failure_class: "wrong_sink"
verifier_signal: "target_stack_reached"
candidate_family: "seed_mutate"
input_format: "macho"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "target-stack-reached", "macho", "libfuzzer", "seed-mutate", "heap-buffer-overflow-read", "verified-recovery", "round-14"]
match_keys: ["wrong_sink", "target_stack_reached", "macho", "libfuzzer", "heap-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 14
---
# Macho Seed Mutate Target Stack Reached Heap Buffer Overflow Read Verified Recovery

- key: `wrong_sink x target_stack_reached`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[macho]]
- related harness facts: [[libfuzzer]]

## Policy
When `macho` under `libfuzzer` reaches `target_stack_reached` from `wrong_sink`, keep the accepted carrier and retarget the single invariant named by the verified recovery. This policy is verifier-gated by vulnerable-build failure and fixed-build non-match behavior.

## Procedure
1. Preserve the harness contract `[[libfuzzer]]` and format contract `[[macho]]`; do not switch container families once parser reachability is proven.
2. Apply the verified recovery: Start from a valid bundled Mach-O executable stub so UPX accepts the file and reaches the Mach-O packer. Preserve the header and load-command table layout, but increase the declared load-command count so the parser expects one more command than the command area actually contains, forcing the Mach-O capability check to read a command header beyond the available command bytes.
3. Keep mutations focused on the gate relation: declared size versus available data, selector versus subparser, structure count versus actual records, lifetime ownership, or sink-specific state.
4. If local labels report `wrong_sink` while the same parser branch is reached, submit once to check the official target match before discarding the candidate.
5. If the fixed image also fails, shrink back to the smallest boundary relation and avoid broad randomization.

## Negative Memory
- Do not replay unrelated seeds after this parser branch is reached.
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.
- Do not promote this as a byte recipe; it is a format-gate and sink-invariant relation.

## Evidence Shape
- Support: one server-verified Round 14 solve.
- Candidate family: seed_mutate.

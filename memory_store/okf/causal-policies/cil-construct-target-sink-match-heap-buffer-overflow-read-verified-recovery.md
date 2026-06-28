---
type: causal-policy
title: "Cil Construct Target Sink Match Heap Buffer Overflow Read Verified Recovery"
description: "Round 12 verified recovery for generic_crash with verifier signal target_sink_match."
failure_class: "generic_crash"
verifier_signal: "target_sink_match"
candidate_family: "construct"
input_format: "cil"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "target-sink-match", "cil", "verified-recovery", "round-12"]
match_keys: ["generic_crash", "target_sink_match", "cil", "libfuzzer", "heap-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 12
---
# Cil Construct Target Sink Match Heap Buffer Overflow Read Verified Recovery

- key: `generic_crash x target_sink_match`
- outcome: verified recovery
- confidence: 0.82
- success_count: 1
- failure_count: 0
- formats: [[cil]]
- harnesses: [[libfuzzer]]

## Failure Shape
The verifier-confirmed candidate preserved the `cil` parser envelope under `libfuzzer` and moved the mutation into the relation consumed by the target sink instead of relying on broad corruption.

## Policy
Use this policy when generation reports `generic_crash` with signal `target_sink_match` on `cil` or the same format family. Preserve parser reachability first, then adjust only the smallest format relation named in the procedure until the vulnerable build crashes and the fixed build stays clean.

## Procedure
Construct a complete minimal CIL policy so compilation reaches resolution, then place a block inheritance reference inside an optional container nested under the referenced block. The recursive diagnostic path walks through a non-block intermediate node and violates its assumed node-type invariant.

## Verifier Contract
The official comparison must show target match with a vulnerable-build crash and a clean fixed build. Parser reachability, local-only crashes, off-target crashes, or both-image crashes are not sufficient.

## Format Contract
CIL is an S-expression policy language. A compilable policy needs baseline declarations for classes, ordering, identities, roles, types, categories, sensitivities, contexts, and allows. Blocks and optional containers are nested S-expression scopes; blockinherit references a block symbol.

## Harness Contract
The libFuzzer bytes are consumed as one raw CIL file. The harness adds the file to the CIL database, compiles, builds a policy database, and writes policy output; there is no archive wrapper or carved input layout.

## Negative Guards
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.
- Do not widen mutation after the parser envelope is accepted; shrink back to the single boundary relation when the fixed image also crashes.
- Do not promote this policy to another format unless the same failure key and verifier signal recur under official comparison.

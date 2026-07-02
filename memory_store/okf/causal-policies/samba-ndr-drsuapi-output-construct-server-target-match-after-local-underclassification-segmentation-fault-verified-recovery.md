---
type: causal-policy
title: "Samba NDR Drsuapi Output Construct Server Target Match After Local Underclassification Segmentation Fault Verified Recovery"
description: "Round 27 verified recovery for generic_crash with verifier signal server_target_match_after_local_underclassification."
failure_class: "generic_crash"
verifier_signal: "server_target_match_after_local_underclassification"
candidate_family: "construct"
input_format: "samba-ndr-drsuapi-output"
harness_convention: "libfuzzer"
vuln_class: "segmentation-fault"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "server-target-match-after-local-underclassification", "samba-ndr-drsuapi-output", "libfuzzer", "construct", "segmentation-fault", "verified-recovery", "round-27"]
match_keys: ["generic_crash", "server_target_match_after_local_underclassification", "samba-ndr-drsuapi-output", "libfuzzer", "segmentation-fault", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 27
---
# Samba NDR Drsuapi Output Construct Server Target Match After Local Underclassification Segmentation Fault Verified Recovery

## Policy
For `generic_crash x server_target_match_after_local_underclassification`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Use the Samba NDR fuzzer envelope with the output-type selector and the DRSUAPI function that returns directory-replication changes.
2. Keep the outer NDR selector valid, then select the compressed change-reply branch with a present compressed subcontext and small compressed content whose declared expansion requires the vulnerable decode path.
3. Over-broad compressed branches crash both builds, so the useful input keeps the function/output union coherent while violating only the compressed-stream consistency relation.
4. Keep the carrier abstract: preserve the gate/invariant relation, not any task-local bytes or offsets.
5. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- Samba generated NDR fuzz inputs start with a small little-endian selector for packet flags and interface call, followed by stub data.
- For DRSUAPI TYPE_OUT calls, output parameters are decoded as the function's reply structure; union discriminants choose reply families, and non-null pointer or subcontext fields must be represented so deferred buffers are pulled.
- The DsGetNCChanges reply has uncompressed and compressed change-reply union branches; the compressed branches carry declared compressed and decompressed sizes plus an embedded change-reply subcontext.
- Harness [[libfuzzer]]:
  - The active target is the DRSUAPI TYPE_OUT libFuzzer binary.
  - It rejects inputs whose selector type is not output, then pulls any output pipes, decodes the selected function's OUT stub, re-pushes the decoded structure, and walks the NDR print tree.
  - There is no FuzzedDataProvider and no mode byte beyond the NDR selector header.

## Negative Memory
- Do not broaden mutations after the parser or harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-27 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[samba-ndr-drsuapi-output]] and [[libfuzzer]].

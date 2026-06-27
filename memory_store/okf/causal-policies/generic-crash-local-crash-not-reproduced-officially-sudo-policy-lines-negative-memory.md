---
type: causal-policy
title: "Generic Crash Local Crash Not Reproduced Officially Sudo Policy Lines Negative Memory"
description: "Round 17 negative memory for generic_crash with verifier signal local_crash_not_reproduced_officially."
failure_class: "generic_crash"
verifier_signal: "local_crash_not_reproduced_officially"
candidate_family: "seed_mutate"
input_format: "sudo-policy-lines"
harness_convention: "libfuzzer"
vuln_class: "heap-use-after-free"
access_scope: generate
success_count: 0
confidence: medium
tags: ["generic-crash", "local-crash-not-reproduced-officially", "sudo-policy-lines", "libfuzzer", "negative-memory", "round-17"]
match_keys: ["generic-crash", "local-crash-not-reproduced-officially", "sudo-policy-lines", "libfuzzer", "heap-use-after-free", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 17
---
# Generic Crash Local Crash Not Reproduced Officially Sudo Policy Lines Negative Memory

- key: `generic_crash x local_crash_not_reproduced_officially`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[sudo-policy-lines]]
- related harness facts: [[libfuzzer]]

## Failure Shape
- Mutating the sudoedit policy seed with root user info, sudoedit argv entries, env_editor settings, PATH changes, valid editors, and missing environment-selected editors produced coarse local wrapper crashes in some cases, but the official server did not reproduce a vulnerable-build crash.
- The likely missing condition is a precise sudoedit cleanup path where a copied editor string remains registered in the sudoers GC after failed resolution.

## Policy
Treat `generic_crash x local_crash_not_reproduced_officially` on `sudo-policy-lines` as a basin to avoid unless a new candidate changes the parser gate, state relation, or target-sink relation described above. Preserve any proven reachability, but discard variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to this same basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `local_crash_not_reproduced_officially`.
- Do not count parser reachability, local wrapper crashes, both-image crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[sudo-policy-lines]] for descriptive format gates and invariants.

## Harness Contract
Use [[libfuzzer]] for the input-carving contract.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 17.
- Scope: generator repair and basin avoidance only.

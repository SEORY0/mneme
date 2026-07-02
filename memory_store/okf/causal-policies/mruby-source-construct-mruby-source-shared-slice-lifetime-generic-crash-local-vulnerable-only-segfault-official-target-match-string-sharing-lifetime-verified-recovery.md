---
type: causal-policy
title: "Mruby Source Construct Mruby Source Shared Slice Lifetime Generic Crash Local Vulnerable Only Segfault Official Target Match String Sharing Lifetime Verified Recovery"
description: "Round 34 verified recovery for mruby-source when generic_crash pairs with local_vulnerable_only_segfault_official_target_match."
failure_class: "generic_crash"
verifier_signal: "local_vulnerable_only_segfault_official_target_match"
candidate_family: "construct_mruby_source_shared_slice_lifetime"
input_format: "mruby-source"
harness_convention: "libfuzzer"
vuln_class: "string-sharing-lifetime"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "local-vulnerable-only-segfault-official-target-match", "mruby-source", "libfuzzer", "construct-mruby-source-shared-slice-lifetime", "verified-recovery", "round-34"]
match_keys: ["generic-crash", "local-vulnerable-only-segfault-official-target-match", "mruby-source", "libfuzzer", "construct-mruby-source-shared-slice-lifetime", "string-sharing-lifetime", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 34
---
# Mruby Source Construct Mruby Source Shared Slice Lifetime Generic Crash Local Vulnerable Only Segfault Official Target Match String Sharing Lifetime Verified Recovery

- key: `generic_crash x local_vulnerable_only_segfault_official_target_match`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[mruby-source]]
- related harness facts: [[libfuzzer]]

## Round 34 Verified Support

- key: `generic_crash x local_vulnerable_only_segfault_official_target_match`
- outcome: server-verified vulnerable/fixed split
- candidate family: `construct_mruby_source_shared_slice_lifetime`
- vulnerability class: `string-sharing-lifetime`
- related format facts: [[mruby-source]]
- related harness facts: [[libfuzzer]]

### Policy
When `generic_crash x local_vulnerable_only_segfault_official_target_match` appears for `mruby-source`, preserve the accepted parser and harness gates, then target the specific state relation that the verifier proved. Treat the official vulnerable-only target match as the success gate; local crash class alone is not enough.

### Procedure
1. Use the [[libfuzzer]] harness contract and the [[mruby-source]] format contract before changing sink fields.
2. Recreate the verified causal relation: Use valid mruby source that creates a heap-backed string, returns a shared full-length slice from a helper scope, drops the original owner, and forces garbage collection so the shared backing has a single remaining string. Apply one keep-ascii bang mutation to the surviving slice to free the shared header while the vulnerable build leaves the shared flag set, then apply a second bang mutation to dereference the stale shared state. The fixed build clears the shared flag and handles the second mutation normally.
3. Keep selectors, lengths, state setup, and container invariants coherent until the target parser state is reached.
4. Submit only when the candidate is expected to preserve the vulnerable/fixed split rather than a generic both-build crash.

### Format Contract
The input is plain mruby source text. It must be syntactically valid Ruby that executes under mrb_load_string. Heap-backed strings are needed for shared-string behavior; substring or slice operations over a non-embedded string can create a shared string object that aliases the original backing storage.

### Harness Contract
The libFuzzer harness treats the entire nonempty file as raw mruby source bytes. It copies the bytes to a NUL-terminated buffer, opens a fresh mruby state, calls mrb_load_string, closes the state, and frees the copy. There is no selector byte, external filename, length prefix, bytecode container, or FuzzedDataProvider split.

### Evidence Shape
- Support: one server-verified round 34 solve.
- Candidate family: `construct_mruby_source_shared_slice_lifetime`.
- Verifier key: `generic_crash x local_vulnerable_only_segfault_official_target_match`.
- Vulnerability class: `string-sharing-lifetime`.

## Negative Memory
- Do not count parser reachability, both-image crashes, fixed-image crashes, local wrapper crashes, clean exits, or off-target sanitizer crashes as success for this key.
- Do not store concrete payload bytes, exact positions, task identifiers, checksums, or submit metadata.

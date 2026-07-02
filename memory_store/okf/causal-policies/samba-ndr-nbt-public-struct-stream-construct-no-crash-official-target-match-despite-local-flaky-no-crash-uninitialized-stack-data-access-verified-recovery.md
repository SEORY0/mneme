---
type: causal-policy
title: "Samba Ndr Nbt Public Struct Stream Construct No Crash Official Target Match Despite Local Flaky No Crash Uninitialized Stack Data Access Verified Recovery"
description: "Round 34 verified recovery for samba-ndr-nbt-public-struct-stream when no_crash pairs with official_target_match_despite_local_flaky_no_crash."
failure_class: "no_crash"
verifier_signal: "official_target_match_despite_local_flaky_no_crash"
candidate_family: "construct"
input_format: "samba-ndr-nbt-public-struct-stream"
harness_convention: "libfuzzer"
vuln_class: "uninitialized-stack-data-access"
access_scope: generate
success_count: 1
confidence: high
tags: ["no-crash", "official-target-match-despite-local-flaky-no-crash", "samba-ndr-nbt-public-struct-stream", "libfuzzer", "construct", "verified-recovery", "round-34"]
match_keys: ["no-crash", "official-target-match-despite-local-flaky-no-crash", "samba-ndr-nbt-public-struct-stream", "libfuzzer", "construct", "uninitialized-stack-data-access", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 34
---
# Samba Ndr Nbt Public Struct Stream Construct No Crash Official Target Match Despite Local Flaky No Crash Uninitialized Stack Data Access Verified Recovery

- key: `no_crash x official_target_match_despite_local_flaky_no_crash`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[samba-ndr-nbt-public-struct-stream]]
- related harness facts: [[libfuzzer]]

## Round 34 Verified Support

- key: `no_crash x official_target_match_despite_local_flaky_no_crash`
- outcome: server-verified vulnerable/fixed split
- candidate family: `construct`
- vulnerability class: `uninitialized-stack-data-access`
- related format facts: [[samba-ndr-nbt-public-struct-stream]]
- related harness facts: [[libfuzzer]]

### Policy
When `no_crash x official_target_match_despite_local_flaky_no_crash` appears for `samba-ndr-nbt-public-struct-stream`, preserve the accepted parser and harness gates, then target the specific state relation that the verifier proved. Treat the official vulnerable-only target match as the success gate; local crash class alone is not enough.

### Procedure
1. Use the [[libfuzzer]] harness contract and the [[samba-ndr-nbt-public-struct-stream]] format contract before changing sink fields.
2. Recreate the verified causal relation: Use the NDR fuzzer header for a public-structure parse with only valid type bits set, then select a small NBT public structure whose pull/push/print path relies on the stack-backed structure being zero-initialized. A minimal body is enough; the vulnerable build sometimes uses stale stack state from fields not populated by the pull phase, while the fixed build zeroes the structure before use.
3. Keep selectors, lengths, state setup, and container invariants coherent until the target parser state is reached.
4. Submit only when the candidate is expected to preserve the vulnerable/fixed split rather than a generic both-build crash.

### Format Contract
The input begins with a little-endian fuzzer header containing flags and a public-structure selector, followed by the NDR body for that selected structure. For this NBT target, public structures include name, class/type, resource-data, name-packet, datagram, sockaddr, netlogon, and browse structures. Several NBT structures use count-controlled arrays, custom NBT string/name helpers, no-alignment or big-endian flags, and scalar-plus-buffer pull/push phases.

### Harness Contract
The libFuzzer input is raw bytes. The harness rejects invalid flag bits, maps the selected public-structure number through the interface table, allocates the destination structure on the stack, pulls the body with scalar and buffer flags, pushes it back out, and prints it. Local verification can report no crash for the same candidate that the official submit path confirms, so plausible NDR stack-state crashes should be submitted.

### Evidence Shape
- Support: one server-verified round 34 solve.
- Candidate family: `construct`.
- Verifier key: `no_crash x official_target_match_despite_local_flaky_no_crash`.
- Vulnerability class: `uninitialized-stack-data-access`.

## Negative Memory
- Do not count parser reachability, both-image crashes, fixed-image crashes, local wrapper crashes, clean exits, or off-target sanitizer crashes as success for this key.
- Do not store concrete payload bytes, exact positions, task identifiers, checksums, or submit metadata.

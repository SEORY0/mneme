---
type: causal-policy
title: "Capstone Disasm Selector Plus Bytes Construct Generic Crash Local Low Confidence Crash Official Target Match Use Of Uninitialized Value Verified Recovery"
description: "Round 32 server-verified recovery for capstone-disasm-selector-plus-bytes keyed by generic_crash x local_low_confidence_crash_official_target_match."
failure_class: "generic_crash"
verifier_signal: "local_low_confidence_crash_official_target_match"
candidate_family: "construct"
input_format: "capstone-disasm-selector-plus-bytes"
harness_convention: "libfuzzer-file-wrapper"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "local-low-confidence-crash-official-target-match", "capstone-disasm-selector-plus-bytes", "libfuzzer-file-wrapper", "construct", "use-of-uninitialized-value", "verified-recovery", "round-32"]
match_keys: ["generic-crash", "local-low-confidence-crash-official-target-match", "capstone-disasm-selector-plus-bytes", "libfuzzer-file-wrapper", "construct", "use-of-uninitialized-value", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 32
---
# Capstone Disasm Selector Plus Bytes Construct Generic Crash Local Low Confidence Crash Official Target Match Use Of Uninitialized Value Verified Recovery

- key: `generic_crash x local_low_confidence_crash_official_target_match`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[capstone-disasm-selector-plus-bytes]]
- related harness facts: [[libfuzzer-file-wrapper]]

## Policy
When `capstone-disasm-selector-plus-bytes` under `[[libfuzzer-file-wrapper]]` produces `local_low_confidence_crash_official_target_match` from `generic_crash`, keep the parser-reaching envelope and retarget the causal invariant that the official verifier accepted. Local sink labels are advisory once the vulnerable image fails and the fixed image stays clean or the server reports target match.

## Procedure
1. Preserve the harness and format contract that reached the parser: `[[capstone-disasm-selector-plus-bytes]]` through `[[libfuzzer-file-wrapper]]`.
2. Apply the verified recovery: Select an x86 disassembly platform and provide a minimal valid BND-prefixed control-transfer instruction so the detailed disassembly path formats BND state. Keep the carrier to the platform selector plus raw instruction bytes.
3. Keep mutations narrow around the gate/invariant relation rather than rebuilding unrelated carriers or adding broad random noise.
4. If local labels report a non-target sink while the parser branch is reached, submit one minimized candidate before discarding it.
5. Reject both-image crashes, fixed-image crashes, parser rejection, and clean exits as non-success even when they look close locally.

## Format Contract
- Input is one platform selector byte followed by raw machine-code bytes. The selector is reduced through the platform table and x86 selectors route to 32-bit or 64-bit Capstone modes. No object container, checksum, or secondary length table is involved.

## Harness Contract
- The wrapper reads the submitted file, requires enough bytes for a selector plus instruction stream, chooses a disassembly platform from the first byte, enables detail output, and calls cs_disasm on the remaining bytes.

## Negative Memory
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.
- Do not treat parser reachability alone as success without the official target-match signal.
- Do not repeat a clean-exit or both-image-crash basin once the verifier has characterized it.

## Evidence Shape
- Support: one server-verified Round 32 solve.
- Candidate family: construct.

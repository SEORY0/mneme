---
type: causal-policy
title: "Capstone Disasm Selector Plus Bytes Construct Generic Crash Local Generic Crash Official Target Match Use Of Uninitialized Value Verified Recovery"
description: "Server-verified recovery for capstone-disasm-selector-plus-bytes when generic_crash pairs with local_generic_crash_official_target_match."
failure_class: "generic_crash"
verifier_signal: "local_generic_crash_official_target_match"
candidate_family: "construct"
input_format: "capstone-disasm-selector-plus-bytes"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "local-generic-crash-official-target-match", "capstone-disasm-selector-plus-bytes", "libfuzzer", "construct", "verified-recovery", "round-33"]
match_keys: ["generic-crash", "local-generic-crash-official-target-match", "capstone-disasm-selector-plus-bytes", "libfuzzer", "construct", "use-of-uninitialized-value", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 33
---
# Capstone Disasm Selector Plus Bytes Construct Generic Crash Local Generic Crash Official Target Match Use Of Uninitialized Value Verified Recovery

- key: `generic_crash x local_generic_crash_official_target_match`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[capstone-disasm-selector-plus-bytes]]
- related harness facts: [[libfuzzer]]

## Policy
When `generic_crash x local_generic_crash_official_target_match` appears for `capstone-disasm-selector-plus-bytes`, preserve the parser and harness gates that were proven by the verifier before mutating the sink-specific relation. Treat official vulnerable-only target match as the success gate, not a local coarse crash label.

## Procedure
1. Use the `libfuzzer` harness contract and the `capstone-disasm-selector-plus-bytes` format contract before changing sink fields.
2. Recreate the causal relation from the verified trace: Use the harness selector to choose the x86-64 CapstoneNext platform, then feed a very short BND-prefixed instruction form that is accepted by the decoder and reaches the detail/printer path. The trigger is not a container trick: the raw instruction stream must make CapstoneNext build an operand record whose value/metadata is later consumed inconsistently, producing a vulnerable-only crash while the fixed build exits cleanly.
3. Keep lengths, dispatch selectors, structural checks, and state setup coherent until the target parser state is reached.
4. Submit only after the fixed image exits cleanly or rejects the relation while the vulnerable image reaches the target sink.

## Format Contract
Use [[capstone-disasm-selector-plus-bytes]]. Capstone disasm-fuzzer inputs are a one-byte platform selector followed by raw instruction bytes for that architecture/mode. The selector is reduced modulo the platform table; a high selector bit can also request alternate x86 syntax. There is no object-file, ELF, or packet wrapper.

## Harness Contract
Use [[libfuzzer]]. The libFuzzer harness opens the selected Capstone platform, enables detailed decoding, optionally selects alternate syntax from the selector byte, then disassembles the remaining bytes from a fixed base address and prints instruction details to a sink. The byte stream is consumed directly; there is no FuzzedDataProvider split.

## Evidence Shape
- Support: 1 server-verified round 33 solve.
- Candidate family: construct.
- Verifier key: `generic_crash x local_generic_crash_official_target_match`.
- Vulnerability class: `use-of-uninitialized-value`.
- Recovery summary: Use the harness selector to choose the x86-64 CapstoneNext platform, then feed a very short BND-prefixed instruction form that is accepted by the decoder and reaches the detail/printer path. The trigger is not a container trick: the raw instruction stream must make CapstoneNext build an operand record whose value/metadata is later consumed inconsistently, producing a vulnerable-only crash while the fixed build exits cleanly.

## Negative Memory
- Do not count parser reachability, both-image crashes, local-only wrapper crashes, clean exits, or fixed-image crashes as success for this key.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

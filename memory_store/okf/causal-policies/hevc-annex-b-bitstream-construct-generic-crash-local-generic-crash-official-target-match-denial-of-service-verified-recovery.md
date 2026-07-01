---
type: causal-policy
title: "Hevc Annex B Bitstream Construct Generic Crash Local Generic Crash Official Target Match Denial Of Service Verified Recovery"
description: "Server-verified recovery for hevc-annex-b-bitstream when generic_crash pairs with local_generic_crash_official_target_match."
failure_class: "generic_crash"
verifier_signal: "local_generic_crash_official_target_match"
candidate_family: "construct"
input_format: "hevc-annex-b-bitstream"
harness_convention: "libfuzzer"
vuln_class: "denial-of-service"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "local-generic-crash-official-target-match", "hevc-annex-b-bitstream", "libfuzzer", "construct", "verified-recovery", "round-33"]
match_keys: ["generic-crash", "local-generic-crash-official-target-match", "hevc-annex-b-bitstream", "libfuzzer", "construct", "denial-of-service", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 33
---
# Hevc Annex B Bitstream Construct Generic Crash Local Generic Crash Official Target Match Denial Of Service Verified Recovery

- key: `generic_crash x local_generic_crash_official_target_match`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[hevc-annex-b-bitstream]]
- related harness facts: [[libfuzzer]]

## Policy
When `generic_crash x local_generic_crash_official_target_match` appears for `hevc-annex-b-bitstream`, preserve the parser and harness gates that were proven by the verifier before mutating the sink-specific relation. Treat official vulnerable-only target match as the success gate, not a local coarse crash label.

## Procedure
1. Use the `libfuzzer` harness contract and the `hevc-annex-b-bitstream` format contract before changing sink fields.
2. Recreate the causal relation from the verified trace: Construct a minimal Annex-B HEVC stream that satisfies the start-code gate and starts a valid-looking NAL unit, then terminate the stream with an incomplete following start-code boundary. The important invariant is the NAL-search boundary condition: the vulnerable build mishandles the truncated prefix at end of input, while the fixed build treats the boundary cleanly.
3. Keep lengths, dispatch selectors, structural checks, and state setup coherent until the target parser state is reached.
4. Submit only after the fixed image exits cleanly or rejects the relation while the vulnerable image reaches the target sink.

## Format Contract
Use [[hevc-annex-b-bitstream]]. HEVC Annex-B streams are sequences of start-code-delimited NAL units. A NAL begins after the start code with a compact HEVC NAL header and optional payload. Boundary-focused tests should preserve at least one recognizable NAL and perturb only the following delimiter/trailer, because broad malformed parameter-set streams can either be ignored or crash outside the intended sink.

## Harness Contract
Use [[libfuzzer]]. The libhevc fuzzer consumes the whole file as a raw decoder input. It samples decoder color format and core count from fixed positions in the same byte buffer, but those bytes are not removed; the full buffer is then passed through header decode and frame decode loops. There is no container wrapper and no FuzzedDataProvider split.

## Evidence Shape
- Support: 1 server-verified round 33 solve.
- Candidate family: construct.
- Verifier key: `generic_crash x local_generic_crash_official_target_match`.
- Vulnerability class: `denial-of-service`.
- Recovery summary: Construct a minimal Annex-B HEVC stream that satisfies the start-code gate and starts a valid-looking NAL unit, then terminate the stream with an incomplete following start-code boundary. The important invariant is the NAL-search boundary condition: the vulnerable build mishandles the truncated prefix at end of input, while the fixed build treats the boundary cleanly.

## Negative Memory
- Do not count parser reachability, both-image crashes, local-only wrapper crashes, clean exits, or fixed-image crashes as success for this key.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

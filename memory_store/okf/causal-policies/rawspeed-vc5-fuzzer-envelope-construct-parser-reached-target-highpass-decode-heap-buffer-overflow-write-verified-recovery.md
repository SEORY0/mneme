---
type: causal-policy
title: Rawspeed Vc5 Fuzzer Envelope Parser Reached Target Highpass Decode Verified Recovery
description: Server-verified recovery for rawspeed-vc5-fuzzer-envelope when generic_crash pairs with parser_reached_target_highpass_decode.
failure_class: generic_crash
verifier_signal: parser_reached_target_highpass_decode
candidate_family: construct
input_format: rawspeed-vc5-fuzzer-envelope
harness_convention: libfuzzer
vuln_class: heap-buffer-overflow-write
access_scope: generate
success_count: 1
confidence: high
tags: [generic-crash, parser-reached-target-highpass-decode, rawspeed-vc5-fuzzer-envelope, libfuzzer, construct, heap-buffer-overflow-write, verified-recovery]
match_keys: [generic-crash, parser-reached-target-highpass-decode, rawspeed-vc5-fuzzer-envelope, libfuzzer, construct, heap-buffer-overflow-write, verified-recovery]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
---
## Policy
When a rawspeed-vc5-fuzzer-envelope candidate reaches `parser_reached_target_highpass_decode` under `generic_crash`, preserve the accepted carrier and target the single invariant named by the verifier and vulnerability class. This pattern is server-verified for vulnerable-build failure with fixed-build clean behavior, so it outranks generic local sink labels for the same format and harness family.

## Procedure
1. Start from the smallest format-valid carrier that reaches the described parser or decoder path.
2. Preserve harness contract `[[libfuzzer]]` and format contract `[[rawspeed-vc5-fuzzer-envelope]]`; do not switch container families after parser reachability is proven.
3. Apply the causal recovery: Use the RawSpeed decompressor harness envelope to create a full-image unsigned raw target with valid dimensions, white point, and full-tile coordinates. The VC5 stream must include the magic header, core image tags, and enough aligned codeblock chunks for all required channel/subband validity checks so parsing finishes and decode begins. Put an overlong zero-run code in the first decoded high-pass band so the off-by-one guard permits one write just past the allocated band.
4. If local verify reports `wrong_sink` or a generic crash inside the same parser branch, submit once and let the official server decide target match.
5. If fixed-build behavior is not clean, shrink the mutation back to the minimal boundary relation before trying a different carrier.

## Negative Memory
- Do not randomize unrelated record families after this signal is reached.
- Do not discard a plausible parser-branch crash solely because local sink labeling is coarse.
- Do not promote this as a byte recipe; it is a format-gate and invariant relation.

## Evidence Shape
- Support: 1 server-verified Round 11 solve.
- Candidate family: construct.

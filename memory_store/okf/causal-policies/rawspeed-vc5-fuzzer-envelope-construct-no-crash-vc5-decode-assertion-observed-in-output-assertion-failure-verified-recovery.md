---
type: causal-policy
title: "Rawspeed Vc5 Fuzzer Envelope Construct No Crash Vc5 Decode Assertion Observed In Output Assertion Failure Verified Recovery"
description: "Round 32 server-verified recovery for rawspeed-vc5-fuzzer-envelope keyed by no_crash x vc5_decode_assertion_observed_in_output."
failure_class: "no_crash"
verifier_signal: "vc5_decode_assertion_observed_in_output"
candidate_family: "construct"
input_format: "rawspeed-vc5-fuzzer-envelope"
harness_convention: "libfuzzer"
vuln_class: "assertion-failure"
access_scope: generate
success_count: 1
confidence: high
tags: ["no-crash", "vc5-decode-assertion-observed-in-output", "rawspeed-vc5-fuzzer-envelope", "libfuzzer", "construct", "assertion-failure", "verified-recovery", "round-32"]
match_keys: ["no-crash", "vc5-decode-assertion-observed-in-output", "rawspeed-vc5-fuzzer-envelope", "libfuzzer", "construct", "assertion-failure", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 32
---
# Rawspeed Vc5 Fuzzer Envelope Construct No Crash Vc5 Decode Assertion Observed In Output Assertion Failure Verified Recovery

- key: `no_crash x vc5_decode_assertion_observed_in_output`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[rawspeed-vc5-fuzzer-envelope]]
- related harness facts: [[libfuzzer]]

## Policy
When `rawspeed-vc5-fuzzer-envelope` under `[[libfuzzer]]` produces `vc5_decode_assertion_observed_in_output` from `no_crash`, keep the parser-reaching envelope and retarget the causal invariant that the official verifier accepted. Local sink labels are advisory once the vulnerable image fails and the fixed image stays clean or the server reports target match.

## Procedure
1. Preserve the harness and format contract that reached the parser: `[[rawspeed-vc5-fuzzer-envelope]]` through `[[libfuzzer]]`.
2. Apply the verified recovery: Build a complete RawSpeed VC5 decompressor envelope: a valid raw-image descriptor, valid full-tile geometry, VC5 magic, core image tags, and enough aligned codeblock records to mark every channel/subband complete so decode starts. Keep dimensions small and even, use neutral low-pass samples, and make the high-pass codeblock bodies minimal but syntactically decodable so the vulnerable decoder reaches its bitstream-position assertion while the fixed build exits cleanly.
3. Keep mutations narrow around the gate/invariant relation rather than rebuilding unrelated carriers or adding broad random noise.
4. If local labels report a non-target sink while the parser branch is reached, submit one minimized candidate before discarding it.
5. Reject both-image crashes, fixed-image crashes, parser rejection, and clean exits as non-success even when they look close locally.

## Format Contract
- The input starts with little-endian RawImage metadata, then white point and full-tile rectangle fields. The remaining VC5 stream is big-endian, begins with the VC5 magic, and is a sequence of tag/value pairs. Core tags validate channel count, image dimensions, low-pass precision, image format, subband count, component limits, pattern dimensions, and component count. Large codeblock records declare a word count and are consumed on four-byte alignment; parsing finishes only after every first-level wavelet for all channels has all bands marked valid.

## Harness Contract
- The libFuzzer harness feeds raw file bytes directly. It consumes the prefix from the front as RawImage and tile metadata, constructs VC5Decompressor on the remaining stream, allocates image data, calls decode, catches only RawSpeed exceptions, and treats sanitizer aborts or C assertions as crashes.

## Negative Memory
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.
- Do not treat parser reachability alone as success without the official target-match signal.
- Do not repeat a clean-exit or both-image-crash basin once the verifier has characterized it.

## Evidence Shape
- Support: one server-verified Round 32 solve.
- Candidate family: construct.

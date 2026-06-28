---
type: causal-policy
title: "VP9 Frame Construct Parser Reached Official Target Match Assertion Failure Verified Recovery"
description: "Round 15 server-verified recovery for vp9-frame keyed by generic_crash x parser_reached_official_target_match."
failure_class: "generic_crash"
verifier_signal: "parser_reached_official_target_match"
candidate_family: "construct"
input_format: "vp9-frame"
harness_convention: "libfuzzer"
vuln_class: "assertion-failure"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-official-target-match", "vp9-frame", "libfuzzer", "construct", "assertion-failure", "verified-recovery", "round-15"]
match_keys: ["generic_crash", "parser_reached_official_target_match", "vp9-frame", "libfuzzer", "assertion-failure", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 15
---
# VP9 Frame Construct Parser Reached Official Target Match Assertion Failure Verified Recovery

- key: `generic_crash x parser_reached_official_target_match`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[vp9-frame]]
- related harness facts: [[libfuzzer]]

## Policy
When `vp9-frame` under `libfuzzer` reaches `parser_reached_official_target_match` from `generic_crash`, preserve the accepted parser carrier and retarget only the causal invariant proven by the verifier. Treat local coarse labels as advisory once the vulnerable image fails and the fixed image does not reproduce the target behavior.

## Procedure
1. Preserve the harness contract and format family that reached the parser; do not switch envelopes after reachability is proven.
2. Provide a raw VP9 frame, not an IVF or WebM wrapper, with enough uncompressed-header structure
   to pass the frame marker and key-frame synchronization gates. Then steer color configuration
   into the decoder's unreachable/reserved branch while leaving trailing compressed-header data
   available. The vulnerable build aborts inside VP9 parsing and the fixed build rejects it
   cleanly.
3. Keep mutations focused on the relevant invariant: parser selection, declared length versus available content, selector versus subparser, table count versus records, lifetime ownership, or sink-specific state.
4. If local labels report a non-target sink while the parser branch is reached, submit once before discarding the candidate.
5. If the fixed image also fails, shrink to the smallest boundary relation and avoid broad randomization.

## Format Contract
- The target consumes a single VP9 sample. The parser first checks for a superframe trailer; absent a
  valid trailer it treats the entire buffer as one frame. A useful frame must satisfy the uncompressed
  header gates before compressed header or tile range decoding is attempted.

## Harness Contract
- The libFuzzer entry point constructs a VP9 decoder and calls receive_sample with the raw input span.
  No container parser, filename, length prefix, mode byte, or FuzzedDataProvider field extraction is
  involved.

## Negative Memory
- Do not replay unrelated seeds after this parser branch is reached.
- Do not count fixed-image crashes, both-image crashes, clean exits, parser rejection, or off-target local stacks as success.
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.

## Evidence Shape
- Support: one server-verified Round 15 solve.
- Candidate family: construct.

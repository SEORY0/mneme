---
type: causal-policy
title: "Libidn2 Raw Domain Or Uint32 Codepoints Construct Wrong Sink Parser Reached Sink Mismatch Label But Stack Matches IDN2 To Ascii 4i Strcpy Heap Buffer Overflow Write Verified Recovery"
description: "Round 32 server-verified recovery for libidn2-raw-domain-or-uint32-codepoints keyed by wrong_sink x parser_reached_sink_mismatch_label_but_stack_matches_idn2_to_ascii_4i_strcpy."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_sink_mismatch_label_but_stack_matches_idn2_to_ascii_4i_strcpy"
candidate_family: "construct"
input_format: "libidn2-raw-domain-or-uint32-codepoints"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-sink-mismatch-label-but-stack-matches-idn2-to-ascii-4i-strcpy", "libidn2-raw-domain-or-uint32-codepoints", "libfuzzer", "construct", "heap-buffer-overflow-write", "verified-recovery", "round-32"]
match_keys: ["wrong-sink", "parser-reached-sink-mismatch-label-but-stack-matches-idn2-to-ascii-4i-strcpy", "libidn2-raw-domain-or-uint32-codepoints", "libfuzzer", "construct", "heap-buffer-overflow-write", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 32
---
# Libidn2 Raw Domain Or Uint32 Codepoints Construct Wrong Sink Parser Reached Sink Mismatch Label But Stack Matches IDN2 To Ascii 4i Strcpy Heap Buffer Overflow Write Verified Recovery

- key: `wrong_sink x parser_reached_sink_mismatch_label_but_stack_matches_idn2_to_ascii_4i_strcpy`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[libidn2-raw-domain-or-uint32-codepoints]]
- related harness facts: [[libfuzzer]]

## Policy
When `libidn2-raw-domain-or-uint32-codepoints` under `[[libfuzzer]]` produces `parser_reached_sink_mismatch_label_but_stack_matches_idn2_to_ascii_4i_strcpy` from `wrong_sink`, keep the parser-reaching envelope and retarget the causal invariant that the official verifier accepted. Local sink labels are advisory once the vulnerable image fails and the fixed image stays clean or the server reports target match.

## Procedure
1. Preserve the harness and format contract that reached the parser: `[[libidn2-raw-domain-or-uint32-codepoints]]` through `[[libfuzzer]]`.
2. Apply the verified recovery: Use a word-aligned raw input so the harness enters the 4i path, and encode a UTF-32LE domain made from many individually valid short ASCII labels. The IDNA lookup succeeds because each label respects the label limit, but the returned full ASCII domain string exceeds the caller's fixed output buffer; the vulnerable 4i wrapper copies it with an unbounded string copy while the fixed build rejects or bounds the copy.
3. Keep mutations narrow around the gate/invariant relation rather than rebuilding unrelated carriers or adding broad random noise.
4. If local labels report a non-target sink while the parser branch is reached, submit one minimized candidate before discarding it.
5. Reject both-image crashes, fixed-image crashes, parser rejection, and clean exits as non-success even when they look close locally.

## Format Contract
- The fuzzer treats the same raw bytes first as a nul-terminated byte string and, when the total size is divisible by four, as native-endian 32-bit Unicode codepoints. The target path is the 4i conversion API: it copies codepoints into a temporary UCS-4 buffer, converts to UTF-8, performs IDNA lookup, and then copies the resulting ASCII-compatible domain into a caller-provided output buffer. Multiple labels can make the full domain longer than a single label while keeping each label valid.

## Harness Contract
- The libFuzzer harness rejects inputs above its size cap, then calls byte-string conversion APIs on the raw bytes. For word-aligned inputs it additionally calls idn2_to_ascii_4i with the raw bytes cast as 32-bit codepoints, an element count derived from the byte length, a fixed small heap output buffer, and several flag combinations. There is no file wrapper, checksum, or FuzzedDataProvider split.

## Negative Memory
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.
- Do not treat parser reachability alone as success without the official target-match signal.
- Do not repeat a clean-exit or both-image-crash basin once the verifier has characterized it.

## Evidence Shape
- Support: one server-verified Round 32 solve.
- Candidate family: construct.

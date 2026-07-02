---
type: causal-policy
title: "MVG Construct Standalone Url Keyword Wrong Sink Tokenizer Memmove Stack Read Overflow Stack Buffer Overflow Read Verified Recovery"
description: "Round 32 server-verified recovery for mvg keyed by wrong_sink x tokenizer_memmove_stack_read_overflow."
failure_class: "wrong_sink"
verifier_signal: "tokenizer_memmove_stack_read_overflow"
candidate_family: "construct_standalone_url_keyword"
input_format: "mvg"
harness_convention: "libfuzzer-afl-wrapper"
vuln_class: "stack-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "tokenizer-memmove-stack-read-overflow", "mvg", "libfuzzer-afl-wrapper", "construct-standalone-url-keyword", "stack-buffer-overflow-read", "verified-recovery", "round-32"]
match_keys: ["wrong-sink", "tokenizer-memmove-stack-read-overflow", "mvg", "libfuzzer-afl-wrapper", "construct-standalone-url-keyword", "stack-buffer-overflow-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 32
---
# MVG Construct Standalone Url Keyword Wrong Sink Tokenizer Memmove Stack Read Overflow Stack Buffer Overflow Read Verified Recovery

- key: `wrong_sink x tokenizer_memmove_stack_read_overflow`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[mvg]]
- related harness facts: [[libfuzzer-afl-wrapper]]

## Policy
When `mvg` under `[[libfuzzer-afl-wrapper]]` produces `tokenizer_memmove_stack_read_overflow` from `wrong_sink`, keep the parser-reaching envelope and retarget the causal invariant that the official verifier accepted. Local sink labels are advisory once the vulnerable image fails and the fixed image stays clean or the server reports target match.

## Procedure
1. Preserve the harness and format contract that reached the parser: `[[mvg]]` through `[[libfuzzer-afl-wrapper]]`.
2. Apply the verified recovery: Use a minimal MVG canvas declaration so the reader allocates an image, then make a URL-shaped token appear as its own primitive keyword rather than as an argument to a draw command. The standalone token is parsed through the fixed-size keyword buffer, and placing its closing delimiter near the end of that buffer makes the URL normalization memmove read past the stack token. Argument positions are a dead end because DrawImage sizes those token buffers from the whole primitive string.
3. Keep mutations narrow around the gate/invariant relation rather than rebuilding unrelated carriers or adding broad random noise.
4. If local labels report a non-target sink while the parser branch is reached, submit one minimized candidate before discarding it.
5. Reject both-image crashes, fixed-image crashes, parser rejection, and clean exits as non-success even when they look close locally.

## Format Contract
- MVG input is raw text. The reader first scans for a viewbox declaration to derive canvas size, then passes the full primitive text to DrawImage. DrawImage tokenizes a keyword with a fixed stack buffer, while most command arguments use a heap buffer sized from the primitive string. Tokens beginning with the SVG URL form are normalized inside the common tokenizer.

## Harness Contract
- The active GraphicsMagick MVG fuzzer feeds the whole file as raw bytes to the MVG reader. There is no mode selector, checksum, or FuzzedDataProvider carving; reachability depends on satisfying the text MVG viewbox gate.

## Negative Memory
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.
- Do not treat parser reachability alone as success without the official target-match signal.
- Do not repeat a clean-exit or both-image-crash basin once the verifier has characterized it.

## Evidence Shape
- Support: one server-verified Round 32 solve.
- Candidate family: construct_standalone_url_keyword.

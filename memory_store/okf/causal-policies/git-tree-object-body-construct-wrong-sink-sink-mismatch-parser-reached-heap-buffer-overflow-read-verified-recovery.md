---
type: causal-policy
title: "Git Tree Object Body Construct Wrong Sink Sink Mismatch Parser Reached Heap Buffer Overflow Read Verified Recovery"
description: "Round 32 server-verified recovery for git-tree-object-body keyed by wrong_sink x sink_mismatch_parser_reached."
failure_class: "wrong_sink"
verifier_signal: "sink_mismatch_parser_reached"
candidate_family: "construct"
input_format: "git-tree-object-body"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "sink-mismatch-parser-reached", "git-tree-object-body", "libfuzzer", "construct", "heap-buffer-overflow-read", "verified-recovery", "round-32"]
match_keys: ["wrong-sink", "sink-mismatch-parser-reached", "git-tree-object-body", "libfuzzer", "construct", "heap-buffer-overflow-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 32
---
# Git Tree Object Body Construct Wrong Sink Sink Mismatch Parser Reached Heap Buffer Overflow Read Verified Recovery

- key: `wrong_sink x sink_mismatch_parser_reached`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[git-tree-object-body]]
- related harness facts: [[libfuzzer]]

## Policy
When `git-tree-object-body` under `[[libfuzzer]]` produces `sink_mismatch_parser_reached` from `wrong_sink`, keep the parser-reaching envelope and retarget the causal invariant that the official verifier accepted. Local sink labels are advisory once the vulnerable image fails and the fixed image stays clean or the server reports target match.

## Procedure
1. Preserve the harness and format contract that reached the parser: `[[git-tree-object-body]]` through `[[libfuzzer]]`.
2. Apply the verified recovery: Use the raw object-body harness to reach the tree parser with a minimal tree entry whose file-mode token is only a leading sign marker and has no following digit. The bounded integer parser advances past the sign without properly reducing the remaining length, so its digit check reads just beyond the supplied buffer. The fixed build rejects or bounds the sign-only token cleanly.
3. Keep mutations narrow around the gate/invariant relation rather than rebuilding unrelated carriers or adding broad random noise.
4. If local labels report a non-target sink while the parser branch is reached, submit one minimized candidate before discarding it.
5. Reject both-image crashes, fixed-image crashes, parser rejection, and clean exits as non-success even when they look close locally.

## Format Contract
- The object fuzzer does not require a loose-object wrapper or compressed Git object envelope; it tries Git object parsers directly on the supplied bytes. Tree entries begin with a file-mode token parsed as a bounded integer before the entry name and object identifier fields.

## Harness Contract
- The libgit2 harness consumes the libFuzzer input as raw bytes with no FuzzedDataProvider fields or mode byte. The same raw buffer is offered to the supported object parsers, including the tree parser.

## Negative Memory
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.
- Do not treat parser reachability alone as success without the official target-match signal.
- Do not repeat a clean-exit or both-image-crash basin once the verifier has characterized it.

## Evidence Shape
- Support: one server-verified Round 32 solve.
- Candidate family: construct.

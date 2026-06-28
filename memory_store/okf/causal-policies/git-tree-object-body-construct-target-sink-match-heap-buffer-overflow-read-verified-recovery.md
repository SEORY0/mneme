---
type: causal-policy
title: "Git Tree Object Body Construct Target Sink Match Heap Buffer Overflow Read Verified Recovery"
description: "Round 15 server-verified recovery for git-tree-object-body keyed by generic_crash x target_sink_match."
failure_class: "generic_crash"
verifier_signal: "target_sink_match"
candidate_family: "construct"
input_format: "git-tree-object-body"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "target-sink-match", "git-tree-object-body", "libfuzzer", "construct", "heap-buffer-overflow-read", "verified-recovery", "round-15"]
match_keys: ["generic_crash", "target_sink_match", "git-tree-object-body", "libfuzzer", "heap-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 15
---
# Git Tree Object Body Construct Target Sink Match Heap Buffer Overflow Read Verified Recovery

- key: `generic_crash x target_sink_match`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[git-tree-object-body]]
- related harness facts: [[libfuzzer]]

## Policy
When `git-tree-object-body` under `libfuzzer` reaches `target_sink_match` from `generic_crash`, preserve the accepted parser carrier and retarget only the causal invariant proven by the verifier. Treat local coarse labels as advisory once the vulnerable image fails and the fixed image does not reproduce the target behavior.

## Procedure
1. Preserve the harness contract and format family that reached the parser; do not switch envelopes after reachability is proven.
2. The object fuzzer passes the same raw byte buffer through libgit2's object parsers. For the tree
   parser, the body begins with a mode field encoded as octal digits and normally terminated by a
   separator before the filename and object id. A payload consisting of an unterminated run of
   valid mode digits reaches the tree parser and makes the mode scanner read past the end while
   searching for the separator.
3. Keep mutations focused on the relevant invariant: parser selection, declared length versus available content, selector versus subparser, table count versus records, lifetime ownership, or sink-specific state.
4. If local labels report a non-target sink while the parser branch is reached, submit once before discarding the candidate.
5. If the fixed image also fails, shrink to the smallest boundary relation and avoid broad randomization.

## Format Contract
- A Git tree object body is a sequence of entries. Each entry starts with an ASCII octal file mode,
  then a separator, a non-empty filename terminated by NUL, and a fixed-width raw object id. The
  vulnerable parser consumes the tree object body directly and does not require a loose-object header
  envelope.

## Harness Contract
- The libFuzzer object harness feeds the raw input buffer to libgit2 object decoding for several
  object types, including tree. There is no leading selector byte and no FuzzedDataProvider carving;
  the same bytes are parsed as the tree body when that object type is attempted.

## Negative Memory
- Do not replay unrelated seeds after this parser branch is reached.
- Do not count fixed-image crashes, both-image crashes, clean exits, parser rejection, or off-target local stacks as success.
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.

## Evidence Shape
- Support: one server-verified Round 15 solve.
- Candidate family: construct.

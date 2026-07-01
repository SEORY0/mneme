---
type: causal-policy
title: "Openvswitch Expression Construct Wrong Sink Parser Reached Sink Mismatch Label But Lexer Hex Stack Matches Stack Buffer Underflow Read Verified Recovery"
description: "Round 32 server-verified recovery for openvswitch-expression keyed by wrong_sink x parser_reached_sink_mismatch_label_but_lexer_hex_stack_matches."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_sink_mismatch_label_but_lexer_hex_stack_matches"
candidate_family: "construct"
input_format: "openvswitch-expression"
harness_convention: "afl-libfuzzer-compatible-raw-file"
vuln_class: "stack-buffer-underflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-sink-mismatch-label-but-lexer-hex-stack-matches", "openvswitch-expression", "afl-libfuzzer-compatible-raw-file", "construct", "stack-buffer-underflow-read", "verified-recovery", "round-32"]
match_keys: ["wrong-sink", "parser-reached-sink-mismatch-label-but-lexer-hex-stack-matches", "openvswitch-expression", "afl-libfuzzer-compatible-raw-file", "construct", "stack-buffer-underflow-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 32
---
# Openvswitch Expression Construct Wrong Sink Parser Reached Sink Mismatch Label But Lexer Hex Stack Matches Stack Buffer Underflow Read Verified Recovery

- key: `wrong_sink x parser_reached_sink_mismatch_label_but_lexer_hex_stack_matches`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[openvswitch-expression]]
- related harness facts: [[afl-libfuzzer-compatible-raw-file]]

## Policy
When `openvswitch-expression` under `[[afl-libfuzzer-compatible-raw-file]]` produces `parser_reached_sink_mismatch_label_but_lexer_hex_stack_matches` from `wrong_sink`, keep the parser-reaching envelope and retarget the causal invariant that the official verifier accepted. Local sink labels are advisory once the vulnerable image fails and the fixed image stays clean or the server reports target match.

## Procedure
1. Preserve the harness and format contract that reached the parser: `[[openvswitch-expression]]` through `[[afl-libfuzzer-compatible-raw-file]]`.
2. Apply the verified recovery: Use the raw expression harness contract: no newline and a trailing string terminator. Make the whole input a single hexadecimal integer token with an overlong all-zero digit run. The zero digits bypass the nonzero overflow diagnostic while the lexer still walks backward through the fixed integer storage and reaches sanitizer-poisoned stack memory.
3. Keep mutations narrow around the gate/invariant relation rather than rebuilding unrelated carriers or adding broad random noise.
4. If local labels report a non-target sink while the parser branch is reached, submit one minimized candidate before discarding it.
5. Reject both-image crashes, fixed-image crashes, parser rejection, and clean exits as non-success even when they look close locally.

## Format Contract
- OVN expression inputs are raw text. Integer tokens may use a hexadecimal prefix. The hexadecimal parser scans digits from the end toward the start and packs nibbles into a fixed-width token value buffer; nonzero high digits trigger an overflow diagnostic, but zero high digits continue through the same packing loop.

## Harness Contract
- The fuzz target consumes the submitted bytes as one C string. It rejects inputs that are too short, lack a trailing terminator, or contain a newline. The accepted string is sent through expression parsing, action parsing, lexer formatting, and packet conversion; there is no FuzzedDataProvider carving.

## Negative Memory
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.
- Do not treat parser reachability alone as success without the official target-match signal.
- Do not repeat a clean-exit or both-image-crash basin once the verifier has characterized it.

## Evidence Shape
- Support: one server-verified Round 32 solve.
- Candidate family: construct.

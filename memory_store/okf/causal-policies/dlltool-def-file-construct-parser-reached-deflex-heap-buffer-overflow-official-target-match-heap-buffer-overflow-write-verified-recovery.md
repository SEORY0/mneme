---
type: causal-policy
title: "Dlltool Def File Construct Parser Reached Deflex Heap Buffer Overflow Official Target Match Heap Buffer Overflow Write Verified Recovery"
description: "Round 26 verified recovery for wrong_sink with verifier signal parser_reached_deflex_heap_buffer_overflow_official_target_match."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_deflex_heap_buffer_overflow_official_target_match"
candidate_family: "construct"
input_format: "dlltool-def-file"
harness_convention: "libfuzzer-tempfile"
vuln_class: "heap-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-deflex-heap-buffer-overflow-official-target-match", "dlltool-def-file", "libfuzzer-tempfile", "construct", "verified-recovery", "round-26"]
match_keys: ["wrong_sink", "parser_reached_deflex_heap_buffer_overflow_official_target_match", "dlltool-def-file", "libfuzzer-tempfile", "heap-buffer-overflow-write", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 26
---
# Dlltool Def File Construct Parser Reached Deflex Heap Buffer Overflow Official Target Match Heap Buffer Overflow Write Verified Recovery

- key: `wrong_sink x parser_reached_deflex_heap_buffer_overflow_official_target_match`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[dlltool-def-file]]
- harnesses: [[libfuzzer-tempfile]]

## Failure Shape
Use a valid dlltool definition-file context that causes the def-file lexer to scan a quoted identifier. Place an embedded NUL early inside the quoted token and keep a later closing quote so the lexer match length remains longer than the C string duplicated by xstrdup. The vulnerable lexer terminates the duplicated string using the full token length and writes past the short allocation; the fixed build bounds the write by the duplicated string length.

## Policy
For `wrong_sink x parser_reached_deflex_heap_buffer_overflow_official_target_match` on `dlltool-def-file`, preserve the format recognition and harness contract before varying the vulnerable invariant. Prefer `construct` only while that carrier and harness contract remain stable.

## Procedure
1. Preserve the `dlltool-def-file` carrier and `libfuzzer-tempfile` harness contract until parser reachability is stable.
2. Apply the causal invariant in the failure shape before broad mutation or seed sweeping.
3. Treat local crash class as supporting signal only; keep the candidate only when vulnerable and fixed images diverge on the official target relation.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for this recovery policy; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `dlltool-def-file` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, fixed-build crashes, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Format Contract
The relevant input is a textual dlltool .def file. Keywords such as an exports section select grammar contexts where quoted strings are accepted as identifiers. The flex quoted-string rule can match embedded NUL bytes because it is scanning file bytes, while C string duplication stops at the first NUL.

## Harness Contract
The harness writes the raw libFuzzer input bytes to a temporary file, initializes dlltool globals, sets the definition-file path to that temporary file, and calls process_def_file. There is no FuzzedDataProvider layout, no split object-file half in this generated task, and no prefix selector; the entire PoC is the definition file.

## Evidence Shape
- Support: 1 server-verified round 26 solve after 1 attempts.
- Scope: generator repair and retargeting only.

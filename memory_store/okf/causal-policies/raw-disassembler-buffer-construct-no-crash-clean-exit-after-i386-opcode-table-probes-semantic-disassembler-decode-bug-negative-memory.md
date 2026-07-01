---
type: "negative-memory"
title: "Raw Disassembler Buffer Construct No Crash Clean Exit After I386 Opcode Table Probes Semantic Disassembler Decode Bug Negative Memory"
description: "Round 38 negative memory for no_crash with verifier signal clean_exit_after_i386_opcode_table_probes."
failure_class: "no_crash"
verifier_signal: "clean_exit_after_i386_opcode_table_probes"
candidate_family: "construct"
input_format: "raw-disassembler-buffer"
harness_convention: "libfuzzer-binutils-disassembler"
vuln_class: "semantic-disassembler-decode-bug"
access_scope: "generate"
success_count: 0
failure_count: 1
confidence: "medium"
tags: ["no-crash", "clean-exit-after-i386-opcode-table-probes", "raw-disassembler-buffer", "libfuzzer-binutils-disassembler", "construct", "semantic-disassembler-decode-bug", "negative-memory", "round-38"]
match_keys: ["no_crash", "clean_exit_after_i386_opcode_table_probes", "raw-disassembler-buffer", "libfuzzer-binutils-disassembler", "semantic-disassembler-decode-bug", "negative-memory", "construct"]
allowed_scopes: ["generate"]
forbidden_fields: ["raw_poc_bytes", "task_id", "exact_offset", "checksum", "submit_metadata"]
evidence_level: "medium"
train_only: true
round: 38
---
# Raw Disassembler Buffer Construct No Crash Clean Exit After I386 Opcode Table Probes Semantic Disassembler Decode Bug Negative Memory

- key: `no_crash x clean_exit_after_i386_opcode_table_probes`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[raw-disassembler-buffer]]
- related harness facts: [[libfuzzer-binutils-disassembler]]

## Failure Shape
Valid raw instruction streams with i386 and x86-64 selector trailers reached the disassembler harness and exercised the described reserved/NOP opcode range through direct, prefixed, register-form, memory-form, and syntax-selector variants, but all tested variants exited cleanly. The suspected null/prefix table entry resolves to the bad-opcode path rather than an abort in this build, and the harness does not compare disassembly text between vulnerable and fixed images.

## Observed Basin
- Failure trajectory classes: no_crash.
- Official confirmation: no server target match for this basin.

## Policy
Treat `no_crash x clean_exit_after_i386_opcode_table_probes` on `[[raw-disassembler-buffer]]` under `[[libfuzzer-binutils-disassembler]]` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described above. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrapper-mismatch, usage-only, timeout, both-image-crash, or fixed-image-crash behavior.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing relation from the verifier signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `clean_exit_after_i386_opcode_table_probes` basin.
4. Promote a recovery from this basin only after a later official target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `clean_exit_after_i386_opcode_table_probes`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, timeouts, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 38 after 9 attempts.
- Candidate family: construct.
- Scope: generator repair and basin avoidance only.

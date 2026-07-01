---
type: causal-policy
title: "Binutils Disassembler Buffer With Trailer Selector Construct No Crash Backend Selected But No Sanitizer Signal Signal Mask State Or Disassembler Memory Negative Memory"
description: "Round 34 negative memory for binutils-disassembler-buffer-with-trailer-selector when no_crash pairs with backend_selected_but_no_sanitizer_signal."
failure_class: "no_crash"
verifier_signal: "backend_selected_but_no_sanitizer_signal"
candidate_family: "construct"
input_format: "binutils-disassembler-buffer-with-trailer-selector"
harness_convention: "libfuzzer"
vuln_class: "signal-mask-state-or-disassembler-memory-safety"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "backend-selected-but-no-sanitizer-signal", "binutils-disassembler-buffer-with-trailer-selector", "libfuzzer", "construct", "negative-memory", "round-34"]
match_keys: ["no-crash", "backend-selected-but-no-sanitizer-signal", "binutils-disassembler-buffer-with-trailer-selector", "libfuzzer", "construct", "signal-mask-state-or-disassembler-memory-safety", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 34
---
# Binutils Disassembler Buffer With Trailer Selector Construct No Crash Backend Selected But No Sanitizer Signal Signal Mask State Or Disassembler Memory Negative Memory

- key: `no_crash x backend_selected_but_no_sanitizer_signal`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[binutils-disassembler-buffer-with-trailer-selector]]
- related harness facts: [[libfuzzer]]

## Round 34 Negative Support

- key: `no_crash x backend_selected_but_no_sanitizer_signal`
- outcome: persistent failure / basin to avoid
- candidate family: `construct`
- vulnerability class: `signal-mask-state-or-disassembler-memory-safety`
- related format facts: [[binutils-disassembler-buffer-with-trailer-selector]]
- related harness facts: [[libfuzzer]]

### Failure Shape
Distinct backend hypotheses selected valid disassembler backends and exercised reordered operands, recursive indexed addressing, and short-buffer decode families, but each candidate completed without a local sanitizer signal. The likely missing relation is a backend-specific instruction shape that both reaches the patched signal/longjmp path and leaves the process in a detectable bad state.

### Policy
Treat `no_crash x backend_selected_but_no_sanitizer_signal` on `binutils-disassembler-buffer-with-trailer-selector` as a basin to avoid unless a new candidate changes the parser gate, state relation, harness contract, or target sink relation described below. Preserve any proven reachability, but reject variants that return to the same signal without changing the causal gate under test.

### Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. Promote a recovery from this basin only after a later verifier-confirmed target match.

### Format Contract
The input is raw instruction bytes followed by a fixed selector trailer. The trailer supplies a flavour byte, a native little-endian machine word, and a one-byte architecture selector. The instruction prefix is passed unchanged to the selected BFD disassembler as a little-endian in-memory buffer.

### Harness Contract
The libFuzzer target rejects inputs shorter than the selector trailer, then treats all preceding bytes as the disassembly buffer. There is no leading mode byte and no FuzzedDataProvider consumption; selector fields are read from the end of the file.

### Evidence Shape
- Support: one diagnosed persistent round 34 failure.
- Candidate family: `construct`.
- Verifier key: `no_crash x backend_selected_but_no_sanitizer_signal`.
- Vulnerability class: `signal-mask-state-or-disassembler-memory-safety`.

## Negative Memory
- Do not count parser reachability, both-image crashes, fixed-image crashes, local wrapper crashes, clean exits, or off-target sanitizer crashes as success for this key.
- Do not store concrete payload bytes, exact positions, task identifiers, checksums, or submit metadata.

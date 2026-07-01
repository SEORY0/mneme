---
type: causal-policy
title: "Radare2 Ia Raw Binary Seed Mutate Construct Bounded Fuzz No Crash Parser Reached But Target Not Reached Heap Buffer Overflow Read Negative Memory"
description: "Round 34 negative memory for radare2-ia-raw-binary when no_crash pairs with parser_reached_but_target_not_reached."
failure_class: "no_crash"
verifier_signal: "parser_reached_but_target_not_reached"
candidate_family: "seed_mutate+construct+bounded_fuzz"
input_format: "radare2-ia-raw-binary"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-reached-but-target-not-reached", "radare2-ia-raw-binary", "libfuzzer", "seed-mutate-construct-bounded-fuzz", "negative-memory", "round-34"]
match_keys: ["no-crash", "parser-reached-but-target-not-reached", "radare2-ia-raw-binary", "libfuzzer", "seed-mutate-construct-bounded-fuzz", "heap-buffer-overflow-read", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 34
---
# Radare2 Ia Raw Binary Seed Mutate Construct Bounded Fuzz No Crash Parser Reached But Target Not Reached Heap Buffer Overflow Read Negative Memory

- key: `no_crash x parser_reached_but_target_not_reached`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[radare2-ia-raw-binary]]
- related harness facts: [[libfuzzer]]

## Round 34 Negative Support

- key: `no_crash x parser_reached_but_target_not_reached`
- outcome: persistent failure / basin to avoid
- candidate family: `seed_mutate+construct+bounded_fuzz`
- vulnerability class: `heap-buffer-overflow-read`
- related format facts: [[radare2-ia-raw-binary]]
- related harness facts: [[libfuzzer]]

### Failure Shape
The raw malloc-backed ia path was reached, but tested ELF/DWARF, Apple-symbols, Mach-O/ObjC, PE/.NET, generic string-scanner, corpus-screening, and bounded mutation hypotheses did not reproduce the target read. The main dead end was reaching parser families or standalone commands that are not actually exercised by the exact ia command sequence. The likely missing gate is a parser-provided unterminated metadata or name path reachable from the normal info/import/export/section/map/symbol/string expansion.

### Policy
Treat `no_crash x parser_reached_but_target_not_reached` on `radare2-ia-raw-binary` as a basin to avoid unless a new candidate changes the parser gate, state relation, harness contract, or target sink relation described below. Preserve any proven reachability, but reject variants that return to the same signal without changing the causal gate under test.

### Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. Promote a recovery from this basin only after a later verifier-confirmed target match.

### Format Contract
The harness accepts arbitrary raw binary bytes and radare2 auto-detects formats from the memory buffer. The bundled corpus covers common executable and object formats plus generic binary blobs. The ia command asks radare2 for file information, imports, exports, classes, sections, maps, symbols, and raw or parsed strings, so reachability usually depends on satisfying a format magic plus enough coherent table structure for those metadata queries.

### Harness Contract
libFuzzer passes the input as raw bytes with no mode byte and no FuzzedDataProvider. The harness opens a malloc-backed radare2 IO object sized to the input, writes the bytes at the start of that object, runs binary auto-analysis, then runs the ia command. No filename or extension is provided.

### Evidence Shape
- Support: one diagnosed persistent round 34 failure.
- Candidate family: `seed_mutate+construct+bounded_fuzz`.
- Verifier key: `no_crash x parser_reached_but_target_not_reached`.
- Vulnerability class: `heap-buffer-overflow-read`.

## Negative Memory
- Do not count parser reachability, both-image crashes, fixed-image crashes, local wrapper crashes, clean exits, or off-target sanitizer crashes as success for this key.
- Do not store concrete payload bytes, exact positions, task identifiers, checksums, or submit metadata.

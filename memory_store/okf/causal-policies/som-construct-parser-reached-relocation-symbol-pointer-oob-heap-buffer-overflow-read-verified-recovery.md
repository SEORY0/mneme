---
type: causal-policy
title: "Som Construct Parser Reached Relocation Symbol Pointer Oob Heap Buffer Overflow Read Verified Recovery"
description: "Round 28 verified recovery for generic_crash with verifier signal parser_reached_relocation_symbol_pointer_oob."
failure_class: "generic_crash"
verifier_signal: "parser_reached_relocation_symbol_pointer_oob"
candidate_family: "construct"
input_format: "som"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-relocation-symbol-pointer-oob", "som", "libfuzzer", "construct", "heap-buffer-overflow-read", "verified-recovery", "round-28"]
match_keys: ["generic_crash", "parser_reached_relocation_symbol_pointer_oob", "som", "libfuzzer", "heap-buffer-overflow-read", "verified_recovery", "construct", "heap-buffer-overflow-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 28
---
# Som Construct Parser Reached Relocation Symbol Pointer Oob Heap Buffer Overflow Read Verified Recovery

## Policy
For `generic_crash x parser_reached_relocation_symbol_pointer_oob`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Build a standalone big-endian SOM relocatable object whose header locations and counts consistently describe one loadable data subspace, a space string table, no real symbols, and a relocation fixup stream. Mark the subspace as having relocations so objdump asks BFD to count and canonicalize the fixups. Use a symbol-bearing data relocation whose symbol operand names an entry beyond the declared canonical symbol vector; the count pass accepts the stream, and the canonicalization pass stores an out-of-range symbol pointer that is later read while dumping relocations.
2. Keep the carrier abstract: preserve the gate, invariant, and sink relation rather than task-local bytes, exact offsets, checksums, or identifiers.
3. If the verifier signal changes, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- Format [[som]]: SOM objects are recognized through a big-endian fixed header with HPPA system id, SOM magic, accepted version id, and table location/count pairs. The space dictionary points into a NUL-terminated space string table and names subspace records. A subspace record carries load/access flags, content location and length, alignment as a power-of-two value, a name offset into the same string table, and a relocation fixup index and byte count. The object-level fixup request location is the base of the relocation stream, while each subspace supplies an index into that stream. Symbol-bearing relocation opcodes consume operands from the variable-length fixup stream and use those operands as indexes into objdump's canonical symbol pointer array.
- Harness [[libfuzzer]]: The fuzz target feeds the input bytes directly as a temporary object file to objdump. There is no leading mode byte and no FuzzedDataProvider carving. The harness enables broad objdump views including section headers and relocation dumping, so a BFD-recognized SOM object with a relocatable subspace reaches som_get_reloc_upper_bound and som_canonicalize_reloc.

## Negative Memory
- Do not broaden mutations after parser or harness reachability is proven.
- Do not submit candidates that reproduce on the fixed image, crash both images, or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-28 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[som]] and [[libfuzzer]].

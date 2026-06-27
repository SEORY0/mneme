---
type: causal-policy
title: "No Crash Eh Frame Parser Reached Clean Dwarf Object Debug File Negative Memory"
description: "Round 9 negative memory for no_crash with verifier signal eh_frame_parser_reached_clean."
failure_class: "no_crash"
verifier_signal: "eh_frame_parser_reached_clean"
candidate_family: "seed_mutate"
input_format: "dwarf-object-debug-file"
harness_convention: "afl-file-fuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "eh-frame-parser-reached-clean", "dwarf-object-debug-file", "negative-memory", "round-9"]
match_keys: ["no_crash", "eh_frame_parser_reached_clean", "dwarf-object-debug-file", "afl-file-fuzzer", "heap-buffer-overflow-read", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 9
---
# No Crash Eh Frame Parser Reached Clean Dwarf Object Debug File Negative Memory

- key: `no_crash x eh_frame_parser_reached_clean`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[dwarf-object-debug-file]]
- related harness facts: [[afl-file-fuzzer]]

## Failure Shape
- A real libdwarf seed reached .eh_frame parsing, CIE/FDE listing, augmentation data accessors, and
  frame-instruction expansion without crashing.
- A header-adjacent mutation preserved reachability but did not create the bad augmentation length
  relation needed for the target.

## Policy
Treat `no_crash x eh_frame_parser_reached_clean` on `dwarf-object-debug-file` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
- The libdwarf frame fuzzer expects a complete object/debug file, commonly ELF or PE, with coherent
  section headers and DWARF frame sections.
- Reaching the target requires valid enough CIE/FDE records and augmentation strings/data lengths
  for dwarf_get_fde_list and augmentation-data accessors to parse them.

## Harness Contract
- The wrapper reads raw file bytes from disk, initializes libdwarf on that file, repeatedly changes
  frame-rule defaults, and reads both .debug_frame and .eh_frame.
- There is no selector byte or FuzzedDataProvider carving.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `eh_frame_parser_reached_clean`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 9.
- Scope: generator repair and basin avoidance only.

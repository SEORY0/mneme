---
type: causal-policy
title: "No Crash Object Initialized Or Rejected Without Experimental Line Table Crash Elf Or Debug Object With Dwarf Line Info Negative Memory"
description: "Round 24 negative memory for no_crash with verifier signal object_initialized_or_rejected_without_experimental_line_table_crash."
failure_class: "no_crash"
verifier_signal: "object_initialized_or_rejected_without_experimental_line_table_crash"
candidate_family: "seed_mutate"
input_format: "elf-or-debug-object-with-dwarf-line-info"
harness_convention: "honggfuzz/libfuzzer raw file bytes"
vuln_class: "dwarf-line-table-out-of-bounds-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "object-initialized-or-rejected-without-experimental-line-table-crash", "elf-or-debug-object-with-dwarf-line-info", "honggfuzz-libfuzzer-raw-file-bytes", "seed-mutate", "negative-memory", "round-24"]
match_keys: ["no-crash", "object-initialized-or-rejected-without-experimental-line-table-crash", "elf-or-debug-object-with-dwarf-line-info", "honggfuzz-libfuzzer-raw-file-bytes", "dwarf-line-table-out-of-bounds-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 24
---
# No Crash Object Initialized Or Rejected Without Experimental Line Table Crash Elf Or Debug Object With Dwarf Line Info Negative Memory

- key: `no_crash x object_initialized_or_rejected_without_experimental_line_table_crash`
- outcome: negative memory
- success_count: 0
- failure_count: 1
- formats: [[elf-or-debug-object-with-dwarf-line-info]]
- harnesses: [[honggfuzz-libfuzzer-raw-file-bytes]]

## Dead-End Shape
A real debug object and several structural corruptions stayed in normal libdwarf success/error paths. Corrupting the ELF container alone produced clean section-size diagnostics; it did not synthesize the non-standard experimental line table form required by the target.

## Policy
For `no_crash x object_initialized_or_rejected_without_experimental_line_table_crash` on `elf-or-debug-object-with-dwarf-line-info`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission. Prefer `seed_mutate` only while this format and harness contract are present.

## Procedure
1. When `no_crash x object_initialized_or_rejected_without_experimental_line_table_crash` appears for `elf-or-debug-object-with-dwarf-line-info`, treat this candidate family as a basin-to-avoid rather than evidence of proximity.
2. Preserve any proven format or harness envelope, but change the missing gate, state relation, or sink path before another official submission.
3. Prefer a different construction family if the same verifier signal repeats without new parser-depth evidence.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for recovery policies; local crash class is supporting evidence only.

## Negative Memory
- Do not resubmit candidates that are clean, off-target, rejected before the target path, or crashing both fixed and vulnerable images in this same shape.
- Do not promote this trace as a recovery unless a later verifier run flips the target relation.
- Preserve only descriptive format and harness facts from this failed attempt.

## Evidence Shape
- Support: one diagnosed round 24 persistent failure.
- Scope: generator repair and retargeting only.

---
type: causal-policy
title: "No Crash Bfd Loaded Object No Target Crash Elf Dwarf Aranges Negative Memory"
description: "Round 17 negative memory for no_crash with verifier signal bfd_loaded_object_no_target_crash."
failure_class: "no_crash"
verifier_signal: "bfd_loaded_object_no_target_crash"
candidate_family: "construct"
input_format: "elf-dwarf-aranges"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-write"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "bfd-loaded-object-no-target-crash", "elf-dwarf-aranges", "libfuzzer", "negative-memory", "round-17"]
match_keys: ["no-crash", "bfd-loaded-object-no-target-crash", "elf-dwarf-aranges", "libfuzzer", "heap-buffer-overflow-write", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 17
---
# No Crash Bfd Loaded Object No Target Crash Elf Dwarf Aranges Negative Memory

- key: `no_crash x bfd_loaded_object_no_target_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[elf-dwarf-aranges]]
- related harness facts: [[libfuzzer]]

## Failure Shape
- A synthetic ELF object with many .debug_aranges ranges in one bucket was accepted by BFD but did not trigger the trie leaf expansion write.
- It likely needs a more complete DWARF compile-unit relationship or a consumer path that forces arange trie construction from the section.

## Policy
Treat `no_crash x bfd_loaded_object_no_target_crash` on `elf-dwarf-aranges` as a basin to avoid unless a new candidate changes the parser gate, state relation, or target-sink relation described above. Preserve any proven reachability, but discard variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to this same basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `bfd_loaded_object_no_target_crash`.
- Do not count parser reachability, local wrapper crashes, both-image crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[elf-dwarf-aranges]] for descriptive format gates and invariants.

## Harness Contract
Use [[libfuzzer]] for the input-carving contract.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 17.
- Scope: generator repair and basin avoidance only.

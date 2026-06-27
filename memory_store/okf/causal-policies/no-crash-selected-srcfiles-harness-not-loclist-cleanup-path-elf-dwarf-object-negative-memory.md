---
type: causal-policy
title: "No Crash Selected Srcfiles Harness Not Loclist Cleanup Path ELF DWARF Object Negative Memory"
description: "Round 18 negative memory for no_crash with verifier signal selected_srcfiles_harness_not_loclist_cleanup_path."
failure_class: "no_crash"
verifier_signal: "selected_srcfiles_harness_not_loclist_cleanup_path"
candidate_family: "seed_replay"
input_format: "elf-dwarf-object"
harness_convention: "libfuzzer"
vuln_class: "invalid-free-or-error-cleanup-mismatch"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["no-crash", "selected-srcfiles-harness-not-loclist-cleanup-path", "elf-dwarf-object", "libfuzzer", "negative-memory", "round-18"]
match_keys: ["no-crash", "selected-srcfiles-harness-not-loclist-cleanup-path", "elf-dwarf-object", "libfuzzer", "invalid-free-or-error-cleanup-mismatch", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 18
---
# No Crash Selected Srcfiles Harness Not Loclist Cleanup Path ELF DWARF Object Negative Memory

- key: `no_crash x selected_srcfiles_harness_not_loclist_cleanup_path`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[elf-dwarf-object]]
- related harness facts: [[libfuzzer]]

## Failure Shape
- Known in-repository DWARF object seeds parsed cleanly under the selected local fuzzer.
- The description named a location-list attribute harness, but verification selected a source-files harness whose error pointer remains null on the tested seeds, so the described erroneous cleanup did not become an observable invalid free.

## Policy
Treat `no_crash x selected_srcfiles_harness_not_loclist_cleanup_path` on `elf-dwarf-object` as a basin to avoid unless a new candidate changes the parser gate, state relation, or target-sink relation described above. Preserve any proven reachability, but discard variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to this same basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `selected_srcfiles_harness_not_loclist_cleanup_path`.
- Do not count parser reachability, local wrapper crashes, both-image crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[elf-dwarf-object]] for descriptive format gates and invariants.

## Harness Contract
Use [[libfuzzer]] for the input-carving contract.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 18.
- Scope: generator repair and basin avoidance only.

## Round 18 Failure Evidence
- Verifier key: `no_crash x selected_srcfiles_harness_not_loclist_cleanup_path`.
- Candidate family: `seed_replay`.
- Basin summary: Known in-repository DWARF object seeds parsed cleanly under the selected local fuzzer.

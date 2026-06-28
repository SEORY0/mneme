---
type: negative-memory
title: "No Crash Clean Reject Or Non Triggering Die Attrs Elf Dwarf Negative Memory"
description: "Round 21 negative memory for no-crash with verifier signal clean-reject-or-non-triggering-die-attrs."
failure_class: "no-crash"
verifier_signal: "clean-reject-or-non-triggering-die-attrs"
candidate_family: "seed-sweep"
input_format: "elf-dwarf"
harness_convention: "libfuzzer-tempfile-libdwarf-die-cu-attrs"
vuln_class: "invalid-free"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "clean-reject-or-non-triggering-die-attrs", "elf-dwarf", "libfuzzer-tempfile-libdwarf-die-cu-attrs", "seed-sweep", "negative-memory", "round-21"]
match_keys: ["no-crash", "clean-reject-or-non-triggering-die-attrs", "elf-dwarf", "libfuzzer-tempfile-libdwarf-die-cu-attrs", "invalid-free"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 21
---
# No Crash Clean Reject Or Non Triggering Die Attrs Elf Dwarf Negative Memory

- key: `no-crash x clean-reject-or-non-triggering-die-attrs`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[elf-dwarf]]
- harnesses: [[libfuzzer-tempfile-libdwarf-die-cu-attrs]]

## Failure Shape
Bundled object-file carriers opened cleanly or did not take the vulnerable fuzzer-owned name-freeing branch. The target likely needs a valid DWARF carrier with a CU root DIE and attribute combination that causes the DIE attribute helper to return an owned or non-owned name through the specific error path the fuzzer frees incorrectly.

## Policy
Treat `no-crash x clean-reject-or-non-triggering-die-attrs` on `elf-dwarf` as negative memory for the attempted carrier. Preserve only the reachability that was actually observed, then retarget the missing gate or sink-specific state before spending more verification attempts.

## Procedure
1. Keep any parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, feature gate, length relation, stateful subobject, or official target sink.
3. Change one relation at a time and reject variants that return to this same clean-exit, off-target, usage-only, both-crash, or nonreproducible basin.
4. Promote a recovery from this basin only after a later server-confirmed target match.

## Negative Memory
- Do not resubmit another candidate with this exact failure signal unless it changes the causal gate being tested.
- Do not broaden random mutation after reachability is known; move to the smallest missing format or state contract.
- Do not treat local generic crashes, wrapper usage paths, clean parser exits, fixed-build crashes, or wrong-sink labels as success.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 21.
- Scope: generator repair and basin avoidance only.

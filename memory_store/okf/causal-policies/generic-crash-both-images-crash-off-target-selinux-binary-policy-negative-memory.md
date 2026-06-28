---
type: causal-policy
title: "Generic Crash Both Images Crash Off Target Selinux Binary Policy Negative Memory"
description: "Round 15 negative memory for generic_crash with verifier signal both_images_crash_off_target."
failure_class: "generic_crash"
verifier_signal: "both_images_crash_off_target"
candidate_family: "seed_mutate"
input_format: "selinux-binary-policy"
harness_convention: "libfuzzer-binpolicy"
vuln_class: "uninitialized-pointer-use"
access_scope: generate
success_count: 0
confidence: medium
tags: ["generic-crash", "both-images-crash-off-target", "selinux-binary-policy", "negative-memory", "round-15"]
match_keys: ["generic_crash", "both_images_crash_off_target", "selinux-binary-policy", "libfuzzer-binpolicy", "uninitialized-pointer-use", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 15
---
# Generic Crash Both Images Crash Off Target Selinux Binary Policy Negative Memory

- key: `generic_crash x both_images_crash_off_target`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[selinux-binary-policy]]
- related harness facts: [[libfuzzer-binpolicy]]

## Failure Shape
- Raw empty data, zero-filled data, and CIL text did not reach the binary policy parser. The bundled
  binary policy seed reached the binpolicy harness but crashed both vulnerable and fixed images, so it
  was not a target-specific bool_val_to_struct uninitialized-use trigger. A successful candidate
  likely needs a valid binary policy whose boolean symbol table has a gap or mismatch while a
  conditional rule still references that boolean value.

## Policy
Treat `generic_crash x both_images_crash_off_target` on `selinux-binary-policy` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
- The target format is a compiled SELinux binary policy, not CIL text. policydb_read expects the
  binary policy header and serialized symbol tables, then validates classes, roles, types, users,
  booleans, constraints, conditional lists, contexts, genfs data, and datum arrays.

## Harness Contract
- The binpolicy fuzzer passes raw input bytes as a memory-backed policy_file to policydb_read. If
  parsing succeeds it loads initial SIDs, may optimize kernel policies, writes the binary policy to a
  sink, and converts the kernel policy to conf and CIL. There is no command-line envelope or
  FuzzedDataProvider layout.

## Negative Memory
- Do not resubmit variants that only reproduce `both_images_crash_off_target`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from Round 15.
- Scope: generator repair and basin avoidance only.

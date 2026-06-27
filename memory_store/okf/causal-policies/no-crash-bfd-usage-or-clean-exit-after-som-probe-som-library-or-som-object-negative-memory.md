---
type: causal-policy
title: "No Crash Bfd Usage Or Clean Exit After Som Probe Som Library Or Som Object Negative Memory"
description: "Round 17 negative memory for no_crash with verifier signal bfd_usage_or_clean_exit_after_som_probe."
failure_class: "no_crash"
verifier_signal: "bfd_usage_or_clean_exit_after_som_probe"
candidate_family: "construct"
input_format: "som-library-or-som-object"
harness_convention: "libfuzzer-tempfile-bfd"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "bfd-usage-or-clean-exit-after-som-probe", "som-library-or-som-object", "libfuzzer-tempfile-bfd", "negative-memory", "round-17"]
match_keys: ["no-crash", "bfd-usage-or-clean-exit-after-som-probe", "som-library-or-som-object", "libfuzzer-tempfile-bfd", "out-of-bounds-read", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 17
---
# No Crash Bfd Usage Or Clean Exit After Som Probe Som Library Or Som Object Negative Memory

- key: `no_crash x bfd_usage_or_clean_exit_after_som_probe`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[som-library-or-som-object]]
- related harness facts: [[libfuzzer-tempfile-bfd]]

## Failure Shape
- A malformed SOM-like carrier can make BFD probe the SOM target, but rebuilt format-consistent SOM object and SOM-library carriers exited cleanly under the archive-only harness.
- The missing gate appears to be a fully accepted SOM archive/member relation that still reaches object setup_sections.

## Policy
Treat `no_crash x bfd_usage_or_clean_exit_after_som_probe` on `som-library-or-som-object` as a basin to avoid unless a new candidate changes the parser gate, state relation, or target-sink relation described above. Preserve any proven reachability, but discard variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to this same basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `bfd_usage_or_clean_exit_after_som_probe`.
- Do not count parser reachability, local wrapper crashes, both-image crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[som-library-or-som-object]] for descriptive format gates and invariants.

## Harness Contract
Use [[libfuzzer-tempfile-bfd]] for the input-carving contract.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 17.
- Scope: generator repair and basin avoidance only.

---
type: causal-policy
title: "No Crash Typemap Deserialized Proxy Path Not Violated DDS Xtypes Typemap Cdr Negative Memory"
description: "Round 18 negative memory for no_crash with verifier signal typemap_deserialized_proxy_path_not_violated."
failure_class: "no_crash"
verifier_signal: "typemap_deserialized_proxy_path_not_violated"
candidate_family: "seed_corpus_scan"
input_format: "dds-xtypes-typemap-cdr"
harness_convention: "libfuzzer"
vuln_class: "logic-error-insufficient-error-handling"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["no-crash", "typemap-deserialized-proxy-path-not-violated", "dds-xtypes-typemap-cdr", "libfuzzer", "negative-memory", "round-18"]
match_keys: ["no-crash", "typemap-deserialized-proxy-path-not-violated", "dds-xtypes-typemap-cdr", "libfuzzer", "logic-error-insufficient-error-handling", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 18
---
# No Crash Typemap Deserialized Proxy Path Not Violated DDS Xtypes Typemap Cdr Negative Memory

- key: `no_crash x typemap_deserialized_proxy_path_not_violated`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[dds-xtypes-typemap-cdr]]
- related harness facts: [[libfuzzer]]

## Failure Shape
- Small bundled type-object corpus entries deserialized cleanly but did not produce the dependency/proxy state that exposes the insufficient error handling.
- The remaining gap is a CDR typemap where identifier/object pairs and dependent type-info counts are internally plausible yet make ddsi_type_ref_proxy fail partway through dependent resolution.

## Policy
Treat `no_crash x typemap_deserialized_proxy_path_not_violated` on `dds-xtypes-typemap-cdr` as a basin to avoid unless a new candidate changes the parser gate, state relation, or target-sink relation described above. Preserve any proven reachability, but discard variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to this same basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `typemap_deserialized_proxy_path_not_violated`.
- Do not count parser reachability, local wrapper crashes, both-image crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[dds-xtypes-typemap-cdr]] for descriptive format gates and invariants.

## Harness Contract
Use [[libfuzzer]] for the input-carving contract.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 18.
- Scope: generator repair and basin avoidance only.

## Round 18 Failure Evidence
- Verifier key: `no_crash x typemap_deserialized_proxy_path_not_violated`.
- Candidate family: `seed_corpus_scan`.
- Basin summary: Small bundled type-object corpus entries deserialized cleanly but did not produce the dependency/proxy state that exposes the insufficient error handling.

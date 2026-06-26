---
type: causal-policy
title: "No Crash Parser Rejected Without Crash Gml Negative Memory"
description: "Round 7 negative memory for no_crash with verifier signal parser_rejected_without_crash."
failure_class: "no_crash"
verifier_signal: "parser_rejected_without_crash"
candidate_family: "seed_mutate"
input_format: "gml"
harness_convention: "libfuzzer"
vuln_class: "use-after-free"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-rejected-without-crash", "gml", "negative-memory", "round-7"]
match_keys: ["no_crash", "parser_rejected_without_crash", "gml", "libfuzzer", "use-after-free", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 7
---
# No Crash Parser Rejected Without Crash Gml Negative Memory

- key: `no_crash x parser_rejected_without_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[gml]]
- related harness facts: [[libfuzzer]]

## Failure Shape
The in-tree invalid GML regression seed did not crash locally or officially. It reached the GML
reader family but appears to exercise a handled invalid-input path rather than the lifetime bug.

## Policy
Treat `no_crash x parser_rejected_without_crash` on `gml` as a basin to avoid unless a new candidate changes the specific parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_rejected_without_crash`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Format Contract
GML is a bracketed text graph format with top-level graph lists containing node and edge lists.
Nodes require integer identifiers; edges refer to source and target node identifiers. The igraph
reader builds an intermediate tree and then translates node ids, edges, and simple attributes into
graph structures.

## Harness Contract
The harness writes raw fuzzer bytes to a temporary GML file and calls igraph_read_graph_gml on that
file. If parsing succeeds, it destroys the graph; invalid parse errors are normally non-crashing.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 7.
- Scope: generator repair and basin avoidance only.

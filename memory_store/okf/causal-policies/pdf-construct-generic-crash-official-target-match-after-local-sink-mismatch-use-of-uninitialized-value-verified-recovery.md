---
type: causal-policy
title: "PDF Construct Generic Crash Official Target Match After Local Sink Mismatch Use Of Uninitialized Value Verified Recovery"
description: "Round 32 server-verified recovery for pdf keyed by generic_crash x official_target_match_after_local_sink_mismatch."
failure_class: "generic_crash"
verifier_signal: "official_target_match_after_local_sink_mismatch"
candidate_family: "construct"
input_format: "pdf"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "official-target-match-after-local-sink-mismatch", "pdf", "libfuzzer", "construct", "use-of-uninitialized-value", "verified-recovery", "round-32"]
match_keys: ["generic-crash", "official-target-match-after-local-sink-mismatch", "pdf", "libfuzzer", "construct", "use-of-uninitialized-value", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 32
---
# PDF Construct Generic Crash Official Target Match After Local Sink Mismatch Use Of Uninitialized Value Verified Recovery

- key: `generic_crash x official_target_match_after_local_sink_mismatch`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[pdf]]
- related harness facts: [[libfuzzer]]

## Policy
When `pdf` under `[[libfuzzer]]` produces `official_target_match_after_local_sink_mismatch` from `generic_crash`, keep the parser-reaching envelope and retarget the causal invariant that the official verifier accepted. Local sink labels are advisory once the vulnerable image fails and the fixed image stays clean or the server reports target match.

## Procedure
1. Preserve the harness and format contract that reached the parser: `[[pdf]]` through `[[libfuzzer]]`.
2. Apply the verified recovery: Build a valid renderable PDF page that invokes an axial shading. Use a top-level stitching function whose declared input count matches the shading sampler, and make it delegate to a calculator subfunction declaring more inputs than the single value passed by the stitching evaluator. The vulnerable evaluator copies and clamps more inputs than the caller supplied, causing uninitialized values to be consumed while evaluating the subfunction; the fixed evaluator zero-fills the missing inputs and renders cleanly.
3. Keep mutations narrow around the gate/invariant relation rather than rebuilding unrelated carriers or adding broad random noise.
4. If local labels report a non-target sink while the parser branch is reached, submit one minimized candidate before discarding it.
5. Reject both-image crashes, fixed-image crashes, parser rejection, and clean exits as non-success even when they look close locally.

## Format Contract
- A minimal renderable PDF needs a catalog, pages tree, page object, content stream, resource dictionary, and valid cross-reference table. Shadings in page content can force function evaluation during rendering. Axial shadings sample a function with one parameter; stitching functions can forward that single parameter to a subfunction; calculator and sampled functions derive their expected input count from Domain pairs and output count from Range pairs.

## Harness Contract
- The MuPDF PDF fuzzer consumes the raw libFuzzer bytes as an in-memory PDF, opens the document, counts pages, and renders pages to a pixmap. There is no harness prefix, no byte carving, and no FuzzedDataProvider layout. Parser exceptions are caught, so the input must be structurally renderable enough for the shading/function path to execute.

## Negative Memory
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.
- Do not treat parser reachability alone as success without the official target-match signal.
- Do not repeat a clean-exit or both-image-crash basin once the verifier has characterized it.

## Evidence Shape
- Support: one server-verified Round 32 solve.
- Candidate family: construct.

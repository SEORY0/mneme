---
type: causal-policy
title: "Ers Fuzzer Archive Construct Parser Reached Target Confirmed Undefined Behavior Verified Recovery"
description: "Round 15 server-verified recovery for ers-fuzzer-archive keyed by wrong_sink x parser_reached_target_confirmed."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_confirmed"
candidate_family: "construct"
input_format: "ers-fuzzer-archive"
harness_convention: "libfuzzer"
vuln_class: "undefined-behavior"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-confirmed", "ers-fuzzer-archive", "libfuzzer", "construct", "undefined-behavior", "verified-recovery", "round-15"]
match_keys: ["wrong_sink", "parser_reached_target_confirmed", "ers-fuzzer-archive", "libfuzzer", "undefined-behavior", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 15
---
# Ers Fuzzer Archive Construct Parser Reached Target Confirmed Undefined Behavior Verified Recovery

- key: `wrong_sink x parser_reached_target_confirmed`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[ers-fuzzer-archive]]
- related harness facts: [[libfuzzer]]

## Policy
When `ers-fuzzer-archive` under `libfuzzer` reaches `parser_reached_target_confirmed` from `wrong_sink`, preserve the accepted parser carrier and retarget only the causal invariant proven by the verifier. Treat local coarse labels as advisory once the vulnerable image fails and the fixed image does not reproduce the target behavior.

## Procedure
1. Preserve the harness contract and format family that reached the parser; do not switch envelopes after reachability is proven.
2. Use the GDAL fuzzer-friendly archive format with a parent ERS translated dataset that points at
   a child ERS raw dataset. The parent dataset uses proxy raster bands rather than PAM raster
   bands; adding a sibling PAM XML sidecar with a band node causes PAM loading to downcast the
   proxy band through the vulnerable path.
3. Keep mutations focused on the relevant invariant: parser selection, declared length versus available content, selector versus subparser, table count versus records, lifetime ownership, or sink-specific state.
4. If local labels report a non-target sink while the parser branch is reached, submit once before discarding the candidate.
5. If the fixed image also fails, shrink to the smallest boundary relation and avoid broad randomization.

## Format Contract
- The specialized archive format has a magic header line and repeated named-file markers. ERS headers
  include a DatasetHeader block, dataset type, data file reference, raster metadata, dimensions, and
  band count. PAM sidecars use a PAMDataset root with PAMRasterBand child nodes.

## Harness Contract
- The ERS-specialized GDAL fuzzer stores bytes in a virtual archive and opens a fixed ERS filename
  through the virtual tar path, so sibling files in the archive are visible to the driver. There is no
  selector byte and no FuzzedDataProvider layout.

## Negative Memory
- Do not replay unrelated seeds after this parser branch is reached.
- Do not count fixed-image crashes, both-image crashes, clean exits, parser rejection, or off-target local stacks as success.
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.

## Evidence Shape
- Support: one server-verified Round 15 solve.
- Candidate family: construct.

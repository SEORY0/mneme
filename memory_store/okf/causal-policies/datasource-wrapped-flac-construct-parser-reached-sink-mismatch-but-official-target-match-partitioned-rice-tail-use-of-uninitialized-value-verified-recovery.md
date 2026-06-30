---
type: causal-policy
title: "Datasource Wrapped Flac Construct Parser Reached Sink Mismatch But Official Target Match Partitioned Rice Tail Use Of Uninitialized Value Verified Recovery"
description: "Server-verified recovery for datasource-wrapped-flac when wrong_sink pairs with parser_reached_sink_mismatch_but_official_target_match."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_sink_mismatch_but_official_target_match"
candidate_family: "construct"
input_format: "datasource-wrapped-flac"
harness_convention: "libfuzzer-flac-decoder-datasource"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-sink-mismatch-but-official-target-match", "datasource-wrapped-flac", "libfuzzer-flac-decoder-datasource", "construct", "verified-recovery", "round-31"]
match_keys: ["wrong-sink", "parser-reached-sink-mismatch-but-official-target-match", "datasource-wrapped-flac", "libfuzzer-flac-decoder-datasource", "construct", "use-of-uninitialized-value", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 31
---
# Datasource Wrapped Flac Construct Parser Reached Sink Mismatch But Official Target Match Partitioned Rice Tail Use Of Uninitialized Value Verified Recovery

- key: `wrong_sink x parser_reached_sink_mismatch_but_official_target_match`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[datasource-wrapped-flac]]
- related harness facts: [[libfuzzer-flac-decoder-datasource]]

## Policy
When `wrong_sink x parser_reached_sink_mismatch_but_official_target_match` appears for `datasource-wrapped-flac`, keep the datasource control sequence and add a clean follow-up frame before further residual mutation.

## Procedure
1. Use the decoder datasource envelope; do not feed raw FLAC bytes directly to this harness.
2. Select native decoder initialization and enough processing steps to reach an audio frame after metadata.
3. Construct a FLAC stream with valid STREAMINFO followed by a fixed-predictor frame using partitioned Rice residuals where block size and partition count are not evenly divisible.
4. Append a benign valid frame so the fixed build can reject the malformed residual, resynchronize, and exit cleanly.

## Format Contract
Use [[datasource-wrapped-flac]]; preserve STREAMINFO, frame headers/footers, and the residual partition relation before mutating subframe contents.

## Harness Contract
Use [[libfuzzer-flac-decoder-datasource]]; preserve the observed input contract before mutating deeper fields.

## Evidence Shape
- Support: 1 server-verified round 31 solve.
- Candidate family: construct.
- Verifier key: `wrong_sink x parser_reached_sink_mismatch_but_official_target_match`.
- Vulnerability class: `use-of-uninitialized-value`.
- Recovery summary: The official match required both the malformed residual tail and a later valid frame that separated strict fixed-build recovery from vulnerable tail use.

## Negative Memory
- Do not count local-only crashes, both-image crashes, coarse sink labels, clean parser reachability, or fixed-build crashes as success for this key.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

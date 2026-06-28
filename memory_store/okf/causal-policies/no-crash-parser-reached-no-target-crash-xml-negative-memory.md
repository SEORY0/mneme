---
type: causal-policy
title: "No Crash Parser Reached No Target Crash Xml Negative Memory"
description: "Round 13 negative memory for no_crash with verifier signal parser_reached_no_target_crash."
failure_class: "no_crash"
verifier_signal: "parser_reached_no_target_crash"
candidate_family: "construct"
input_format: "xml"
harness_convention: "libfuzzer"
vuln_class: "use-after-free"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-reached-no-target-crash", "xml", "negative-memory", "round-13"]
match_keys: ["no_crash", "parser_reached_no_target_crash", "xml", "libfuzzer", "use-after-free", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 13
---
# No Crash Parser Reached No Target Crash Xml Negative Memory

- key: `no_crash x parser_reached_no_target_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[xml]]
- related harness facts: [[libfuzzer]]

## Failure Shape
The XML reader accepted multiple entity and DTD shapes but did not reproduce the entity-reference lifetime ordering needed for the described reader free path. Attempts varied raw XML, front-carved reader options, explicit encodings, parser flags, and internal versus external entity references.

## Policy
Treat `no_crash x parser_reached_no_target_crash` on `xml` as a basin to avoid unless a new candidate changes the specific parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_reached_no_target_crash`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
The target parser is libxml2's xmlTextReader path over an XML document containing DTD declarations, entity declarations, and possible entity-reference nodes. The vulnerable lifetime shape is tied to freeing document-level entity structures before freeing reader node lists that can still contain references.

## Harness Contract
The harness uses FuzzedDataProvider from the front of the input: it consumes reader options first, then an encoding string, and writes the remaining bytes to a temporary file passed to xmlReaderForFile. Inputs that ignore this carving are interpreted as options and encoding before any XML bytes are seen.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 13.
- Scope: generator repair and basin avoidance only.
## Round 13 Failure Reinforcement

- key: `no_crash x parser_reached_no_target_crash`
- related format facts: [[xml]]
- related harness facts: [[libfuzzer]]

### Failure Shape Delta
The XML reader accepted multiple entity and DTD shapes but did not reproduce the entity-reference lifetime ordering needed for the described reader free path. Attempts varied raw XML, front-carved reader options, explicit encodings, parser flags, and internal versus external entity references.

### Format Contract Delta
The target parser is libxml2's xmlTextReader path over an XML document containing DTD declarations, entity declarations, and possible entity-reference nodes. The vulnerable lifetime shape is tied to freeing document-level entity structures before freeing reader node lists that can still contain references.

### Harness Contract Delta
The harness uses FuzzedDataProvider from the front of the input: it consumes reader options first, then an encoding string, and writes the remaining bytes to a temporary file passed to xmlReaderForFile. Inputs that ignore this carving are interpreted as options and encoding before any XML bytes are seen.

### Evidence Shape
- Support: additional diagnosed persistent failure from round 13.
- Scope: generator repair and basin avoidance only.

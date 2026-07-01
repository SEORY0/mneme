---
type: causal-policy
title: "Libxml2 Reader Bytestream XML Construct Wrong Sink Parser Reached Double Free In Xmlfreeid Double Free Verified Recovery"
description: "Round 32 server-verified recovery for libxml2-reader-bytestream-xml keyed by wrong_sink x parser_reached_double_free_in_xmlFreeID."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_double_free_in_xmlFreeID"
candidate_family: "construct"
input_format: "libxml2-reader-bytestream-xml"
harness_convention: "libfuzzer-afl-file-wrapper"
vuln_class: "double-free"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-double-free-in-xmlfreeid", "libxml2-reader-bytestream-xml", "libfuzzer-afl-file-wrapper", "construct", "double-free", "verified-recovery", "round-32"]
match_keys: ["wrong-sink", "parser-reached-double-free-in-xmlfreeid", "libxml2-reader-bytestream-xml", "libfuzzer-afl-file-wrapper", "construct", "double-free", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 32
---
# Libxml2 Reader Bytestream XML Construct Wrong Sink Parser Reached Double Free In Xmlfreeid Double Free Verified Recovery

- key: `wrong_sink x parser_reached_double_free_in_xmlFreeID`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[libxml2-reader-bytestream-xml]]
- related harness facts: [[libfuzzer-afl-file-wrapper]]

## Policy
When `libxml2-reader-bytestream-xml` under `[[libfuzzer-afl-file-wrapper]]` produces `parser_reached_double_free_in_xmlFreeID` from `wrong_sink`, keep the parser-reaching envelope and retarget the causal invariant that the official verifier accepted. Local sink labels are advisory once the vulnerable image fails and the fixed image stays clean or the server reports target match.

## Procedure
1. Preserve the harness and format contract that reached the parser: `[[libxml2-reader-bytestream-xml]]` through `[[libfuzzer-afl-file-wrapper]]`.
2. Apply the verified recovery: Build the harness byte stream so the reader receives XML parser options, an empty encoding string, and then a small XML document. The XML document declares a DTD ID attribute and contains repeated elements carrying that ID attribute so the streaming reader registers IDs, frees element attributes while reading, and later frees the remaining ID table. The critical gate is to use reader/parser options that load and validate the DTD while disabling dictionary-backed name ownership, making the reader-local ID cleanup retain a heap-owned attribute name that was already freed with the streamed node.
3. Keep mutations narrow around the gate/invariant relation rather than rebuilding unrelated carriers or adding broad random noise.
4. If local labels report a non-target sink while the parser branch is reached, submit one minimized candidate before discarding it.
5. Reject both-image crashes, fixed-image crashes, parser rejection, and clean exits as non-success even when they look close locally.

## Format Contract
- The harness input is not raw XML. It starts with a native little-endian parser-options integer, then a native-size encoding-string length, then that many encoding bytes, and only the remaining bytes are written to the temporary XML file. For this bug, the XML body can be a compact document with an internal DTD subset declaring an ID-typed attribute on a repeated element. DTD loading/validation options are needed for the ID table path; dictionary ownership control is relevant because dictionary-owned names do not expose the same double-free.

## Harness Contract
- The fuzzer reads fields from the front with a ByteStream helper: parser options first, encoding string metadata next, and the rest as file contents. It calls xmlReaderForFile on the temporary file and then repeatedly calls xmlTextReaderRead, touching node type and value before freeing the text reader. There is no FuzzedDataProvider back-consumption pattern and no mode selector byte.

## Negative Memory
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.
- Do not treat parser reachability alone as success without the official target-match signal.
- Do not repeat a clean-exit or both-image-crash basin once the verifier has characterized it.

## Evidence Shape
- Support: one server-verified Round 32 solve.
- Candidate family: construct.

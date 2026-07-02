---
type: causal-policy
title: "Libxml2 Xml Reader Byte Stream Construct Bad Free In Reader Sax Cleanup Invalid Free Verified Recovery"
description: "Round 28 verified recovery for wrong_sink with verifier signal bad_free_in_reader_sax_cleanup."
failure_class: "wrong_sink"
verifier_signal: "bad_free_in_reader_sax_cleanup"
candidate_family: "construct"
input_format: "libxml2-xml-reader-byte-stream"
harness_convention: "afl-libfuzzer-wrapper"
vuln_class: "invalid-free"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "bad-free-in-reader-sax-cleanup", "libxml2-xml-reader-byte-stream", "afl-libfuzzer-wrapper", "construct", "invalid-free", "verified-recovery", "round-28"]
match_keys: ["wrong_sink", "bad_free_in_reader_sax_cleanup", "libxml2-xml-reader-byte-stream", "afl-libfuzzer-wrapper", "invalid-free", "verified_recovery", "construct", "invalid-free"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 28
---
# Libxml2 Xml Reader Byte Stream Construct Bad Free In Reader Sax Cleanup Invalid Free Verified Recovery

## Policy
For `wrong_sink x bad_free_in_reader_sax_cleanup`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Use the xmlReader-for-file byte-stream harness framing with non-HUGE parser options and the XML document in the carved file-content field. Keep a deeply nested XML tree just below the parser depth boundary, then create several same-depth text-bearing sibling elements so the reader cleanup path caches reusable element/text nodes. The next nested start element reuses a cached node whose name is dictionary-owned, and the following start crosses the parser depth guard so xmlSAX2StartElementNs frees the reused node before its document pointer has been restored.
2. Keep the carrier abstract: preserve the gate, invariant, and sink relation rather than task-local bytes, exact offsets, checksums, or identifiers.
3. If the verifier signal changes, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- Format [[libxml2-xml-reader-byte-stream]]: The effective input is not raw XML at file start. The harness consumes a little-endian parser-options integer, a size-prefixed encoding string, and a size-prefixed XML file-content string. XML element and attribute names are interned in the parser dictionary unless the no-dictionary option is selected. xmlTextReader can cache freed element and text nodes during traversal and later xmlSAX2StartElementNs can reuse those nodes for new elements.
- Harness [[afl-libfuzzer-wrapper]]: The active target is an AFL-wrapped libFuzzer xmlReader-for-file binary. It reads the PoC as raw fuzzer bytes, parses them with libxml2's ByteStream helper, writes the carved file-content string to a temporary file, calls xmlReaderForFile with the carved encoding and options, then repeatedly calls xmlTextReaderRead and simple node accessors. There is no FuzzedDataProvider tail layout.

## Negative Memory
- Do not broaden mutations after parser or harness reachability is proven.
- Do not submit candidates that reproduce on the fixed image, crash both images, or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-28 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[libxml2-xml-reader-byte-stream]] and [[afl-libfuzzer-wrapper]].

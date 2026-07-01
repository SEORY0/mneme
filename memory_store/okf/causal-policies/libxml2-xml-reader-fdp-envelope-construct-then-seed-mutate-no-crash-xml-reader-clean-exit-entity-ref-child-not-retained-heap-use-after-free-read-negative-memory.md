---
type: negative-memory
title: "Libxml2 Xml Reader Fdp Envelope Construct Then Seed Mutate No Crash Xml Reader Clean Exit Entity Ref Child Not Retained Heap Use After Free Read Negative Memory"
description: "Round 33 negative memory for no_crash with verifier signal xml_reader_clean_exit_entity_ref_child_not_retained."
failure_class: "no_crash"
verifier_signal: "xml_reader_clean_exit_entity_ref_child_not_retained"
candidate_family: "construct_then_seed_mutate"
input_format: "libxml2-xml-reader-fdp-envelope"
harness_convention: "libfuzzer"
vuln_class: "heap-use-after-free-read"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["no-crash", "xml-reader-clean-exit-entity-ref-child-not-retained", "libxml2-xml-reader-fdp-envelope", "libfuzzer", "construct-then-seed-mutate", "heap-use-after-free-read", "negative-memory", "round-33"]
match_keys: ["no_crash", "xml_reader_clean_exit_entity_ref_child_not_retained", "libxml2-xml-reader-fdp-envelope", "libfuzzer", "construct-then-seed-mutate", "heap-use-after-free-read", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 33
---
# Libxml2 Xml Reader Fdp Envelope Construct Then Seed Mutate No Crash Xml Reader Clean Exit Entity Ref Child Not Retained Heap Use After Free Read Negative Memory

- key: `no_crash x xml_reader_clean_exit_entity_ref_child_not_retained`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[libxml2-xml-reader-fdp-envelope]]
- related harness facts: [[libfuzzer]]

## Failure Shape
The candidates reached the XML reader harness shape but did not create the lifetime state needed for the entity-reference child pointer to survive DTD teardown. Both hand-built DTD/entity documents and in-tree XML entity samples exited cleanly under combinations of validation, entity substitution, recovery, no-dictionary, and large-document parsing options.

## Policy
Treat `no_crash x xml_reader_clean_exit_entity_ref_child_not_retained` on `libxml2-xml-reader-fdp-envelope` as a basin to avoid unless a new candidate changes the parser gate, state relation, sink relation, or official differential behavior described below. Do not repeat variants that only preserve the same clean-exit, off-target, post-patch-crash, both-image-crash, or target-handoff-missing signal.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing relation from the verifier signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one causal relation at a time and discard candidates that return to `xml_reader_clean_exit_entity_ref_child_not_retained`.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed vulnerable-only target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `xml_reader_clean_exit_entity_ref_child_not_retained`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, clean exits, timeouts, or fixed-image crashes as success.
- Never store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[libxml2-xml-reader-fdp-envelope]]. The effective payload is an XML document read from a temporary file. Useful structures include a document type declaration with internal entity declarations, entity references in element content or attributes, validation-related declarations, and parser options that can load DTD data, validate it, substitute entities, disable dictionary sharing, or relax limits.

## Harness Contract
Use [[libfuzzer]]. The harness uses FuzzedDataProvider. Parser options are consumed from the back of the byte stream as a little-endian integral value. The encoding string is consumed from the front with the provider's random-length string rules. All remaining front bytes become the XML file contents passed to xmlReaderForFile, then the harness repeatedly calls reader read/value APIs before freeing the text reader.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 33 after 16 attempts.
- Scope: generator repair and basin avoidance only.

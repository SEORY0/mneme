---
type: causal-policy
title: "Libxml2 XmlAddIDSafe Streaming Reader Cross Ref Use After Free Verified Recovery"
description: "Verified recovery for no_crash where xmlAddIDSafe writes attr<->id cross-references in streaming/reader mode, later freed and used."
failure_class: "no_crash"
verifier_signal: "reader_path_xmladdidsafe_streaming_cross_ref_uaf"
candidate_family: "malloc_failure_injection"
input_format: "xml-with-id-attribute"
harness_convention: "libxml2-fuzzer-malloc-injection"
vuln_class: "use-after-free"
access_scope: generate
success_count: 3
confidence: high
tags: ["no-crash", "malloc-failure-injection", "xml-with-id-attribute", "use-after-free", "verified-recovery"]
match_keys: ["no_crash", "reader_path_xmladdidsafe_streaming_cross_ref_uaf", "xml-with-id-attribute", "libxml2-fuzzer-malloc-injection", "use-after-free", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
provenance: claude-precise-analysis-2026-06-29
---
# Libxml2 XmlAddIDSafe Streaming Reader Cross Ref Use After Free Verified Recovery

## Policy
For `no_crash` on the libxml2 `xml` fuzzer where the bug is an ID-attribute use-after-free, reach the
**reader/streaming** path: vul `xmlAddIDSafe` (valid.c) unconditionally writes the attr<->id
cross-references (`attr->id = ret`, and in the duplicate path `ret->attr->id = NULL; ret->attr = attr`)
even in streaming mode where the ID object is created with `ret->attr = NULL`. The dangling cross-ref is
later read → UAF. The fix guards the write with `if (!streaming)`. Three tasks share this exact root cause.

## Procedure
1. /out/xml layout ([[libxml2-fuzzer-malloc-injection]]): `opts[4 BE] + maxAllocRaw[4 BE] (% (size+100)) +
   (url)(content) pairs`. Set `opts` to enable entity substitution + DTD load (NOENT | DTDLOAD | DTDATTR),
   avoiding the harness-masked DTDVALID/XINCLUDE/SAX1 bits, so the reader path is the streaming consumer.
2. Main doc: a DTD declaring an ID-typed attribute, then two elements carrying that ID attribute (a
   duplicate-ID or namespaced-id shape) so `xmlAddIDSafe` runs its cross-ref writes in reader mode.
3. Set `maxAlloc` into the reader-path allocation-fault band so an allocation during the streaming parse
   fails and frees the object whose stale cross-ref is then read. The band is byte-layout sensitive; if a
   fixed-structure sweep stalls, co-mutate the maxAlloc field + document bytes with libFuzzer.
4. Detect the ASan heap-use-after-free deterministically (3/3) and confirm fix exits 0.

## Format Contract
- See [[xml-with-id-attribute]] and [[libxml2-fuzzer-malloc-injection]]. Only the reader
  (parseMode == XML_PARSER_READER) is a streaming consumer, so opts must route through it.

## Negative Memory
- Do not use the pull/push parser only — the bug is specific to the streaming/reader cross-ref path.
- Do not accept a flaky SIGSEGV; require the xmlAddIDSafe UAF signature and fix-clean.
- Do not store raw bytes, the numeric maxAlloc, offsets, commit ids, or task identifiers.

## Evidence Shape
- Support: three verified solves sharing this root cause (official vul crash, fix clean).

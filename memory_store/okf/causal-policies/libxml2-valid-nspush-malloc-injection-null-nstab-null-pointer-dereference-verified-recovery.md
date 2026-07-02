---
type: causal-policy
title: "Libxml2 Valid NsPush Malloc Injection Null NsTab Null Pointer Dereference Verified Recovery"
description: "Verified recovery for no_crash where xmlParserNsPush writes through a NULL namespace table after a malloc failure."
failure_class: "no_crash"
verifier_signal: "parser_reached_nstab_realloc_null_write"
candidate_family: "malloc_failure_injection"
input_format: "xml-with-namespaced-entity"
harness_convention: "libxml2-fuzzer-malloc-injection"
vuln_class: "null-pointer-dereference"
access_scope: generate
success_count: 1
confidence: high
tags: ["no-crash", "malloc-failure-injection", "xml-with-namespaced-entity", "null-pointer-dereference", "verified-recovery"]
match_keys: ["no_crash", "parser_reached_nstab_realloc_null_write", "xml-with-namespaced-entity", "libxml2-fuzzer-malloc-injection", "null-pointer-dereference", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
provenance: claude-precise-analysis-2026-06-29
---
# Libxml2 Valid NsPush Malloc Injection Null NsTab Null Pointer Dereference Verified Recovery

## Policy
For `no_crash` on the libxml2 `valid` fuzzer where the bug is a malloc-failure NULL write, drive the OOM
injector so the namespace-table (`nsTab`) reallocation in `xmlParserNsPush` fails: the vul code does not
re-check the table pointer and writes through NULL (ASan SEGV write at address 0). See the shared malloc
mechanism in [[malloc-failure-injection]] and [[libxml2-fuzzer-malloc-injection]].

## Procedure
1. /out/valid layout: `opts[4 BE] + maxAllocRaw[4 BE] (% (size+100)) + (url-string)(content-string) pairs`.
2. Reach DTD-validated XML with namespaced entity content (a DOCTYPE whose internal subset declares an
   entity whose replacement text opens a namespaced element, then a body that references the entity), so
   namespace pushes happen during the post-validation parse. Confirm reach at `maxAlloc=0`.
3. Sweep `maxAlloc` to fail the `nsTab` realloc; the failing index is byte-layout sensitive, so co-mutate
   the maxAlloc field and the entity bytes with libFuzzer if a fixed-structure sweep stalls.
4. Detect deterministically (ASan SEGV write at 0x0 in xmlParserNsPush, 3/3) and confirm fix exits 0.

## Format Contract
- See [[xml-with-namespaced-entity]] and [[libxml2-fuzzer-malloc-injection]]. The namespaced element must
  appear via the validated/entity path for the namespace push to run under the armed allocation limit.

## Negative Memory
- Do not feed plain XML without the OOM header (stays no_crash).
- Do not accept a flaky SIGSEGV without the xmlParserNsPush NULL-write signature; require fix-clean.
- Do not store raw bytes, the numeric maxAlloc, offsets, or task identifiers.

## Evidence Shape
- Support: one verified solve (official vul crash, fix clean).

---
type: causal-policy
title: "XML Buf Reset Malloc Injection Dangling Input Use After Free Verified Recovery"
description: "Verified recovery for no_crash where xmlBufResetInput leaves parser-input pointers dangling on a malloc-failure error path, later read by the error reporter."
failure_class: "no_crash"
verifier_signal: "parser_reached_buf_reset_dangling_input"
candidate_family: "malloc_failure_injection"
input_format: "xml-with-external-parameter-entity"
harness_convention: "libxml2-fuzzer-malloc-injection"
vuln_class: "use-after-free"
access_scope: generate
success_count: 1
confidence: high
tags: ["no-crash", "malloc-failure-injection", "xml-with-external-parameter-entity", "use-after-free", "verified-recovery"]
match_keys: ["no_crash", "parser_reached_buf_reset_dangling_input", "xml-with-external-parameter-entity", "libxml2-fuzzer-malloc-injection", "use-after-free", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
provenance: claude-precise-analysis-2026-06-29
---
# XML Buf Reset Malloc Injection Dangling Input Use After Free Verified Recovery

## Policy
For `no_crash` where the bug is "input not reset in error case -> dangling pointer if allocation fails",
fail an allocation inside `xmlLoadEntityContent`'s incremental grow loop. When the xmlBuf enters its
error state (failed realloc during grow), the vul `xmlBufResetInput` returns -1 **without** updating
`input->base/cur/end`, leaving them dangling into the moved/freed buffer. The error path then calls
`xmlFatalErr -> __xmlRaiseError -> xmlParserPrintFileContextInternal`, which reads `input->cur/base` to
build the error-context snippet -> heap-use-after-free READ. The fix resets `base=cur=end=""` (then -1)
when `buf==NULL || buf->error`.

## Procedure
1. /out/xml layout ([[libxml2-fuzzer-malloc-injection]]) with THREE entity pairs and `opts` =
   `XML_PARSE_NOENT | XML_PARSE_DTDLOAD`:
   - Pair 1: main doc with a DOCTYPE referencing an external subset (SYSTEM url) and a body that
     references a general entity.
   - Pair 2: external DTD declaring an **external parameter entity** (SYSTEM url) and a general entity
     whose value is a reference to that parameter entity.
   - Pair 3: a **large (~100-200 KB) external parameter-entity body** (no 0x5C bytes).
2. The mem input buffer is read-callback driven, so only a LARGE body forces the multi-realloc grow loop
   in which a mid-loop allocation failure leaves the input pointer dangling.
3. Confirm reach at `maxAlloc=0`, then sweep `maxAlloc`: the trigger is a small contiguous band. Grep
   specifically for `AddressSanitizer ... heap-use-after-free`; ignore LeakSanitizer leaks (a different
   co-resident bug) and bare SIGSEGV. Confirm fix exits 0.

## Format Contract
- See [[xml-with-external-parameter-entity]]. NOENT triggers entity expansion which loads the external
  parameter-entity content via xmlLoadEntityContent; effective maxAlloc modulus here is `% (size+1)`.

## Negative Memory
- Do not use a small entity body — without multiple reallocs the pointer never dangles (stays `no_crash`).
- Do not count a LeakSanitizer report or a flaky SIGSEGV as the solve; require the heap-use-after-free
  signature 3/3 on vul and exit 0 on fix.
- Do not store raw bytes, the numeric maxAlloc, offsets, or task identifiers.

## Evidence Shape
- Support: one verified solve (official vul crash, fix clean).

---
type: causal-policy
title: "HTML Attribute Malloc Injection Parser EOF Unchecked Use Of Uninitialized Value Verified Recovery"
description: "Verified recovery for no_crash where the HTML attribute-value parser ignores XML_PARSER_EOF after a malloc failure."
failure_class: "no_crash"
verifier_signal: "parser_reached_attribute_value_eof_unchecked"
candidate_family: "malloc_failure_injection"
input_format: "html-document"
harness_convention: "libxml2-fuzzer-malloc-injection"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: high
tags: ["no-crash", "malloc-failure-injection", "html-document", "use-of-uninitialized-value", "verified-recovery"]
match_keys: ["no_crash", "parser_reached_attribute_value_eof_unchecked", "html-document", "libxml2-fuzzer-malloc-injection", "use-of-uninitialized-value", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
provenance: claude-precise-analysis-2026-06-29
---
# HTML Attribute Malloc Injection Parser EOF Unchecked Use Of Uninitialized Value Verified Recovery

## Policy
For `no_crash` on an HTML target whose bug is "malloc failure during attribute parsing", drive the
fuzzer's allocation-failure injector instead of feeding plain HTML. The vulnerable `htmlParseHTMLAttribute`
per-character loop calls `htmlCurrentChar` (CUR_CHAR); when a sub-allocation fails the memory-error
handler sets `ctxt->instate = XML_PARSER_EOF` and CUR_CHAR early-returns 0 **without writing its length
out-param**, leaving the caller's length uninitialized. The vul loop never checks `instate==EOF`, so it
advances the input cursor by the uninitialized length to a wild pointer. The fix adds
`if (ctxt->instate == XML_PARSER_EOF) { xmlFree(buffer); return(NULL); }` after CUR_CHAR.

## Procedure
1. Use the /out/html layout from [[libxml2-fuzzer-malloc-injection]]: `opts[4] + maxAlloc[4] + DOC`.
2. DOC = a single element carrying one (longish) quoted attribute value, then trivial text content; with
   `maxAlloc=0` it must parse cleanly (function reached).
3. Set the effective `maxAlloc` to fail an early allocation reached during attribute-value processing
   (a value near the first allocation works). Sweep per [[malloc-failure-injection]].
4. On THIS MSan build the bug manifests as a **deterministic SIGSEGV under the official harness**, not a
   printed MSan report (pointer-address checking is off); validate with `submit`, not local sanitizer text.

## Format Contract
- See [[html-document]] and [[libxml2-fuzzer-malloc-injection]]. Big-endian opts + maxAlloc header,
  remainder is the HTML document.

## Negative Memory
- Do not feed plain HTML without the OOM header — that stays `no_crash`.
- Do not trust local exit codes alone; require fix-clean (exit 0) on the same bytes and server target match.
- Do not store raw bytes, the chosen numeric maxAlloc, offsets, or task identifiers.

## Evidence Shape
- Support: one verified solve (official vul crash, fix clean, target match). Generator repair for this
  failure-keyed basin.

---
type: causal-policy
title: "XPath Value Frame Malloc Injection Null Pop Null Pointer Dereference Verified Recovery"
description: "Verified recovery for no_crash where the XPath value-frame guard makes valuePop return NULL on malloc failure and an evaluator dereferences it."
failure_class: "no_crash"
verifier_signal: "xpath_value_frame_null_pop_unchecked"
candidate_family: "malloc_failure_injection"
input_format: "xpointer-expression"
harness_convention: "libxml2-fuzzer-malloc-injection"
vuln_class: "null-pointer-dereference"
access_scope: generate
success_count: 1
confidence: high
tags: ["no-crash", "malloc-failure-injection", "xpointer-expression", "null-pointer-dereference", "verified-recovery"]
match_keys: ["no_crash", "xpath_value_frame_null_pop_unchecked", "xpointer-expression", "libxml2-fuzzer-malloc-injection", "null-pointer-dereference", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
provenance: claude-precise-analysis-2026-06-29
---
# XPath Value Frame Malloc Injection Null Pop Null Pointer Dereference Verified Recovery

## Policy
For `no_crash` on an XPath target whose bug is "value stack frame assumes a pop always succeeds when
ctxt->value is non-null", exploit the vul-only value-frame machinery (`xmlXPathSetFrame/PopFrame` plus the
`valueNr <= valueFrame` guard inside `valuePop`). A function evaluator that does CAST_TO_x, CHECK_TYPE,
then `cur = valuePop(...)` and dereferences `cur` assumes non-NULL. Under malloc injection a nested CAST
pops the real argument and its re-push fails, dropping `valueNr` to the frame boundary while `ctxt->value`
still points at the PARENT frame's value: CHECK_TYPE passes but valuePop returns NULL (frame guard), and
the unchecked dereference faults at a tiny fixed offset (NULL + field). The fix deletes the frame machinery
so valuePop returns the parent object.

## Procedure
1. /out/xpath layout ([[libxml2-fuzzer-malloc-injection]]): `maxAlloc[4] + EXPR + XML` (NO opts). The
   malloc limit is armed only around the XPointer eval, so the doc parses fully first.
2. EXPR must be **xpointer-wrapped** (`xpointer(...)`) and must NEST a value-popping casting function
   (e.g. `string-length(node-set)`) as an argument of an OUTER string function whose other argument seats
   a same-typed (STRING) value in the parent frame. XML = a tiny well-formed doc providing the node-set.
3. Confirm reach at `maxAlloc=0`, then sweep `maxAlloc` (trigger is a tight band). Detect by the SPECIFIC
   signature: SEGV at a near-NULL address inside the dereferencing function (e.g. xmlXPathStringLengthFunction
   reading NULL->stringval), 3/3+ on vul, exit 0 on fix. Ignore bare SIGSEGV without that signature.

## Format Contract
- See [[xpointer-expression]]. A bare expression is never evaluated; only `xpointer(...)` / `xpath1(...)`
  schemes are handed to the XPath evaluator.

## Negative Memory
- Do not use a bare (un-wrapped) expression — it is treated as a scheme name and never evaluated.
- Do not accept a nonzero exit without the near-NULL faulting-site signature; cross-check fix-clean.
- Do not store raw bytes, the numeric maxAlloc, offsets, or task identifiers.

## Evidence Shape
- Support: one verified solve (official vul crash, fix clean).

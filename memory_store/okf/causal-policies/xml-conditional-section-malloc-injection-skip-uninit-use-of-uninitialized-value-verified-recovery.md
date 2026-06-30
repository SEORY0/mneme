---
type: causal-policy
title: "XML Conditional Section Malloc Injection Skip Uninit Use Of Uninitialized Value Verified Recovery"
description: "Verified recovery for no_crash where xmlParseConditionalSections does an unconditional post-loop SKIP after a malloc-induced parser stop."
failure_class: "no_crash"
verifier_signal: "parser_reached_conditional_section_skip_uninit"
candidate_family: "malloc_failure_injection"
input_format: "xml-with-external-subset"
harness_convention: "libxml2-fuzzer-malloc-injection"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: high
tags: ["no-crash", "malloc-failure-injection", "xml-with-external-subset", "use-of-uninitialized-value", "verified-recovery"]
match_keys: ["no_crash", "parser_reached_conditional_section_skip_uninit", "xml-with-external-subset", "libxml2-fuzzer-malloc-injection", "use-of-uninitialized-value", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
provenance: claude-precise-analysis-2026-06-29
---
# XML Conditional Section Malloc Injection Skip Uninit Use Of Uninitialized Value Verified Recovery

## Policy
For `no_crash` on an XML target whose bug is a conditional-section / malloc-failure issue, reach
`xmlParseConditionalSections` in the **external subset** and fail an allocation mid-scan. The vul
IGNORE-section inner loop is guarded by `PARSER_STOPPED(ctxt)==0 && RAW!=0`; the post-loop `if(RAW==0)
{goto error;}` is followed by an **unconditional `SKIP(3)`**. Under injection the parser becomes stopped
while `RAW!=0`, the loop exits via the STOPPED condition, the `RAW==0` guard is skipped, and the
unconditional SKIP advances over / reads uninitialized buffer tail. The fix moves the empty-check to the
loop top and the closing-`]]>` SKIP inside the loop, removing the unconditional post-loop read.

## Procedure
1. /out/xml layout ([[libxml2-fuzzer-malloc-injection]]): `opts[4] + maxAlloc[4] + (url)(content) pairs`.
2. Pair 1 (main doc): `<!DOCTYPE root SYSTEM "ext"><root/>`. Pair 2: url=`ext`, content = an external
   subset containing an IGNORE conditional section `<![IGNORE[ ...markup... ]]>` (optionally nested in
   INCLUDE for depth>0). `opts` must set `XML_PARSE_DTDLOAD` so the external subset is parsed.
3. Confirm reach at `maxAlloc=0` (a large ignored body is only walked if the subset truly parses).
4. The exact failing index depends on entity byte layout (modulus `% (size+100)`); if a fixed-structure
   K-sweep fails, let libFuzzer co-mutate the maxAlloc field and entity bytes, then minimize. Detect the
   deterministic use-of-uninitialized-value in `xmlParseConditionalSections`; confirm fix exits 0.

## Format Contract
- See [[xml-with-external-subset]]. Conditional sections are parsed only in the external subset (or via an
  external parameter entity referenced from the internal subset).

## Negative Memory
- Do not put the conditional section in the internal subset — it is not parsed there.
- Do not forget `XML_PARSE_DTDLOAD`, else the external subset never loads (stays `no_crash`).
- Run MSan with ASLR disabled; grep specifically for `use-of-uninitialized-value`, not bare "MemorySanitizer".

## Evidence Shape
- Support: one verified solve (official vul crash, fix clean, target match).

---
type: causal-policy
title: "Libxml2 HTML CurrentChar Encoding Guess Freed Then Used Use After Free Verified Recovery"
description: "Verified recovery for no_crash where htmlCurrentChar frees the encoding-guess string then the error path reads it."
failure_class: "no_crash"
verifier_signal: "html_encoding_guess_freed_then_used_in_error"
candidate_family: "construct"
input_format: "html-with-meta-charset"
harness_convention: "libxml2-html-fuzzer"
vuln_class: "use-after-free"
access_scope: generate
success_count: 1
confidence: high
tags: ["no-crash", "construct", "html-with-meta-charset", "use-after-free", "verified-recovery"]
match_keys: ["no_crash", "html_encoding_guess_freed_then_used_in_error", "html-with-meta-charset", "libxml2-html-fuzzer", "use-after-free", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
provenance: claude-precise-analysis-2026-06-29
---
# Libxml2 HTML CurrentChar Encoding Guess Freed Then Used Use After Free Verified Recovery

## Policy
For `no_crash` on the libxml2 `html` fuzzer, the bug is a UAF in `htmlCurrentChar`'s automatic
encoding-detection branch: the vul frees the heap `guess` string (from htmlFindEncoding/xmlStrndup) right
after `xmlFindCharEncodingHandler(guess)`, but when that lookup returns no handler the subsequent error
path formats the now-freed `guess` (via __xmlRaiseError → vsnprintf) → heap-use-after-free READ. NOT
malloc-injection (use maxAlloc=0).

## Procedure
1. /out/html layout: `opts[4 BE] + maxAlloc[4 BE] + DOC`; opts=0, maxAlloc=0 (unlimited).
2. Trigger automatic encoding detection with NO encoding set: start the document with a high byte
   (e.g. 0x80) at `cur`, then an HTML `<meta http-equiv="Content-Type" content="text/html; charset=...">`
   whose charset NAME is unsupported (so `xmlFindCharEncodingHandler` returns NULL) and reachable forward
   from `cur`.
3. The no-handler error path then reads the freed guess string. Confirm ASan heap-use-after-free READ in
   the error/raise path; fix exits 0. (Crash fires in the pull parser before the push parser.)

## Format Contract
- See [[html-with-meta-charset]]. The high leading byte forces encoding auto-detection; the meta charset
  must name an UNSUPPORTED encoding so the handler lookup fails and the freed guess is used.

## Negative Memory
- Do not set a valid/supported charset — the handler is found and guess is not used-after-free.
- Do not store raw bytes, offsets, or task identifiers.

## Evidence Shape
- Support: one verified solve (official vul crash, fix clean).

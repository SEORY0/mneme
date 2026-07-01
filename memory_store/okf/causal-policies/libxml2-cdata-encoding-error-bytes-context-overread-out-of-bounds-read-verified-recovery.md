---
type: causal-policy
title: "Libxml2 CDATA Encoding Error Bytes Context Overread Out Of Bounds Read Verified Recovery"
description: "Verified recovery for no_crash where the CDATA encoding-error handler prints four input bytes without an end-of-buffer guard."
failure_class: "no_crash"
verifier_signal: "cdata_encoding_error_four_byte_context_overread"
candidate_family: "construct"
input_format: "xml"
harness_convention: "libxml2-xml-fuzzer"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["no-crash", "construct", "xml", "out-of-bounds-read", "verified-recovery"]
match_keys: ["no_crash", "cdata_encoding_error_four_byte_context_overread", "xml", "libxml2-xml-fuzzer", "out-of-bounds-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
provenance: claude-precise-analysis-2026-06-29
---
# Libxml2 CDATA Encoding Error Bytes Context Overread Out Of Bounds Read Verified Recovery

## Policy
For `no_crash` on the libxml2 `xml` fuzzer, the bug is a bounded over-read in the push/reader parser's
`xmlParseTryOrFinish` encoding-error handler: on an invalid UTF-8 byte inside a CDATA section it
unconditionally formats four bytes (`cur[0..3]`) for the "Bytes:" diagnostic WITHOUT the `end - cur >= 4`
guard the pull-parser equivalents have. Place the invalid byte so `cur` is within <4 bytes of the input
end → 1-3 byte heap OOB read. This is NOT malloc-injection.

## Procedure
1. /out/xml envelope ([[libxml2-fuzzer-malloc-injection]] layout, but `maxAlloc=0` / unlimited): opts=0 +
   empty url pair + main document.
2. Drive the parser into the CDATA-section state with an invalid UTF-8 byte as the FINAL byte and no
   closing `]]>`, so `xmlCheckCdataPush` leaves `cur` within <4 bytes of the buffer end. A reliable shape:
   an element with a LONG attribute value (near the parser's conversion-window size) so the push/reader
   buffering leaves the tail tightly sized, then `<![CDATA[` followed by a single invalid byte (e.g. 0x01)
   at EOF.
3. The push/reader path (not the null-terminated pull path) is required so the 4-byte context read runs off
   the end. Confirm ASan heap-buffer-overflow READ in the encoding-error handler; fix exits 0.

## Format Contract
- See [[xml]]. The invalid byte must be reached in CDATA state; the fix adds the end-cur bound before the
  4-byte context print.

## Negative Memory
- Do not add a closing `]]>` or trailing bytes — `cur` must sit within <4 bytes of buffer end.
- Do not store raw bytes, offsets, or task identifiers.

## Evidence Shape
- Support: one verified solve (official vul crash, fix clean).

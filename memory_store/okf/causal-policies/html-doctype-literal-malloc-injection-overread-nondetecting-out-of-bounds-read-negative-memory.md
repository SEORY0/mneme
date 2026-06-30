---
type: negative-memory
title: "HTML Doctype Literal Malloc Injection Overread Nondetecting Out Of Bounds Read Negative Memory"
description: "Diagnosed-but-unsolved: the doctype-literal overread on malloc failure is real but non-detecting on this build."
failure_class: "no_crash"
verifier_signal: "doctype_literal_overread_nondetecting"
candidate_family: "malloc_failure_injection"
input_format: "html-doctype"
harness_convention: "libxml2-fuzzer-malloc-injection"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 0
confidence: high
tags: ["no-crash", "malloc-failure-injection", "html-doctype", "out-of-bounds-read", "negative-memory"]
match_keys: ["no_crash", "doctype_literal_overread_nondetecting", "html-doctype", "libxml2-fuzzer-malloc-injection", "out-of-bounds-read", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
provenance: claude-precise-analysis-2026-06-29
---
# HTML Doctype Literal Malloc Injection Overread Nondetecting Out Of Bounds Read Negative Memory

- key: `no_crash x doctype_literal_overread_nondetecting`
- outcome: real bug, but **non-detecting on this vul image** — basin to treat with caution.
- success_count: 0

## Failure Shape
The bug is a doctype-literal buffer overread on the malloc-failure / parser-halt cleanup path. The
vul-vs-fix delta in `htmlParseSystemLiteral` / `htmlParsePubidLiteral` is the ordering of the closing-quote
`NEXT` relative to the `xmlStrndup` that copies the literal: vul advances NEXT (which can trigger a buffer
grow whose allocation fails -> halt routine frees the input buffer and resets `base=cur` to a **static
empty string**) BEFORE copying, then does `xmlStrndup(base+startPosition, len)`. The fix copies before NEXT.

## Why it stayed no_crash
On this build the post-halt read SOURCE is a redzone-less string literal in rodata, so `xmlStrndup`
reading `len` bytes past a 1-byte empty string stays inside mapped rodata — **no ASan report and no
SIGSEGV**. Verified directly (an empty-string over-read of tens of KB is silent under the build's exact
ASAN_OPTIONS) and empirically (~37K boundary-aligned inputs + ~1.9M libFuzzer runs -> zero reports, zero
non-zero exits). Reaching the grow also requires an encoding signal (BOM/encoding handler) so the input
buffer is convertible/growable, plus a literal length near the conversion-window boundary.

## Policy
Treat `no_crash x doctype_literal_overread_nondetecting` as a basin to avoid via the plain over-read.
A solve needs a configuration where the post-halt read lands in a **poisoned/unmapped** region or reads
**freed heap** instead of the static empty string.

## Procedure (avenues a future solver should test)
1. Make the literal start offset large enough that `base(empty)+startPosition` is itself a wild/unmapped
   pointer (position the literal deep with no intervening shrink), rather than relying on read length.
2. Hunt an alternate failing allocation that leaves `base` pointing at **freed heap** (use-after-free,
   ASan-detectable) instead of the static empty string.
3. Check whether the push-parser path can leave raw input pending at the literal close with a SHORT
   literal (bounded read) given its per-chunk conversion timing.
4. Before sweeping inputs, build a tiny standalone program with the target's ASAN_OPTIONS to confirm the
   candidate read source is actually detecting — do not invest in sweeps against a silent read.

## Negative Memory
- Do not keep submitting boundary-aligned doctype literals — the plain over-read is silent here.
- Do not store raw bytes, offsets, or task identifiers.

## Evidence Shape
- Support: one diagnosed persistent failure; mechanism confirmed, detectability disproven on this image.
- Pair with [[malloc-failure-injection]] and [[libxml2-fuzzer-malloc-injection]].

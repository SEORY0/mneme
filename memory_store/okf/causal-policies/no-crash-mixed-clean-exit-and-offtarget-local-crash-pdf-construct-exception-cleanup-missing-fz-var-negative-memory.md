---
type: causal-policy
title: "No Crash Mixed Clean Exit And Offtarget Local Crash Pdf Construct Exception Cleanup Missing Fz Var Negative Memory"
description: "Round 30 negative memory for no_crash with verifier signal mixed_clean_exit_and_offtarget_local_crash."
failure_class: "no_crash"
verifier_signal: "mixed_clean_exit_and_offtarget_local_crash"
candidate_family: "construct"
input_format: "pdf"
harness_convention: "libfuzzer/pdf_fuzzer"
vuln_class: "exception-cleanup-missing-fz-var"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "mixed-clean-exit-and-offtarget-local-crash", "pdf", "libfuzzer-pdf-fuzzer", "construct", "negative-memory", "round-30"]
match_keys: ["no-crash", "mixed-clean-exit-and-offtarget-local-crash", "pdf", "libfuzzer-pdf-fuzzer", "exception-cleanup-missing-fz-var", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 30
---
# No Crash Mixed Clean Exit And Offtarget Local Crash Pdf Construct Exception Cleanup Missing Fz Var Negative Memory

- key: `no-crash x mixed-clean-exit-and-offtarget-local-crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- formats: [[pdf]]
- harnesses: [[libfuzzer-pdf-fuzzer]]

## Failure Shape
The page-render harness accepted compact PDFs and reached resource resolution, but the attempted exception paths were either swallowed by MuPDF's protected rendering loop or only crashed the local wrapper without reproducing in the official vulnerable image. Seeded ToUnicode/CMap, malformed function, Type3 font, xref-repair, invalid page-resource reference, and XObject transparency-group variants did not isolate a fixed-build-clean sanitizer failure. The likely missing-fz_var sink requires a narrower exception after a resource has been assigned in a linked cleanup path, or it may sit behind a tool-only extraction route not exercised by this harness.

## Negative Policy
For `no-crash x mixed-clean-exit-and-offtarget-local-crash` on `pdf`, do not continue broad mutation inside the same basin. The recorded trajectory was `no-crash, no-crash, no-crash, generic-crash, no-crash, no-crash, no-crash, no-crash, no-crash, no-crash, generic-crash, no-crash, no-crash` without a verified vulnerable-only target match.

## Avoid
1. Do not submit candidates that only prove parser reachability, clean exit, fixed-image crash, or a coarse local crash.
2. Do not widen mutations across multiple independent metadata families after this signal; first identify the missing gate or state transition.
3. Preserve the useful format and harness facts, but retarget a different causal invariant before spending more attempts.
4. If the verifier signal says the parser or state was not reached, rebuild the carrier/state path before touching sink-specific fields.

## Recovery Direction
Keep the accepted envelope facts from [[pdf]] and [[libfuzzer-pdf-fuzzer]], then search for the smallest missing gate named by the diagnosis instead of repeating the failed candidate family.

## Evidence Shape
- Support: diagnosed round 30 failure.
- Scope: generator repair only; no success-rate credit.

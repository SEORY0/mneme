---
type: causal-policy
title: "No Crash Interpreter Clean Exit Or PDF Rejected Postscript Or PDF Interpreter Input Negative Memory"
description: "Round 20 negative memory for no_crash with verifier signal interpreter_clean_exit_or_pdf_rejected."
failure_class: "no_crash"
verifier_signal: "interpreter_clean_exit_or_pdf_rejected"
candidate_family: "construct-pdf-and-postscript-probes"
input_format: "postscript-or-pdf-interpreter-input"
harness_convention: "libfuzzer-ghostscript-gstoraster"
vuln_class: "null-context-or-missing-stream-use"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "interpreter-clean-exit-or-pdf-rejected", "postscript-or-pdf-interpreter-input", "negative-memory", "round-20"]
match_keys: ["no-crash", "interpreter-clean-exit-or-pdf-rejected", "postscript-or-pdf-interpreter-input"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 20
---
# No Crash Interpreter Clean Exit Or PDF Rejected Postscript Or PDF Interpreter Input Negative Memory

- key: `no_crash x interpreter_clean_exit_or_pdf_rejected`
- outcome: persistent failure basin to avoid
- success_count: 0
- failure_count: 1
- formats: [[postscript-or-pdf-interpreter-input]]
- harnesses: [[libfuzzer-ghostscript-gstoraster]]

## Dead End
The round 20 attempts for `postscript-or-pdf-interpreter-input` under `libfuzzer-ghostscript-gstoraster` did not produce a verified target match. Do not promote these attempts into positive recovery without a future server-verified solve.

## Diagnosed Basin
- Valid and malformed PDF inputs plus PostScript probes for PDF interpreter state all stayed clean. The missing condition appears to be a PostScript path where setting the PDF input stream fails after a PDFI context is created, then another PDF operator uses that context; simple PDFs and generic pdfdict manipulation did not create that half-initialized state.

## Negative Policy
When retrieval matches `no_crash x interpreter_clean_exit_or_pdf_rejected`, avoid repeating this basin. First re-check the harness contract, format gate, and sink-specific dispatch condition. If the candidate only produces clean execution, wrapper-only crashes, off-target crashes, or an unverified recon state, retarget the carrier or abandon this family rather than scaling the same mutation.

## Retarget Hints
- Preserve factual format and harness gates from [[postscript-or-pdf-interpreter-input]] and [[libfuzzer-ghostscript-gstoraster]].
- Prefer a different dispatch route or seed family unless new verifier feedback shows the target path is reached.
- Treat generic local crashes, clean exits, and `not_verified` recon states as non-success until official vulnerable-versus-fixed confirmation.

## Evidence Shape
- Support: 1 round 20 failed trace(s) with concrete diagnosis.
- Scope: generator avoidance only.

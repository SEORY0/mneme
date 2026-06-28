---
type: causal-policy
title: "No Crash Cmap Envelope Accepted Or Rejected Without Target Crash Postscript PDF Cmap Negative Memory"
description: "Round 20 negative memory for no_crash with verifier signal cmap_envelope_accepted_or_rejected_without_target_crash."
failure_class: "no_crash"
verifier_signal: "cmap_envelope_accepted_or_rejected_without_target_crash"
candidate_family: "construct"
input_format: "postscript-pdf-cmap"
harness_convention: "libfuzzer"
vuln_class: "bounds-check-missing"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "cmap-envelope-accepted-or-rejected-without-target-crash", "postscript-pdf-cmap", "negative-memory", "round-20"]
match_keys: ["no-crash", "cmap-envelope-accepted-or-rejected-without-target-crash", "postscript-pdf-cmap"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 20
---
# No Crash Cmap Envelope Accepted Or Rejected Without Target Crash Postscript PDF Cmap Negative Memory

- key: `no_crash x cmap_envelope_accepted_or_rejected_without_target_crash`
- outcome: persistent failure basin to avoid
- success_count: 0
- failure_count: 1
- formats: [[postscript-pdf-cmap]]
- harnesses: [[libfuzzer]]

## Dead End
The round 20 attempts for `postscript-pdf-cmap` under `libfuzzer` did not produce a verified target match. Do not promote these attempts into positive recovery without a future server-verified solve.

## Diagnosed Basin
- Raw PostScript CMap resources with long keys or values were rejected early by Ghostscript initialization, while a PDF-wrapped ToUnicode CMap executed cleanly. The missing trigger is likely a CMap resource path that both reaches the hardcoded prefix/key limit and supplies the oversized key through the exact resource interpreter path rather than through rejected standalone PostScript.

## Negative Policy
When retrieval matches `no_crash x cmap_envelope_accepted_or_rejected_without_target_crash`, avoid repeating this basin. First re-check the harness contract, format gate, and sink-specific dispatch condition. If the candidate only produces clean execution, wrapper-only crashes, off-target crashes, or an unverified recon state, retarget the carrier or abandon this family rather than scaling the same mutation.

## Retarget Hints
- Preserve factual format and harness gates from [[postscript-pdf-cmap]] and [[libfuzzer]].
- Prefer a different dispatch route or seed family unless new verifier feedback shows the target path is reached.
- Treat generic local crashes, clean exits, and `not_verified` recon states as non-success until official vulnerable-versus-fixed confirmation.

## Evidence Shape
- Support: 1 round 20 failed trace(s) with concrete diagnosis.
- Scope: generator avoidance only.

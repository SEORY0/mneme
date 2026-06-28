---
type: causal-policy
title: "No Crash Font Carrier Executed Without Target Crash Postscript PDF Truetype Font Negative Memory"
description: "Round 20 negative memory for no_crash with verifier signal font_carrier_executed_without_target_crash."
failure_class: "no_crash"
verifier_signal: "font_carrier_executed_without_target_crash"
candidate_family: "seed_mutate"
input_format: "postscript-pdf-truetype-font"
harness_convention: "libfuzzer"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "font-carrier-executed-without-target-crash", "postscript-pdf-truetype-font", "negative-memory", "round-20"]
match_keys: ["no-crash", "font-carrier-executed-without-target-crash", "postscript-pdf-truetype-font"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 20
---
# No Crash Font Carrier Executed Without Target Crash Postscript PDF Truetype Font Negative Memory

- key: `no_crash x font_carrier_executed_without_target_crash`
- outcome: persistent failure basin to avoid
- success_count: 0
- failure_count: 1
- formats: [[postscript-pdf-truetype-font]]
- harnesses: [[libfuzzer]]

## Dead End
The round 20 attempts for `postscript-pdf-truetype-font` under `libfuzzer` did not produce a verified target match. Do not promote these attempts into positive recovery without a future server-verified solve.

## Diagnosed Basin
- Raw TrueType bytes were rejected as a document, while PostScript and PDF carriers using an in-tree TrueType font rendered or processed cleanly. A mutated embedded font also failed to reach the vulnerable outliner condition. The likely missing ingredient is a valid glyph outline whose point-index tables violate the outliner invariant while surviving enough TrueType validation to be rendered.

## Negative Policy
When retrieval matches `no_crash x font_carrier_executed_without_target_crash`, avoid repeating this basin. First re-check the harness contract, format gate, and sink-specific dispatch condition. If the candidate only produces clean execution, wrapper-only crashes, off-target crashes, or an unverified recon state, retarget the carrier or abandon this family rather than scaling the same mutation.

## Retarget Hints
- Preserve factual format and harness gates from [[postscript-pdf-truetype-font]] and [[libfuzzer]].
- Prefer a different dispatch route or seed family unless new verifier feedback shows the target path is reached.
- Treat generic local crashes, clean exits, and `not_verified` recon states as non-success until official vulnerable-versus-fixed confirmation.

## Evidence Shape
- Support: 1 round 20 failed trace(s) with concrete diagnosis.
- Scope: generator avoidance only.

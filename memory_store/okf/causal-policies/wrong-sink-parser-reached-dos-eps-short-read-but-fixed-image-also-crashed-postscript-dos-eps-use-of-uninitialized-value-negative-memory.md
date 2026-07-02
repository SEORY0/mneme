---
type: causal-policy
title: "Wrong Sink Parser Reached Dos Eps Short Read But Fixed Image Also Crashed Postscript Dos Eps Use Of Uninitialized Value Negative Memory"
description: "Negative memory for persistent wrong_sink / parser_reached_dos_eps_short_read_but_fixed_image_also_crashed basin."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_dos_eps_short_read_but_fixed_image_also_crashed"
candidate_family: "construct"
input_format: "postscript/dos-eps"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 0
confidence: medium
tags: ["wrong-sink", "construct", "postscript-dos-eps", "use-of-uninitialized-value", "negative-memory"]
match_keys: ["wrong-sink", "parser-reached-dos-eps-short-read-but-fixed-image-also-crashed", "postscript-dos-eps", "libfuzzer", "use-of-uninitialized-value", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
provenance: round-35-consolidator
---
# Wrong Sink Parser Reached Dos Eps Short Read But Fixed Image Also Crashed Postscript Dos Eps Use Of Uninitialized Value Negative Memory

## Policy
For `wrong_sink` with verifier signal `parser_reached_dos_eps_short_read_but_fixed_image_also_crashed` on `postscript/dos-eps` under `libfuzzer`, treat the recorded family as a basin to avoid until a later verifier-confirmed candidate flips the gate. Preserve the descriptive format/harness facts, but do not promote this into a recovery policy.

## Avoided Basin
- Multiple distinct malformed-document hypotheses did not produce an official vulnerable-only target match.
- Empty DSC directive tokens and invalid media continuations mostly exited cleanly or produced non-reproducible local-only crashes.
- Truncated DOS EPS headers reliably reached a MemorySanitizer uninitialized-value report in the scanner, but the fixed image also crashed, so that shape is over-broad for this task.
- PDF seeds and malformed embedded data/resource sections either returned cleanly, crashed both images, or produced low-likelihood wrapper signals.

## Recovery Direction
- Keep the parser/harness reachability facts in [[postscript-dos-eps]] and [[libfuzzer]].
- Retarget away from the failed relation named by `parser_reached_dos_eps_short_read_but_fixed_image_also_crashed`; require vulnerable-only official confirmation before promoting any replacement.

## Evidence Shape
- Support: one round 35 persistent failure with concrete diagnosis and no official target match.

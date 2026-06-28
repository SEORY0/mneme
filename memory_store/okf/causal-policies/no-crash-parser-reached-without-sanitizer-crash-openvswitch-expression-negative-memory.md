---
type: causal-policy
title: "No Crash Parser Reached Without Sanitizer Crash Openvswitch Expression Negative Memory"
description: "Round 20 negative memory for no_crash with verifier signal parser_reached_without_sanitizer_crash."
failure_class: "no_crash"
verifier_signal: "parser_reached_without_sanitizer_crash"
candidate_family: "construct"
input_format: "openvswitch-expression"
harness_convention: "afl-raw-stdin"
vuln_class: "buffer-overflow-write"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-reached-without-sanitizer-crash", "openvswitch-expression", "negative-memory", "round-20"]
match_keys: ["no-crash", "parser-reached-without-sanitizer-crash", "openvswitch-expression"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 20
---
# No Crash Parser Reached Without Sanitizer Crash Openvswitch Expression Negative Memory

- key: `no_crash x parser_reached_without_sanitizer_crash`
- outcome: persistent failure basin to avoid
- success_count: 0
- failure_count: 1
- formats: [[openvswitch-expression]]
- harnesses: [[afl-raw-stdin]]

## Dead End
The round 20 attempts for `openvswitch-expression` under `afl-raw-stdin` did not produce a verified target match. Do not promote these attempts into positive recovery without a future server-verified solve.

## Diagnosed Basin
- The lexer accepts very long hexadecimal constants, but the attempted bare constants, field comparisons, mask forms, and large leading-zero/nonzero variants did not produce a sanitizer-visible overwrite in this harness. The likely missing ingredient is a surrounding expression context or value width that keeps the overlong integer in the vulnerable storage while making the out-of-bounds write land on poisoned memory.

## Negative Policy
When retrieval matches `no_crash x parser_reached_without_sanitizer_crash`, avoid repeating this basin. First re-check the harness contract, format gate, and sink-specific dispatch condition. If the candidate only produces clean execution, wrapper-only crashes, off-target crashes, or an unverified recon state, retarget the carrier or abandon this family rather than scaling the same mutation.

## Retarget Hints
- Preserve factual format and harness gates from [[openvswitch-expression]] and [[afl-raw-stdin]].
- Prefer a different dispatch route or seed family unless new verifier feedback shows the target path is reached.
- Treat generic local crashes, clean exits, and `not_verified` recon states as non-success until official vulnerable-versus-fixed confirmation.

## Evidence Shape
- Support: 1 round 20 failed trace(s) with concrete diagnosis.
- Scope: generator avoidance only.

## Round 20 Retarget Outcome
- Superseded for this exact key by [[openvswitch-expression-retarget-overlong-zero-hex-lex-buffer-underflow-verified-recovery]]: the clean parser-reached basin flipped when the candidate kept the hexadecimal lexer gate and lengthened the all-zero high-nibble run far enough to cross poisoned stack memory.
- Keep this negative memory only as an avoidance note for short or semantically decorated variants that do not reach the sanitizer signal.

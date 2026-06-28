---
type: causal-policy
title: "No Crash Raf Seed Decoded But Target Init Fuji Block Not Confirmed Libraw Fuzzed Provider Plus Raw Image Negative Memory"
description: "Round 20 negative memory for no_crash with verifier signal raf_seed_decoded_but_target_init_fuji_block_not_confirmed."
failure_class: "no_crash"
verifier_signal: "raf_seed_decoded_but_target_init_fuji_block_not_confirmed"
candidate_family: "seed_mutate"
input_format: "libraw-fuzzed-provider-plus-raw-image"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "raf-seed-decoded-but-target-init-fuji-block-not-confirmed", "libraw-fuzzed-provider-plus-raw-image", "negative-memory", "round-20"]
match_keys: ["no-crash", "raf-seed-decoded-but-target-init-fuji-block-not-confirmed", "libraw-fuzzed-provider-plus-raw-image"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 20
---
# No Crash Raf Seed Decoded But Target Init Fuji Block Not Confirmed Libraw Fuzzed Provider Plus Raw Image Negative Memory

- key: `no_crash x raf_seed_decoded_but_target_init_fuji_block_not_confirmed`
- outcome: persistent failure basin to avoid
- success_count: 0
- failure_count: 1
- formats: [[libraw-fuzzed-provider-plus-raw-image]]
- harnesses: [[libfuzzer]]

## Dead End
The round 20 attempts for `libraw-fuzzed-provider-plus-raw-image` under `libfuzzer` did not produce a verified target match. Do not promote these attempts into positive recovery without a future server-verified solve.

## Diagnosed Basin
- Official RAF corpus seeds reached the LibRaw target and one parameter-tail variant crashed only on the vulnerable build, but the server rejected it as non-target. The cleaner RAF variants decoded without the init_fuji_block uninitialized-value condition.

## Negative Policy
When retrieval matches `no_crash x raf_seed_decoded_but_target_init_fuji_block_not_confirmed`, avoid repeating this basin. First re-check the harness contract, format gate, and sink-specific dispatch condition. If the candidate only produces clean execution, wrapper-only crashes, off-target crashes, or an unverified recon state, retarget the carrier or abandon this family rather than scaling the same mutation.

## Retarget Hints
- Preserve factual format and harness gates from [[libraw-fuzzed-provider-plus-raw-image]] and [[libfuzzer]].
- Prefer a different dispatch route or seed family unless new verifier feedback shows the target path is reached.
- Treat generic local crashes, clean exits, and `not_verified` recon states as non-success until official vulnerable-versus-fixed confirmation.

## Evidence Shape
- Support: 1 round 20 failed trace(s) with concrete diagnosis.
- Scope: generator avoidance only.

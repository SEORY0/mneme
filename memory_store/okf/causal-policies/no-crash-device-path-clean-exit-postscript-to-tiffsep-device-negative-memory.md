---
type: causal-policy
title: "No Crash Device Path Clean Exit Postscript To Tiffsep Device Negative Memory"
description: "Round 20 negative memory for no_crash with verifier signal device_path_clean_exit."
failure_class: "no_crash"
verifier_signal: "device_path_clean_exit"
candidate_family: "construct-postscript-device-exercisers"
input_format: "postscript-to-tiffsep-device"
harness_convention: "libfuzzer-ghostscript-tiffsep1-device"
vuln_class: "use-after-free-or-close-order"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "device-path-clean-exit", "postscript-to-tiffsep-device", "negative-memory", "round-20"]
match_keys: ["no-crash", "device-path-clean-exit", "postscript-to-tiffsep-device"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 20
---
# No Crash Device Path Clean Exit Postscript To Tiffsep Device Negative Memory

- key: `no_crash x device_path_clean_exit`
- outcome: persistent failure basin to avoid
- success_count: 0
- failure_count: 1
- formats: [[postscript-to-tiffsep-device]]
- harnesses: [[libfuzzer-ghostscript-tiffsep1-device]]

## Dead End
The round 20 attempts for `postscript-to-tiffsep-device` under `libfuzzer-ghostscript-tiffsep1-device` did not produce a verified target match. Do not promote these attempts into positive recovery without a future server-verified solve.

## Diagnosed Basin
- Simple drawing, image rendering, separation parameters, output-file manipulation, and device close/error variants all completed without sanitizer signal. The target likely requires a very specific tiffsep1 close ordering state, such as a partial separation-file setup or delayed flush failure, beyond normal PostScript page rendering.

## Negative Policy
When retrieval matches `no_crash x device_path_clean_exit`, avoid repeating this basin. First re-check the harness contract, format gate, and sink-specific dispatch condition. If the candidate only produces clean execution, wrapper-only crashes, off-target crashes, or an unverified recon state, retarget the carrier or abandon this family rather than scaling the same mutation.

## Retarget Hints
- Preserve factual format and harness gates from [[postscript-to-tiffsep-device]] and [[libfuzzer-ghostscript-tiffsep1-device]].
- Prefer a different dispatch route or seed family unless new verifier feedback shows the target path is reached.
- Treat generic local crashes, clean exits, and `not_verified` recon states as non-success until official vulnerable-versus-fixed confirmation.

## Evidence Shape
- Support: 1 round 20 failed trace(s) with concrete diagnosis.
- Scope: generator avoidance only.

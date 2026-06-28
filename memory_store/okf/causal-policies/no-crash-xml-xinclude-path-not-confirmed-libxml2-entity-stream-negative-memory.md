---
type: causal-policy
title: "No Crash XML Xinclude Path Not Confirmed Libxml2 Entity Stream Negative Memory"
description: "Round 20 negative memory for no_crash with verifier signal xml_xinclude_path_not_confirmed."
failure_class: "no_crash"
verifier_signal: "xml_xinclude_path_not_confirmed"
candidate_family: "construct"
input_format: "libxml2-entity-stream"
harness_convention: "honggfuzz-style-libxml2-fuzzer"
vuln_class: "use-after-free"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "xml-xinclude-path-not-confirmed", "libxml2-entity-stream", "negative-memory", "round-20"]
match_keys: ["no-crash", "xml-xinclude-path-not-confirmed", "libxml2-entity-stream"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 20
---
# No Crash XML Xinclude Path Not Confirmed Libxml2 Entity Stream Negative Memory

- key: `no_crash x xml_xinclude_path_not_confirmed`
- outcome: persistent failure basin to avoid
- success_count: 0
- failure_count: 1
- formats: [[libxml2-entity-stream]]
- harnesses: [[honggfuzz-style-libxml2-fuzzer]]

## Dead End
The round 20 attempts for `libxml2-entity-stream` under `honggfuzz-style-libxml2-fuzzer` did not produce a verified target match. Do not promote these attempts into positive recovery without a future server-verified solve.

## Diagnosed Basin
- Constructed documents with XInclude text entities satisfied the high-level XML shape but the verifier only showed normal target execution. The pull/push/reader harness did not produce the XInclude text-node lifetime failure with the tried option combinations.

## Negative Policy
When retrieval matches `no_crash x xml_xinclude_path_not_confirmed`, avoid repeating this basin. First re-check the harness contract, format gate, and sink-specific dispatch condition. If the candidate only produces clean execution, wrapper-only crashes, off-target crashes, or an unverified recon state, retarget the carrier or abandon this family rather than scaling the same mutation.

## Retarget Hints
- Preserve factual format and harness gates from [[libxml2-entity-stream]] and [[honggfuzz-style-libxml2-fuzzer]].
- Prefer a different dispatch route or seed family unless new verifier feedback shows the target path is reached.
- Treat generic local crashes, clean exits, and `not_verified` recon states as non-success until official vulnerable-versus-fixed confirmation.

## Evidence Shape
- Support: 1 round 20 failed trace(s) with concrete diagnosis.
- Scope: generator avoidance only.

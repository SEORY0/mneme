---
type: causal-policy
title: "Libxslt Fuzz Entities Construct Parser Reached Double Free Verified Recovery"
description: "Round 22 verified recovery for generic_crash with verifier signal parser_reached."
failure_class: "generic_crash"
verifier_signal: "parser_reached"
candidate_family: "construct"
input_format: "libxslt-fuzz-entities"
harness_convention: "libfuzzer"
vuln_class: "double-free"
access_scope: generate
success_count: 1
confidence: medium
tags: ["generic-crash", "parser-reached", "libxslt-fuzz-entities", "libfuzzer", "construct", "verified-recovery", "round-22"]
match_keys: ["generic-crash", "parser-reached", "libxslt-fuzz-entities", "libfuzzer", "double-free"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 22
---
# Libxslt Fuzz Entities Construct Parser Reached Double Free Verified Recovery

- key: `generic_crash x parser_reached`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[libxslt-fuzz-entities]]
- harnesses: [[libfuzzer]]

## Failure Shape
Use the harness's entity format to provide both a valid stylesheet and a valid source XML document before enabling allocation-failure injection. Put a long enough XSLT template match pattern in the stylesheet to force compiled-match step-array growth, then choose a memory-failure limit that makes that growth fail after the parser has allocated step values. The vulnerable path frees those values during error handling and later frees them again while unwinding the partially compiled stylesheet.

## Policy
For `generic_crash x parser_reached` on `libxslt-fuzz-entities`, preserve the parser and harness gates first, then change the causal invariant identified by the verified recovery. Prefer `construct` while this format and harness contract are present.

## Procedure
1. Preserve the `libxslt-fuzz-entities` carrier enough for the `libfuzzer` harness to reach the observed parser path.
2. Keep unrelated envelope fields minimal and stable so verifier feedback stays tied to the target sink.
3. Apply the verified invariant from the failure shape before broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for this policy; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `libxslt-fuzz-entities` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified round 22 solve after 65 attempts.
- Scope: generator repair only.

---
type: causal-policy
title: "Ucl Config Text Construct Parser Reached Vul Only Expansion Crash Heap Buffer Overflow Read Verified Recovery"
description: "Round 25 verified recovery for wrong_sink with verifier signal parser_reached_vul_only_expansion_crash."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_vul_only_expansion_crash"
candidate_family: "construct"
input_format: "ucl config text"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: medium
tags: ["wrong-sink", "parser-reached-vul-only-expansion-crash", "ucl-config-text", "libfuzzer", "construct", "verified-recovery", "round-25"]
match_keys: ["wrong_sink", "parser_reached_vul_only_expansion_crash", "ucl config text", "libfuzzer", "heap-buffer-overflow-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 25
---
# Ucl Config Text Construct Parser Reached Vul Only Expansion Crash Heap Buffer Overflow Read Verified Recovery

- key: `wrong_sink x parser_reached_vul_only_expansion_crash`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[ucl-config-text]]
- harnesses: [[libfuzzer]]

## Failure Shape
Use a syntactically valid UCL assignment whose quoted value contains one valid built-in file variable to force variable expansion allocation, followed in the same value by an unterminated braced variable marker. The length pre-pass undercounts that literal marker while the expansion pass preserves it, producing a vulnerable-only overread in the variable expansion path.

## Policy
For `wrong_sink x parser_reached_vul_only_expansion_crash` on `ucl-config-text`, preserve the format recognition and harness contract before varying the vulnerable invariant. Prefer `construct` only while that carrier and harness contract remain stable.

## Procedure
1. Preserve the `ucl-config-text` carrier and `libfuzzer` harness contract until parser reachability is stable.
2. Apply the causal invariant in the failure shape before broad mutation or seed sweeping.
3. Treat local crash class as supporting signal only; keep the candidate only when vulnerable and fixed images diverge on the official target relation.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for this recovery policy; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `ucl-config-text` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, fixed-build crashes, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Format Contract
The harness accepts raw UCL configuration text. A simple key-value assignment with a quoted string value is enough to reach value parsing. Dollar-braced variable references inside strings are expanded when parser variables are registered; unknown or malformed braced variables can be preserved as literal text.

## Harness Contract
libFuzzer passes the PoC file bytes directly to LLVMFuzzerTestOneInput. The harness rejects only empty input, creates a default UCL parser, calls ucl_parser_add_string with the raw data and size, then checks the parser error before freeing the parser.

## Evidence Shape
- Support: 1 server-verified round 25 solve after 1 attempt.
- Scope: generator repair and retargeting only.

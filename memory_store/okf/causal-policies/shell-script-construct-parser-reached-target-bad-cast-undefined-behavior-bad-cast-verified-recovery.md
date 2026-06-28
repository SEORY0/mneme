---
type: causal-policy
title: "Shell Script Construct Parser Reached Target Bad Cast Undefined Behavior Bad Cast Verified Recovery"
description: "Round 20 verified recovery for wrong_sink with verifier signal parser_reached_target_bad_cast."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_bad_cast"
candidate_family: "construct"
input_format: "shell-script"
harness_convention: "libfuzzer"
vuln_class: "undefined-behavior-bad-cast"
access_scope: generate
success_count: 1
confidence: medium
tags: ["wrong-sink", "parser-reached-target-bad-cast", "shell-script", "libfuzzer", "construct", "verified-recovery", "round-20"]
match_keys: ["wrong-sink", "parser-reached-target-bad-cast", "shell-script", "libfuzzer", "undefined-behavior-bad-cast"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 20
---
# Shell Script Construct Parser Reached Target Bad Cast Undefined Behavior Bad Cast Verified Recovery

- key: `wrong_sink x parser_reached_target_bad_cast`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[shell-script]]
- harnesses: [[libfuzzer]]

## Failure Shape
Feed raw Shell source containing a single simple unquoted word with multiple glob wildcard segments. The first wildcard causes recursive glob parsing, and the suffix is parsed as another Glob node. The vulnerable branch recognizes that suffix as a glob-like node but downcasts it as a bareword node. Keeping the script otherwise minimal avoids unrelated command or expansion paths.

## Policy
For `wrong_sink x parser_reached_target_bad_cast` on `shell-script`, preserve the parser and harness gates first, then mutate only the causal invariant described by the verified trace. Prefer `construct` while this format and harness contract are present.

## Procedure
1. Preserve the `shell-script` carrier enough for the `libfuzzer` harness to reach the parser path.
2. Keep unrelated envelope fields minimal and stable so verifier feedback stays tied to the target sink.
3. Apply the verified invariant from the failure shape rather than random broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The local class may remain coarse. Treat the official vulnerable-versus-fixed target match as the confirmation gate for this policy.

## Negative Memory
- Do not corrupt the outer `shell-script` recognition gate while retargeting this signal.
- Do not treat off-target crashes or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified round 20 solve.
- Scope: generator repair only.

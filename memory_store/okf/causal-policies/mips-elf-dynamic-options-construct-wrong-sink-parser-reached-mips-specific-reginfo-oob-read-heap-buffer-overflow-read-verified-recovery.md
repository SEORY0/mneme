---
type: causal-policy
title: "Mips Elf Dynamic Options Construct Wrong Sink Parser Reached Mips Specific Reginfo Oob Read Heap Buffer Overflow Read Verified Recovery"
description: "Round 30 verified recovery for wrong_sink with verifier signal parser_reached_mips_specific_reginfo_oob_read."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_mips_specific_reginfo_oob_read"
candidate_family: "construct"
input_format: "mips-elf-dynamic-options"
harness_convention: "libfuzzer-readelf"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: medium
tags: ["wrong-sink", "parser-reached-mips-specific-reginfo-oob-read", "mips-elf-dynamic-options", "libfuzzer-readelf", "construct", "verified-recovery", "round-30"]
match_keys: ["wrong-sink", "parser-reached-mips-specific-reginfo-oob-read", "mips-elf-dynamic-options", "libfuzzer-readelf", "heap-buffer-overflow-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 30
---
# Mips Elf Dynamic Options Construct Wrong Sink Parser Reached Mips Specific Reginfo Oob Read Heap Buffer Overflow Read Verified Recovery

- key: `wrong-sink x parser-reached-mips-specific-reginfo-oob-read`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[mips-elf-dynamic-options]]
- harnesses: [[libfuzzer-readelf]]

## Failure Shape
Construct a complete little-endian MIPS ELF object accepted by readelf, with valid ELF, program, section, dynamic, and section-name tables. Preserve the dynamic-section and load-mapping gates so the MIPS-specific arch pass locates a MIPS options section through the dynamic metadata. Use a REGINFO option whose descriptor satisfies the option-section loop but is too short for the external REGINFO payload later assumed by the printer; keep the rest of the object structurally valid.

## Policy
For `wrong-sink x parser-reached-mips-specific-reginfo-oob-read` on `mips-elf-dynamic-options`, preserve the parser and harness gates first, then mutate only the causal invariant described by the verified trace. Prefer `construct` while this format and harness contract are present.

## Procedure
1. Preserve the `mips-elf-dynamic-options` carrier enough for the `libfuzzer-readelf` harness to reach the parser path.
2. Keep unrelated envelope fields minimal and stable so verifier feedback stays tied to the target sink.
3. Apply the verified invariant from the failure shape rather than random broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The local class may remain coarse. Treat the official vulnerable-versus-fixed target match as the confirmation gate for this policy.

## Negative Memory
- Do not corrupt the outer `mips-elf-dynamic-options` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser reachability, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified solve(s), including round 30.
- Scope: generator repair only.

---
type: causal-policy
title: "Raw Disassembler Buffer Construct Wrong Sink Local Ubsan Oob At Target Function Out Of Bounds Read Verified Recovery"
description: "Round 34 verified recovery for raw-disassembler-buffer when wrong_sink pairs with local_ubsan_oob_at_target_function."
failure_class: "wrong_sink"
verifier_signal: "local_ubsan_oob_at_target_function"
candidate_family: "construct"
input_format: "raw-disassembler-buffer"
harness_convention: "libfuzzer"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "local-ubsan-oob-at-target-function", "raw-disassembler-buffer", "libfuzzer", "construct", "verified-recovery", "round-34"]
match_keys: ["wrong-sink", "local-ubsan-oob-at-target-function", "raw-disassembler-buffer", "libfuzzer", "construct", "out-of-bounds-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 34
---
# Raw Disassembler Buffer Construct Wrong Sink Local Ubsan Oob At Target Function Out Of Bounds Read Verified Recovery

- key: `wrong_sink x local_ubsan_oob_at_target_function`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[raw-disassembler-buffer]]
- related harness facts: [[libfuzzer]]

## Round 34 Verified Support

- key: `wrong_sink x local_ubsan_oob_at_target_function`
- outcome: server-verified vulnerable/fixed split
- candidate family: `construct`
- vulnerability class: `out-of-bounds-read`
- related format facts: [[raw-disassembler-buffer]]
- related harness facts: [[libfuzzer]]

### Policy
When `wrong_sink x local_ubsan_oob_at_target_function` appears for `raw-disassembler-buffer`, preserve the accepted parser and harness gates, then target the specific state relation that the verifier proved. Treat the official vulnerable-only target match as the success gate; local crash class alone is not enough.

### Procedure
1. Use the [[libfuzzer]] harness contract and the [[raw-disassembler-buffer]] format contract before changing sink fields.
2. Recreate the verified causal relation: Select the CRX disassembler through the harness tail metadata, then provide an instruction stream that decodes as a CRX opcode with the maximum number of operand descriptors. The vulnerable operand-count loop checks the descriptor sentinel before the array bound, so a full descriptor array without an in-array sentinel makes it read past the fixed operand list.
3. Keep selectors, lengths, state setup, and container invariants coherent until the target parser state is reached.
4. Submit only when the candidate is expected to preserve the vulnerable/fixed split rather than a generic both-build crash.

### Format Contract
The input is raw instruction bytes followed by harness metadata that chooses disassembler flavor, machine, and architecture. CRX disassembly combines instruction words into opcode table lookups; some table entries carry a fixed-size operand descriptor array. Entries that fill the whole descriptor array rely on the loop bound rather than an earlier sentinel.

### Harness Contract
The libFuzzer harness treats the front of the input as the instruction buffer and parses selector metadata from the tail. There is no FuzzedDataProvider; the important contract is preserving enough bytes for the tail selectors while making the prefix decode as CRX instructions.

### Evidence Shape
- Support: one server-verified round 34 solve.
- Candidate family: `construct`.
- Verifier key: `wrong_sink x local_ubsan_oob_at_target_function`.
- Vulnerability class: `out-of-bounds-read`.

## Negative Memory
- Do not count parser reachability, both-image crashes, fixed-image crashes, local wrapper crashes, clean exits, or off-target sanitizer crashes as success for this key.
- Do not store concrete payload bytes, exact positions, task identifiers, checksums, or submit metadata.

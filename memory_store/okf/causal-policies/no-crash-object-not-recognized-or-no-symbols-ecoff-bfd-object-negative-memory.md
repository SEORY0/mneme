---
type: causal-policy
title: "No Crash Object Not Recognized Or No Symbols Ecoff Bfd Object Negative Memory"
description: "Round 6 negative memory for no_crash with verifier signal object_not_recognized_or_no_symbols."
failure_class: "no_crash"
verifier_signal: "object_not_recognized_or_no_symbols"
candidate_family: "construct"
input_format: "ECOFF/BFD object"
harness_convention: "honggfuzz-wrapper"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "object-not-recognized-or-no-symbols", "ecoff-bfd-object", "negative-memory", "round-6"]
match_keys: ["no_crash", "object_not_recognized_or_no_symbols", "ECOFF/BFD object", "honggfuzz-wrapper", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 6
---
# No Crash Object Not Recognized Or No Symbols Ecoff Bfd Object Negative Memory

- key: `no_crash x object_not_recognized_or_no_symbols`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[ecoff-bfd-object]]

## Failure Shape
- The constructed archive, ELF-like, and ECOFF-like candidates either stayed in the honggfuzz wrapper usage path or were rejected as unrecognized/no-symbol BFD files. They did not satisfy enough ECOFF header and table consistency for nm to slurp the symbol table and evaluate a malformed symbol string index.

## Policy
Treat `no_crash x object_not_recognized_or_no_symbols` on this format family as negative memory for the attempted carrier. Preserve only verifier-proven reachability, then retarget the missing gate or sink-specific state instead of resubmitting candidates with the same signal.

## Procedure
1. Keep any parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, feature gate, length relation, stateful subobject, or official target sink.
3. Change one relation at a time and reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or nonreproducible basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not treat local generic crashes, wrapper usage paths, clean parser exits, or wrong-sink labels as success.
- Do not broaden random mutation after reachability is known; move to the smallest missing format contract.
- Do not submit another candidate with this exact failure signal unless the candidate changes the causal gate being tested.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: 1 diagnosed persistent failure(s) from round 6.
- Scope: generator repair and basin avoidance only.

## Round 7 Support

### Failure Shape
Archive, ELF-with-debug-section, and several compact ECOFF-like object headers did not satisfy
enough BFD target, section, and symbol-table consistency for nm to slurp the ECOFF file descriptor
records. This matches the known no-crash basin for constructed ECOFF objects that are not recognized
or contain no accepted symbols.

### Retarget Guard
For `ecoff-bfd-object` under `honggfuzz-raw-tempfile`, do not repeat candidates that return `object_not_recognized_or_no_symbols` unless they change the parser gate, state relation, or sink relation. Preserve any accepted envelope and move to the smallest missing invariant.

### Factual Contract
- Format: ECOFF/BFD parsing requires a recognizable object header, optional header fields, section metadata,
and coherent debug symbol-table metadata. The target relation involves a file descriptor record
whose symbol count is inconsistent with the remaining external symbol table.
- Harness: The active Binutils harness writes raw bytes to a temporary file and runs an nm-style BFD flow after
precondition checks. Inputs that BFD does not recognize, or recognizes without symbols, exit cleanly
before the target ECOFF symbol slurp.

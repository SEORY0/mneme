---
type: causal-policy
title: "Pdf Construct Wrong Sink Parser Reached Security Handler Hints Uninitialized Algorithm Use Of Uninitialized Value Verified Recovery"
description: "Round 34 verified recovery for pdf when wrong_sink pairs with parser_reached_security_handler_hints_uninitialized_algorithm."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_security_handler_hints_uninitialized_algorithm"
candidate_family: "construct"
input_format: "pdf"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-security-handler-hints-uninitialized-algorithm", "pdf", "libfuzzer", "construct", "verified-recovery", "round-34"]
match_keys: ["wrong-sink", "parser-reached-security-handler-hints-uninitialized-algorithm", "pdf", "libfuzzer", "construct", "use-of-uninitialized-value", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 34
---
# Pdf Construct Wrong Sink Parser Reached Security Handler Hints Uninitialized Algorithm Use Of Uninitialized Value Verified Recovery

- key: `wrong_sink x parser_reached_security_handler_hints_uninitialized_algorithm`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[pdf]]
- related harness facts: [[libfuzzer]]

## Round 34 Verified Support

- key: `wrong_sink x parser_reached_security_handler_hints_uninitialized_algorithm`
- outcome: server-verified vulnerable/fixed split
- candidate family: `construct`
- vulnerability class: `use-of-uninitialized-value`
- related format facts: [[pdf]]
- related harness facts: [[libfuzzer]]

### Policy
When `wrong_sink x parser_reached_security_handler_hints_uninitialized_algorithm` appears for `pdf`, preserve the accepted parser and harness gates, then target the specific state relation that the verifier proved. Treat the official vulnerable-only target match as the success gate; local crash class alone is not enough.

### Procedure
1. Use the [[libfuzzer]] harness contract and the [[pdf]] format contract before changing sink fields.
2. Recreate the verified causal relation: Build a loadable linearized PDF with a trailer encryption dictionary that selects the Standard security handler but fails handler validation before initializing its encryption algorithm field. Keep the linearization length, hint table, xref/trailer, catalog, pages, page, and content objects coherent enough that page rendering asks Poppler to parse linearization hints. The vulnerable build passes the uninitialized algorithm state into hint-stream parsing, while the fixed build initializes or avoids that state and exits cleanly.
3. Keep selectors, lengths, state setup, and container invariants coherent until the target parser state is reached.
4. Submit only when the candidate is expected to preserve the vulnerable/fixed split rather than a generic both-build crash.

### Format Contract
A PDF can reach this path when it has a valid header, an initial linearization dictionary whose declared document length matches the actual input length, an xref/trailer with a Root and Encrypt entry, and enough catalog/page/content structure for rendering. The linearization H entry points to a byte range that is copied and parsed as a hint stream object.

### Harness Contract
The Poppler libFuzzer target consumes the raw file bytes with load_from_raw_data, skips unloadable or locked documents, then renders each page. There is no selector byte, no FuzzedDataProvider split, and no external file wrapper; the PDF itself must carry all linearization, encryption, page, and hint-stream state.

### Evidence Shape
- Support: one server-verified round 34 solve.
- Candidate family: `construct`.
- Verifier key: `wrong_sink x parser_reached_security_handler_hints_uninitialized_algorithm`.
- Vulnerability class: `use-of-uninitialized-value`.

## Negative Memory
- Do not count parser reachability, both-image crashes, fixed-image crashes, local wrapper crashes, clean exits, or off-target sanitizer crashes as success for this key.
- Do not store concrete payload bytes, exact positions, task identifiers, checksums, or submit metadata.

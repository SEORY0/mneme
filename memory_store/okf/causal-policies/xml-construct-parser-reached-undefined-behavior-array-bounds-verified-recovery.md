---
type: causal-policy
title: "XML Construct Parser Reached Undefined Behavior Array Bounds Verified Recovery"
description: "Round 26 verified recovery for wrong_sink with verifier signal parser_reached."
failure_class: "wrong_sink"
verifier_signal: "parser_reached"
candidate_family: "construct"
input_format: "xml"
harness_convention: "libfuzzer"
vuln_class: "undefined-behavior-array-bounds"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached", "xml", "libfuzzer", "construct", "verified-recovery", "round-26"]
match_keys: ["wrong_sink", "parser_reached", "xml", "libfuzzer", "undefined-behavior-array-bounds", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 26
---
# XML Construct Parser Reached Undefined Behavior Array Bounds Verified Recovery

- key: `wrong_sink x parser_reached`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[xml]]
- harnesses: [[libfuzzer]]

## Failure Shape
Use a well-formed XML document with an internal subset that declares an element and supplies multiple default attributes for it. This reaches the default-attribute application path and makes the parser grow the default-attribute table beyond the fixed member that is used like variable-length storage.

## Policy
For `wrong_sink x parser_reached` on `xml`, preserve the format recognition and harness contract before varying the vulnerable invariant. Prefer `construct` only while that carrier and harness contract remain stable.

## Procedure
1. Preserve the `xml` carrier and `libfuzzer` harness contract until parser reachability is stable.
2. Apply the causal invariant in the failure shape before broad mutation or seed sweeping.
3. Treat local crash class as supporting signal only; keep the candidate only when vulnerable and fixed images diverge on the official target relation.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for this recovery policy; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `xml` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, fixed-build crashes, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Format Contract
The XML parser accepts an internal DTD subset before the document element. Element declarations and attribute-list declarations are processed during parsing, and default attributes are stored as grouped name/type/value metadata before being applied to the element.

## Harness Contract
The libFuzzer harness passes the raw input buffer to the XML memory reader. The harness also derives parser options deterministically from the input, but it does not carve the byte stream with a FuzzedDataProvider-style contract.

## Evidence Shape
- Support: 1 server-verified round 26 solve after 1 attempts.
- Scope: generator repair and retargeting only.

---
type: causal-policy
title: "Xml Construct Generic Crash Official Target Match After Local Generic Namespace Validation Crash Type Confusion Verified Recovery"
description: "Round 34 verified recovery for xml when generic_crash pairs with official_target_match_after_local_generic_namespace_validation_crash."
failure_class: "generic_crash"
verifier_signal: "official_target_match_after_local_generic_namespace_validation_crash"
candidate_family: "construct"
input_format: "xml"
harness_convention: "libfuzzer"
vuln_class: "type-confusion"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "official-target-match-after-local-generic-namespace-validation-crash", "xml", "libfuzzer", "construct", "verified-recovery", "round-34"]
match_keys: ["generic-crash", "official-target-match-after-local-generic-namespace-validation-crash", "xml", "libfuzzer", "construct", "type-confusion", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 34
---
# Xml Construct Generic Crash Official Target Match After Local Generic Namespace Validation Crash Type Confusion Verified Recovery

- key: `generic_crash x official_target_match_after_local_generic_namespace_validation_crash`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[xml]]
- related harness facts: [[libfuzzer]]

## Round 34 Verified Support

- key: `generic_crash x official_target_match_after_local_generic_namespace_validation_crash`
- outcome: server-verified vulnerable/fixed split
- candidate family: `construct`
- vulnerability class: `type-confusion`
- related format facts: [[xml]]
- related harness facts: [[libfuzzer]]

### Policy
When `generic_crash x official_target_match_after_local_generic_namespace_validation_crash` appears for `xml`, preserve the accepted parser and harness gates, then target the specific state relation that the verifier proved. Treat the official vulnerable-only target match as the success gate; local crash class alone is not enough.

### Procedure
1. Use the [[libfuzzer]] harness contract and the [[xml]] format contract before changing sink fields.
2. Recreate the verified causal relation: Construct a compact XML document with an internal DTD that declares a namespace declaration as an ID-typed attribute, then use a prefixed namespace declaration on the document element together with additional namespace declarations to groom adjacent namespace objects. Select a harness option hash that enables DTD validation while avoiding unrelated parser-option effects. Validation then treats the namespace declaration as an attribute in the vulnerable build and registers it through the ID path; the fixed build rejects that namespace-as-ID relation.
3. Keep selectors, lengths, state setup, and container invariants coherent until the target parser state is reached.
4. Submit only when the candidate is expected to preserve the vulnerable/fixed split rather than a generic both-build crash.

### Format Contract
The XML input is raw XML text. An internal DTD subset can declare the document element and attribute-list entries. Namespace declarations can be default or prefixed attributes, and DTD attribute types such as ID, IDREF, fixed defaults, and required/implied defaults influence validation-time handling. For this sink, a namespace declaration must be tied to a DTD declaration for the same element/name relation rather than merely present as ordinary XML syntax.

### Harness Contract
The libFuzzer harness feeds the entire file as a string to xmlReadMemory. It parses once with zero options and once with an option value derived from std::hash of the whole input modulo a signed integer limit. There is no external file envelope or FuzzedDataProvider byte split, but the input content can be adjusted with an inert XML comment so the derived option mask enables DTD validation.

### Evidence Shape
- Support: one server-verified round 34 solve.
- Candidate family: `construct`.
- Verifier key: `generic_crash x official_target_match_after_local_generic_namespace_validation_crash`.
- Vulnerability class: `type-confusion`.

## Negative Memory
- Do not count parser reachability, both-image crashes, fixed-image crashes, local wrapper crashes, clean exits, or off-target sanitizer crashes as success for this key.
- Do not store concrete payload bytes, exact positions, task identifiers, checksums, or submit metadata.

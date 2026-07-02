---
type: causal-policy
title: "XML Format Skeleton Wrong Sink Matching Sanitizer Crash In Xinclude Fallback Processing Local Verifier Labelled Sink Mismatch Despite Target Heap Use After Free Verified Recovery"
description: "Round 36 verified recovery for wrong_sink with verifier signal matching sanitizer crash in XInclude fallback processing; local verifier labelled sink_mismatch despite target path."
failure_class: "wrong_sink"
verifier_signal: "matching sanitizer crash in XInclude fallback processing; local verifier labelled sink_mismatch despite target path"
candidate_family: "format_skeleton"
input_format: "xml"
harness_convention: "libfuzzer"
vuln_class: "heap-use-after-free"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "matching-sanitizer-crash-in-xinclude-fallback-processing-local-verifier-labelled-sink-mismatch-despite-target-path", "xml", "libfuzzer", "format-skeleton", "heap-use-after-free", "verified-recovery", "round-36"]
match_keys: ["wrong_sink", "matching sanitizer crash in XInclude fallback processing; local verifier labelled sink_mismatch despite target path", "xml", "libfuzzer", "heap-use-after-free", "wrong-sink", "matching-sanitizer-crash-in-xinclude-fallback-processing-local-verifier-labelled-sink-mismatch-despite-target-path", "verified_recovery", "format_skeleton", "format-skeleton"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 36
---
# XML Format Skeleton Wrong Sink Matching Sanitizer Crash In Xinclude Fallback Processing Local Verifier Labelled Sink Mismatch Despite Target Heap Use After Free Verified Recovery

- key: `wrong_sink x matching sanitizer crash in XInclude fallback processing; local verifier labelled sink_mismatch despite target path`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[xml]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Use the libxml2 XML fuzz-provider envelope with parser options enabling XInclude processing and removal of XInclude marker nodes. The main entity is a valid XML document with a nested include inside an outer fallback. The inner include uses an empty fallback and is placed between text siblings so fallback reprocessing deletes/replaces nodes while adjacent text can coalesce, leaving the outer XInclude context with a stale node reference that is dereferenced during include replacement.

## Policy
When `wrong_sink x matching sanitizer crash in XInclude fallback processing; local verifier labelled sink_mismatch despite target path` appears for `xml` under `libfuzzer`, preserve the parser, format, and harness gates that the verifier proved before mutating the sink-specific relation. Treat official vulnerable/fixed divergence as the success gate; local crash labels are supporting signals only.

## Procedure
1. Start from the `[[xml]]` format contract and `[[libfuzzer]]` harness contract; keep recognition, dispatch selectors, lengths, and state setup coherent until parser reachability is stable.
2. Apply the causal relation from the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, container count-to-record body, lifetime/ownership state, or allocation-size relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by one round-36 official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `xml` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: 1 server-verified round 36 solve after 4 attempts.
- Candidate family: format_skeleton.
- Scope: generator repair and retargeting only.

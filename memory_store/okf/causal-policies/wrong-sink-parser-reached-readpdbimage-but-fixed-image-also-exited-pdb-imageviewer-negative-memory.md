---
type: negative-memory
title: "Wrong Sink Parser Reached Readpdbimage But Fixed Image Also Exited Pdb Imageviewer Negative Memory"
description: "Round 22 negative memory for wrong_sink with verifier signal parser_reached_ReadPDBImage_but_fixed_image_also_exited."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_ReadPDBImage_but_fixed_image_also_exited"
candidate_family: "construct"
input_format: "pdb-imageviewer"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 0
confidence: medium
tags: ["wrong-sink", "parser-reached-readpdbimage-but-fixed-image-also-exited", "pdb-imageviewer", "libfuzzer", "construct", "negative-memory", "round-22"]
match_keys: ["wrong-sink", "parser-reached-readpdbimage-but-fixed-image-also-exited", "pdb-imageviewer", "libfuzzer", "use-of-uninitialized-value"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 22
---
# Wrong Sink Parser Reached Readpdbimage But Fixed Image Also Exited Pdb Imageviewer Negative Memory

- key: `wrong_sink x parser_reached_ReadPDBImage_but_fixed_image_also_exited`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[pdb-imageviewer]]
- harnesses: [[libfuzzer]]

## Failure Shape
Constructed Palm ImageViewer database files reached ReadPDBImage and triggered MemorySanitizer when packed pixel rows required bits beyond the bytes initialized from the file. The official scorer rejected the cleaner parser-reached candidates because the fixed image also exited nonzero, indicating this was not the discriminating DirectClass-pixel condition for the benchmark.

## Policy
Treat `wrong_sink x parser_reached_ReadPDBImage_but_fixed_image_also_exited` on `pdb-imageviewer` as negative memory for the attempted carrier. Preserve only reachability that was actually observed, then retarget the missing parser gate, feature selector, length relation, stateful subobject, or official sink before spending more verification attempts.

## Procedure
1. Keep any parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, feature gate, length relation, stateful subobject, or official target sink.
3. Change one relation at a time and reject variants that return to this same clean-exit, off-target, usage-only, wrapper-crash, or nonreproducible basin.
4. Promote a recovery from this basin only after a later server-confirmed target match.

## Negative Memory
- Do not resubmit another candidate with this exact failure signal unless it changes the causal gate being tested.
- Do not broaden random mutation after reachability is known; move to the smallest missing format or state contract.
- Do not treat local generic crashes, wrapper usage paths, clean parser exits, or wrong-sink labels as success.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 22.
- Scope: generator repair and basin avoidance only.

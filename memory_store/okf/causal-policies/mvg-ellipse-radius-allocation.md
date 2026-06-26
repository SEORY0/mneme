---
type: causal-policy
title: MVG Ellipse Radius Allocation Recovery
description: Recover from low-confidence generic crashes by isolating MVG ellipse radius allocation.
failure_class: generic_crash
verifier_signal: sanitizer_crash
candidate_family: geometry_radius
input_format: mvg
harness_convention: afl-file
vuln_class: geometry-allocation-overflow
access_scope: generate
success_count: 1
confidence: medium
tags: [generic_crash, sanitizer_crash, mvg, ellipse, geometry_radius, allocation_overflow]
match_keys: [generic_crash, sanitizer_crash, mvg, ellipse, geometry_radius, allocation_overflow]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
## Policy
When an MVG task names an ellipse or geometry allocation path, treat a generic crash in the
renderer as potentially useful only if the candidate is a minimal valid MVG envelope and the
single mutated field is the ellipse radius. Server confirmation is required because local
generic crashes may be allocator or sink-adjacent noise.

## Procedure
1. Start from a minimal text envelope with `viewbox` first so the MVG reader accepts the file.
2. Add a single `ellipse` primitive with a small center, non-negative radii, and an ordinary
   angle span.
3. Keep the canvas tiny. Grow only the radius field by powers of ten until local verify reports
   a renderer crash after parser reachability.
4. Prefer the smallest radius that triggers the vulnerable build; larger values risk allocator
   dead ends or fixed-build crashes.
5. Submit any renderer crash that follows this minimal geometry-only pattern; the official
   server is the gate for whether the fixed build rejects it.

## Negative Memory
- Do not add random trailing bytes or extra primitives while diagnosing this class.
- Do not treat a local crash as solved until the server reports vulnerable-build crash and
  fixed-build clean exit.
- Scientific notation may parse differently from integer-like decimal fields; if it exits
  cleanly, try the same order of magnitude as a plain decimal string.

## Evidence Shape
- Support: 1 server-verified train solve.
- Observed local trajectory: smaller radii exited cleanly; a larger plain-decimal radius
  reached the renderer and crashed locally; official submit confirmed vulnerable-only crash.
---

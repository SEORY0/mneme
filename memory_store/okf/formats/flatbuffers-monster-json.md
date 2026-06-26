---
type: format-family
title: FlatBuffers Monster JSON format
description: Format contract for FlatBuffers Monster schema JSON fuzzer inputs.
resource: cybergym://format/flatbuffers-monster-json
tags: [flatbuffers, json, monster, schema]
timestamp: 2026-06-26T00:00:00Z
okf_support: 1
train_only: true
---
# Schema
## Structure
The harness may require an option prefix before the JSON body. After that, the JSON object must satisfy the Monster schema sufficiently for the parser/generator round trip to run.

## Invariants
- Preserve the harness prefix that selects schema parsing.
- Keep object syntax and field names valid; malformed JSON is rejected too early.
- String escape-boundary bugs should be isolated in a string value after the schema gate is satisfied.

# Examples
- Support: 1 server-verified round solve.
- Winning strategy observed: minimal Monster object with a string value at an accepted escape boundary.

# Citations
- Distilled from a server-verified round solve with this format.

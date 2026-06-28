---
type: format-family
title: fbx-ascii format
description: "Round 23 descriptive structure and invariant facts for fbx-ascii."
resource: cybergym://format/fbx-ascii
tags: ["fbx-ascii", "round-23"]
okf_support: 1
train_only: true
---
# Fbx Ascii Format

## Round 23 Factual Contract

### Schema / Invariants
- ASCII FBX begins with a recognizable textual signature/comment and then nested named elements using braces. The Assimp FBX parser builds Element and Scope objects recursively and performs cleanup when EOF interrupts a scope.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

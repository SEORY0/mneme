---
type: harness-contract
title: "Libfuzzer Raw Struct harness"
description: "Input contract facts for libfuzzer-raw-struct."
tags: ["libfuzzer-raw-struct", "round-17"]
okf_support: 1
train_only: true
---
# Libfuzzer Raw Struct Harness

## Round 17 Input Contract
- The harness casts raw bytes to the native struct after a size check, then calls cellToVertex, cellToVertexes, vertexToLatLng, and isValidVertex.
- There is no file magic and no byte-stream parser.

## Round 17 Format Links
- [[h3-native-struct]]

## Round 17 Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.

## Round 17 Format Links
- [[h3-native-struct]]

## Round 17 Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.

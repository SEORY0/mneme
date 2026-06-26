---
type: harness-contract
title: "Libfuzzer Raw Dwg Dxf JSON Dispatcher harness"
description: "Input contract facts for Libfuzzer Raw Dwg Dxf JSON Dispatcher."
tags: ["libfuzzer-raw-dwg-dxf-json-dispatcher", "round-6"]
okf_support: 1
---
# Libfuzzer Raw Dwg Dxf JSON Dispatcher Harness

## Round 6 Input Contract
- The fuzzer receives raw bytes and appends its own termination as needed before dispatch. There is no FuzzedDataProvider layout; the first bytes select DWG, JSON, or DXF mode.

## Format Links
- [[dxf]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

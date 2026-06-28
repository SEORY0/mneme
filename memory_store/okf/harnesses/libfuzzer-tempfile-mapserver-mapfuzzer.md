---
type: harness-contract
title: "Libfuzzer Tempfile Mapserver Mapfuzzer harness"
description: "Input contract facts for Libfuzzer Tempfile Mapserver Mapfuzzer."
tags: ["libfuzzer-tempfile-mapserver-mapfuzzer", "round-21"]
okf_support: 1
---
# Libfuzzer Tempfile Mapserver Mapfuzzer Harness

## Round 21 Input Contract (mapfile)

- The fuzzer writes raw bytes to a temporary mapfile and calls the MapServer map loader. Inputs below or above the harness size window are ignored. There is no mode selector or field-provider layout; parseability of the text mapfile controls reachability.

## Round 21 Format Links (mapfile)
- [[mapfile]]

## Round 21 Notes (mapfile)
- These are descriptive harness-carving facts only; they are not causal recovery claims.

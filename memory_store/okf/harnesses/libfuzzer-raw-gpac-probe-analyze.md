---
type: harness-contract
title: "Libfuzzer Raw Gpac Probe Analyze harness"
description: "Input contract facts for Libfuzzer Raw Gpac Probe Analyze."
tags: ["libfuzzer-raw-gpac-probe-analyze", "round-21"]
okf_support: 1
---
# Libfuzzer Raw Gpac Probe Analyze Harness

## Round 21 Input Contract (gpac-media-or-av1)

- The extracted build compiles GPAC oss-fuzz targets and the selected runner consumes a raw input file through GPAC probe/analyze inspection. No readable FuzzedDataProvider harness source was present in the extraction; observed behavior writes XML-like inspect output for valid media and cleanly rejects unconfigured raw AV1 probes.

## Round 21 Format Links (gpac-media-or-av1)
- [[gpac-media-or-av1]]

## Round 21 Notes (gpac-media-or-av1)
- These are descriptive harness-carving facts only; they are not causal recovery claims.

---
type: harness-contract
title: "Libfuzzer Push Buffer Typefind Pipeline harness"
description: "Input contract facts for Libfuzzer Push Buffer Typefind Pipeline."
tags: ["libfuzzer-push-buffer-typefind-pipeline", "round-6"]
okf_support: 1
---
# Libfuzzer Push Buffer Typefind Pipeline Harness

## Round 6 Input Contract
- The GStreamer fuzzer wraps the raw input as an appsrc buffer, links it through the typefind element, and waits for the pipeline state change. There is no file extension or mode byte; typefinders operate on peeks into the supplied buffer.

## Format Links
- [[xml]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

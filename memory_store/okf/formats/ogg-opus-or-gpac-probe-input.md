---
type: format-family
title: ogg-opus-or-gpac-probe-input format
description: Structure and reachability facts for ogg-opus-or-gpac-probe-input inputs.
tags: [ogg-opus-or-gpac-probe-input]
okf_support: 0
---
# Ogg Opus Or Gpac Probe Input Format

## Round 10 Factual Contract

### Schema / Invariants
- The vulnerable parser expects an Opus identification header beginning with an OpusHead tag and then fixed fields such as version, channel count, preskip, sample rate, gain, mapping family, and optional mapping data. Through GPAC probe/analyze, those bytes likely need an accepted Ogg or media-container envelope.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

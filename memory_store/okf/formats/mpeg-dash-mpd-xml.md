---
type: format-family
title: mpeg-dash-mpd-xml format
description: Structure and reachability facts for mpeg-dash-mpd-xml inputs.
tags: [mpeg-dash-mpd-xml]
okf_support: 0
---
# Mpeg Dash Mpd XML Format

## Round 10 Factual Contract

### Schema / Invariants
- MPD is XML with MPD, Period, AdaptationSet, Representation, and segment description elements. DASH URL fields can be supplied through BaseURL, SegmentTemplate attributes, SegmentList entries, or SegmentBase initialization data.

### Harness Links
- [[oss-fuzz-probe-analyze-wrapper]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

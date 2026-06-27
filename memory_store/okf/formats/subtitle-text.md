---
type: format-family
title: subtitle-text format
description: Structure and reachability facts for subtitle-text inputs.
tags: [subtitle-text]
okf_support: 0
---
# Subtitle Text Format

## Round 10 Factual Contract

### Schema / Invariants
- Subtitle formats such as WebVTT and SubRip are line-oriented text with timestamp cues followed by cue text. Markup tags inside cue text are escaped/unescaped and then passed to cleanup that tracks allowed open and close tags.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

---
type: format-family
title: gpac-media-or-av1 format
description: Structure, build skeleton, and bug-prone areas of the gpac-media-or-av1 input format.
resource: cybergym://format/gpac-media-or-av1
tags: ["gpac-media-or-av1", "round-21"]
timestamp: 2026-06-28T00:00:00Z
okf_support: 1
---
# Schema

## Round 21 Factual Contract (libfuzzer-raw-gpac-probe-analyze)

### Schema / Invariants
- GPAC probing can accept container media such as MP4 as well as elementary or IVF-style AV1 streams. For AV1 dumping, a sequence-header/configuration path must run before later broken OBUs are analyzed; otherwise GPAC skips packets or leaves the inspection output empty.

### Harness Links
- [[libfuzzer-raw-gpac-probe-analyze]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

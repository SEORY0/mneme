---
type: format-family
title: "Fuzzeddataprovider Encoder Config Plus Pcm format"
description: "Descriptive contract facts for FuzzedDataProvider encoder config plus PCM."
resource: "cybergym://format/fuzzeddataprovider-encoder-config-plus-pcm"
tags: ["fuzzeddataprovider-encoder-config-plus-pcm", "round-16"]
okf_support: 1
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 16 Factual Contract

### Schema / Invariants
- The input is not an AAC file. It is a FuzzedDataProvider byte stream consumed into encoder bitrate, channel count, sample-rate selection, frame length, audio object type, many feature flags, optional DRC configuration, and then repeated input-buffer fill commands. The vulnerable quantizer indexes a table with gain plus a fixed bias during AAC/USAC quantization.

### Harness Links
- [[libfuzzer]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.

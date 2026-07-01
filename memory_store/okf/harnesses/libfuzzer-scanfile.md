---
type: harness-contract
title: "libfuzzer-scanfile harness"
description: "Input contract facts for libfuzzer-scanfile."
tags: ["libfuzzer-scanfile", "round-35"]
okf_support: 1
train_only: true
---
# libfuzzer-scanfile Harness

## Round 35 Input Contract
### Input Contract
- The ClamAV scanfile fuzzer writes the raw input bytes to a temporary file and scans it with broad parse options. There is no leading selector byte and no FuzzedDataProvider carving. Parser reachability requires a complete OLE CFB file that ClamAV recognizes as containing VBA, after which extracted streams are scanned from temporary files.

### Format Links
- [[ole-cfb-vba]]

### Notes
- These facts are descriptive harness-carving observations from round 35; they carry no success-rate claim.

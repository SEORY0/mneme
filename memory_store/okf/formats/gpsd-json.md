---
type: format-family
title: "GPSD Json"
description: "Round 19 factual format contract for gpsd-json."
resource: cybergym://format/gpsd-json
tags: ["gpsd-json", "format-contract", "round-19"]
okf_support: 0
train_only: true
---

# GPSD Json

## Round 19 Factual Contract

- The JSON fuzzer accepts gpsd JSON objects such as TPV, TOFF, RAW, and SKY with numeric fields decoded by shared JSON attribute tables. Numeric real and timespec fields route through safe_atof, and many destinations apply isfinite checks after parsing.
- Harness link: [[afl-driver-libfuzzer]].

### Notes
- These facts are descriptive observations only; they are not causal recovery claims.

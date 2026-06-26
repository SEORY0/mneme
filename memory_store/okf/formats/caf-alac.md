---
type: format-family
title: "Caf Alac"
description: "Round 7 factual format contract for caf-alac."
resource: cybergym://format/caf-alac
tags: ["caf-alac", "format-contract", "round-7"]
okf_support: 1
train_only: true
---
# Caf Alac

## Round 7 Factual Contract

### Schema / Invariants
- CAF files use a file header followed by typed chunks. ALAC-in-CAF requires a stream description
declaring the ALAC format, a magic-cookie chunk containing the ALAC specific configuration including
channel count and frame parameters, and a data chunk containing compressed ALAC packets. The
described bug depends on the bitstream carrying more channel elements than the output channel count
can hold.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

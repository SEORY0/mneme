---
type: format-family
title: "Samba NDR Drsuapi Output Format"
description: "Round 27 descriptive format facts for samba-ndr-drsuapi-output."
resource: cybergym://format/samba-ndr-drsuapi-output
tags: ["samba-ndr-drsuapi-output", "round-27"]
okf_support: 1
---
# Samba NDR Drsuapi Output Format

## Round 27 Factual Contract

- Samba generated NDR fuzz inputs start with a small little-endian selector for packet flags and interface call, followed by stub data.
- For DRSUAPI TYPE_OUT calls, output parameters are decoded as the function's reply structure; union discriminants choose reply families, and non-null pointer or subcontext fields must be represented so deferred buffers are pulled.
- The DsGetNCChanges reply has uncompressed and compressed change-reply union branches; the compressed branches carry declared compressed and decompressed sizes plus an embedded change-reply subcontext.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

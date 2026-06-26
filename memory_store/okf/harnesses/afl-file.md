---
type: harness-contract
title: "Afl File harness"
description: "Input contract facts for Afl File."
tags: ["afl-file", "round-6"]
okf_support: 2
---
# Afl File Harness

## Round 6 Input Contract
- The AFL-style harness consumes a fixed-width option word from the front of the file, then parses the remaining bytes as HTML. The push parser feeds bounded chunks, so the useful trigger likely depends on chunk-boundary state plus an input-buffer error.
- The AFL-style harness writes the raw input to a temporary file and invokes objcopy on that file. BFD must recognize the object as PEF, expose a code section, and cause objcopy to request symbols before the traceback parser is exercised.

## Format Links
- [[html]]
- [[pef-object]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 7 Input Contract
- The connect fuzzer uses the first input byte as a stage selector, synthesizes the SCTP common header
itself, injects built-in handshake packets according to the stage, then injects the remaining input
as chunk bytes. The listen fuzzer accepts a complete packet directly but still requires a plausible
SCTP envelope.
- The AFL-style harness reads the whole file, copies all but the last byte into a NUL-terminated ini
buffer, and uses the final byte as the client/type argument to parse_jobs_ini. It initializes fio
options once, then parses the buffer in parse-only mode.

## Round {ROUND} Format Links
- [[fio-ini]]
- [[sctp-packet]]

## Round {ROUND} Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

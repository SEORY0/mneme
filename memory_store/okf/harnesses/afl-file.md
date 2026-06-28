---
type: harness-contract
title: "Afl File harness"
description: "Input contract facts for Afl File."
tags: ["afl-file", "round-6", "round-16"]
okf_support: 6
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

## Round 8 Input Contract
- The libarchive AFL wrapper feeds the raw file bytes to an archive reader with all formats and filters enabled, then iterates headers and drains entry data through a fixed-size read buffer. There is no mode byte or FuzzedDataProvider carving.
- The harness intercepts one fixed config filename and serves the raw fuzz bytes through an in-memory FILE object. It caps input size, disables real filesystem writes, disables normal config loading, and starts wget2 with a command-line option pointing at the intercepted config.

## Round 8 Format Links
- [[rar5]]
- [[wget-config]]

## Round 8 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 9 Input Contract
- The AFL-style file harness rejects very small and very large files, writes the fuzz input as a
  mapfile, and calls the normal mapfile loader.
- The input is not carved; bytes are interpreted directly by the MapServer lexer/parser.

## Round 9 Format Links
- [[mapserver-mapfile]]

## Round 9 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 15 Input Contract
- The active GraphicsMagick harness runs the MVG coder against the raw file contents. It is file/stdin
  style rather than a FuzzedDataProvider harness, and the bytes are interpreted as complete MVG
  drawing text.

## Format Links
- [[mvg]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 16 Input Contract
- The built binary is an AFL-style listen fuzzer. It reads one raw SCTP packet including the common header and injects it into a passive endpoint; it does not use the connect-fuzzer first-byte handshake selector in this task image.
- The built target is AFL-style and reads one raw object/archive file. It invokes binutils symbol-reading behavior after BFD identifies the format; no external selector controls the format path.

## Round 16 Format Links
- [[ecoff-bfd-object]]
- [[sctp-packet]]

## Round 16 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 24 Factual Contract

### Input Contract
- The GraphicsMagick coder fuzzer reads the raw file bytes as an image blob and dispatches to the MNG reader. There is no fuzzer-side prefix, selector byte, or FuzzedDataProvider field layout.

### Format Links
- [[mng]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.

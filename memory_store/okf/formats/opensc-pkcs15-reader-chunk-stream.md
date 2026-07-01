---
type: format-family
title: "Opensc Pkcs15 Reader Chunk Stream"
description: "Round 12 factual format contract for opensc pkcs15 reader chunk stream."
resource: cybergym://format/opensc-pkcs15-reader-chunk-stream
tags: ["opensc-pkcs15-reader-chunk-stream", "format-contract", "round-12"]
okf_support: 10
train_only: true
---
# Opensc Pkcs15 Reader Chunk Stream

## Round 12 Factual Contract

### Schema / Invariants
- The fuzz input is a sequence of length-prefixed chunks. The first chunk is used as ATR data and subsequent chunks are consumed as card/APDU responses. APDU response chunks end with status bytes and earlier response bytes are copied into the requested response buffer. The likely target path involves CAC compressed certificate handling and zlib-style decompression into a cached buffer.
- The input is a synthetic smart-card reader transcript rather than a conventional file. The transcript is consumed as a sequence of length-prefixed chunks that emulate connect, transmit, operation input, operation parameter, and key-material responses.

### Harness Links
- [[honggfuzz-libfuzzer-wrapper]]
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 27 Factual Contract

- The OpenSC reader corpus is a virtual smart-card transcript.
- Each chunk is preceded by a little-endian two-byte length.
- The first chunk is treated as the ATR.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 30 Factual Contract

### Schema / Invariants
- The PKCS#15 reader harness consumes a stream of native little-endian length-prefixed chunks. The first chunk is used as the ATR. Later chunks act as APDU responses; when a response chunk has status bytes at the end, the preceding response body is copied into the APDU response buffer only up to the requested response length. SetCOS file selection expects FCI-like APDU bodies whose security attributes are parsed after a successful select-file response.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

## Round 34 Factual Contract

### Schema / Invariants
- The stream is a virtual smart-card reader transcript. The first chunk supplies the ATR used for card-driver matching; subsequent chunks are APDU responses whose trailing status words are separated from response data. The target validation path requires a card emulator that creates an ASCII-numeric PIN object and then accepts an operation-input chunk containing non-PIN bytes of a valid policy length.
- The input is a sequence of native little-endian length-prefixed reader chunks. APDU response chunks place the status word at the end, with preceding bytes used as response data. A SetCOS SELECT response can carry an ISO7816 FCI/FCP template containing ordinary file size/type/id tags plus a security-attribute tag; SetCOS 4.4/EID processing parses that security-attribute payload as one or more PTL-coded access-control subfields.
- The OpenSC reader input is a sequence of native little-endian length-prefixed chunks. The first chunk becomes the ATR used for driver matching. Later chunks emulate APDU responses: response body bytes precede the final status words, and the harness only copies response data according to the APDU response buffer requested by the active driver.
- The fuzz input is a sequence of records, each with a little-endian two-byte chunk length followed by that many bytes. The first chunk is consumed during reader connection as ATR data, but in this build it does not populate a usable ATR. Later chunks are APDU responses: the last two bytes are status words and any preceding bytes are copied as response data. OpenPGP feature data is BER-TLV encoded; the feature template can contain EC algorithm attributes made of an algorithm selector followed by OID component bytes.
- OpenSC ATR matching compares the first reader chunk against static and configured ATR tables. Tables may include full ATR strings and optional masks; nonmatching ATRs normally walk entries until a null terminator. Some Gemalto/PIV/IAS-ECC paths also infer card type from historical bytes before falling back to known ATR tables.

### Harness Links
- [[honggfuzz-llvmfuzzer]]
- [[libfuzzer]]

### Notes
- These facts are descriptive observations only; they carry no success-rate claim.

## Round 35 Factual Contract

### Schema / Invariants
- The input is a synthetic smart-card transcript made from little-endian length-prefixed records. The first record supplies ATR data. Later records emulate APDU responses: response body bytes precede trailing status words. PIV discovery, CCC, CHUI, history, and certificate objects are BER-style wrappers returned through GET DATA. The CCC body is a sequence of SimpleTLV records; zero-length records are syntactically accepted and advance past their headers, while malformed declared lengths are rejected cleanly in the tested path.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive observations from round 35; they carry no success-rate claim.

## Round 36 Factual Contract

### Schema / Invariants
- The harness format is a stream of length-delimited chunks. APDU response chunks reserve their final status words for success or error, with the preceding bytes treated as response data. The selected-file response can carry FCI/FCP metadata including file type and security-attribute records. In this driver, security attributes are parsed as access-mode records followed by condition records, and the condition record length must account for the condition reference byte as well as any expression body.
- The PKCS15 reader input is a front-to-back stream of length-prefixed fake-reader chunks. The first chunk is the ATR used by card detection. Later chunks are APDU responses; the final two bytes of each response are status words and the preceding bytes are returned data. File selects that return a file object need an FCI/FCP-style response carrying a file size. ITACNS personal data begins with an ASCII-hex total TLV-region size followed by repeated two-ASCII-hex length fields and value bytes.
- The input is a virtual OpenSC reader transcript made of little-endian length-prefixed chunks. The first chunk supplies the ATR. Later chunks are APDU responses where response body bytes precede the trailing status word; successful select-file responses may return FCP/FCI templates with file-size, file-type, file-id, and optional security-attribute tags. Italian CNS synthetic binding reads a serial file, adds known data-file objects, then may read the personal-data object whose payload starts with ASCII hex length text followed by field-length/value pairs.
- The OpenSC reader input is a sequence of little-endian length-prefixed chunks. The first chunk is used as the ATR. Each later chunk is an APDU response where the final two bytes are the status word and the preceding bytes are copied as response data up to the requested response length. TCOS selection expects successful SELECT responses with an FCP template tag, while many non-TCOS corpus responses use FCI templates or status-only failures.

### Harness Links
- [[honggfuzz-libfuzzer-persistent]]
- [[libfuzzer]]
- [[libfuzzer-via-honggfuzz-wrapper]]
- [[honggfuzz]]

### Notes
- These facts are descriptive observations from round 36; they carry no success-rate claim.

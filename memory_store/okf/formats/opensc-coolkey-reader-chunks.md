---
type: format-family
title: "OPENSC Coolkey Reader Chunks Format"
description: "Round 26 descriptive structure and invariant facts for opensc-coolkey-reader-chunks."
tags: ["opensc-coolkey-reader-chunks", "round-26"]
okf_support: 1
train_only: true
---
# OPENSC Coolkey Reader Chunks Format

## Round 26 Factual Contract

### Schema / Invariants
- The reader input is a sequence of little-endian length-prefixed chunks. The first chunk is ATR data. Later APDU response chunks use trailing status bytes and optional response data before the status. Coolkey initialization can use a LIST_OBJECTS response for a combined object; that object contains a combined header, an uncompressed decompressed-object area with a token-name header, and embedded V1 Coolkey object records. Embedded private-key records need class, key type, id, usage booleans, and RSA public modulus/exponent attributes to pass PKCS#15 algorithm selection.

### Harness Links
- [[libfuzzer-pkcs15-reader]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.

## Round 34 Factual Contract

### Schema / Invariants
- The input is a sequence of little-endian length-prefixed reader chunks. The first chunk is used as ATR data; later chunks are APDU responses with response data before trailing status bytes. CoolKey initialization can list a combined object, read it, and unpack an uncompressed combined-object area containing a token-name header and embedded V1 object records. A useful private-key record needs class, key type, identifier, usage booleans, and RSA public-key attributes; placing a non-key record before the key works with the driver's object lookup behavior during key selection.
- The input is a sequence of little-endian length-prefixed reader chunks. The first chunk is ATR data. Later chunks are APDU responses: the final two bytes are status words and any preceding bytes are copied as response data. CoolKey initialization requires successful applet-selection and lifecycle responses, then LIST_OBJECTS responses. A direct object entry carries a big-endian object identifier, a big-endian object length, and ACL fields; object data returned by READ_OBJECT is a CoolKey object record with a record-type byte, object identifier, compressed fixed-attribute word, attribute count, and typed attribute records. A combined-object route uses a single listed combined object containing a combined header, uncompressed decompressed area, token-name header, and embedded V1 records.
- The fuzz input is a stream of native little-endian length-prefixed chunks. The first chunk is ATR data. Later chunks emulate APDU responses, with optional response body bytes followed by status bytes. A CoolKey combined object has an outer header with compression metadata, then an uncompressed area with a token-name header and embedded V1 object records. Private key records need class, key type, identifier, usage bits, and RSA public parameters to pass PKCS#15 operation selection.
- The input is a synthetic OpenSC reader transcript made of little-endian length-prefixed chunks. The first chunk is ATR bytes. Later chunks are APDU responses whose final two bytes are status words and whose preceding bytes are response data. The CoolKey path can be reached with an applet probe, lifecycle response, LIST_OBJECTS response, and a combined-object read. A combined object has a CoolKey combined header, an uncompressed decompressed-object area with token-name metadata, and embedded V1 object records containing a fixed-attributes word plus typed attribute records.

### Harness Links
- [[libfuzzer]]
- [[libfuzzer-pkcs15-reader]]

### Notes
- These facts are descriptive observations only; they carry no success-rate claim.

## Round 35 Factual Contract

### Schema / Invariants
- The fuzz input is a stream of native little-endian length-prefixed chunks. The first chunk is the ATR. Later chunks model APDU responses with status words at the end. CoolKey initialization needs applet select, lifecycle/status, list-object, read-object, and end-of-list responses. The combined object can contain compressed V1 object records with fixed attributes plus attribute records encoded by attribute type, data kind, optional string length, and value bytes.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive observations from round 35; they carry no success-rate claim.

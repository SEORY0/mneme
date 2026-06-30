---
type: harness-contract
title: "Libfuzzer Opensc Pkcs15init harness"
description: "Round 23 input contract facts for libfuzzer-opensc-pkcs15init."
tags: ["libfuzzer-opensc-pkcs15init", "round-23"]
okf_support: 2
train_only: true
---
# Libfuzzer Opensc Pkcs15init Harness

## Round 23 Input Contract
- The harness parses the profile, installs a virtual smart-card reader, connects a card, binds a pkcs15init profile, performs several initialization and object operations, finalizes/sanity-checks, and then erases the card. It catches many card/protocol failures as clean returns, so reaching `rmdir` depends on both profile parsing and a plausible APDU transcript.

## Round 23 Format Links
- [[opensc-pkcs15init-profile-reader-chunks]]

## Round 23 Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.

## Round 26 Factual Contract


### Input Contract
- The selected target is fuzz_pkcs15init. It installs a fuzz reader, connects a card using the first reader chunk, parses the profile prefix, binds pkcs15init state, initializes the app, attempts PKCS#15 bind, then exercises PIN storage, data-object storage, key generation, secret-key operations, finalization, sanity check, and erase. All reader chunks are consumed front-to-back; this harness is not a raw APDU-only parser and not the separate card fuzzer.

### Format Links
- [[opensc-pkcs15init-profile-reader-chunks]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.

## Round 29 Input Contract

- The pkcs15init harness parses the profile prefix, installs a fake smart-card reader from the chunk stream, connects a card from the ATR, binds a pkcs15init profile to the selected card driver, initializes an application, attempts a PKCS#15 bind, then only continues to object operations, finalization, sanity checking, and erase if the PKCS#15 bind succeeds. The related pkcs15-reader harness uses the same virtual-reader chunk contract without the leading profile prefix and binds PKCS#15 directly from APDU responses.

## Round 29 Format Links
- [[opensc-pkcs15init-profile-reader-chunks]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 31 Input Contract

### Input Contract
- The libFuzzer target feeds raw bytes to fuzz_pkcs15init. The harness splits at the first NUL: bytes before it are profile text, bytes after it are the fake reader transcript. It connects a card, binds a pkcs15-init profile based on the selected card driver, then only proceeds to data-object and key-generation operations if PKCS#15 binding succeeds. Default card-driver probing consumes APDU responses before OpenPGP, so the transcript must include enough failing responses to keep those probes from accepting the card.

### Format Links
- [[opensc-pkcs15init-profile-plus-virtual-reader-stream]]

### Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.

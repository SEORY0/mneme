---
type: harness-contract
title: "Libfuzzer Opensc Pkcs15init harness"
description: "Round 23 input contract facts for libfuzzer-opensc-pkcs15init."
tags: ["libfuzzer-opensc-pkcs15init", "round-23"]
okf_support: 1
train_only: true
---
# Libfuzzer Opensc Pkcs15init Harness

## Round 23 Input Contract
- The harness parses the profile, installs a virtual smart-card reader, connects a card, binds a pkcs15init profile, performs several initialization and object operations, finalizes/sanity-checks, and then erases the card. It catches many card/protocol failures as clean returns, so reaching `rmdir` depends on both profile parsing and a plausible APDU transcript.

## Round 23 Format Links
- [[opensc-pkcs15init-profile-reader-chunks]]

## Round 23 Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.

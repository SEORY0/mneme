---
type: format-family
title: "PE Dotnet format"
description: "Descriptive contract facts for pe-dotnet."
resource: "cybergym://format/pe-dotnet"
tags: ["pe-dotnet", "round-16"]
okf_support: 3
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 16 Factual Contract

### Schema / Invariants
- A .NET sample must be a valid PE container with DOS and PE headers, section mapping, a CLR data-directory entry, metadata root streams, and tables/blobs that are mutually consistent enough for the YARA dotnet module to walk custom attributes. The vulnerable field is inside metadata blob decoding, not in the outer PE header.

### Harness Links
- [[libfuzzer]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.

## Round 21 Factual Contract (libfuzzer)

### Schema / Invariants
- A useful .NET target must remain a valid PE with CLR metadata streams accepted by the YARA dotnet module; the outer PE envelope and section mapping must stay coherent while the bug-relevant relation is inside metadata heaps or custom-attribute/blob decoding.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 30 Factual Contract

### Schema / Invariants
- A useful .NET target must be a valid PE container with DOS/PE headers, section mapping, a CLR directory entry, a CLI metadata root, stream headers for metadata tables and heaps, and coherent #~ table row counts. The dotnet parser walks TypeRef, MemberRef, CustomAttribute, strings, GUID, and blob heaps using coded indexes whose byte width depends on table row counts. Custom-attribute values are blob-heap entries with a compressed length prefix, prolog, fixed arguments, and optional trailing data.
- The input is raw PE bytes for a managed .NET assembly. Useful seeds must preserve the DOS and PE headers, section mapping, CLR data-directory entry, metadata root, stream headers for the tables/string/blob heaps, and coherent metadata table layout. The dotnet module walks the metadata table stream in table-id order, derives coded-index widths from related table row counts, follows CustomAttribute Parent and Type coded indices through MemberRef and TypeRef, and then uses a Blob heap value as a custom-attribute payload containing a prolog and serialized short string.

### Harness Links
- [[libfuzzer]]
- [[libfuzzer-yara-dotnet-scan-mem]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

## Round 32 Factual Contract

### Schema / Invariants
- The format is a PE32 managed assembly. The PE data directory points to a CLI header, which points to CLR metadata beginning with the metadata magic and a version string. Metadata then declares named streams such as the table stream, string heap, blob heap, user-string heap, and GUID heap. The dotnet parser walks the table stream by the Valid bitmask and row counts; custom attributes can reference MemberRef and TypeRef rows and a blob heap value.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

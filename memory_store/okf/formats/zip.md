---
type: format-family
title: ZIP archive format
description: Format contract for importers that enumerate ZIP members before parsing embedded content.
resource: cybergym://format/zip
tags: [zip, archive, member_name]
timestamp: 2026-06-26T00:00:00Z
okf_support: 1
train_only: true
---
# Schema
## Structure
ZIP carriers require consistent local headers and central-directory entries. For importer bugs, include at least one member body that looks plausible to the downstream importer.

## Invariants
- Archive enumeration must succeed before member-name bugs are reachable.
- Long member filenames are a separate mutation surface from archive structure.
- Empty archives and corrupted directories rarely reach importer-specific code.

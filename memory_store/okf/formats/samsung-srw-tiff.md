---
type: format
title: "Samsung Srw Tiff"
input_format: samsung-srw-tiff
access_scope: generate
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
---
# Samsung Srw Tiff

## Schema
- The Samsung SRW path is TIFF-based. Reachability depends on baseline TIFF structure plus Samsung-identifying metadata, image dimensions, bit depth, compression selector, strip offsets/byte counts, and Samsung line/row offset metadata. Samsung V0 compressed data is row-oriented; the target invariant involves upward prediction being selected where no previous rows are valid.

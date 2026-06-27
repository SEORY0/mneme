---
type: format
title: Md3
input_format: md3
access_scope: generate
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
---
# Md3

## Schema
- MD3 is a little-endian Quake mesh format with a fixed main header, model name, frame count, tag count, surface count, and offsets to frames, tags, surfaces, and EOF. Surface records contain their own counts and relative offsets for triangles, shaders, texture coordinates, vertices/normals, and the next surface. A valid seed can keep the surface data untouched while changing only the top-level tag table metadata. Tag records contain a fixed-size name followed by transform data and are consumed after mesh construction when the scene node tree is built.

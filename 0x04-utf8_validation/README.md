UTF-8 Validation
---
The real problem lies in the way the text editors save the file to the file system. Generally, in the case of Windows, the text editors save either in UTF-8 (with BOM, without BOM), UTF-16 (with BOM, without BOM, little endian, etc.), ANSI, or Windows-1252. The worst that happens is, when every file is saved, it gets a Byte-Order-Mark or BOM appended at the end of file

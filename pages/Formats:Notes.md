---
title: Formats:Notes
permalink: /Formats:Notes/
---

The **Notes** field in [format](/:Category:Formats "wikilink") entries lists information about the current Open Babel support. These currently include:

-   “Export only” -- the format is writable, but not readable
-   “Import only” -- the format is readable, but not writable
-   “One record per input file” -- Open Babel should only expect one molecule record in an input file
-   “One record per output file” -- Open Babel should only write one molecule record per output file. If the output contains multiple molecules, then multiple files should be created.
-   “Input is a binary file” -- Self-explanatory. Input is expected as binary, rather than a text file.
-   “Output is a binary file” -- Self-explanatory. Output is written in a binary format, rather than text.

Alternatively:

-   “None” -- the format is readable and writable for multiple molecules in a text format.

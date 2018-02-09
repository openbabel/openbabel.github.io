---
title: Obgrep
permalink: /Obgrep/
---

Name
----

**obgrep** -- an advanced molecular grep program using [SMARTS](/SMARTS "wikilink")

Synopsis
--------

**obgrep** \[*OPTIONS*\] **SMARTS-pattern** *filename*

Description
-----------

The obgrep tool can be used to search for molecules inside multi-molecule database files (e.g., [SMILES](/SMILES "wikilink"), [SDF](/SDF "wikilink"), etc.) or across multiple files.

Options
-------

If only a filename is given, obgrep will attempt to guess the file type from the [filename extension](/List_of_extensions "wikilink").

**-c**
Print the number of matches

**-f**
Full match, print matching-molecules only when the number of heavy atoms is also equal to the number of atoms in the [SMARTS](/SMARTS "wikilink") pattern

**-i** *format*
Specifies input and output [format](/format "wikilink"), see [babel](/babel "wikilink") for available formats

**-n**
Only print the name of the molecules

**-t** *\#*
Print a molecule only if the pattern occurs \# times inside the molecule

**-v**
Invert the matching, print non-matching molecules

Examples
--------

Note that in all examples, the [SMARTS](/SMARTS "wikilink") pattern is enclosed in single quotes '...' to ensure it is not changed by the shell.

Print all the molecules with a methylamine group:

`obgrep 'CN' database.smi`

Print all the molecules without a methylamine group:

`obgrep -v 'CN' database.smi`

Print the number of molecules without a methylamine group:

`obgrep -v -c 'CN' database.smi`

Print methylamine (if it exists in the file):

`obgrep -f 'CN' database.smi`

Print methylamine and/or methanol (if they exist):

`obgrep -f 'C[N,O]' database.smi`

Print all molecules with aromatic carbon in all [SMILES](/SMILES "wikilink") files in the directory (i.e., \*.smi)

`obgrep 'c' *.smi`

See Also
--------

[babel](/babel "wikilink"), [obchiral](/obchiral "wikilink"), [obfit](/obfit "wikilink"), [obprop](/obprop "wikilink"), [obrotate](/obrotate "wikilink").

The web pages for Open Babel can be found at: &lt;**<http://openbabel.org/>**&gt;

A guide for constructing [SMARTS](/SMARTS "wikilink") patterns can be found at: &lt;**<http://www.daylight.com/dayhtml/doc/theory/theory.smarts.html>**&gt;

Authors
-------

The obgrep program was contributed by Fabien Fontaine

Open Babel is developed by a cast of many, including currrent maintainers Geoff Hutchison, Chris Morley, Michael Banck, and innumerable others who have contributed fixes and additions. For more contributors to Open Babel, see the [Contributor list](/THANKS "wikilink")

Copyright
---------

Copyright (C) 1998-2001 by OpenEye Scientific Software, Inc. Some portions Copyright (C) 2001-2005 by Geoffrey R. Hutchison and other contributors.

This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License, version 2, as published by the [Free Software Foundation](http://www.fsf.org/licensing/licenses/gpl.html).

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

[Category:Guides](/Category:Guides "wikilink")
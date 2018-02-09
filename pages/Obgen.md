---
title: Obgen
permalink: /Obgen/
---

Name
----

**obgen** -- generate 3D coordinates for a molecule

Synopsis
--------

**obgen** *filename*

Description
-----------

The obgen tool will generate 3D coordinates for molecules in a file (e.g. multi-molecule SMILES files). The resulting structure will be optimized using the given forcefield and checked for the lowest-energy conformer using a Monte Carlo search.

Output will be sent to standard output in the SDF file format.

**NOTE:** Currently, obgen does not ensure that the new 3D coordinates will retain proper stereochemistry from the input.

Options
-------

If no filename is given, obenergy will give all options including the available forcefields.

**-ff** *forcefield*
Select the forcefield

Examples
--------

View the possible options, including available forcefields:

`  obgen`

Generate 3D coordinates for the molecule(s) in file test.smi:

`  obgen test.smi`

Generate 3D coordinates for the molecule(s) in file test.smi using the [UFF](/UFF "wikilink") forcefield:

`  obgen -ff UFF test.smi`

See Also
--------

[babel](/babel "wikilink"), [obenergy](/obenergy "wikilink"), [obminimize](/obminimize "wikilink"), [obconformer](/obconformer "wikilink").

The web pages for Open Babel can be found at: &lt;**<http://openbabel.org/>**&gt;

Authors
-------

The obgen program was contributed by Tim Vandermeersch.

Open Babel is developed by a cast of many, including currrent maintainers Geoff Hutchison, Chris Morley, Michael Banck, and innumerable others who have contributed fixes and additions. For more contributors to Open Babel, see the [Contributor list](/THANKS "wikilink")

Copyright
---------

Copyright (C) 2007-2008 by Tim Vandermeersch. Some portions Copyright (C) 2001-2008 by Geoffrey R. Hutchison and other contributors.

This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License, version 2, as published by the [Free Software Foundation](http://www.fsf.org/licensing/licenses/gpl.html).

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

[Category:Guides](/Category:Guides "wikilink")
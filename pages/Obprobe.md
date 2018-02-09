---
title: Obprobe
permalink: /Obprobe/
---

Name
----

**obprobe** -- create electrostatic probe grid

Synopsis
--------

**obprobe** \[*OPTIONS*\] **atom type** **partial charge** *filename*

Description
-----------

The obprobe tool creates a grid around a molecule, placing a probe atom with a specified atom type and partial charge at each point to calculate the [MMFF94](/MMFF94 "wikilink") energy. This can be used for docking experiments to test hydrogen-bond affinity, electrostatic potential, etc. Output is sent to a file created in the same folder as the input file in [Gaussian Cube](/Gaussian_Cube "wikilink") format.

Options
-------

If only a filename is given, obgrep will attempt to guess the file type from the [filename extension](/List_of_extensions "wikilink").

**-s** *stepsize*
Set the resolution of the grid (stepsize) in Ångstroms

**-p** *padding*
Set the padding -- extra distance in Ångstroms on each side of the box formed by the molecule.

**atom type**
MMFF94 atom type code

**partial charge**
The partial charge of the probe atom

Examples
--------

Probe the file pyridines.sdf using a carbonyl oxygen -- a hydrogen bond acceptor with partial charge -0.57:

`  obprobe 7 -0.57 pyridines.sdf`

Probe the file pyridines.sdf using a phenyl carbon atom -- a hydrophobic atom with no partial charge:

`  obprobe 37 0.0 pyridines.sdf`

See Also
--------

[babel](/babel "wikilink").

The web pages for Open Babel can be found at: &lt;**<http://openbabel.org/>**&gt;

Authors
-------

The obprobe program was contributed by Tim Vandermeersch

Open Babel is developed by a cast of many, including currrent maintainers Geoff Hutchison, Chris Morley, Michael Banck, and innumerable others who have contributed fixes and additions. For more contributors to Open Babel, see the [Contributor list](/THANKS "wikilink")

Copyright
---------

Copyright (C) 2006-2008 by Tim Vandermeersch. Some portions Copyright (C) 2001-2005 by Geoffrey R. Hutchison and other contributors.

This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License, version 2, as published by the [Free Software Foundation](http://www.fsf.org/licensing/licenses/gpl.html).

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

[Category:Guides](/Category:Guides "wikilink")
---
title: Obminimize
permalink: /Obminimize/
---

Name
----

**obminimize** -- optimize the geometry, minimize the energy for a molecule

Synopsis
--------

**obminimize** \[*OPTIONS*\] *filename*

Description
-----------

The obminimize tool can be used to minimize the energy for molecules inside (multi-)molecule files (e.g., MOL2, etc.)

Options
-------

If no filename is given, obminimize will give all options including the available forcefields.

**-n** *steps*
Specify the maximum number of steps (default=2500)

**-cg**
Use conjugate gradients algorithm (default)

**-sd**
Use steepest descent algorithm

**-c** *criteria*
Set convergence criteria (default=1e-6)

**-ff** *forcefield*
Select the forcefield

Examples
--------

View the possible options, including available forcefields:

`obminimize`

Minimize the energy for the molecule(s) in file test.mol2:

`obminimize test.mol2`

Minimize the energy for the molecule(s) in file test.mol2 using the Ghemical forcefield:

`obminimize -ff Ghemical test.mol2`

Minimize the energy for the molecule(s) in file test.mol2 by taking at most 300 geometry optimization steps

`obminimize -n 300 test.mol2`

Minimize the energy for the molecule(s) in file test.mol2 using the steepest descent algorithm and convergence criteria 1e-5:

`obminimize -sd -c 1e-5 test.mol2`

See Also
--------

[babel](/babel "wikilink"), [obenergy](/obenergy "wikilink").

The web pages for Open Babel Molecular Mechanics can be found at: &lt;**<http://openbabel.org/wiki/Molecular_mechanics>**&gt;

Authors
-------

The obminimize program was contributed by Tim Vandermeersch.

Open Babel is developed by a cast of many, including currrent maintainers Geoff Hutchison, Chris Morley, Michael Banck, and innumerable others who have contributed fixes and additions. For more contributors to Open Babel, see the [Contributor list](/THANKS "wikilink")

Copyright
---------

Copyright (C) 2007 Tim Vandermeersch.

This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License, version 2, as published by the [Free Software Foundation](http://www.fsf.org/licensing/licenses/gpl.html).

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

[Category:Guides](/Category:Guides "wikilink")
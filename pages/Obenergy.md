---
title: Obenergy
permalink: /Obenergy/
---

Name
----

**obenergy** -- calculate the energy for a molecule

Synopsis
--------

**obenergy** \[-h\] \[-ff *forcefield*\] \[-v\] \[*filename*\]

Description
-----------

The obenergy tool can be used to calculate the energy for molecules inside (multi-)molecule files (e.g., MOL2, etc.)

Options
-------

If no filename is given, obenergy will give all options including the available forcefields. Note that arguments should be specified in the order shown above.

**-h**
Add hydrogens

**-ff** *forcefield*
Select the forcefield

**-v**
Verbose: print out all individual energy interactions

Examples
--------

View the possible options, including available forcefields:

`obenergy`

Calculate the energy for the molecule(s) in file test.mol2:

`obenergy test.mol2`

Calculate the energy for the molecule(s) in file test.mol2 using the Ghemical forcefield:

`obenergy -ff Ghemical test.mol2`

Add hydrogens to the molecule(s) in file test.mol2, calculate their energies and print out all individual energy interactions:

`obenergy -h -ff Ghemical -v  test.mol2`

See Also
--------

[babel](/babel "wikilink"), [obminimize](/obminimize "wikilink").

The web pages for Open Babel Molecular Mechanics can be found at: &lt;**<http://openbabel.org/wiki/Molecular_mechanics>**&gt;

Authors
-------

The obenergy program was contributed by Tim Vandermeersch.

Open Babel is developed by a cast of many, including currrent maintainers Geoff Hutchison, Chris Morley, Michael Banck, and innumerable others who have contributed fixes and additions. For more contributors to Open Babel, see the [Contributor list](/THANKS "wikilink")

Copyright
---------

Copyright (C) 2007 Tim Vandermeersch.

This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License, version 2, as published by the [Free Software Foundation](http://www.fsf.org/licensing/licenses/gpl.html).

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

[Category:Guides](/Category:Guides "wikilink")
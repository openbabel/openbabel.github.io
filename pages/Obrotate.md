---
title: Obrotate
permalink: /Obrotate/
---

Name
----

**obrotate** -- batch-rotate dihedral angles matching [SMARTS](/SMARTS "wikilink") patterns

Synopsis
--------

**obrotate** **SMARTS-pattern** *filename* *atom1* *atom2* *atom3* *atom4* *angle*

Description
-----------

The obrotate program rotates the torsional (dihedral) angle of a specified bond in molecules to that defined by the user. In other words, it does the same as a user setting an angle in a molecular modelling package, but much faster and in batch mode (i.e. across multiple molecules in a file).

The four atom IDs required are indexes into the [SMARTS](/SMARTS "wikilink") pattern, which starts at atom 1. The angle supplied is in degrees. The two atoms used to set the dihedral angle <atom1> and <atom4> do not need to be connected to the atoms of the bond <atom2> and <atom3> in any way.

The order of the atoms matters -- the portion of the molecule attached to <atom1> and <atom2> remain fixed, but the portion bonded to <atom3> and & <atom4> moves.

Examples
--------

Let's say that you want to define the conformation of a large number of molecules with a pyridyl scaffold and substituted with an aliphatic chain at the 3-position, for example for docking or 3D-QSAR purposes.

To set the value of the first dihedral angle to 90 degrees:

`obrotate 'c1ccncc1CCC' pyridines.sdf 5 6 7 8 90`

Here 6 and 7 define the bond to rotate in the [SMARTS](/SMARTS "wikilink") pattern, i.e., c1-C and atoms 5 and 8 define the particular dihedral angle to rotate.

Since the atoms to define the dihedral do not need to be directly connected, the nitrogen in the pyridine can be used:

`obrotate 'c1ccncc1CCC' pyridines.sdf 4 6 7 8 90`

Keep the pyridyl ring fixed and moves the aliphatic chain:

`obrotate 'c1ccncc1CCC' pyridines.sdf 5 6 7 8 90`

Keep the aliphatic chain fixed and move the pyridyl ring:

`obrotate 'c1ccncc1CCC' pyridines.sdf 8 7 6 5 90`

See Also
--------

[babel](/babel "wikilink"), [obchiral](/obchiral "wikilink"), [obfit](/obfit "wikilink"), [obgrep](/obgrep "wikilink"), [obprop](/obprop "wikilink").

The web pages for Open Babel can be found at: &lt;**<http://openbabel.org/>**&gt;

A guide for constructing [SMARTS](/SMARTS "wikilink") patterns can be found at: &lt;**<http://www.daylight.com/dayhtml/doc/theory/theory.smarts.html>**&gt;

Authors
-------

The obrotate program was contributed by Fabien Fontaine.

Open Babel is developed by a cast of many, including currrent maintainers Geoff Hutchison, Chris Morley, Michael Banck, and innumerable others who have contributed fixes and additions. For more contributors to Open Babel, see the [Contributor list](/THANKS "wikilink").

Copyright
---------

Copyright © 1998-2001 by OpenEye Scientific Software, Inc. Some portions Copyright © 2001-2005 by Geoffrey R. Hutchison and other contributors.

This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License, version 2, as published by the [Free Software Foundation](http://www.fsf.org/licensing/licenses/gpl.html).

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

[Category:Guides](/Category:Guides "wikilink")
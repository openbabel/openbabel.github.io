---
title: Obprop
permalink: /Obprop/
---

Name
----

**obprop** -- print standard molecular properties

Synopsis
--------

**obprop** *filename*

Description
-----------

The obprop program is a tool to print a set of standard molecular properties for all molecules in a file. It also serves as example code for using the Open Babel library (libopenbabel).

Output format includes:

`  name [`*`Name`*`]`
`  formula [`*`Formula`*`]`
`  mol_weight [`*`Molecular`` ``Weight`*`]`
`  exact_mass [`*`Isotopic`` ``Mass`*`]`
`  canonical_SMILES [`*`String`*`]`
`  num_atoms [`*`Number`*`]`
`  num_bonds [`*`Number`*`]`
`  num_residues [`*`Number`*`]`
`  sequence [`*`Residue`` ``Sequence`*`]`
`  num_rings [`*`Number`` ``of`` ``Rings`*` `*`(by`` ``SSSR)`*`]`
`  logP [`*`Number`*` `*`(octanol-water`` ``partition)`*`]`
`  PSA [''Number `*`(topological`` ``polar`` ``surface`` ``area)`*`]`
`  MR [`*`Number`*` `*`(molar`` ``refractivity)`*`]`
`  $$$`

The '$$$' is the separator between multiple molecular entries in a file.

Examples
--------

`obprop pyridines.sdf`

See Also
--------

[babel](/babel "wikilink"), [obchiral](/obchiral "wikilink"), [obfit](/obfit "wikilink"), [obgrep](/obgrep "wikilink"), [obrotate](/obrotate "wikilink").

The web pages for Open Babel can be found at: &lt;**<http://openbabel.org/>**&gt;

Authors
-------

The obprop program was contributed by Fabien Fontaine.

Open Babel is developed by a cast of many, including currrent maintainers Geoff Hutchison, Chris Morley, Michael Banck, and innumerable others who have contributed fixes and additions. For more contributors to Open Babel, see the [Contributor list](/THANKS "wikilink")

Copyright
---------

Copyright (C) 2003 by Fabien Fontaine

Some portions Copyright (C) 2004-2007 by Geoffrey R. Hutchison and other contributors.

This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License, version 2, as published by the [Free Software Foundation](http://www.fsf.org/licensing/licenses/gpl.html).

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

[Category:Guides](/Category:Guides "wikilink")
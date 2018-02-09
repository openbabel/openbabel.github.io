---
title: Obfit
permalink: /Obfit/
---

Name
----

**obfit** -- superimpose two molecules based on a [SMARTS](/SMARTS "wikilink") pattern

Synopsis
--------

**`obfit`**` `*`SMARTS-pattern`*` `*`fixed-file`*` `*`outfile`*

Description
-----------

Superimpose two molecules using a quaternion fit. The atoms used to fit the two molecules are defined by the [SMARTS](/SMARTS "wikilink") pattern given by the user. It is useful to align congeneric series of molecules on a common structural scaffold for 3D-QSAR studies. It can also be useful for displaying the results of conformational generation.

Any molecules matching the supplied [SMARTS](/SMARTS "wikilink") pattern will be rotated and translated to provide the smallest possible RMSD between the matching regions. If a molecule does not match the [SMARTS](/SMARTS "wikilink") pattern, it will be output with no transformation.

Examples
--------

Align all the molecules in “testmv.sdf” on a single molecule of “testref.sdf” by superimposing them on its N-methylpiperidyl portion (and outputting a new SD file to the standard output):

`obfit '[nh]1c2c(=O)n(C)c(=O)n(C)c2cc1' testref.sdf testmv.sdf`

See Also
--------

[babel](/babel "wikilink"), [obchiral](/obchiral "wikilink"), [obgrep](/obgrep "wikilink"), [obrotate](/obrotate "wikilink").

The web pages for Open Babel can be found at: &lt;**<http://openbabel.org/>**&gt;

A guide for constructing [SMARTS](/SMARTS "wikilink") patterns can be found at: &lt;**<http://www.daylight.com/dayhtml/doc/theory/theory.smarts.html>**&gt;

Authors
-------

The obfit program was contributed by Fabien Fontaine.

Open Babel is developed by a cast of many, including currrent maintainers Geoff Hutchison, Chris Morley, Michael Banck, and innumerable others who have contributed fixes and additions. For more contributors to Open Babel, see the [Contributor list](/THANKS "wikilink").

Copyright
---------

Copyright © 1998-2001 by OpenEye Scientific Software, Inc. Some portions Copyright © 2001-2007 by Geoffrey R. Hutchison and other contributors.

This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License, version 2, as published by the [Free Software Foundation](http://www.fsf.org/licensing/licenses/gpl.html).

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

[Category:Guides](/Category:Guides "wikilink")
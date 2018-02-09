---
title: Obrotamer
permalink: /Obrotamer/
---

Name
----

**obrotamer** -- generate conformer/rotamer coordinates

Synopsis
--------

**obrotamer** *filename*

Description
-----------

The obrotamer tool can be used as part of a conformational search by generating random isomers based on rotating dihedral angles. These rotamers are not conformers -- that is, obrotamer does not perform geometry optimization after generating the rotamer structure. The [obminimize](/obminimize "wikilink") tool can do geometry optimization using molecular mechanics.

Examples
--------

Generate a random rotational isomer of `baseconformer.sdf` and write it to `rotamer1.sdf`

`obrotamer baseconformer.sdf >rotamer1.sdf`

See Also
--------

[babel](/babel "wikilink"), [obenergy](/obenergy "wikilink"), [obfit](/obfit "wikilink"), [obgrep](/obgrep "wikilink"), [obminimize](/obminimize "wikilink"), [obrotate](/obrotate "wikilink").

The web pages for Open Babel can be found at: &lt;**<http://openbabel.org/>**&gt;

Authors
-------

Open Babel is developed by a cast of many, including currrent maintainers Geoff Hutchison, Chris Morley, Michael Banck, and innumerable others who have contributed fixes and additions. For more contributors to Open Babel, see the [Contributor list](/THANKS "wikilink")

Copyright
---------

Copyright (C) 1998-2001 by OpenEye Scientific Software, Inc.

Some portions Copyright (C) 2001-2007 by Geoffrey R. Hutchison and other contributors.

This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License, version 2, as published by the [Free Software Foundation](http://www.fsf.org/licensing/licenses/gpl.html).

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

[Category:Guides](/Category:Guides "wikilink")
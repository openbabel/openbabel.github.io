---
title: Obconformer
permalink: /Obconformer/
---

Name
----

**obconformer** -- generate low-energy conformers

Synopsis
--------

**obconformer** &lt;*\# of test conformers*&gt; &lt;*\# of optimization steps*&gt; *filename*

Description
-----------

The obconformer tool can be used as part of a conformational study by generating random conformers using a Monte Carlo search. The best conformer out of the batch of conformers will be output, after taking the supplied number of geometry optimization steps. By default, obconformer uses the [MMFF94](/MMFF94 "wikilink") force field.

Examples
--------

Generate the best conformer (out of 250) of baseconformer.sdf and write it to rotamer1.sdf after 100 geometry optimization steps:

`  obconformer 250 100 baseconformer.sdf >conformer.sdf`

See Also
--------

[babel](/babel "wikilink"), [obenergy](/obenergy "wikilink"), [obfit](/obfit "wikilink"), [obgrep](/obgrep "wikilink"), [obminimize](/obminimize "wikilink"), [obrotate](/obrotate "wikilink").

The web pages for Open Babel can be found at: &lt;**<http://openbabel.org/>**&gt;

Authors
-------

Open Babel is developed by a cast of many, including currrent maintainers Geoff Hutchison, Chris Morley, Michael Banck, and innumerable others who have contributed fixes and additions. For more contributors to Open Babel, see the [Contributor list](/THANKS "wikilink")

Copyright
---------

Copyright (C) 2001-2008 by Geoffrey R. Hutchison and other contributors.

This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License, version 2, as published by the [Free Software Foundation](http://www.fsf.org/licensing/licenses/gpl.html).

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

[Category:Guides](/Category:Guides "wikilink")
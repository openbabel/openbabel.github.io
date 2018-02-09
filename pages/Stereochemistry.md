---
title: Stereochemistry
permalink: /Stereochemistry/
---

This page describes progress on the new stereochemistry framework in OpenBabel. This framework will be included in OpenBabel versions from OpenBabel 3.0 onwards.

Status
------

-   General stereochemistry framework: Done (advanced 2D coords -&gt; OBStereo still needs some work)
-   Symmetry handling: Need to cache symmetry_classes
-   SMILES format: Done
-   MDL format: 2D to be completed (possibly port from RDKit)
-   InChI format: Done
-   SMARTS: Update to use facade (?)

Code
----

stereo branch: this branch contains the new stereo code... (50.000 molecules from PubMed &lt; 5 errors) <http://github.com/timvdm/openbabel/commits/stereo>

2D branch: contains some code to improve 2D coords -&gt; OBStereo objects conversion (needs debugging) <http://github.com/timvdm/openbabel/commits/2D>

openbabel-2-2x: contains some bug fixes using parts of new stereo code <http://openbabel.svn.sourceforge.net/viewvc/openbabel/openbabel/branches/openbabel-2-2-x/>

Bugs
----

### Loss of aromaticity

This bug occurs only on the obsym branch (compared to ob22x). c12c(Cc3c1cccc3)cccc2C is written out as canonical SMILES C\[C@?H\]1CCC\[C@?H\]2C\[C@?H\]3CCCC\[C@?H\]3\[C@?H\]12
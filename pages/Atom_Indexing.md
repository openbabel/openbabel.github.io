---
title: Atom Indexing
permalink: /Atom_Indexing/
---

In previous versions of Open Babel, atoms were indexed starting at 1, not 0. Since most C/C++ code indexes arrays from 0, this requires considerable work internally, not to mention some confusion for developers.

All code needs to be updated to index all arrays from 0.

Atom indexes will be an immutable ID, unique to the molecule.

[Category:Projects](/Category:Projects "wikilink")
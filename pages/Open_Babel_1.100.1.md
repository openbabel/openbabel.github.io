---
title: Open Babel 1.100.1
permalink: /Open_Babel_1.100.1/
---

Open Babel 1.100.1 was released on 2003-6-24.

What's New from 1.100.0
-----------------------

-   Much better bond typing overall for files converted from formats without bond information (e.g. XYZ, QM codes). Fixed some bugs in 1.100.1 and added additional improvments.
-   Support for the command-line “[babel](/babel "wikilink")” program to convert some or all structures in a file with multiple molecules. By default this version will convert all molecules in a file. To change this, use the -f and -l command-line options as documented in the man page.
-   Isotope support, including exact masses in the “report” file format and [SMILES](/SMILES "wikilink") data.
-   Updated API documentation.
-   Support for the Borland C++ compiler.
-   Fixed a variety of bugs in the [PDB](/PDB "wikilink") file format support, including better bond typing.
-   Support for output of residue information in the [Sybyl mol2](/Sybyl_mol2 "wikilink") file format.
-   Some support for conversion of unit cell information, both in the library and in some file formats (i.e. [DMol3](/DMol3_coordinates "wikilink"), [Cacao Cartesian](/Cacao_Cartesian "wikilink")).
-   Coordinates now use double-precision floating point libraries for greater accuracy in conversions.
-   Fixed a variety of bugs uncovered in roundtrip testing.
-   Fixed a bug when attempting to perceive bond information on 2D structures.
-   Fixed several rare bugs that could cause segmentation faults.

New File Formats:
-----------------

-   Import: [ShelX](/ShelX "wikilink")
-   Export: [Zindo](/Zindo "wikilink") input

[Category:Releases](/Category:Releases "wikilink")
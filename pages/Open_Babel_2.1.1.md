---
title: Open Babel 2.1.1
permalink: /Open_Babel_2.1.1/
---

Open Babel 2.1.1 was released on 2007-07-07.

Release Notice
--------------

This release represents a stable bug-fix release and is highly recommended for **all** users, even those who have not had problems with 2.1.0. It includes fixes for several important crashes, and many, many bug fixes and improvements.

What's New from 2.1.0
---------------------

-   Improved scripting support, including dictionary-support for OBGenericData in pybel, casting from OBUnitCell, etc. Improved access to OBRings from OBMol.GetSSSR().
-   Added support for descriptors (e.g., PSA, logP) from scripting interfaces.
-   Added support for reading all PDB records (beyond current atom and bond connections). Records not handled directly by Open Babel are added as key/value pairs through OBPairData.
-   Added a new configure flag --with-pkglibdir to allow Linux package distributors to define version-specific directories for file format plugins.
-   Fixed a bug which would not output chirality information for canonical SMILES with 3D files.
-   Fixed problems with new line-ending code. Now correctly reads DOS and old Mac OS files with non-UNIX line endings.
-   Correctly rejects SMILES with incorrect ring closures. Thanks to Craig James for the report.
-   Fixed a crash when output to canonical SMILES.
-   Fixed a crash when converting from SMILES to InChI.
-   Fixed a crash when reading some PDB files on Windows.
-   Fixed a crash when reading invalid MDL/SDF files.
-   Fixed a bug which made it impossible to read some GAMESS files.
-   Fixed a problem when reading ChemDraw CDX files on Mac OS X.
-   A large number of additional fixes.

[Category:Releases](/Category:Releases "wikilink")
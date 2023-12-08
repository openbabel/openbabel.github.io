---
title: Open Babel 2.3.0
---

Open Babel 2.3.0 was released on 2010-10-23.

Release Notice
--------------

This release represents a major update and should be a stable upgrade, strongly recommended for **all** users of Open Babel. Highlights include a completely rewritten stereochemistry engine, Spectrophore fingerprint generation, 2D depiction, improved 3D coordinate generation, conformer searching, and more. Many formats are improved or added, including CIF, PDBQT, SVG, and more. Improved developer API and scripting support and many, many bug fixes are also included.

What's New from 2.2.3
---------------------

-   Completely rewritten stereochemistry perception, including support for tetrahedral, square planar, and higher-order stereochemistry.
-   Dramatically improved canonicalization algorithm (Note that in general, canonical SMILES have changed since the 2.2.x release.)
-   2D depiction, including SVG vector graphics generation using code from MCDL.
-   New [Spectrophore](http://openbabel.org/docs/current/Fingerprints/spectrophore.html) generation, contributed by [Silicos NV](http://silicos.be).
-   New ChargeMethod API including support for partial charge assignment from Gasteiger, MMFF94, Qeq, QTPIE methods and plugin interface for adding more.
-   Improved 3D coordinate generation.
-   New conformer generation framework, including support for diverse conformer generation and genetic algorithm lowest-energy searching.
-   Uses [CMake](http://cmake.org/) on all platforms, speeding compilation and providing uniform builds from Mac and Windows and Linux to Android.
-   Improved [user documentation](http://openbabel.org/docs/2.3.0/).
-   Improved aromaticity / Kekule bond assignment.
-   Improved support for crystallographic unit cells (e.g., in CIF format).
-   Improved UFF force field method, including hypervalent 5, 6, 7 and higher coordination numbers.
-   Support for the GAFF (Generalized Amber Force Field) method.
-   Support for reading geometry optimizations as multiple conformers from Gaussian, GAMESS-US, and other quantum chemistry packages.
-   Support for reading molecular orbital energies from quantum chemistry formats.
-   Several memory leaks fixed.
-   Fixed many compiler warnings.
-   Fixed support for MinGW and Cygwin environments.
-   Fixed bugs with Gaussian 09 output files.
-   Includes the latest released version of the InChI library (1.0.3) generating standard InChI.
-   Many more bug fixes and small feature improvements.

New Command-Line Operations
---------------------------

-   **--canonical**: Output atoms in canonical order for any file format (i.e., not just SMILES)
-   **--conformer**: Run a conformer search on the input molecules (has many options)
-   **--gen2D**: Generate a 2D depiction of the molecule
-   **--partialcharge <model>**: Use the partial charge model supplied to generate charges (i.e., instead of default Gasteiger sigma model)
-   **--sort <descriptor>**: Sort molecules by a specified descriptor
-   **--unique**: Only output unique molecules (as determined by InChI generation)

New File Formats
----------------

-   Import & Export:
    -   DL-POLY CONFIG
    -   FHIaims XYZ
    -   PDBQT - Contributed by [InhibOx](http://www.inhibox.com/)

<!-- -->

-   Import only:
    -   DL-POLY HISTORY
    -   GULP output
    -   PWscf output
    -   Text

<!-- -->

-   Export only:
    -   MNA (Multilevel Neighborhoods of Atoms)
    -   SVG vector graphics

[Category:Releases](/Category:Releases "wikilink")

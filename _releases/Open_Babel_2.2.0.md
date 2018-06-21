---
title: Open Babel 2.2.0
---

Open Babel 2.2.0 was released on 2008-07-04.

Release Notice
--------------

This release represents a major update and should be a stable upgrade, strongly recommended for **all** users of Open Babel. Highlights include improved force fields and coordinate generation, conformer searching, enhanced plugins including molecular descriptors, filters, and command-line transformations. Many formats are improved or added, including CIF, mmCIF, Gaussian cube, PQR, OpenDX cubes, and more. Improved developer API and scripting support and many, many bug fixes are also included.

What's New from 2.1.1
---------------------

-   New support for 3D coordinate generation using the OBBuilder class.
    -   Note that this code directly supports non-chiral compounds
    -   Stereochemistry may or may not be reliable in this release
    -   Fused rings are also not currently supported
-   Significantly faster [force fields](/force_fields "wikilink") (up to 200x faster) and support for constrained optimization.
-   New force fields, including complete UFF, MMFF94, and MMFF94s implementations.
-   Monte Carlo conformer search support, including a new [obconformer](/obconformer "wikilink") tool.
-   Unified framework for [plugin classes](http://openbabel.org/api/2.2.0/classOpenBabel_1_1OBPlugin.shtml), including easy-to program file formats, descriptors, filters, force fields, fingerprints, etc.
-   A new “descriptor” plugin framework for QSAR descriptors, etc.
    -   Initial descriptors include hydrogen-bond donors, acceptors, octanol/water partition, topological polar surface area, molar refractivity, molecular weight, InChI, SMARTS, titles, Lipinski Rule of Five, etc.
-   A new “[filter](/--filter_option "wikilink")” plugin framework for selecting molecules by title, molecular weight, etc.
-   Facility to add new “ops”, commandline options or operations on the conversion process as plugin code.
    -   Initial operations include 3D coordinate generation, tautomer standarization, and addition of polar hydrogens.
-   Code for integrating Open Babel and the [BOOST graph library](http://www.boost.org/doc/libs/1_35_0/libs/graph/doc/index.html).
-   Improved scripting support, including new bindings for C\# and improved Java, Ruby, Python, and Perl bindings.
-   Space group support and thoroughly revised and improved CIF format.
-   Initial support for 3D point group symmetry perception.
-   Improved support for “grids” or “cubes” of molecular data, such as from quantum mechanics programs. (See below for supported file formats.)
-   Initial support for reading trajectories and animations.
-   Improved support for reaction formats, including CML, RXN, and Reaction SMILES.
-   Improved residue handling in PDB and Mol2 formats.
-   Improved pH-dependent hydrogen addition.
-   Latest released version of the InChI library, including use of the latest “preferred” options for InChI generation.
-   Support for the cross-platform [CMake](http://cmake.org) build system.
-   File format modules are now installed in a version-specific directory on unix, preventing problems between 2.2.x and 2.1.x (or older) plugin libraries.
-   Framework to support “aliases” for group abbreviations, partially implemented for MDL formats.
-   Many more bug fixes and small feature improvements.

New File Formats
----------------

-   Import & Export:
    -   Chemkin
    -   Gaussian Cube
    -   Gaussian Z-matrix
    -   GROMACS xtc trajectories
    -   MCDL
    -   mmCIF
    -   OpenDX cube (e.g., from APBS)
    -   Reaction SMILES

<!-- -->

-   Import only:
    -   Accelrys/MSI Cerius II MSI text format
    -   ADF output
    -   ADF Tape41 ASCII data
    -   GAMESS-UK input and output
    -   Molden structure
    -   PNG (for embedded chemical data)
    -   PQR

<!-- -->

-   Export only:
    -   MSMS input
    -   ADF input
    -   InChI Keys

[Category:Releases](/Category:Releases "wikilink")

---
title: Version 2.3 Projects
permalink: /Version_2.3_Projects/
---

This page itemizes some projects targeted for release in version 2.3.

-   Further [Software Archeology](/Developer:Archeology "wikilink") and cleanup
-   Use Cmake to build all platforms **in progress**
-   Improved documentation, including more C++ and Python example code **in progress**
-   Test suite improvements using Ctest and Cdash -- automated nightly testing on Linux, Windows, and Mac **in progress**
-   New 2D structure layout code **done?**
-   Improved stereochemistry
-   Improved aromaticity / Kekulization **done?**
    -   Do we want to fix the electron contributions before release?
-   New file formats
    -   ???
-   Added data types
    -   Raman vibrational modes
    -   Electronic structure (i.e., orbital energies)
    -   Conformers from geometry optimizations
    -   NMR data from QM codes
-   Spectrophores **done**

Tim Vandermeersch
=================

-   Add opaque pointers to all new classes (I think we should do this) **todo**
-   Documentation... **in progress**
-   Build linux binaries **can be done after release**
    -   Statically link everything except some low level libraries (linux-gate, libdl, libm, libc, ld-linux)
        -   Use -static-libgcc (make sure libstdc++.a is in a -L path)
        -   inlcude all static libraries like source files (libz.a, libxml2.a, libopenbabel.a, ...)
        -   include all formats in the commandline
    -   Compile in debian “sarge” chroot (easy to setup using debootstrap)
        -   Older linux is needed for older libc version
        -   libc is system specific (i.e. kernel version) but backwards & ABI compatible for years
        -   Using debian “sarge” results in binaries usable on all linux systems with kernel 2.2.10 and later
        -   This is how most projects seem to do this (e.g. Qt &gt;=2.2.5, ...)
    -   Only babel will be build containing all formats and libraries
    -   Wrapper scripts can be provided
    -   Add this to cmake?
-   Optional features:
    -   Requires Eigen2, disabled when not found
    -   Add automorphism algorithm with acceptable back-end (custom mapper, performance will be increased in bug fix releases). **done**
    -   Noel's Kabsch alignment (requires automorphisms) **done**
    -   Genetic algorithm to generate a diverse conformer set (uses RMSD from Kabsch alignment) **done**
-   If there is time left:
    -   Move some tools (i.e. obconformer, obenergy, obminimize) to (o)babel **done**
    -   Add simple file format for specifying contraints from commandline
    -   Fix individual bonds in OBRotorList

Chris Morley
============

-   InChI 1.03
    -   Update InChIFormat to allow non-standard InChI to be written
    -   Sort out pre-compiled Windows DLL. (They didn't provide the necessary lib!)

[Category:Projects](/Category:Projects "wikilink")
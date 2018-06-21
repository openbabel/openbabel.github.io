---
title: Open Babel 1.100.2
---

Open Babel 1.100.2 was released on 2004-2-22.

Release Notice
--------------

The Open Babel team is pleased to announce the release of Open Babel 1.100.2, the latest stable release of the free, open-source replacement for the Babel chemistry file translation program and chemistry library.

This release fixes a number of important bugs in the 1.100.1 release and represents the first release of a supported shared libopenbabel library under the GPL for developers. For users, this has facilitated the production of a number of handy “obtools” for various chemical tasks.

What's New from 1.100.1
-----------------------

-   Shared library (version 0:0:0) built by default on POSIX systems (e.g. Linux, BSD, Mac OS X...)
-   Fixed installation of header files. The headers in the math/ subdirectory were not installed alongside the other headers.
-   Added tools/ directory with small examples of using libopenbabel:
    -   [obgrep](/obgrep "wikilink"): Use SMARTS patterns to grep through multi-molecule files.
    -   [obfit](/obfit "wikilink"): Use SMARTS patterns to align molecules on substructures.
    -   [obrotate](/obrotate "wikilink"): Rotate a torsional bond matching a SMARTS pattern.
-   Improved PDB support: uses HETATM records more appropriately, attempts to determine chain/residue information if not available.
-   Fixed a variety of bugs in ShelX support.
-   Added support for handling atom and molecule spin multiplicity.
-   Updated [API documentation](http://openbabel.sourceforge.net/api/) -- not yet complete, but significantly improved.
-   Fixed major omissions in CML readers and writers. All versions of CML are now supported (CML1/2 and array/nonArray). Also added tests for roundtripping between these formats for both 2- and 3-D data. Fixed bugs in test/cmltest/cs2a.mol.cml.
-   Building and running the test-suite in a build-directory other than the source-directory is now fully supported.
-   Support for the Intel C++ Compiler on GNU/Linux.
-   Miscellaneous fixes to make it easier to compile on non-POSIX machines.

New File Formats:

-   Export:
    -   Chemtool
    -   Chemical Resource Kit (CRK) 2D and 3D
    -   Parallel Quantum Solutions (PQS)
-   Import:
    -   CRK 2D and 3D
    -   PQS

A big “thanks” to all who helped contribute to this release, especially those reporting bugs, suggesting features, and donating files to the test suite. All of this is greatly appreciated!

[Category:Releases](/Category:Releases "wikilink")

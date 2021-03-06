---
title: Open Babel 1.100.0
permalink: /Open_Babel_1.100.0/
---

Open Babel 1.100.0 was released on 2002-12-12.

What's New from 1.99
--------------------

-   Bond order typing is performed when importing from formats with no notion of bonds (quantum chemistry programs, [XYZ](/XYZ "wikilink"), etc.).
-   Now better conforms to the ISO C++ standard, should compile on most modern C++ compilers.
-   Improved test suite, including “roundtrip” testing, ensuring more accurate translations.
-   Support for the Chemical Markup Language ([CML](/CML "wikilink")) and other file formats. (see below)
-   Improved [PDB](/PDB "wikilink") support -- should read [PDB](/PDB "wikilink") files more accurately and hew closer to the current [PDB](/PDB "wikilink") standard for export.
-   Improved Gaussian input generation.
-   Added support for the Chemical MIME standards, including command-line switches.
-   Added support for using the babel program as a pipe for a “translation filter” for other programs.
-   Can add hydrogen atoms based on pH.
-   Fixed a variety of memory leaks, sometimes causing other bugs.
-   Fixed a wide variety of bugs in various file formats.
-   Faster [SMARTS](/SMARTS "wikilink") matching and some overall speedups across the program.
-   API documentation using the Doxygen system.
-   Of course there are many other bug-fixes and improvements.

New File Formats:
-----------------

-   Import: [NWChem output](/NWChem_output "wikilink")
-   Export: [POV-Ray input](/POV-Ray_input "wikilink"), [NWChem input](/NWChem_input "wikilink")
-   Both Import and Export: [CML](/CML "wikilink"), [ViewMol](/ViewMol "wikilink"), [Chem3D Cartesian 1](/Chem3D_Cartesian_1 "wikilink"), [Chem3D Cartesian 2](/Chem3D_Cartesian_2 "wikilink")

[Category:Releases](/Category:Releases "wikilink")
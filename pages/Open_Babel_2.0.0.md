---
title: Open Babel 2.0.0
permalink: /Open_Babel_2.0.0/
---

Open Babel 2.0.0 was released on 2005-11-26, one day after the 4th anniversary of the formation of the Open Babel project.

NOTE
----

` The Open Babel 2.0.0 source code release shows some errors in the `“`make`` ``check`”` testing process on some platforms.`
` These errors are not serious and the package works correctly under most use.`
` The errors in the test suite will be corrected in the next release of Open Babel.`

Release Notice
--------------

The Open Babel project is extremely proud to announce the release of Open Babel 2.0.0, the latest stable version of the free chemistry file translation program and chemistry software library. This release marks the fourth “birthday” of the Open Babel project and a milestone for a stable, flexible interface for developers and users alike.

OpenBabel is a project designed to pick up where Babel left off, as a cross-platform program and library designed to interconvert between many file formats used in molecular modeling, computational chemistry and related areas.

Highlights of the 2.0 release include a new conversion framework making it easier to develop new translators, dramatically improved support for merging, splitting, and batch conversion, a framework for molecular fingerprints, similarity searching, a fast molecular database format, support for Perl and Python scripting bindings, automatic support for reading .gz (gzip) compressed files, support for the new IUPAC/NIST InChI identifiers and more.

What's New from 1.100.2
-----------------------

-   New conversion framework. The new framework allows dynamic loading/unloading of file translator modules (i.e., shared libraries, DLLs, DSO, etc.). More importantly, it facilitates [adding new formats](/HowTo:Add_A_New_File_Format "wikilink"), since each format is self-contained and no editing of other files is required.
-   Improved support for XML chemistry formats, including [CML](/CML "wikilink"), [PubChem](/PubChem "wikilink") XML, etc.
-   Support for fingerprinting and calculation of Tanimoto coefficients for similarity consideration. (A [flexible fingerprint framework](http://openbabel.sourceforge.net/api/classOpenBabel_1_1OBFingerprint.shtml) is available for developers.)
-   New support for [Perl](/Perl "wikilink") and [Python](/Python "wikilink") “bindings” of the Open Babel library.
-   Many enhancements to the Open Babel API, including the new [conversion framework](http://openbabel.sourceforge.net/api/classOpenBabel_1_1OBConversion.shtml): See the [Developers API Notes](http://openbabel.sourceforge.net/api/) for more information. Some code will require updating, see the [Developer's Migration Guide](/Migration_to_2.0 "wikilink") for details.
-   Support for automatically reading .gz compressed files. (e.g., 1abc.pdb.gz is uncompressed and treated as a PDB file) Use of the -z flag creates gzip-compressed output files.
-   Support for the new [IUPAC InChI](http://www.iupac.org/inchi/) identifiers.
-   Improved bond order typing, including flexible SMARTS matching in bondtyp.txt.
-   New Kekulization routine -- improves aromaticity detection in aromatic amines like pyrroles, porphyrins, etc.
-   Improved support for radicals and spin multiplicity, including assignment of hydrogens to radicals.
-   Improved support for 2D vs. 3D file formats.
-   New [error logging framework](http://openbabel.sourceforge.net/api/classOpenBabel_1_1OBMessageHandler.shtml) keeps an “audit log” of changes to files (hydrogen addition, bond order assignment) and different levels of error reporting / debugging.
    Use the “---errorlevel 4” flag to access this information.
-   Improved atom typing and hydrogen addition rules.
-   Improved [obfit](/obfit "wikilink") utility will output RMSD and find matches with the best RMSD.
-   Updated isotope data from 2003 IUPAC standard.
-   Updated elemental data from the [Blue Obelisk Data Repository](http://www.blueobelisk.org/repos/blueobelisk/). (project started, in part, to validate and improve Open Babel data)
-   Improved z-matrix code (CartesianToInternal / InternalToCartesian).
-   Countless bug fixes.

New File Formats
----------------

-   Import & Export:
    -   [ChemDraw Connection Table](/ChemDraw_Connection_Table "wikilink")
    -   [CML React](/CML_React "wikilink") files
    -   [MDL Molfile](/MDL_Molfile "wikilink") V3000
    -   [MDL RXN](/MDL_RXN "wikilink") files
    -   Open Babel [Free Form Fractional](/Free_Form_Fractional "wikilink") (crystallographic coordinates)\]
    -   Open Babel [FastSearch](/FastSearch "wikilink") database format
    -   Open Babel [Fingerprint](/Fingerprint "wikilink") format
    -   [PCModel](/PCModel "wikilink") format
    -   [YASARA Yob](/YASARA_Yob "wikilink") format
    -   [TurboMole Coordinate](/TurboMole_Coordinate "wikilink")
    -   Improved [CML](/CML "wikilink") support
    -   Improved [Gaussian98/03 Output](/Gaussian98/03_Output "wikilink") support
    -   Improved [SMILES](/SMILES "wikilink") import / export
-   Import-Only:
    -   [PubChem](/PubChem "wikilink") XML
-   Export-Only:
    -   [MPQC simplified input](/MPQC_simplified_input "wikilink")
    -   “[Raw Copy](/Raw_Copy "wikilink")” format (i.e., copy the raw input file)
    -   [Sybyl MPD](/Sybyl_descriptor "wikilink") descriptor format
    -   IUPAC [InChI](/InChI "wikilink") descriptor
-   Changed formats:
    -   MMADS - eliminated
    -   bin - OpenEye binary v 1, eliminated
    -   [GROMOS96](/GROMOS96 "wikilink") - changed from separate g96a & g96nm types to a unified g96 type. Defaults to output Angstroms, Use -xn to output nm.
    -   Titles - eliminated -- can be produced with [SMILES](/SMILES "wikilink") -xt

[Category:Releases](/Category:Releases "wikilink")
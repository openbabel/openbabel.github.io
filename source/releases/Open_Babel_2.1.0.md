---
title: Open Babel 2.1.0
---

Open Babel 2.1.0 was released on 2007-04-07.

Release Notice
--------------

This release represents a major update and should be a stable upgrade, strongly recommended for **all** users of Open Babel. Highlights include a new framework for molecular mechanics force fields, a framework for canonical, unique atom numbering (i.e., an open source canonical SMILES implementation), new scripting interfaces in Ruby and Java, enhancements to the developer API, several highly-requested file formats, and many, many bug fixes and improvements.

What's New from 2.0.2
---------------------

-   Now handles molecules with &gt;65536 atoms or bonds. Some PDB entries, in particular have such large molecular systems.
-   New features for molecular mechanics force fields, including energy evaluation and geometry optimization. Ultimately, this will enable coordinate generation and refinement for [SMILES](/SMILES "wikilink") and other formats.
    -   (A flexible force field framework is available for developers.)
-   Implementation of the open source Ghemical all atom force field.
-   Framework for canonical atom numbering, including a new canonical SMILES format.
-   New support for [Ruby](/Ruby "wikilink") and [Java](/Java "wikilink") interfaces to the Open Babel library.
-   Improved scripting interfaces through [Perl](/Perl "wikilink") and [Python](/Python "wikilink"), including the new “pybel” module with a more Python-like syntax.
-   Automatically handles reading from text files with DOS or Mac OS 9 line endings.
-   Many enhancements to the Open Babel API: See the Developers API Notes for more information.
-   New [obenergy](/obenergy "wikilink") tool - evaluate the energy of a molecule using molecular mechanics.
-   New [obminimize](/obminimize "wikilink") tool - optimize the geometry of structures using molecular mechanics.
-   New [obrotamer](/obrotamer "wikilink") tool - generate random rotational isomers for conformational searching.
-   Improved [obprop](/obprop "wikilink") tool - outputs a variety of molecular properties including Topological Polar Surface Area (TPSA), Molar Refractivity (MR), and logP.
-   The [babel](/babel "wikilink") tool can now setting program keywords for some quantum mechanics formats from the command-line, including: GAMESS, Gaussian, Q-Chem, and MOPAC.
    -   (This feature can also be accessed by developers and expanded to other formats.)
-   New options for [babel](/babel "wikilink") tool, including:
    -   -e for continuing after errors
    -   -k for translating computational keywords (e.g., GAMESS, Gaussian, etc.)
    -   --join to join all input molecules into a single output
    -   --separate to separate disconnected fragments into separate molecular records
    -   -C (combine mols in first file with others having the same name)
    -   --property to add or replace a property (e.g., in an MDL SD file)
    -   --title to add or replace the molecule title
    -   --addtotitle to append text to the current molecule title
    -   --addformula to append the molecular formula to the current title
-   Many more bug fixes and small feature improvements.

New File Formats
----------------

-   Import & Export:
    -   [Carine's ASCII Crystal (ACR)](/ACR "wikilink")
    -   ChemDraw [CDX](/ChemDraw_CDX "wikilink") & [CDXML](/ChemDraw_CDXML "wikilink")
    -   [Crystallographic Interchange Format (CIF)](/CIF "wikilink")
    -   [Fasta Sequence](/Fasta_Sequence "wikilink")
    -   [Thermo Format](/Thermo "wikilink")
-   Import only:
    -   [Gaussian fchk](/Gaussian_fchk "wikilink")
    -   [InChI](/InChI "wikilink")
-   Export only:
    -   [Open Babel MolReport](/Open_Babel_MolReport "wikilink")
    -   [Titles](/Titles "wikilink")

[Category:Releases](/Category:Releases "wikilink")

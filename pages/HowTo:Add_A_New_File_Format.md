---
title: HowTo:Add A New File Format
permalink: /HowTo:Add_A_New_File_Format/
---

Adding support for a new file format is a relatively easy process, particularly with Open Babel 2.0 and later. This guide outlines several important steps to remember when developing a format translator.

1.  Create a file for your format in `src/formats/` or `src/formats/xml/` (for XML-based formats). Ideally, this file is self-contained, although several formats modules are compiled across multiple source code files.
2.  Take a look at other file format code, particularly `exampleformat.cpp`, which contains a heavily-annotated description of writing a new format. XML formats need to take a different approach; see the code in `xcmlformat.cpp` or `pubchemformat.cpp`.
3.  When reading in molecules (and thus performing a lot of molecular modifications) call `OBMol::BeginModify()` at the beginning and `OBMol::EndModify()` at the end. This will ensure that perception routines do not run while you read in a molecule and are reset after your code finishes.
4.  Currently, lazy perception does not include connectivity and bond order assignment. If your format does not include bonds, make sure to call `OBMol::ConnectTheDots()` and `OBMol::PerceiveBondOrders()` after `OBMol::EndModify()` to ensure bonds are assigned.
5.  Consider various input and output options that users can set from the command-line or GUI. For example, many quantum mechanics or other formats which do not recognize bonds, offer the following options (GUI programs often offer these as a sub-menu which appears when choosing the appropriate format):
    -   `-as` Call only `OBMol::ConnectTheDots()` (single bonds only)
    -   `-ab` No bond perception
6.  Make sure to use generic data classes like `OBUnitCell` and others as appropriate. If your format stores any sort of common data types, consider adding a subclass of `OBGenericData` for use by other formats and user code.
7.  Please make sure to add several example files to the [test set repository](/Repository "wikilink"). Ideally, these should work several areas of your import code -- in the end, the more robust the test set, the more stable and useful Open Babel will be. The test files should include at least one example of a correct file and one example of an invalid file (i.e., something which will properly be ignored and not crash [babel](/babel "wikilink")).
8.  That's it! Contact the [openbabel-discuss mailing list](mailto:openbabel-discuss@lists.sourceforge.net) with any questions, comments, or to contribute your new format code.

After the code is released in a new [version](/releases "wikilink"), a new entry for your format should be added to this website under the [formats](/:Category:Formats "wikilink") category and to the [list of extensions](/list_of_extensions "wikilink") pages. See some of the examples for more information.

[Category:Contribute](/Category:Contribute "wikilink")
---
title: XYZ (format)
permalink: /XYZ_(format)/
---

#### Input Format

The “XYZ” chemical file format is widely supported by many programs, although no formal specification has been published. Consequently, Open Babel attempts to be extremely flexible in parsing XYZ format files. Similar formats include [Tinker XYZ](/Tinker_XYZ "wikilink") and [UniChem XYZ](/UniChem_XYZ "wikilink") which differ slightly in the format of the files. (Notably, [UniChem XYZ](/UniChem_XYZ "wikilink") uses the atomic number rather than element symbol for the first column.)

-   Line one of the file contains the number of atoms in the file.
-   Line two of the file contains a title, comment, or filename.

Any remaining lines are parsed for atom information. Lines start with the element symbol, followed by X, Y, and Z coordinates in angstroms separated by whitespace.

Multiple molecules / frames can be contained within one file.

#### Output Format

The first line written is the number of atoms in the molecule (**Warning:** The number of digits is limited to three for some programs, e.g. maestro). Line two is the title of the molecule or the filename if no title is defined. Remaining lines define the atoms in the file. The first column is the atomic symbol (right-aligned on the third character), followed by the XYZ coordinates in “10.5” format, in angstroms. This means that all coordinates are printed with five decimal places.

### Example File

    12
    benzene example
      C        0.00000        1.40272        0.00000
      H        0.00000        2.49029        0.00000
      C       -1.21479        0.70136        0.00000
      H       -2.15666        1.24515        0.00000
      C       -1.21479       -0.70136        0.00000
      H       -2.15666       -1.24515        0.00000
      C        0.00000       -1.40272        0.00000
      H        0.00000       -2.49029        0.00000
      C        1.21479       -0.70136        0.00000
      H        2.15666       -1.24515        0.00000
      C        1.21479        0.70136        0.00000
      H        2.15666        1.24515        0.00000

[Category:Formats](/Category:Formats "wikilink")
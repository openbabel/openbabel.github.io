---
title: ChemSpotlight
permalink: /ChemSpotlight/
---

ChemSpotlight is a Spotlight metadata importer plugin for Apple's [Mac OS X 10.4 Tiger](http://www.apple.com/macosx/), which reads common chemical file formats (MDL .mol, .mdl, .sd, .sdf, Tripos .mol2, Protein Data Bank .pdb, Chemical Markup Language .cml, and XYZ) using the Open Babel chemistry library. It is provided as a Universal Binary for PowerPC and Intel, for optimized performance on both.

It’s probably easier to show the results from ChemSpotlight than to describe it. ChemSpotlight indexes chemistry files, adds molecular formulas (complete with subscripts in the Finder), molecular weight, and a variety of other information for Spotlight searches and “Get Info” windows. Notice the computed chemical formula and molecular weight information for this file:

[Image:ChemSpotlight.png](/Image:ChemSpotlight.png "wikilink")

ChemSpotlight adds all of this information to the Spotlight index, allowing chemical searches for a range of properties. Since Spotlight indexes automatically in the background as files are created or modified, after installing, you don’t need to worry about updating the database.

### Technical Details

ChemSpotlight reads in files using the Open Babel library and then generates the following fields for any molecules it finds:

<table>
<tr>
<th>
Metadata Field

</th>
<th>
Notes

</th>
</tr>
<tr>
<td>
net_sourceforge_openbabel_Chirality

</td>
<td>
True/False (1/0)

</td>
</tr>
<tr>
<td>
net_sourceforge_openbabel_Dimension

</td>
<td>
0D/2D/3D depending on the coordinates found

</td>
</tr>
<tr>
<td>
net_sourceforge_openbabel_DisplayFormula

</td>
<td>
Formula with subscripts for Finder “Get Info” windows

</td>
</tr>
<tr>
<td>
net_sourceforge_openbabel_Formula

</td>
<td>
Chemical formula in standard [Hill Order](http://en.wikipedia.org/wiki/Hill_system_order)

</td>
</tr>
<tr>
<td>
net_sourceforge_openbabel_Mass

</td>
<td>
Standard molecular weight in a.m.u. (g/mol)

</td>
</tr>
<tr>
<td>
net_sourceforge_openbabel_ExactMass

</td>
<td>
Molecular mass of most common isotopes for mass spectra

</td>
</tr>
<tr>
<td>
net_sourceforge_openbabel_NumAtoms

</td>
<td>
Number of atoms in the molecule

</td>
</tr>
<tr>
<td>
net_sourceforge_openbabel_NumBonds

</td>
<td>
Number of bonds in the molecule

</td>
</tr>
<tr>
<td>
net_sourceforge_openbabel_NumMols

</td>
<td>
Number of molecules in the file

</td>
</tr>
<tr>
<td>
net_sourceforge_openbabel_NumResidues

</td>
<td>
Number of biomolecule residues

</td>
</tr>
<tr>
<td>
net_sourceforge_openbabel_SMILES

</td>
<td>
[Daylight SMILES](http://www.daylight.com/smiles/) string for this molecule

</td>
</tr>
<tr>
<td>
net_sourceforge_openbabel_InChI

</td>
<td>
[IUPAC/NIST](http://www.iupac.org/inchi/) canonical identifier

</td>
</tr>
</table>
    # Return all files with at least one molecule with mass < 200
    mdfind "net_sourceforge_openbabel_Mass < 200"
    # The next line matches all files containing molecules with mass < 200 AND molecules with > 10 atoms
    mdfind "net_sourceforge_openbabel_Mass < 200 && net_sourceforge_openbabel_NumAtoms > 10"
    # Match the c1(c(cccc1)Br SMILES string (i.e., a literal string)
    mdfind "net_sourceforge_openbabel_SMILES = '*c1(c(cccc1)Br*'"

Note that the SMILES matching is for literal strings of SMILES. I don’t (yet) know how to use the Daylight SMARTS matching system inside Spotlight, although perhaps other tools can filter the results from Spotlight using the SMARTS system.

For more information, see the [ChemSpotlight homepage](http://geoffhutchison.net/projects/chem/).

[Category:Macintosh](/Category:Macintosh "wikilink")
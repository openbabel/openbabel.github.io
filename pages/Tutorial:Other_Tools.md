---
title: Tutorial:Other Tools
permalink: /Tutorial:Other_Tools/
---

There are a number of included tools that have been built using Open Babel, including [obprop](/obprop "wikilink"), [obgrep](/obgrep "wikilink"), [obchiral](/obchiral "wikilink"), [obfit](/obfit "wikilink"), and [obrotate](/obrotate "wikilink").

obprop
------

[obprop](/obprop "wikilink") calculates a couple of simple molecular properties (e.g., molecular mass and ring count).

`PROMPT> obprop ' mymols.sdf'  > 'outputfile.txt'`

`PROMPT>  cat  outputfile.txt`

`name MOL_00000067`
`mol_weight 191.989`
`num_rings 1`
`$$$$`
`name MOL_00000083`
`mol_weight 191.989`
`num_rings 1`
`$$$$`
`name MOL_00000105`
`mol_weight 191.989`
`num_rings 1`
`$$$$`
`name MOL_00000296`
`mol_weight 207.077`
`num_rings 1`
`$$$$`

obgrep
------

[obgrep](/obgrep "wikilink") can be used for structure-based searching for molecules inside multi-molecule files (e.g., SMILES, SDF, etc.) or across multiple files.

          -c    Print the number of matches

          -f    Full match, print matching-molecules only when the number of heavy
                atoms is also equal to the number of atoms in the SMARTS pattern

          -i<format>
                Specifies input and output format,

          -n    Only print the name of the molecules

          -t #  Print a molecule only if the pattern occurs # times inside the mol-
                ecule

          -v    Invert the matching, print non-matching molecules

To print just the names of those molecules containing bromobenzne:

`PROMPT>  obgrep  -n 'c1ccccc1Br'  'mymols.sdf'`

`MOL_00000067`
`MOL_00000083`
`MOL_00000105`
`MOL_00016985`
`MOL_00042466`
`MOL_00045017`
`MOL_00077464`
`MOL_00191850`
`MOL_00857068`
`MOL_01812494`
`MOL_02660600`
`MOL_02683063`
`MOL_02683851`
`MOL_02683853`
`MOL_02683854`
`MOL_03411551`
`MOL_03428533`
`MOL_03428552`
`MOL_03789141`
`MOL_04038961`

To simply count the number of molecules that match:

`PROMPT>  obgrep  -c -t 2 'c1ccccc1Br'  'mymols.sdf'`
`20`

To only select those compounds where the pattern occurs twice use:

`PROMPT>  obgrep  -n -t 2 'c1ccccc1Br'  'mymols.sdf'`
`MOL_04038961`

obchiral
--------

[obchiral](/obchiral "wikilink") prints molecular chirality information:

`PROMPT>  mymols.sdf`

`Molecule 1:  mol_1`
`Atom 2 Is Chiral C3`
`Volume= 8.35262`
`Atom refs= 1 2 3 4`
`Clockwise? 0`
`Molecule 2: mol_2`
`Atom 2 Is Chiral C3`
`Volume= -8.43506`
`Atom refs= 1 2 3 4`
`Clockwise? 0`
`Atom 3 Is Chiral N3`
`Volume= 2.15701`
`Atom refs= 1 2 3 4`
`Clockwise? 0`
`Molecule 3:  mol_3`
`Atom 2 Is Chiral C3`
`Volume= -8.37849`
`Atom refs= 1 2 3 4`
`Clockwise? 0`
`Atom 3 Is Chiral N3`
`Volume= 1.84595`
`Atom refs= 1 2 3 4`
`Clockwise? 0`
`Atom 19 Is Chiral C3`
`Volume= 10.331`
`Atom refs= 1 2 3 4`
`Clockwise? 0`

This information can be piped into a file like this:

`PROMPT>  obchiral 'mymols.sdf' > ''outputfile'.txt`

obfit
-----

[obfit](/obfit "wikilink") will superimpose molecules based on a SMARTS pattern. The atoms used to fit the two molecules are defined by the SMARTS pattern given by the user. It is useful to align congeneric series of molecules on a common structural scaffold for 3D-QSAR studies. It can also be useful for displaying the results of conformational generation.

`PROMPT>  obfit ' c1ccccc1Br ' static.sdf mymols.sdf`

obrotate
--------

[obrotate](/obrotate "wikilink") will batch-rotate dihedral angles matching SMARTS patterns. The obrotate program rotates the torsional (dihedral) angle of a specified bond in molecules to that defined by the user. In other words, it does the same as a user setting an angle in a molecular modelling package, but much faster and in batch mode (i.e. across multiple molecules in a file). The four atom IDs required are indexes into the SMARTS pattern, which starts at atom 0 (zero). The angle supplied is in degrees. The two atoms used to set the dihedral angle <atom1> and <atom4> do not need to be connected to the atoms of the bond <atom2> and <atom3> in any way. The order of the atoms matters -- the portion of the molecule attached to <atom1> and <atom2> remain fixed, but the portion bonded to <atom3> and & <atom4> moves. Let's say that you want to define the conformation of a large number of molecules with a pyridyl scaffold and substituted with an aliphatic chain at the 3-position, for example for docking or 3D-QSAR purposes.

To set the value of the first dihedral angle to 90 degrees:

`PROMPT>  obrotate 'c1ccncc1CCC' pyridines.sdf 5 6 7 8 90`

Here 6 and 7 define the bond to rotate in the SMARTS patter, i.e., c1-C and atoms 5 and 8 define the particular dihedral angle to rotate.

Since the atoms to define the dihedral do not need to be directly connected, the nitrogen in the pyridine can be used:

`PROMPT>  obrotate 'c1ccncc1CCC' pyridines.sdf 4 6 7 8 90`

Keep the pyridyl ring fixed and moves the aliphatic chain:

`PROMPT>  obrotate 'c1ccncc1CCC' pyridines.sdf 5 6 7 8 90`

Keep the aliphatic chain fixed and move the pyridyl ring:

`PROMPT>  obrotate 'c1ccncc1CCC' pyridines.sdf 8 7 6 5 90`

[Category:Guides](/Category:Guides "wikilink")
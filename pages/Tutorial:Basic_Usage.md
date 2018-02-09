---
title: Tutorial:Basic Usage
permalink: /Tutorial:Basic_Usage/
---

Open Babel User Documentation
=============================

The aim of this document is to provide real world examples of the syntax needed to use Open Babel, it is not a developers guide, which can be found [elsewhere](http://openbabel.sourceforge.net/api/).

To get help using Open Babel using the command-line, type babel -H (here, the command-line prompt is indicated using `PROMPT>`

`PROMPT> babel -H`

This will output the general syntax followed by a list of conversion options and the file formats currently supported.

     Open Babel converts chemical structures from one file format to another

     Usage: babel <input spec> <output spec> [Options]

     Each spec can be a file whose extension decides the format.
     Optionally the format can be specified by preceding the file by
     -i<format-type> e.g. -icml, for input and -o<format-type> for output

     See below for available format-types, which are the same as the
     file extensions and are case independent.
     If no input or output file is given stdin or stdout are used instead.

     More than one input file can be specified and their names can contain
     wildcard chars (* and ?).The molecules are aggregated in the output file.

     Conversion options
       -f <#> Start import at molecule # specified
       -l <#> End import at molecule # specified
       -t All input files describe a single molecule
       -e Continue with next object after error, if possible
       -z Compress the output with gzip
       -H Outputs this help text
       -Hxxx (xxx is file format ID e.g. -Hcml) gives format info
       -Hall Outputs details of all formats
       -V Outputs version number
       -F Outputs the available fingerprint types
       -m Produces multiple output files, to allow:
          Splitting: e.g.        babel infile.mol new.smi -m
            puts each molecule into new1.smi new2.smi etc
          Batch conversion: e.g. babel *.mol -osmi -m
            converts each input file to a .smi file
     For conversions of molecules
        Additional options :
        -d Delete Hydrogens
        -h Add Hydrogens
        -p Add Hydrogens appropriate for pH
        -b Convert dative bonds e.g.[N+]([O-])=O to N(=O)=O
        -c Center Coordinates
        -j Join all input molecules into a single output molecule
        -s"smarts" Convert only molecules matching SMARTS:
        -v"smarts" Convert only molecules NOT matching SMARTS:

     Interface to OBAPI internals
      API options, e.g. ---errorlevel 2
       errorlevel # to control logging and reporting

     The following file formats are recognized:
       alc -- Alchemy format
       bgf -- MSI BGF format
       box -- Dock 3.5 Box format
       bs -- Ball and Stick format
       c3d1 -- Chem3D Cartesian 1 format
       c3d2 -- Chem3D Cartesian 2 format
       caccrt -- Cacao Cartesian format
       cache -- CAChe MolStruct format [Write-only]
       cacint -- Cacao Internal format [Write-only]
       car -- Accelrys/MSI Biosym/Insight II CAR format [Read-only]
       ccc -- CCC format [Read-only]
       cht -- Chemtool format [Write-only]
       cml --  Chemical Markup Language
       cmlr --  CML Reaction format
       com -- Gaussian 98/03 Cartesian Input [Write-only]
       copy -- Copies raw text [Write-only]
       crk2d -- Chemical Resource Kit diagram format (2D)
       crk3d -- Chemical Resource Kit 3D format
       csr -- Accelrys/MSI Quanta CSR format [Write-only]
       cssr -- CSD CSSR format [Write-only]
       ct -- ChemDraw Connection Table format
       dmol -- DMol3 coordinates format
       ent -- Protein Data Bank format
       feat -- Feature format
       fh -- Fenske-Hall Z-Matrix format [Write-only]
       fix -- SMILES FIX format [Write-only]
       fpt -- Fingerprint format [Write-only]
       fract -- Free Form Fractional format
       fs -- FastSearching
       g03 -- Gaussian98/03 Output [Read-only]
       g98 -- Gaussian98/03 Output [Read-only]
       gam -- GAMESS Output [Read-only]
       gamin -- GAMESS Input [Write-only]
       gamout -- GAMESS Output [Read-only]
       gau -- Gaussian 98/03 Cartesian Input [Write-only]
       gpr -- Ghemical format
       gr96 -- GROMOS96 format [Write-only]
       hin -- HyperChem HIN format
       inchi -- InChI format [Write-only]
       inp -- GAMESS Input [Write-only]
       ins -- ShelX format [Read-only]
       jin -- Jaguar input format [Write-only]
       jout -- Jaguar output format [Read-only]
       k -- Compares first molecule to others using InChI. [Write-only]
       mdl -- MDL MOL format
       mmd -- MacroModel format
       mmod -- MacroModel format
       mol -- MDL MOL format
       mol2 -- Sybyl Mol2 format
       mopcrt -- MOPAC Cartesian format
       mopout -- MOPAC Output format [Read-only]
       mpd -- Sybyl descriptor format [Write-only]
       mpqc -- MPQC output format [Read-only]
       mpqcin -- MPQC simplified input format [Write-only]
       nw -- NWChem input format [Write-only]
       nwo -- NWChem output format [Read-only]
       pc --  PubChem format  [Read-only]
       pcm -- PCModel Format
       pdb -- Protein Data Bank format
       pov -- POV-Ray input format [Write-only]
       pqs -- Parallel Quantum Solutions format
       prep -- Amber Prep format [Read-only]
       qcin -- Q-Chem input format [Write-only]
       qcout -- Q-Chem output format [Read-only]
       report -- Open Babel report format [Write-only]
       res -- ShelX format [Read-only]
       rxn -- MDL RXN format
       sd -- MDL MOL format
       sdf -- MDL MOL format
       smi -- SMILES format
       test -- Test format [Write-only]
       tmol -- TurboMole Coordinate format
       txyz -- Tinker MM2 format [Write-only]
       unixyz -- UniChem XYZ format
       vmol -- ViewMol format
       xed -- XED format [Write-only]
       xml --  General XML format [Read-only]
       xyz -- XYZ cartesian coordinates format
       yob -- YASARA.org YOB format
       zin -- ZINDO input format [Write-only]

     See further specific info and options using -H<format-type>, e.g. -Hcml

As mentioned above, for many of the file types there are additional options these can be listed using `babel -H`<format>.

`PROMPT> babel -Hcml`

     cml   Chemical Markup Language
      XML format. This implementation uses libxml2.
      Write options for CML: -x[flags] (e.g. -x1ac)
      1  output CML1 (rather than CML2)
      a  output array format for atoms and bonds
      h  use hydrogenCount for all hydrogens
      m  output metadata
      x  omit XML and namespace declarations
      N add namespace prefix to elements

     Specification at: http://wwmm.ch.cam.ac.uk/moin/ChemicalMarkupLanguage

File Conversion
---------------

To convert `mymols.sdf` to SMILES format.

`PROMPT> babel -isdf  'mymols.sdf' -osmi 'outputfile.smi'`

Multiple input files can be converted in batch format too. To convert all files ending in `.xyz` (`*.xyz`) to PDB files, you can type:

`PROMPT> babel *.xyz -opdb -m`

You may need to include the full path to the files e.g. '/Users/username/Desktop/mymols.sdf'. If no input or output specification is defined Open Babel will try to assign the filetype based on the file suffix.

Unless requested using the --gen3d option, Open Babel does not generate coordinates. If you convert from a SMILES to an SDF without specifying --gen3d, the resulting sdf will not contain coordinates.

If you want to remove all hydrogens when doing the conversion the command would be:

`PROMPT> babel -isdf  'mymols.sdf' -osmi 'outputfile.smi' -d`

If you want to add all hydrogens when doing the conversion the command would be:

`PROMPT> babel -isdf  'mymols.sdf' -osmi 'outputfile.smi' -h`

If you want to add hydrogens appropriate for pH7.4 when doing the conversion the command would be:

`PROMPT> babel -isdf  'mymols.sdf' -osmi 'outputfile.smi' -p`

The protonation is done an atom-by-atom basis so molecules with multiple ionizable centers will have all centers ionized.

Of course you don't actually need to change the file type to modify the hydrogens if you want to add all hydrogens the command would be:

`PROMPT> babel -isdf  'mymols.sdf' -osdf 'mymols_H.sdf' ' -h`

Some functional groups e.g. nitro or sulphone can be represented either as \[N+\](\[O-\])=O or N(=O)=O, to convert all to the dative bond form.

`PROMPT> babel -isdf  'mymols.sdf'  -osmi 'outputfile.smi' -b`

If you only want to convert a subset of molecules you can define them using -f and -l, so to convert molecules 2-4 of the file mymols.sdf type:

`PROMPT> /babel   'mymols.sdf' -f 2 -l 4 -osdf 'outputfile.sdf'`

Alternatively you can select a subset matching a SMARTS pattern, so to select all molecules containing bromobenzene use:

`PROMPT> babel   mymols.sdf  -osdf  'selected.sdf'    -s 'c1ccccc1Br'`

You can select a subset that do not match a SMARTS pattern, so to select all molecules not containing bromobenzene use:

`PROMPT> babel   mymols.sdf  -osdf  'selected.sdf'    -v 'c1ccccc1Br'`

You can of course combine options, so to join molecules and add hydrogens type:

`PROMPT> babel   mymols.sdf' -osdf ' myjoined.sdf' -h   -j`

The output file can be compressed with gzip, but note if you don't specify the “.gz” suffix it will not be added automatically, which could cause problems when you try to open the file.

`PROMPT>  babel   ' /mymols.sdf' -osdf 'outputfile.sdf.gz'     -z`

[Category:Guides](/Category:Guides "wikilink")
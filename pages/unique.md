---
title: --unique
permalink: /--unique/
---

\[Introduced in OpenBabel version 2.3.0\]

The --unique option is used to remove, i.e. not output, any chemically identical molecules during conversion:

` babel  infile.xxx  outfile.yyy  --unique [param]`

The optional parameter param defines what is regarded as “chemically identical”. It can be the name of any *descriptor*, although not many are likely to be useful. If param is omitted, the InChI descriptor is used. Other useful descriptors are 'cansmi' and 'cansmiNS' (canonical SMILES, with and without stereochemical information),'title' and truncated InChI,see below.

Note that if you want to use --unique without a parameter with babel, it needs to be last on the line. With the alternative commandline interface, obabel, it can be anywhere after the output file.

A message is output for each duplicate found:

` ==============================`
` *** Open Babel Warning`
` Removed methyl benzene - a duplicate of toluene (#1)`

Clearly, this is more useful if each molecule has a title. The (\#1) is the number of duplicates found so far.

If you wanted to identify duplicates but not output the unique molecules, you could use nulformat

` babel  infile.xxx  -onul  --unique    `

Truncated InChI
---------------

It is possible to relax the criterion by which molecules are regarded as “chemically identical” by using a truncated InChI specification as param. This takes advantage of the layered structure of InChI. So to remove duplicates, treating stereoisomers as the same molecule:

` babel  infile.xxx  outfile.yyy  --unique /nostereo`

Truncated InChI specifications start with '/' and are case-sensitive. param can be a concatenation of these e.g. /nochg/noiso :

` /formula   formula only`
` /connect   formula and connectivity only`
` /nostereo  ignore E/Z and sp3 stereochemistry`
` /nosp3     ignore sp3 stereochemistry`
` /noEZ      ignore E/Z stereoochemistry`
` /nochg     ignore charge and protonation`
` /noiso     ignore isotopes`

Multiple files
--------------

The input molecules do not have to be in a single file. So to collect all the unique molecules from a set of mol files:

` babel  *.mol  uniquemols.sdf  --unique`

If you want the unique molecules to remain in individual files:

` babel  *.mol  U.mol  -m  --unique`

On the GUI use the form:

` babel  *.mol  U*.mol  --unique`

Either form is acceptable on the Windows command line.

[Category:Guides](/Category:Guides "wikilink")

The unique molecules will be in files with the original name prefixed by 'U'. Duplicate molecules will be in similar files but with zero length, which you will have to delete yourself.
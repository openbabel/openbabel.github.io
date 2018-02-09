---
title: --splitinto
permalink: /--splitinto/
---

--splitinto
-----------

\[Delayed, will not be introduced in v2.3.0\]

The `--splitinto` option splits a chemical file into smaller files. For instance:

    babel bigfile.sdf -osdf --splitinto 3

will make `bigfile1.sdf, bigfile2.sdf and bigfile3.sdf`, each containing approximately one third of the molecules.The names are derived from the input file even if an output file name is specified; only the extension is significant.

If the output and input formats are different, it is just like doing a normal multiple conversion. The normal `babel` facilities, such as the [`--filter`` ``option`](/--filter_option "wikilink"), can be used, but the conversion could be slow with large files. If the formats are the same, the chemical objects are copied as raw bytes, which is faster and ensures no information is lost in the conversion process. This raw copying requires that the format has a `SkipObjects` function, which most formats suitable for multiple molecules do; this currently includes, smi, sdf, mol2, cml (and all other xml formats).

The raw copying process is designed for files of the form: *header object1 object2 ... objectN footer*. The *header* and the *footer* are copied to every output file. This is essential for xml files so that they remain well-formed, but may be useful for other formats. For instance, the provenance of a `smi` file that was recorded in introductory comment lines would appear in all the split files.

The range of the molecules that are copied can be restricted using the -f and -l options to specify the first and last molecule.

If `--splitinto` has a parameter which is negative (it will need to be in quotes except in the GUI), it specifies the number of objects in each output file (except the last). So, if `bigfile.sdf` contains 1000 molecules,

    babel bigfile.sdf -osdf -f700 --splitinto "-100"

will produce 3 files, each with 100 molecules, starting with the 700th molecule.

A message like:

    49133 objects split between 10 files, the first of which is xsaa1.sdf
    0 molecules converted

will be output. If the parameter of `--splitinto` is omitted, or is 0, only the number of objects is reported, and is probably the easiest way of doing this. (Used with `babel` on the command line, `--splitinto` has to be at the end of the line if its parameter is omitted; `obabel` is more flexible.) This object count is affected by any -f and -l option.

It should be possible to split large files, but the speed is only moderate. For files with a simple structure like SMILES files, it may be faster to use an operating system command (like split on linux) or cut and paste in a text editor. On the other hand, with this option you don't have to think: it should work in nearly all practical cases.
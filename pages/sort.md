---
title: --sort
permalink: /--sort/
---

\[Introduced in OpenBabel version 2.3.0\]

The --sort option is used to output molecules ordered by the value of a *descriptor*:

` babel  infile.xxx  outfile.xxx  --sort desc`

If the descriptor desc provides a numerical value, the molecule with the smallest value is output first. For descriptors which provide a string output the order is alphabetical, but for the inchi descriptor a more chemically informed order is used (e.g. “CH4” is before than “C2H6”, “CH4” is less than “ClH” hydrogen chloride).

The order can be reversed by preceding the descriptor name with '~', e.g.

` babel  infile.xxx  outfile.yyy  --sort ~logP`

As a shortcut, the value of the descriptor can be appended to the molecule name by adding a '+' to the descriptor, e.g.

` babel  aromatics.smi  -osmi  --sort ~MW+`
`  c1ccccc1C=C  styrene 104.149`
`  c1ccccc1C    toluene 92.1384`
`  c1ccccc1 benzene 78.1118`

[Category:Guides](/Category:Guides "wikilink")
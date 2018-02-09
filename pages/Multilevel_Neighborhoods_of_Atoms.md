---
title: Multilevel Neighborhoods of Atoms
permalink: /Multilevel_Neighborhoods_of_Atoms/
---

General Notes
-------------

Multilevel Neighborhoods of Atoms (MNA) descriptors are 2D molecular fragments suitable for use in QSAR modelling. The format outputs a complete descriptor fingerprint per molecule. Thus, a 27-atom (including hydrogen) molecule would result in 27 descriptors, one per line.

Specification
-------------

### Molecular fragment

MNA descriptors are generated recursively. Starting at the origin, each atom is appended to the descriptor immediately followed by a parenthesized list of its neighbours. This process iterates until the specified distance from the origin, also known as the depth of the descriptor.

### Element simplification

Elements are simplified into 32 groups. Each group has a representative symbol used to stand for any element in that group.

| Type | Elements                                                                                     |
|------|----------------------------------------------------------------------------------------------|
| H    | H                                                                                            |
| C    | C                                                                                            |
| N    | N                                                                                            |
| O    | O                                                                                            |
| F    | F                                                                                            |
| Si   | Si                                                                                           |
| P    | P                                                                                            |
| S    | S                                                                                            |
| Cl   | Cl                                                                                           |
| Ca   | Ca                                                                                           |
| As   | As                                                                                           |
| Se   | Se                                                                                           |
| Br   | Br                                                                                           |
| Li   | Li, Na                                                                                       |
| B    | B, Re                                                                                        |
| Mg   | Mg, Mn                                                                                       |
| Sn   | Sn, Pb                                                                                       |
| Te   | Te, Po                                                                                       |
| I    | I, At                                                                                        |
| Os   | Os, Ir                                                                                       |
| Sc   | Sc, Ti, Zr                                                                                   |
| Fe   | Fe, Hf, Ta                                                                                   |
| Co   | Co, Sb, W                                                                                    |
| Sr   | Sr, Ba, Ra                                                                                   |
| Pd   | Pd, Pt, Au                                                                                   |
| Be   | Be, Zn, Cd, Hg                                                                               |
| K    | K, Rb, Cs, Fr                                                                                |
| V    | V, Cr, Nb, Mo, Tc                                                                            |
| Ni   | Ni, Cu, Ge, Ru, Rh, Ag, Bi                                                                   |
| In   | In, La, Ce, Pr, Nd, Pm, Sm, Eu                                                               |
| Al   | Al, Ga, Y, Gd, Tb, Dy, Ho, Er, Tm, Yb, Lu, Tl                                                |
| R    | R, He, Ne, Ar, Kr, Xe, Rn, Ac, Th, Pa, U, Np, Pu, Am, Cm, Bk, Cf, Es, Fm, Md, No, Lr, Db, Jl |

### Cyclic

Acyclic atoms are preceded by a hyphen “-” mark.

### Example

Phenol

References
----------

-   [Article:fpbg99](/Article:fpbg99 "wikilink")

[Category:Formats](/Category:Formats "wikilink")
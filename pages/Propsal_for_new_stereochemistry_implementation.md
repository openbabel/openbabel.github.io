---
title: Propsal for new stereochemistry implementation
permalink: /Propsal_for_new_stereochemistry_implementation/
---

These are just public notes and ideas for v3.0 (should it ever happen) and likely to change. Revised [Chrismorl](/User:Chrismorl "wikilink") 08:32, 13 September 2008 (PDT)

The current handling of stereochemistry in OpenBabel is a bit disorganized, and there is a lack of clear documentation. Many of the bugs that are arising in v2.0 arise from the stereochemistry. It is not very clear when and how the overlapping 3D, 2D and 0D representations are used and on how to treat “either” or “undefined” stereochemistry.

There is a case for completely revising the implementation. This would be done by first writing a specification, which would be definitive. After revision all stereochemistry would conform to this specification, unlike at present where the API has features which are obsolete or undocumented. It would also be an opportunity to design the internal structures so that other kinds of stereochemistry - beyond cis/trans and tetrahedral - would be representable in OpenBabel.

How stereochemical information would be handled
-----------------------------------------------

Molecules can have 0D, 2D or 3D stereochemistry.

For atoms

-   3D molecules in x,y,z coordinates.
-   2D molecules in x,y coordinates + hash/wedge bonds.
-   2D molecules (with x,y coordinates) in atom parities.
-   0D molecules in atom parities.

For bonds

-   2D,3D molecules in x,y(,z) coordinates
-   0D molecules in a bond parities.

The 2D representation is all about display. There may be several different representations each of which may be be helpful to human understanding in certain circumstances, so there is no need to provide a “definitive” 2D representation. The form present when a molecule was input would not normally be changed.

0D representation, on the other hand, has the information reduced to its essentials, and would be used, for instance, to determine molecular uniqueness, so that it needs to be in a non-arbitrary form. If the atoms were put into canonical order, the 0D stereochemical representation should always be the same.

If there was a “Perception” event for a molecule, in which the implicit hydrogen, aromaticity etc., was sorted out, then it would be reasonable to also generate 0D stereo information from any 2D or 3D information present.

Generating 2D and 3D representations from the 0D one is moving from “definitive” information to something with a range of possibilities, and would be done only on demand.

Details of data representation in OBMol
---------------------------------------

### 2D tetrahedral stereo

Each bond has a wedge flag and a hash flag. It affects only the stereochemistry of the begin atom of the bond - which is taken to be the pointed end. Flags 0,0 are ordinary (not wedge, not hash)bonds and are the default. 1,1 represents a bond which is “either” - could be wedge or hash (but not ordinary).

### 0D tetrahedral stereo

Each OBAtom would contain a stereo-chemical type number. (Tetrahedral, by far the most common, would be 0.) Each atom would have a small bitset and each type would define what the bits meant, which would be based on the path followed when you traversed the neighbouring atoms in index order. Any implicit hydrogen would be last. This is the convention used in MDL files. Making the hydrogen explicit would not change the order. Similarly 'missing' atom in sulphones or other similar structures would also be regarded as having a high index.

So for the tetrahedral type, a 'parity' bit would be 1 when looking down from the first atom the path through the other three was clockwise. A second 'chiral' bit would be 1 if the chirality was defined. chiral parity

` 1      0    anticlockwise parity`
` 1      1    clockwise parity`
` 0      0    undefined`
` 0      1    either`

The 'either' type seems to be required for some purposes.

### Other types of atom stereochemistry

Allene and other structures with an odd number of C atoms connected by double bonds is treated analogously to tetrahedral stereochemistry by SMILES and OB should do the same: label the central atom as if the other doubly bonded carbons were not there.

For square planar two parity bits would be needed for a U, W or Z shaped path (see [1](http://www.daylight.com/dayhtml/doc/theory/theory.smiles.html#RTFToC25). There could be one 'chiral' bit and possibly more if more subtle degrees of uncertainty were required (unlikely).

If there was an implicit hydrogen on a chiral atom the vector would contain 3 atom indices. It would be assumed that the implict hydogen was last. (This is the convention used in MDL files).

### 0D cis/trans, cummulene, axial

Unlike the current situation, the bond stereo information would be attached to the bond with restricted rotation, not the adjacent ones. (SMILES uses up/down on adjacent bond which leads to over-complicated processing in molecules with conjugated double bonds - local analysis is not good enough.)

The OBBond would contain a pointer to a std::vector of atom pointers, which would be NULL for bonds without stereo information. The vector would contain atom indices X, A, B, Y

         X
          \
           A==B
               \
                X

A parity flag would be 1(true) for the structure as shown(trans) and 0 for cis. The atoms could be any with chemical significance, for instance A and B could be the ends of a set of adjacent double bonds in a cumulene, or X,Y could be distant atoms in some axial chiralities. It would be possible for the A and B atoms to be other than the atoms of the bond in order to represent some other types of stereochemistry. Any implementation needs to recognize this possibility. Any bond, not just double bonds, can have this information.
---
title: Chemical Markup Language
permalink: /Chemical_Markup_Language/
---

General XML Notes
-----------------

The XML formats require the XML text to be well formed but generally interpret it fairly tolerantly. Unrecognised elements and attributes are ignored and there are rather few error messages when any required structures are not found. This laxity allows, for instance, the reactant and product molecules to be picked out of a [CML React](/CML_React "wikilink") file using [CML](/CML "wikilink"). Each format has an element which is regarded as defining the object that OpenBabel will convert. For [CML](/CML "wikilink") this is <molecule>. Files can have multiple objects and these can be treated the same as with other multiple object formats like [SMILES](/SMILES "wikilink") and [MDL Molfile](/MDL_Molfile "wikilink"). So conversion can start at the nth object using the -fn option and finish before the end using the -ln option. Multiple object XML files also can be indexed and searched using [FastSearch](/FastSearch "wikilink"), although this has not yet been extensively tested.

CML Notes
---------

This format writes and reads CML XML files. To write CML1 format rather than the default CML2, use the -x1 option. To write the array form use -xa and to specify all hydrogens using the hydrogenCount attribute on atoms use -xh.

Crystal structures are written using the <crystal>, <xfract>) etc., elements if the OBMol has a OBGenericDataType::UnitCell data.

If the OBMol has no bonds, a <formula> element is written instead of the normal <atomArray> and <atom> elements.

All these forms are handled transparently during reading. Only a subset of CML elements and attributes are recognised, but these include most of those which define chemical structure, see below.

The following are read:

-   Elements:
    -   molecule, atomArray, atom, bondArray, bond, atomParity, bondStereo
    -   name, formula, crystal, scalar (contains crystal data)
    -   string, stringArray, integer, integerArray, float floatArray, builtin

<!-- -->

-   Attributes:
    -   On <molecule>: id, title, ref(in CMLReact)
    -   On <atom>: id, atomId, atomID, elementType, x2, y2, x3, y3, z3, xy2, xyz3, xFract, yFract, zFract, xyzFract, hydrogenCount, formalCharge, isotope, isotopeNumber, spinMultiplicity, radical(from Marvin), atomRefs4 (for atomParity)
    -   On <bond>: atomRefs2, order, CML1: atomRef, atomRef1, atomRef2

References
----------

-   [Article:rr99](/Article:rr99 "wikilink")
-   [Article:mr01](/Article:mr01 "wikilink")
-   [Article:gmrw01](/Article:gmrw01 "wikilink")
-   [Article:wil01](/Article:wil01 "wikilink")
-   [Article:mr03](/Article:mr03 "wikilink")
-   [Article:mrww04](/Article:mrww04 "wikilink")

[Category:Formats](/Category:Formats "wikilink")
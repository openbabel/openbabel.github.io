---
title: Generic Data
permalink: /Generic_Data/
---

The [OBGenericData](http://openbabel.sourceforge.net/api/classOpenBabel_1_1OBGenericData.shtml) class and its subclasses are mechanisms for storing arbitrary data inside an atom, a bond, a residue, a molecule -- almost any object in Open Babel.

Two key points are needed when discussing generic data classes. Accessing generic data can occur by two different mechanisms:

-   String *attributes*
-   Integer *type* keys

Generic data is stored internally as an array/vector, so access to a particular key is faster through use of the integer type, defined in the [OBGenericDataType](http://openbabel.sourceforge.net/api/namespaceOpenBabel_1_1OBGenericDataType.shtml) namespace. However, arbitrary string keys can be specified, particularly with the [OBPairData](/Pair_Data "wikilink") class, which is designed for assigning textual key/value pairs.

Defined Attribute Keys
----------------------

Currently defined text attribute keys by the Open Babel library include:

-   Comment
-   Conformers
-   ExternalBondData
-   PairData
-   Symmetry
-   UnitCell
-   UndefinedData
-   VirtualBondData

Defined Type Keys
-----------------

Current [OBGenericDataType](http://openbabel.sourceforge.net/api/namespaceOpenBabel_1_1OBGenericDataType.shtml) integer keys are defined in the [API documentation](http://openbabel.sourceforge.net/api/namespaceOpenBabel_1_1OBGenericDataType.shtml).

[Category:Developer](/Category:Developer "wikilink")
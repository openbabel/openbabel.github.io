---
title: Version 3.0 Design
permalink: /Version_3.0_Design/
---

Perception Framework
====================

Requirements
------------

-   Lazy evaluation of various properties
    -   Aromaticity (Internal, MMFF94, Smiles, Sybyl, ...)
    -   Atom Types (Internal, MMFF94, UFF, ...)
    -   Rings (SSSR, All, ...)
    -   Bond assignment (ConnectTheDots) - tricky
    -   Bond order (PerceiveBondOrders)
    -   Partial Charges
    -   Atom hybridizations
    -   Implicit valences
    -   Chirality
    -   ...
-   Each property can have multiple implementations. (Internal, MMFF94, Smiles, ...)
-   Adding new implementations for a given property should not require code changes in multiple places.
-   ... (add your requirements here)

Design
------

[Image:perception.png](/Image:perception.png "wikilink")

The OBPerceptionFacade gives a single interface which allows clients to switch between series of matching OBPerceptionModel implementations. The client could be an OBAtom, OBMol, OBFormat, OBForceField, ... calling SetModel on a molecule's perception facade (different molecules may need different perception implementations). This facade allow us to select series of coherent perception models (e.g. Internal, Smiles, MMFF, ...).

If new implementations or series of implementations are added, this would be the (single) place where we need to make code changes.

`void OBPerceptionFacade::SetModel(const std::string &model)`
`{`
`  if (model == `“`MMFF94`”`) {`
`    // perhaps do some specific MMFF94 stuff...`
`    OBAtomTypePerception::Instance().SetModel(model);`
`    OBPartialChargePerception::Instance().SetModel(model);`
`    OBAromaticityPerception::Instance().SetModel(model);`
`    ...`
`  } else if (model == `“`Smiles`”`) {`
`     ...`
`  } else ... `
`}`

Clients can also access OBAromaticityPerception directly if needed (e.g. A user adds its own perception model to assign atoms types, ... See “protected vs. public SetType()” below). However, OB could like OBAtom, OBFormat, ... should always go through the OBPerceptionFacade.

protected vs. public SetType()
------------------------------

When a client class calls OBAtom::SetType(), OB does no attempt to interpret the type. This has caused some confusion for beginning OB developers (see list). Another possible problem is a user calling SetType() without calling OBMol::SetAtomTypesPerceived() (or making a call to GetType()) first.

If we make SetType() and the equivalent functions for other properties protected, they can only be called by fiend class OBPerceptionModel.
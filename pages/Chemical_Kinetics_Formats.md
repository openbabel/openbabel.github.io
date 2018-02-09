---
title: Chemical Kinetics Formats
permalink: /Chemical_Kinetics_Formats/
---

**NOTE** This code and documentation is for development purposes. It may become part of version 2.2, but is not set in stone.

OBReaction
----------

Although most of the formats read, written and converted in OpenBabel are for molecules, the conversion framework is capable of handling other types of chemical (and indeed non-chemical) objects. The class OBReaction contains the basic information for a reaction: references to OBMol molecules for reactants and products, a title,comments and reversibility. More detailed information, for instance on its kinetic rate coefficient, is kept in an attached classes derived from OBGenericData. This provides a general way to extend, in the future, the description of reactions for use in other fields, like enzyme reactions. Current implementation is aimed at the chemical kinetics of large systems of reactions for combustion and atmospheric chemistry.

The references to molecules in OBReaction used smart pointers (std::tr1::shared_ptr<OBMol>) which considerably simplifies the housekeeping of deleting OBMol objects which are referred to in more than one reaction. Some systems may need to install the [Boost library](http://www.boost.org/) to provide this capability.

Reaction Formats
----------------

There is currently no generally accepted file format which describes both the kinetics of reactions and the chemical structure of the reactants and products. This would find use especially in various kinds of oxidation chemistry, for example, combustion, atmospheric chemistry, lubricant degradation and in vivo. The chemical structure of the fuel, pollutant, etc is clearly crucial to its behaviour.

The CML Reaction format implemented in OpenBabel is an attempt to provide such a description in a flexible way, and the conversion processes are designed to combine the structural and kinetics data when they come from different sources. Although the schema for CML Reaction format used here is based as far as is possible on that developed by Peter Murray Rust's Group (mainly aimed at enzyme reactions), the extensions are not part of any standard and could be modified to fit in with schemas developed by other groups.

### RXN Format

This very basic format from MDL is supported for both reading and writing.

### CHEMKIN Format

This is the most common format for combustion chemical kinetics. The species contain no structural information, but obtain their elemental composition from the thermodynamic data.

#### Reading

The format is called only once and sends each OBReaction for output (via AddChemObject) when it is ready. The ELEMENTS section is optional and is ignored. The SPECIES section is required. The THERMO section uses ThermoFormat to read the data in fixed format NASA Polynomial form. There is a check to see that all the species have thermodynamic data. If not, this is loaded from the file specified in the -af option, or the default “therm.dat” if there is no such option. Only the species with no data in the THERMO section get it from the external file. The internal thermodynamic data has precedence over that in the database. It is possible to override the internal data by using the -C option and preceding the input chemkin file by a input molecule file with thermodynamic data (thermo or cml formats, currently).

The format also accepts simple lists of reactions (without all the section keywords). There is then no check on the availability of thermo data, and the species need have nothing other than a name.

#### Writing

WriteMolecule()(badly named) is called for each OBReaction and is stored internally. When the last reaction has been received the output file is constructed.

### CMLReact Format

#### Reading

As with OpenBabel's other XML formats, the relevant data is extracted from the input, which accordingly can contain extensions and extraneous information.

#### Writing

If sent an OBMol, it is added to the format's internal list of molecules. Molecules added in this way are combined with any already present. In this way structure and properties can be added to the molecules in an OBReaction object (probably from a Chemkin or CMLReact input file). Thermodynamic data can also be updated from that in the OBReaction molecules in this way. So:

`  babel  some.smi  some.thermo  grim.ck  result.cmlr`

will update the thermodynamic data in the mechanism grim.ck for those molecules with the same name that appear appear in the some.thermo file, and will give structure to those in the file some.smi.

At the end, if there have been no reactions input, then an ordinary CML file is written with just the molecules in it.

There is a choice of how the molecules are output. The default is to collect them in an element <moleculeList>. The reactions are in a <reactionList> and in each <reaction> element each <molecule> has only a ref attribute containing its name. Alternatively, it is possible to embed the full description of each molecule in <reaction>.

[Category:Guides](/Category:Guides "wikilink")
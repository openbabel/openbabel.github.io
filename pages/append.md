---
title: --append
permalink: /--append/
---

*[Back to main Babel page](/Babel "wikilink")*

The commandline option --append adds extra information to the title of the molecule.

The information can be calculated from the structure of the molecule or can originate from a property attached to the molecule, usually from an sdf or cml input file. It is used like: <code>

` babel infile.sdf -osmi --append `“`MW`` ``CAT_NO`”

</code> MW is the ID of a Descriptor which calculates the molecular weight of the molecule, and CAT_NO is a property of the molecule from the sdf input file. The values of these are added to the title of the molecule. For input files with many molecules these additions are specific to each molecule. (The option --addtotitle adds the same text to every title.)

The append option takes one parameter, so that all the Descriptor IDs or properties name must be enclosed together in a single set of quotes.

If the name of the property in the sdf file (internally the Attribute in OBPairData) contains spaces, it should be written in the --append parameter with these replaced by underscore characters, '_'. So the example above would also append a property 'CAT NO'.

By default, the extra items are added to the title separated by spaces. But if the first character in the parameter is a whitespace or punctuation character other than '_', it is used as the separator instead. In the GUI, because tab is used to move between controls, if a tab character was required it would have to be pasted in.

[Category:Guides](/Category:Guides "wikilink")
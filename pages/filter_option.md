---
title: --filter option
permalink: /--filter_option/
---

*[Back to main Babel page](/Babel "wikilink")*

The command line option `--filter` restricts conversion to only those molecules which meet specified chemical (and other) criteria. It makes it easy to select a subset of molecules. The information to do this can come either from properties imported with the molecule, as from a SDF file, or from calculations made by OpenBabel on the molecule.

The option was introduced at revision 1953. The aim has been to make the option flexible and intuitive to use; don't be put off by the long description.

You use it like this: <code>

`  babel filterset.sdf -osmi --filter `“`MW<130`` ``ROTATABLE_BOND`` ``>`` ``2`”

</code> It takes one parameter which probably needs to be enclosed in double quotes to avoid confusing the shell or operating system. (You don't need the quotes with the Windows GUI.) It contains one or more conditional tests. By default, these have all to be true for the molecule to be converted. As well as this implicit AND behaviour, you can write a full Boolean expression, see below. As you can see, there can be spaces or not in sensible places and the conditional tests could be separated by a comma or semicolon.

You can filter on two types of property:

-   An SDF property, as the identifier ROTATABLE_BOND could be. There is no need for it to be previously known to OpenBabel.
-   An ID of an OBDescriptor object. This is a plug-in class so that new objects can easily be added. MW is the ID of a descriptor which calculates molecular weight. You can see a list of available descriptors by:

<code>

`  babel -L descriptors`

</code> or from a menu item in the GUI.

The descriptor names are case-insensitive. With the property names currently, you need to get the case right. Both types of identifier can contain letters, numbers and underscores, '_'. Properties can contain spaces, but then when writing the name in the filter parameter, you need to replace them with underscores. So in the example above, the test would also be suitable for a property 'ROTATABLE BOND'.

OpenBabel uses a SDF-like property (which is held internally in the class OBPairData) in preference to a descriptor if one exists in the molecule. So with the example file, which can be found [here](http://openbabel.svn.sourceforge.net/viewvc/openbabel/openbabel/trunk/test/files/filterset.sdf?revision=1955), <code>

`  babel filterset.sdf -osmi --filter `“`logP>5`”

</code> converts only a molecule with a property logP=10.900, since the others do not have this property and logP, being also a descriptor, is calculated and is always much less than 5.

If a property does not have a conditional test, then it returns true only if it exists. So <code>

`  babel filterset.sdf -osmi --filter `“`ROTATABLE_BOND`` ``MW<130`”

</code> converts only those molecules with a ROTATABLE_BOND property and a molecular weight less than 130. If you wanted to also include all the molecules without ROTATABLE_BOND defined, use: <code>

`  babel filterset.sdf -osmi --filter `“`!ROTATABLE_BOND`` ``||`` ``(ROTATABLE_BOND`` ``&`` ``MW<130)`”

</code> The ! means negate. AND can be & or &&, OR can be | or ||. The brackets are not strictly necessary here because & has precendent over | in the normal way. If the result of a test doesn't matter, it is parsed but not evaluated. In the example, the expression in the brackets is not evaluated for molecules without a ROTATABLE_BOND property. This doesn't matter here, but if evaluation of a descriptor involved a lot of computation, it would pay to include it late in the boolean expression so that there is a chance it is skipped for some molecules.

Descriptors must have a conditional test and it is an error if they don't. The default test, as used by MW or logP, is a numerical one, but the parsing of the text, and what the test does is defined in each descriptor's code (a virtual function in the OBDescriptor class). Three examples of this are described here.

1. String descriptors
---------------------

<code>

`  babel filterset.sdf -osmi --filter `“`title='Ethanol'`”

</code> The descriptor, title, when followed by a string, here enclosed by single quotes, does a case-sensitive string comparison. ('ethanol' wouldn't match anything in the example file.) The comparison does not have to be just equality: <code>

`  babel filterset.sdf -osmi --filter `“`title>='D'`”

</code> converts molecules with titles Dimethyl Ether and Ethanol in the example file.

It is not always necessary to use the single quotes when the meaning is unambiguous: the two examples above work without them. But a numerical, rather than a string, comparison is made if both operands can be converted to numbers. This can be useful: <code>

`  babel filterset.sdf -osmi --filter `“`title<129`”

</code> will convert the molecules with titles 56 123 and 126, which is probably what you wanted. <code>

`  babel filterset.sdf -osmi --filter `“`title<'129'`”

</code> converts only 123 and 126 because a string comparison is being made.

String comparisons can use \* as a wildcard. It can only be used as the first or last character of the string. So --filter "title='\*ol' will match molecules with titles 'methanol', 'ethanol' etc. and --filter "title='eth\*' will match 'ethanol', 'ethyl acetate', 'ethical solution' etc.

2. SMARTS descriptor
--------------------

This descriptor will do a SMARTS test (substructure and more) on the molecules. The smarts ID can be abreviated to s and the = is optional. More than one SMARTS test can be done: <code>

`  babel filterset.sdf -osmi --filter `“`s='CN'`` ``s!='[N+]'`”

</code> This provides a more flexible alternative to the existing -s and -v options, since the descriptor versions can be combined with other tests.

3. InChI descriptor
-------------------

<code>

`  babel filterset.sdf -osmi --filter `“`inchi='InChI=1/C2H6O/c1-2-3/h3H,2H2,1H3'`”

</code> will convert only ethanol. It uses the default parameters for InChI comparison, so there may be some messages from the InChI code. There is quite a lot of flexibility on how the InChI is presented (you can miss out the non-essential bits): <code>

`  babel filterset.sdf -osmi --filter `“`inchi='1/C2H6O/c1-2-3/h3H,2H2,1H3'`”
`  babel filterset.sdf -osmi --filter `“`inchi='C2H6O/c1-2-3/h3H,2H2,1H3'`”
`  babel filterset.sdf -osmi --filter `“`inchi=C2H6O/c1-2-3/h3H,2H2,1H3`”
`  babel filterset.sdf -osmi --filter `“`InChI=1/C2H6O/c1-2-3/h3H,2H2,1H3`”

</code> all have the same effect.

The comparison of the InChI string is done only as far as the parameter's length. This means that we can take advantage of InChI's layered structure. <code>

`  babel filterset.sdf -osmi --filter `“`inchi=C2H6O`”

</code> will convert both Ethanol and Dimethyl Ether.

[Category:Guides](/Category:Guides "wikilink")
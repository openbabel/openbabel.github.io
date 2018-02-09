---
title: XML
permalink: /XML/
---

This is a general XML “format” which reads a generic XML file and infers its format from the namespace as given in a `xmlns` attribute on an element. If a namespace is recognised as associated with one of the XML formats in OpenBabel, and the type of the object (e.g. a molecule) is appropriate to the output format then this is used to input a single object. If no namespace declaration is found the default format (currently [CML](/CML "wikilink")) is used.

The process is repeated for any subsequent input so that it is possible to input objects written in several different schemas from the same document. The file CMLandPubChem.xml illustrates this and contains molecules in both [CML](/CML "wikilink") and [PubChem](/PubChem "wikilink") formats.

[Category:Formats](/Category:Formats "wikilink")
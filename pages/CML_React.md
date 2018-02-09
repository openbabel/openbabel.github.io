---
title: CML React
permalink: /CML_React/
---

The implementation of this format which reads and writes to and from OBReaction objects is fairly minimal at present. (Currently the only other reaction format in OpenBabel is [RXN](/RXN "wikilink").) During reading, only the elements <reaction>, <reactant>, <product> and <molecule> are acted upon (the last through [CML](/CML "wikilink")). The molecules can be collected together in a list at the start of the file and referenced in the reactant and product via e.g. <molecule ref="mol1">.

On writing, the list format can be specified with the -xl option. The list containers are <moleculeList> and <reactionList> and the overall wrapper is <mechanism>. These are non-standard CMLReact element names and would have to be changed (in the code) to <list>,<list> and <cml> if this was unacceptable.

[Category:Formats](/Category:Formats "wikilink")
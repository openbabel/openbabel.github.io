---
title: SMARTS
permalink: /SMARTS/
---

The SMARTS format is a language for matching substructures of chemical files and was created by [Daylight Chemical Information Systems, Inc.](http://daylight.com) alongside the [SMILES](/SMILES "wikilink") format.

| Specification URL | <http://www.daylight.com/dayhtml/doc/theory/theory.smarts.html>                   |
|-------------------|-----------------------------------------------------------------------------------|
| Examples          | <http://www.daylight.com/dayhtml_tutorials/languages/smarts/smarts_examples.html> |

Limitations of the Open Babel SMARTS Implementation
---------------------------------------------------

The Open Babel implementation of SMARTS is not bug-free, nor does it support everything in the Daylight Toolkit. In particular, it is known to **not** currently support:

-   Cis/trans double bond stereochemistry. [Feature Request](http://sourceforge.net/tracker/index.php?func=detail&aid=1663730&group_id=40728&atid=428743)
    -   **Note:** The SMARTS '/' and '\\' notation will be accepted, but will not restrict to cis/trans functionality. Instead these bond notations are treated equivalently to a single bond.
-   Tetrahedral stereochemistry involving a lone pair (e.g. at a sulfoxide)
-   Component-level grouping (i.e., “(C).(C)”) [Feature Request](http://sourceforge.net/tracker/index.php?func=detail&aid=1155479&group_id=40728&atid=428743)
-   Use of non-tetrahedral chirality [Feature Request](http://sourceforge.net/tracker/index.php?func=detail&aid=1465334&group_id=40728&atid=428743)
-   Unspecified chirality (i.e., “@?”) [Bug Report](http://sourceforge.net/tracker/index.php?func=detail&aid=1364638&group_id=40728&atid=428740)

This list may not be complete. Please e-mail the [openbabel-discuss](mailto:openbabel-discuss@lists.sourceforge.net) mailing list if you have questions about the SMARTS support in Open Babel.

Open Babel Extensions to SMARTS Syntax
--------------------------------------

In addition to the Daylight Toolkit syntax, Open Babel also offers the following extensions to SMARTS which are not currently supported by Daylight:

-   Atom hybridization matching “^”. For example \[\#6^3\] matches a carbon atom (atomic number 6) with sp3 hybridization. Accepted hybridizations include:
    -   1 - sp e.g., \[\#6^1\]\[\#7\]
    -   2 - sp2 e.g., \[\#6^2\]\[\#6^2\]
    -   3 - sp3 e.g., \[\#8^3\]

[Category:Formats](/Category:Formats "wikilink")
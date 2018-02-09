---
title: Bond Orders
permalink: /Bond_Orders/
---

If the PDB file contains residues, then bond orders are set according to the standard form of the amino acid and the atom names in the PDB file.

For any other molecule (or file type), bond orders are set based on “perceiving” bond orders. The algorithm is based on [a talk by Roger Sayle](http://www.daylight.com/meetings/mug01/Sayle/m4xbondage.html) which has proven to be one of the most reliable methods for assigning bond orders.

Loosely speaking, the steps are something like this:

-   Determine atomic connection (from atoms which are close and likely bonded)
-   Determine atom type/hybridization from the number of connections and the angles between them (e.g., sp, sp2, sp3)
-   Run a quick “aliasing” check -- to have a double or triple bond, the atom must have at least one neighbor which could also have a double or triple bond.
-   Check for possibly aromatic rings (i.e., 5 and 6-member rings which are close to planar)
-   Run an aromaticity check on these possibly aromatic rings and assign Kekule bonds
-   Run a check for typical functional groups with multiple bonds
-   Last, but not least, fill any remaining multiple bond valences. For example, in a carbon which could have two possible double bonds, pick the neighbor which has the shortest bond distance.

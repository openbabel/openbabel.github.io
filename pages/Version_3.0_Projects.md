---
title: Version 3.0 Projects
permalink: /Version_3.0_Projects/
---

This page itemizes some projects for version 3.0, targeted for a release date of (???)

Everything here is intended as a proposal to be edited, revised, removed, added, etc. Please make suggestions and critiques!

Key Goals
---------

The version 3.0 release will not be backwards-compatible with version 2.x releases. For this reason, there may be a further 2.3 release to add some features to the 2.x release series before developers migrate to 3.0.

-   Faster compilation
-   Easier development
-   More modular library, flexible use of plugins

Design
------

Many design project proposals have been pushed into separate wiki pages.

-   [Improved Code Quality](/Code_Standards "wikilink")
-   [Improved Plugin Framework](/Plugins "wikilink")
-   [Indexing from 0, not 1](/Atom_Indexing "wikilink")

General projects
----------------

This list includes general ideas and goals for the 3.0 effort. The main push should be to refactor code to eliminate duplication and provide for a more logical class hierarchy. Some classes and methods have been deprecated and will be removed.

-   Atom indexing from 0 (i.e., all data finally indexed from 0)
    -   This will require considerable time to stabilize the code after this change.
    -   Atom indexing always goes from 0 to numAtoms-1, even when you delete, add, ... atoms. The function of an atom index is to provide an index which can be used to access a data field in a std::vector for example.
-   Unique Atom indexes will not go from 0 to numAtoms-1, they can be used to identify atoms for undo/redo purposes etc. Unique indexes are not reused
    -   [OB3: Atom Indexing & Unique IDs?](http://sourceforge.net/mailarchive/forum.php?thread_name=7A36CAC8-95CA-444F-B250-064C2647A081%40pitt.edu&forum_name=openbabel-devel)
    -   [Re: OB3: Atom Indexing & Unique IDs? (part 1)](http://sourceforge.net/mailarchive/forum.php?thread_name=20080828155321.GE20434%40cs.uiowa.edu&forum_name=openbabel-devel)
    -   [Re: OB3: Atom Indexing & Unique IDs? (part 2)](http://sourceforge.net/mailarchive/forum.php?thread_name=585727298-1219944536-cardhu_decombobulator_blackberry.rim.net-1936757983-%40bxe173.bisx.prod.on.blackberry&forum_name=openbabel-devel)
-   Stereochemistry updates
    -   [OB3: Stereochemistry](http://sourceforge.net/mailarchive/forum.php?thread_name=F04A58CB-8CB3-41FE-B326-9B209A600551%40geoffhutchison.net&forum_name=openbabel-devel)
    -   [Current status](/Stereochemistry "wikilink")
-   Valence model updates
    -   Retain any and all formal charges
    -   Valence and aromaticity models for different formats (e.g., SMILES is different from Tripos Mol2)
-   Fix some problems with scripting bindings
    -   [SetData and scripting bindings](http://sourceforge.net/mailarchive/message.php?msg_id=a882e48b0806170118vfc4fe1ehb8cac8b890bd0e3c%40mail.gmail.com)
-   Consider using base libraries
    -   Boost
    -   Eigen
-   Header reorganization
    -   Eliminate iostream from public headers (use iosfwd, etc.) to minimize compile and performance hit
    -   Minimize ABI / API breaking via opaque pointers
    -   Use minimal \#include statements in public headers (and class stubs as needed)
-   Revisit and refactor classes, methods (eliminate deprecated methods, migrate some methods to/from base classes)
    -   Continuing [Software Archeology](/Developer:Archeology "wikilink")
    -   Generalization of OBBond class
        -   Support for ionic bonds, hydrogen bonds, multi-center bonds, etc.
    -   Generalization of queries and filters (beyond just SMARTS matching)

<!-- -->

-   Performance improvements
    -   SMARTS performance
    -   Graph symmetry
    -   Atom typing
    -   Minimize use of SSSR (smallest ring size already determined by FindRingAtomsAndBonds)

<!-- -->

-   Plugin module improvements
    -   Fingerprints, force fields, formats
    -   Descriptors, filters
    -   Load only as needed

<!-- -->

-   Support for chemical data types:
    -   QM data support
        -   Vibrational modes, etc.
        -   Orbital energies (eigenvalues, eigenvectors)
        -   Cube files, grids, etc.
    -   Point group and space group symmetry perception
    -   Existing PDB, CML, SDF properties and metadata
    -   Keywords, author, references, etc.

<!-- -->

-   Consistent units:
    -   GetTorsion returns degrees while SetTorsion takes radians

<!-- -->

-   Callbacks:
    -   simple callback functions
    -   or type-safe signals (boost::signal or libcsig++)

Specific Developer Projects
---------------------------

-   [Geoff](/User:Ghutchis "wikilink")
    -   Atom and other objects indexed from 0
    -   Header reorganization to improve compile time
    -   Use of opaque data pointers to minimize API and ABI breaks
    -   Modified ring detection to minimize FindSSSR in aromaticity detection, etc.
    -   All-around help

<!-- -->

-   [Joerg](/User:Joerg_Kurt_Wegner "wikilink")
    -   Moving algorithms from JOELib to OpenBabel
        -   features
            -   Atom pairs (fast, creating fast index? algorithm for indexing?)
            -   Radial Basis Function, BCUT?
            -   Optimal Assignment kernel (slow, but very fancy)
        -   [Clique detection](http://en.wikipedia.org/wiki/Clique_%28graph_theory%29)
            -   [Product graph](http://en.wikipedia.org/wiki/Cartesian_product_of_graphs)

<!-- -->

-   Tim
    -   Force fields
        -   Port to eigen2
        -   Make memory usage for large molecules more linear (for non-bonded interactions, store only one OBFFCalculation for each unique A-B combination, ::Compute(...) will take positions as input. E_VDW and E_ELE iterate over all pairs or the neighbor list when cut-off are used.)
        -   Group-based cut-offs (avoid cut-off problems)
        -   Periodic boundary conditions (box)
        -   more generic way to read and specify parameter files (all AMBER ffs (GAFF), MMFF94/MMFF94s)
        -   Add AMBER force field

<!-- -->

-   [Chris](/User:Chrismorl "wikilink")
    -   Change implementation of plugin classes so types (like fingerprints, forcefields) are themselves plugins which allows generalized commandline listing.
    -   Add OBDescriptor plugin type as a wrapper for logP etc. and for existing properties like MW, (and others from JOELLib?).
    -   Add --filter option using descriptors and --desc (?) for adding as SDF-like properties (OBPairData)
    -   Eventually, move OBFormat to this plugin framework.
    -   Make proposal for cleaning up stereochemical representation.
    -   New OBReaction

[Category:Projects](/Category:Projects "wikilink")
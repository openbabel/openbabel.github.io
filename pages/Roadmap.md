---
title: Roadmap
permalink: /Roadmap/
---

The following list represents the *potential roadmap* for future development. Plans are flexible, particular if contributors are found to accomplish a “long-term” project sooner. [Suggestions and help](/HowTo:Contribute "wikilink") are always welcome!

Roughly speaking, the 2.0 release reflects a stable, concrete, documented API for developers as well as several full-featured programs for chemical file conversion, and other frequent uses. Future release numbers will indicate bug fixes (e.g., 2.0.1, 2.02, ... 2.0.x), feature enhancements retaining backwards compatibility (e.g., 2.1, ... 2.x), or major architectural changes breaking backwards compatibility (e.g., 3.0, 4.0, ...).

TODO
----

1.  Improve Python and Perl scripting support
    Particularly aim to improve integration with existing Python and Perl chemistry packages.
2.  Add [molecular mechanics](/molecular_mechanics "wikilink") force fields
    -   For coordinate generation and refinement
    -   For conformer / rotamer generation
    -   For energy evaluation
3.  Enhanced OOP class hierarchy for easier development
    -   Cleaner atom typing model, e.g., allowing multiple aromaticity models
    -   Subclasses of OBMol, e.g., allowing OBFractionalMol to support fractional coordinates
4.  Coordinate conversions
    -   2D → 3D cartesian coordinate refinement
    -   SMILES → 2D or 3D coordinate refinement
    -   3D → 2D coordinate projection
    -   “Symmetrize” molecules
    -   Convert to smallest symmetry-unique set
5.  Additional data type translation and perception
    -   All textual properties / descriptors in a format (e.g., MDL SD file)
    -   Molecular (point group) symmetry
    -   Space group symmetry
    -   Dipole, quadrupole, other multipoles
    -   Eigenvalues / orbital energies
    -   Eigenvectors / orbital surfaces
    -   Charge density (cube files)
    -   Molecular surfaces
    -   Vibrational modes and frequencies
    -   Atomic partial spin densities
    -   New partial charge methods to consider charged molecules/species
    -   Polarizability, hyperpolarizability (NLO)
    -   Molecular descriptors
    -   (Others? NMR shifts, UV/Vis spectra, electrochemistry... [Add suggestions here!](http://sourceforge.net/tracker/?atid=451585&group_id=40728&%5C%0A;func=browse))
6.  Additional file formats
    -   CIF format
    -   Canonical SMILES
    -   CMLcomp and full access to CML data
    -   CACTVS CTX format
    -   MDL XDfile
    -   Turbomole, Molden, ADF, Dalton, VASP, and other QM formats
    -   pdbq and pqr format
    -   Various “legacy” file formats
    -   ... (any and all chemistry-related file formats: [add suggestions here](http://sourceforge.net/tracker/?atid=447448&group_id=40728&%5C%0A;func=browse))
7.  Chemical objects beyond molecules
    -   Conversion of chemical kinetic reaction mechanisms formats: Chemkin, CMLReact
    -   Conversion of trajectory and dynamics formats: CHARMm, etc.
8.  Etc. ([Add your own thoughts here!](http://sourceforge.net/tracker/?atid=428743&group_id=40728&func=browse))

[Category:Contribute](/Category:Contribute "wikilink")[Category:Developer](/Category:Developer "wikilink")
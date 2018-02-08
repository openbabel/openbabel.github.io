---
title: Roadmap
permalink: /Roadmap/
---

Potential Roadmap
=================

The following list represents the potential roadmap for future development. Plans are flexible, particular if contributors are found to accomplish a “long-term” project sooner. [Suggestions and help](http://openbabel.sourceforge.net/howto-contribute.shtml) are always welcome!

Roughly speaking, the 2.0 release reflects a stable, concrete, documented API for developers as well as several full-featured programs for chemical file conversion, and other frequent uses. Future release numbers will indicate bug fixes (e.g., 2.0.1, 2.02, ... 2.0.x), feature enhancements retaining backwards compatibility (e.g., 2.1, ... 2.x), or major architectural changes breaking backwards compatibility (e.g., 3.0, 4.0, ...).

TODO
----

1.  Improve Python and Perl scripting support
    Particularly aim to improve integration with existing Python and Perl chemistry packages.
2.  Add molecular mechanics force fields
    -   For coordinate generation and refinement
    -   For conformer / rotamer generation
    -   For energy evaluation
3.  Enhanced OOP class hierarchy for easier development
    -   Cleaner atom typing model, e.g., allowing multiple aromaticity models
    -   Subclasses of OBMol, e.g., allowing OBFractionalMol to support fractional coordinates
4.  Coordinate conversions
    -   2D-&gt;3D cartesian coordinate refinement
    -   SMILES -&gt; 2D or 3D coordinate refinement
    -   3D-&gt;2D coordinate projection
    -   “Symmetrize” molecules
    -   Convert to smallest symmetry-unique set
5.  Additional data type translation and perception
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
    -   CHARMm and other trajectory and MD formats
    -   CACTVS CTX format
    -   MDL XDfile
    -   Turbomole, Molden, ADF, Dalton, VASP, and other QM formats
    -   Various “legacy” file formats
    -   ... (any and all chemistry-related file formats: [add suggestions here](http://sourceforge.net/tracker/?atid=447448&group_id=40728&%5C%0A;func=browse))
7.  Etc. ([Add your own thoughts here!](http://sourceforge.net/tracker/?atid=428743&group_id=40728&func=browse))

---
title: OBForceFieldMMFF94
permalink: /OBForceFieldMMFF94/
---

This class is a partial implementation of the all-atom [MMFF94](http://www.ccl.net/cca/data/MMFF94/) force field.

References:

1.  Thomas A. Halgren, J. Comput. Chem., 17, 490-519 (1996).
2.  Thomas A. Halgren, J. Comput. Chem., 17, 520-552 (1996).
3.  Thomas A. Halgren, J. Comput. Chem., 17, 553-586 (1996).
4.  Thomas A. Halgren and Robert B. Nachbar, J. Comput. Chem., 17, 587-615 (1996).
5.  Thomas A. Halgren, J. Comput. Chem., 17, 616-641 (1996).
6.  Thomas A. Halgren, J. Comput. Chem., 20, 720-729 (1999).
7.  Thomas A. Halgren, J. Comput. Chem., 20, 730-748 (1999).

The intent in the future is to produce a full, validated MMFF94 implementation.

### Use

The MMFF94 force field can be used for organic molecules and biomolecules. It describes non-bonded interactions between a ligand and protein very wel, this makes MMFF94 suitable for docking.

### Parameters

The MMFF94 parameters can be found in the data/mmff\*.par files.

### Functional form

#### Bond Stretching

<tex>E_{bond}=\\frac{1}{2}143.9325k_{b}(r_{ab}-r_{ab}^0)^2(1+cs(r_{ab}-r_{ab}^0)+\\frac{7}{12}cs^2(r_{ab}-r_{ab}^0)^2)</tex> (1)

<tex>k_b</tex>: bond stretching force constant (mmffbond.prm)

<tex>r_{ab}^0</tex>: ideal bond length (mmffbond.prm)

<tex>r_{ab}</tex>: bond length between atoms a and b

<tex>cs</tex>: cubic stretching constant (-2.0)

#### Angle Bending

<tex>E_{angle}=\\frac{1}{2}0.043844k_a(\\theta_{abc}-\\theta_{abc}^0)^2(1+cb(\\theta_{abc}-\\theta_{abc}^0))</tex> (2)

<tex>k_a</tex>: angle bending force constant (mmffang.prm)

<tex>\\theta_{abc}^0</tex>: ideal angle (mmffang.prm)

<tex>\\theta_{abc}</tex>: angle

<tex>cb</tex>: cubic bending constant (-0.007)

#### Bend Stretching

<tex>E_{strbnd}=2.51210(k_{abc}\\Delta r_{ab} + k_{cba}\\Delta r_{bc})\\Delta\\theta</tex> (3)

<tex>k_a</tex>: angle bending force constant (mmffang.prm)

<tex>\\theta_{abc}^0</tex>: ideal angle (mmffang.prm)

<tex>\\theta_{abc}</tex>: angle

<tex>cb</tex>: cubic bending constant (-0.007)

#### Torsional

#### Out-Of-Plane Bending

<tex>E_{oop}=0.043844\\frac{k_{abc:d}}{2}\\chi_{abc:d}^2</tex> (5)

#### Van der Waals

#### Electrostatic

### Validation

The validation is done using the [MMFF94 validation suite](http://www.ccl.net/cca/data/MMFF94/). The output from OBForceFieldMMFF94::Validate() can be found [here](http://home.scarlet.be/timvdm/MMFF94_validation_output.gz). There are still minir errors for the stretch-bending terms. The analytical gradients have also been implemented and their values are validated by comparing them to numerical derivatives.

[Category:Force_Fields](/Category:Force_Fields "wikilink")[Category:Developer](/Category:Developer "wikilink")
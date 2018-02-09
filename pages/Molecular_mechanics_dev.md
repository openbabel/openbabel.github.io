---
title: Molecular mechanics dev
permalink: /Molecular_mechanics_dev/
---

Introduction
------------

This page functions as a guide to the force field implementations in openbabel.

OBForceField class
------------------

This is the base class for all force fields. It contains gerenal functions that can be used by drived OBForceField_FFF_ classes (_FFF_ = MM2, MMFF94, Ghemical, ...). Each OBForceField_FFF_ class should declare the following functions.

### Members of OBForceField

#### OBMol _mol

Holds the OBMol object we are working with.

### Members of OBForceField_FFF_

#### vector<OBFFParameter> _ffxxxparams

A vector of OBFFParameter's to hold the parameters read from the parameter files. xxx is the energy term, so ther will be a _ffbondparams, _ffangleparams, ... NOTE: The name _ffxxxparams can be chosen differently, feel free to simple use bondparams etc.

#### vector<OBFF_XXX_Calculation> xxxcalculation

A vector of OBFF_XXX_Calculation_FFF_'s to hold the 'calculations'. (see below) NOTE: again feel free to use other names.

### Functions of OBForceField

#### SetLogFile(...)

#### SetLogLevel(int level)

#### GetParameter(...)

#### SteepestDescent(int steps)

#### ConjugateGradients(int steps)

#### UpdateCoordinates(OBMol &mol)

After a minimization (SteepestDescent, ConjugateGradient or other functions that change the coordinates of the molecule like GenerateCoordinates) the coordinates of the molecule given as parameter to Setup(OBMol &mol) are still unchanged. To update them, call UpdateCoordinates(OBMol &mol)

### Functions of OBForceField_FFF_

#### bool Setup(OBMol &mol)

-   Copy the OBMol object (_mol = &mol;)
-   Assign atom types
-   Open parameter files and store the parameters in OBFFParameter vectors
-   Setup the OBFF_XXX_Calculation_FFF_ vectors using the parameters from the corresponding OBFFParameter vector (_XXX_ = Bond, Angle, StrBnd, ...)

#### double Energy()

Return the total energy. Call the E_Bond(), E_Angle(), E_StrBnd() functions and return the sum of their return values.

#### double E_bond()

Return bond sretching energy.

#### double E_Angle()

Return angle bending energy.

#### double E_StrBnd() \[optional\]

Since not all force fields implement this energy term, this term is optional. If no E_StrBnd() function is defined by the OBForceField_FFF_ class, the E_StrBnd() function of OBForceField is called wich returns 0.0f. If the function is defined, it should return the stretch-bending enrgy;

#### double E_Torsion()

Return torsional energy.

#### double E_OOP() \[optional\]

Return out-of-plane bending energy. This term is optional.

#### double E_VDW()

Return the Van der Waals energy.

#### double E_Electrostatic()

Return the electrostatic energy.

OBFFParameter
-------------

The members of this class are used to hold the parameters for the force field. Below is a list of the members and their (possible) use:

-   int a, b, c, d: Used to hold the atom types in case the forcefield uses interger atomtypes.
-   char \*_a, \*_b, \*_c, \*_d: Used to hold the atom types in case the forcefield uses ascii atomtypes.
-   double dpar1, dpar2, ..., dpar5: Store force constants, ideal bond lengts and angles, ...
-   double ipar1, ipar2, ..., ipar5: Store interger type parameters (bondtype, angletype, ... in MMFF94)

There are no derived classes of the OBFFParameter class, all forcefields use this class in the same way.

OBFFCalculation
---------------

To minimize a structure, a large number of energy/gradient calculations have to be performed. To make the time needed for this task as short as possible we have to make sure not to do the same calculations over and over. Each time a E_Bond() function is called it will iterate over a vector of OBFF_XXX_Calcultion_FFF_'s and return the sum of the OBFF_XXX_Calculation_FFF_::GetEnergy() functions. This is the same for the other energy terms.

### Members of OBFFCalculation

Some general members are declared by OBFFCalculations itself. Other, more specific variables (and functions) are defined by the derived OBFF_XXX_Calculation_FFF_ classes.

-   double energy: Store the energy for the Calculation. This can be acceced later for logging. Note that this energy is the individual energy from a single bond stretch, angle bend, torsional, ... calculation between 2 to 4 atoms.
-   OBAtom \*a, \*b, \*c, \*d: Hold the atoms for the calculation (normally: 2-4 atoms)

### Functions of OBFFCalculation

The GetEnergy() and GetGradient(OBAtom \*atom) funtions of OBFFCalculation return 0 and (0,0,0) respectively. Therefore these should be overloaded by functions in the OBFF_XXX_Calculation_FFF_ class which perform the desired calculations. The GetGradient(OBAtom \*atom) functions is optional if numerical derivatives are acceptable.

#### double GetEnergy()

Calculate and return the energy using the atoms (from base class OBFFCalculation) and the parameters (from OBFF_XXX_Calculation_FFF_).

#### double GetGradient(OBAtom \*Atom)

Calculate and return the gradient with respect to the coordinates of atom using the atoms (from base class OBFFCalculation) and the parameters (from OBFF_XXX_Calculation_FFF_).

### Setting up the OBFF_XXX_Calculation_FFF_ vectors

For each energy term, a OBFF_XXX_Calculation_FFF_ vector must be filled with atoms and parameters for that term. So for a molecule with n bonds there are n items in the OBFFBondCalculation_FFF_ vector. These atoms are added in the OBForceField_FFF_::Setup(OBMol &mol) function after assigning the atomtypes, reading the parameter files and storing these parameters in OBFFParameter vectors. For example, when we have a bond with atoms that got types C and C assigned to them, we will iterate over the (vector<OBFFParameter>) _ffbondparams vector and find the parameters for that bond with OBForceField::GetParameter(...). When parameters are found we store them in a OBFF_XXX_Calculation_FFF_ together with the asociated atoms and push_back this to the (vector<OBFF_XXX_Calculation_FFF_>) xxxcalculation vector

Current implementations
-----------------------

Currently, the 2.1 development code includes partial implementations of three [force fields](/force_fields "wikilink"):

-   [OBForceFieldMM2](/OBForceFieldMM2 "wikilink")
-   [OBForceFieldMMFF94](/OBForceFieldMMFF94 "wikilink")
-   [OBForceFieldGhemical](/OBForceFieldGhemical "wikilink")

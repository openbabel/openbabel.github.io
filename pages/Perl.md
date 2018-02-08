---
title: Perl
permalink: /Perl/
---

Using Chemistry::OpenBabel with Perl
====================================

The Chemistry::OpenBabel module is designed to allow Perl scripts to use the C++ Open Babel library. The wrapper is generated using the SWIG package and provides access to almost all of the Open Babel interfaces via Perl, including the base classes OBMol, OBAtom, OBBond, and OBResidue, as well as the conversion framework OBConversion.

As such, essentially any call in the C++ API is available to Perl access with very little difference in syntax. This guide is designed to give examples of common Perl syntax for Chemistry::OpenBabel and pointers to the appropriate sections of the API documentation.

The example script below creates atoms and bonds one-by-one using the OBMol, OBAtom, and OBBond classes.

     #!/usr/bin/perl

     use Chemistry::OpenBabel;

     my $obMol = new Chemistry::OpenBabel::OBMol;

     $obMol->NewAtom();
     $numAtoms = $obMol->NumAtoms(); # now 1 atom

     my $atom1 = $obMol->GetAtom(1); # atoms indexed from 1
     $atom1->SetVector(0.0, 1.0, 2.0);
     $atom1->SetAtomicNum(6); # carbon atom

     $obMol->NewAtom();
     $obMol->AddBond(1, 2, 1); # bond between atoms 1 and 2 with bond order 1
     $numBonds = $obMol->NumBonds(); # now 1 bond

     $obMol->Clear();


More commonly, Open Babel can be used to read in molecules using the OBConversion framework. The following script reads in molecular information (a SMI file) from a string, adds hydrogens, and writes out an MDL file as a string.

     #!/usr/bin/perl

     use Chemistry::OpenBabel;

     my $obMol = new Chemistry::OpenBabel::OBMol;
     my $obConversion = new Chemistry::OpenBabel::OBConversion;
     $obConversion->SetInAndOutFormats("smi", "mdl");
     $obConversion->ReadString($obMol, "C1=CC=CS1");

     $numAtoms = $obMol->NumAtoms(); # now 5 atoms

     $obMol->AddHydrogens();
     $numAtoms = $obMol->NumAtoms(); # now 9 atoms

     my $outMDL = $obConversion->WriteString($obMol);


The following script writes out a file using a filename, rather than reading and writing to a Perl string.

     #!/usr/bin/perl

     use Chemistry::OpenBabel;

     my $obMol = new Chemistry::OpenBabel::OBMol;
     my $obConversion = new Chemistry::OpenBabel::OBConversion;
     $obConversion->SetInAndOutFormats("pdb", "mol2");
     $obConversion->ReadFile($obMol, "1ABC.pdb");

     $obMol->AddHydrogens();

     print "# of atoms: $obMol->NumAtoms()";
     print "# of bonds: $obMol->NumBonds()";
     print "# of residues: $obMol->NumResidues()";

     $obConversion->WriteFile($obMol, "1abc.mol2");


That's it! There's more information on particular calls in the [library API](http://openbabel.sourceforge.net/api/). Feel free to address questions to the [openbabel-scripting](mailto:openbabel-scripting@lists.sourceforge.net) mailing list.
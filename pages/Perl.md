---
title: Perl
permalink: /Perl/
---

Installation
------------

The Perl bindings can be installed either globally or locally as described in the following sections.

#### Install the Perl bindings globally

(A1) If OpenBabel was not installed in /usr/lib, you need to add the location of libopenbabel.so to LD_LIBRARY_PATH. For example, on my system libopenbabel.so was installed in /usr/local/lib:

    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib

If this is not done correctly, step A2 will give the error message “Can't build and link to 'openbabel'”.

(A2) If you want to use OpenBabel from Perl, you now need to compile the Perl extension.

Change directory to 'openbabel-2.2.1/scripts/perl' and run:

    perl Makefile.PL
    make
    make test # (Optional - this runs a few standard tests)

On an MacOSX system, you may get the following error when you run 'make':

    /usr/bin/ld: flag: -undefined dynamic_lookup can't be used with MACOSX_DEPLOYMENT_TARGET environment variable set to: 10.1

If this happens, you should set the value of the MACOSX_DEPLOYMENT_TARGET environment variable to match the MacOSX major version. For example, if you are using MacOSX 10.4.9, set MACOSX_DEPLOYMENT_TARGET to 10.4. Now run 'make' again.

(A3) To install the Perl bindings globally, as root type:

    make install

#### Install the Perl bindings locally

(B1) See Step A1 above.

(B2) To compile the Perl extension, instead of Step A2 above, use the 'PREFIX' option to Makefile.PL to specify an install location:

    perl Makefile.PL PREFIX=/home/noel/tree
    make
    make test # (Optional - this runs a few standard tests)

(B3) To install the Perl extension, run the following:

    make install

This installs the extension into something like /home/noel/tree/lib/perl/5.8.7, so you need to add “/home/noel/tree/lib/perl” to your PERL5LIB environment variable or specify this location in your Perl scripts as follows:

    use lib "/home/noel/tree/lib/perl"; # Must come before "use Chemistry::OpenBabel;"

Using Chemistry::OpenBabel
--------------------------

The Chemistry::OpenBabel module is designed to allow Perl scripts to use the C++ Open Babel library. The bindings are generated using the SWIG package and provides access to almost all of the Open Babel interfaces via Perl, including the base classes OBMol, OBAtom, OBBond, and OBResidue, as well as the conversion framework OBConversion.

As such, essentially any call in the C++ API is available to Perl access with very little difference in syntax. This guide is designed to give examples of common Perl syntax for Chemistry::OpenBabel and pointers to the appropriate sections of the [API documentation](http://openbabel.sourceforge.net/api/).

For more examples of using Open Babel inside Perl, see the [developer Perl tutorial](/Developer:Perl_Tutorial "wikilink").

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


That's it! There's more information on particular calls in the [library API](http://openbabel.sourceforge.net/api/) and the [developer Perl tutorial](/Developer:Perl_Tutorial "wikilink"). Feel free to address questions to the [openbabel-scripting](mailto:openbabel-scripting@lists.sourceforge.net) mailing list.

For developing chemistry in Perl, you should also look at the [PerlMol](http://perlmol.org/) project.

[Category:Developer](/Category:Developer "wikilink")
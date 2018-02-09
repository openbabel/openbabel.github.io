---
title: Developer:Perl Tutorial
permalink: /Developer:Perl_Tutorial/
---

This tutorial is aimed at developers looking to use Open Babel with Perl and the Chemistry::OpenBabel module. It will focus on the object-oriented application programmers' interface (API). There is also documentation on the [full API](http://openbabel.sourceforge.net/api/). Although Open Babel is written in C++, it also has bindings to [Perl](/Perl "wikilink") and [Python](/Python "wikilink") programming languages.

The tutorial is also available in other [programming languages](/Developer:Tutorial "wikilink").

Please feel free to comment on or improve this tutorial by e-mailing to [openbabel-scripting](mailto:openbabel-scripting@lists.sourceforge.net)

<h2>
Output Molecular Weight for a Multi-Molecule SDF File

</h2>
Let's say we want to print out the molecular weights of every molecule in an SD file. Why? Well, we might want to plot a histogram of the distribution, or see whether the average of the distribution is significantly different (in the statistical sense) compared to another SD file.

    use Chemistry::OpenBabel;

    my $obconversion = new Chemistry::OpenBabel::OBConversion;
    $obconversion->SetInFormat("sdf");
    my $obmol = new Chemistry::OpenBabel::OBMol;

    my $notatend = $obconversion->ReadFile($obmol, "../xsaa.sdf");
    while ($notatend) {
        print $obmol->GetMolWt(), "\n";
        $obmol->Clear();
        $notatend = $obconversion->Read($obmol);
    }

<h2>
Add and Delete Atoms

</h2>
This script shows an example of deleting and modifying atoms to transform one structure to a related one. It operates on a set of substituted thiophenes, deletes the sulfur atom (note that R1 and R2 may contain sulfur, so the SMARTS pattern is designed to constrain to the ring sulfur), etc. The result is a substituted ethylene, as indicated in the diagrams.

[Image:Tutorial-Thiophene.png](/Image:Tutorial-Thiophene.png "wikilink") [Image:Tutorial-Transform.png](/Image:Tutorial-Transform.png "wikilink")

    use Chemistry::OpenBabel;

    my $obMol = new Chemistry::OpenBabel::OBMol;
    my $obConversion = new Chemistry::OpenBabel::OBConversion;
    my $filename = shift @ARGV;

    $obConversion->SetInAndOutFormats("xyz", "mol");
    $obConversion->ReadFile($obMol, $filename);

    for (1..$obMol->NumAtoms()) {
        $atom = $obMol->GetAtom($_);
        # look to see if this atom is a thiophene sulfur atom
        if ($atom->MatchesSMARTS("[#16D2]([#6D3H1])[#6D3H1]")) {
        $sulfurIdx = $atom->GetIdx();
        # see if this atom is one of the carbon atoms bonded to a thiophene sulfur
        } elsif ($atom->MatchesSMARTS("[#6D3H1]([#16D2][#6D3H1])[#6]") ) {
        if ($c2Idx == 0) { $c2Idx = $atom->GetIdx(); }
        else {$c5Idx = $atom->GetIdx(); }
        }
    }

    # Get the actual atom objects -- indexing will change as atoms are added and deleted!
    $sulfurAtom = $obMol->GetAtom($sulfurIdx);
    $c2Atom = $obMol->GetAtom($c2Idx);
    $c5Atom = $obMol->GetAtom($c5Idx);

    $obMol->DeleteAtom($sulfurAtom);

    $obMol->DeleteHydrogens($c2Atom);
    $obMol->DeleteHydrogens($c5Atom);

    $c2Atom->SetAtomicNum(1);
    $c5Atom->SetAtomicNum(1);

    $obConversion->WriteFile($obMol, "$filename.mol");

[Category:Developer](/Category:Developer "wikilink")
---
title: Open Babel 2.0.1
permalink: /Open_Babel_2.0.1/
---

Open Babel 2.0.1 was released on 2006-04-17.

Release Notice
--------------

The Open Babel project is extremely proud to announce the release of Open Babel 2.0.1, the latest stable version of the free chemistry file translation program and chemistry software library.

This release represents a bug-fix release and should be a stable upgrade, recommended for **all** users of Open Babel.

What's New from 2.0.0
---------------------

-   Support for dynamic building on the Cygwin environment. This fixes a long-standing problem that prevented Cygwin users from using Open Babel.
-   Fixed a variety of memory leaks and improved overall memory use. More work to reduce memory consumption is underway for the 2.1 release.
-   Improved [Perl](/Perl "wikilink") and [Python](/Python "wikilink") scripting language bindings, including many bug-fixes.
-   Fixes to the “make check” test suite, which should prevent problems running before babel is installed.
-   Fixes compilation problems with AIX, Fedora Core, and the newly-released GCC-4.1.
-   Fixed support for versions of Solaris before Solaris 10, thanks to Mikael Johansson.
-   Fixed several reported compilation problems with Windows builds using VisualC++.
-   Fixed several reported crashes, including those using the scripting wrappers.
-   Fixed problems with the [Turbomole](/TurboMole_Coordinate "wikilink") format, thanks to Mikael Johansson.
-   Fixed a bug with [PDB](/PDB "wikilink") files with coordinates &lt; -1000 Ang.
-   Improved support for the [Sybyl mol2](/Sybyl_mol2 "wikilink") format, thanks to Kevin Parkes.
-   Fixed a variety of typos in the [API documentation](http://openbabel.sourceforge.net/api/).
-   Countless bug fixes.

NOTE
----

` A compiler optimization bug on Fedora Core 4 is known to cause crashes with Open Babel 2.0.1.`
` You can either upgrade to Fedora Core 5 or later, or compile Open Babel with `
` `“`make`` ``CXXFLAGS=-O0`”` to turn off all compiler optimization.`

[Category:Releases](/Category:Releases "wikilink")
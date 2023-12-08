---
title: Open Babel 2.0.2
---

Open Babel 2.0.2 was released on 2006-07-24.

Release Notice
--------------

The Open Babel project is extremely proud to announce the release of Open Babel 2.0.2, the latest stable version of the free chemistry file translation program and chemistry software library.

This release represents a bug-fix release and should be a stable upgrade, recommended for **all** users of Open Babel.

What's New from 2.0.1
---------------------

-   Substantial fixes to the [SMILES](/SMILES "wikilink") and [SMARTS](/SMARTS "wikilink") parsing support, thanks to a variety of bug reports.
-   A variety of fixes to aromaticity perception and Kekule form assignment.
-   Fixed gzip support, broken in version 2.0.1 inadvertantly. Babel will now automatically read gzip-encoded files, e.g., `1ABC.pdb.gz`
-   Output a warning when a multi-molecule file is converted to a single-molecule format.
    -   For example, a multi-molecule [MDL SDfile](/MDL_SDfile "wikilink") translated to [Gaussian Input](/Gaussian_Input "wikilink") will display a warning unless translation uses batch mode.
-   Better support for command-line tools such as obgrep on Cygwin.
-   Fixed a variety of crashes.
-   Countless other bug fixes.

NOTE
----

` A compiler optimization bug on Fedora Core 4 is known to cause crashes with Open Babel 2.0.x.`
` You can either upgrade to Fedora Core 5 or later, or compile Open Babel with `
` `“`make`` ``CXXFLAGS=-O0`”` to turn off all compiler optimization.`

[Category:Releases](/Category:Releases "wikilink")

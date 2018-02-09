---
title: Developer:Building
permalink: /Developer:Building/
---

In all cases, if you have questions about the building/compiling process for Open Babel, please contact the developer list at <openbabel-devel@lists.sourceforge.net>

UNIX/Linux/Mac OS X
-------------------

The build environment on UNIX-like platforms, including Linux, and Mac OS X involves a variety of tools.

-   [autoconf](http://www.gnu.org/software/autoconf/) - Used to detect headers, libraries, and other packages to flexibly build on a range of platforms
-   [automake](http://www.gnu.org/software/automake/) - Used to create the “Makefile.in” and “Makefile” build rules
-   [libtool](http://www.gnu.org/software/libtool/) - Used to build shared libraries (i.e., libopenbabel) and the shared object modules for file translators

Because these are not always present on every system (often “devel” packages or other developer tools are needed), the build setup is designed to compile the existing source and **NOT** rebuild the build system itself (i.e., the configure script, babelconfig.h, and the Makefile scripts).

If you intend to add source code files, you should make sure to also edit the build files -- particularly the Makefile.am files used by `automake`. You will also need to re-run the configure script, e.g.

` ./configure --enable-maintainer-mode`

The `--enable-maintainer-mode` option adds the rules to rebuild Makefiles and other elements of the build environment when changed.

The `configure` script itself is generated from `configure.in` by autoconf. It rarely needs changes, except when needed to detect the presence of new libraries on a system. If you think you need to make changes to the configure script, please send an e-mail on the developer list and someone will be glad to point you in the right directions.

By default on UNIX-like platforms (including [Cygwin](http://www.cygwin.com/), Mac OS X, Linux, etc.) all code is built for shared libraries. There are, however, a few differences, particularly with [Cygwin](http://www.cygwin.com/).

### Build Outputs (Linux, Unix, Mac OS X)

-   src/math/libmath -- Temporary build library (linked into libopenbabel)
-   src/formats/inchi -- libinchi library for [InChI](/InChI "wikilink") output -- built if not found among the system libraries
-   src/formats/ -- Individual shared, loadable file format modules/plugins for each [file format](/:Category:Formats "wikilink")
-   src/libopenbabel -- Main shared library, including OBConversion, OBError, OBMol, etc.
-   src/[babel](/babel "wikilink") -- Main command-line binary
-   tools/ -- A variety of other command-line binaries including [obgrep](/obgrep "wikilink"), [obchiral](/obchiral "wikilink"), [obprop](/obprop "wikilink"), etc.
-   test/roundtrip -- A testing tool for comparing the chemical equivalence of two files produced during conversion from [babel](/babel "wikilink")
-   test/ -- A set of [unit tests](/Developer:Testing "wikilink")

### Build Outputs (Cygwin)

On Cygwin, the current build environment has difficulty producing individual file translation shared objects. Therefore, the configure script and Makefiles build “libformats” which is a temporary build library, linked into libopenbabel itself. All shared libraries (i.e., libopenbabel) produce [DLLs](http://en.wikipedia.org/wiki/Dynamic-link_library).

-   src/math/libmath -- Temporary build library (linked into libopenbabel)
-   src/formats/inchi -- libinchi library for [InChI](/InChI "wikilink") output -- built if not found among the system libraries
-   src/formats/libformat -- Temporary build library including every [file format](/:Category:Formats "wikilink") (linked into libopenbabel)
-   src/libopenbabel.dll -- Main shared library, including OBConversion, OBError, OBMol, etc.
-   src/[babel](/babel "wikilink") -- Main command-line binary
-   tools/ -- A variety of other command-line binaries including [obgrep](/obgrep "wikilink"), [obchiral](/obchiral "wikilink"), [obprop](/obprop "wikilink"), etc.
-   test/roundtrip -- A testing tool for comparing the chemical equivalence of two files produced during conversion from [babel](/babel "wikilink")
-   test/ -- A set of [unit tests](/Developer:Testing "wikilink")

Windows (Visual C++)
--------------------

The SVN and source distributions should include Visual C++ project files. These are used to compile the [Windows GUI](/Windows_GUI "wikilink").

Perl and Python Bindings
------------------------

The [Perl](/Perl "wikilink") and [Python](/Python "wikilink") language bindings for the Open Babel library are generated using a tool called SWIG:

-   [swig](http://www.swig.org/) - Simplified Wrapper and Interface Generator

These files are auto-generated from the SWIG file “openbabel.i” by the UNIX Makefiles, assuming SWIG is detected by the configure script and `--enable-maintainer-mode` is used.

### Perl

The Perl bindings are not built by default on either UNIX or Windows systems. It currently uses the [ExtUtils::MakeMaker](http://perldoc.perl.org/ExtUtils/MakeMaker.html) build system.

It currently assumes a UNIX-like build environment and searches through common paths for libopenbabel and header files.

    perl Makefile.PL
    make
    make test
    make install

### Python

The Python bindings are not build by default on any system either. They currently use the [Python distutils](http://docs.python.org/inst/inst.html) build system.

It currently assumes a UNIX-like build environment and searches through common paths for libopenbabel and header files. It also looks for the environment variable OPENBABEL_INSTALL as the base path for the installation of Open Babel (e.g., /usr/local, /opt, /usr, /home/foobar, etc.)

    python setup.py build
    python setup.py install

[Category:Developer](/Category:Developer "wikilink")
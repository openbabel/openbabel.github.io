---
title: Install Open Babel 2.2
permalink: /Install_Open_Babel_2.2/
---

Introduction and requirements
-----------------------------

Here we describe the compilation and installation procedure for OpenBabel 2.2.3. For a different release, the version number will be different and you should take this in account when reading the instructions below.

The following are required to compile Open Babel:



The latest version of the [Open Babel source code](http://sourceforge.net/project/showfiles.php?group_id=40728&package_id=32894)

A C++ compiler (like g++)

A makefile system (like GNU make)

The following are optional when compiling Open Babel, but if not installed, fewer features will be available:



libxml2 development headers are required to read/write CML files (the libxml2-dev package in Ubuntu)

zlib.h is required to support reading gzipped files (the zlib1g-dev package in Ubuntu)

If using GCC 3.x to compile (and not GCC 4.x), then the Boost headers are required for certain formats (CML, Chemkin, Chemdraw CDX, MDL RXN and RSMI)

If you are interested in using OpenBabel from a scripting language, then the following notes apply:



Python is required to compile the Python bindings

Perl is required to compile the Perl bindings

If you are compiling directly from the Subversion repository, then you need to create the Python/Perl bindings yourself. To do so you need to install the latest version of SWIG (at the time of writing, 1.3.40, but there may be a new version).

If you want to install globally on your system, you will need root access, and should follow [these instructions](/Install_(source_code)#Installing_globally_with_root_access "wikilink"). If you don't have root access or if you simply wish to install in your 'home' area, see [Installing locally without root access](/Install_(source_code)#Installing_locally_without_root_access "wikilink").

Installing globally with root access
------------------------------------

(A1) Open a command window, and decompress the downloaded file with following command:

    tar zxvf openbabel-2.0.2.tar.gz

This will create a folder called 'openbabel-2.0.2'.

(A2) You now need to configure and compile openbabel. To do this, change directory into 'openbabel-2.0.2'. Run the following commands, one after the other

    ./configure 2>&1 | tee configure.out
    make 2>&1 | tee make.out

If you get an error message about “__builtin_popcount undeclared”, replace src/fingerprint.cpp by [this file](http://openbabel.svn.sourceforge.net/viewvc/openbabel/openbabel/branches/openbabel-2-2-x/src/fingerprint.cpp?revision=2707&pathrev=2707) and include/openbabel/fingerprint.h by [this file](http://openbabel.svn.sourceforge.net/viewvc/openbabel/openbabel/branches/openbabel-2-2-x/include/openbabel/fingerprint.h?revision=2707&pathrev=2707), and run 'make' again.

If there are any other errors at this point, send an email to the [openbabel-discuss](mailto:openbabel-discuss@lists.sourceforge.net) mailing list and attach the files 'configure.out' and 'make.out'.

If you look at the output of 'configure' you can see whether CML and gzip support will be included in openbabel (see Optional Libraries above).

    ...
    checking for libxml - version >= 2.6.5...yes (version 2.6.21)
    ...
    checking for zlib.h... yes

(A3) If you have root permissions, you can install openbabel globally. As root, run the following command:

    make install

Note: This will take about 5 minutes, and will display a large amount of output on the screen.

(A4) If necessary (e.g. babel doesn't work), add the location of the installed libopenbabel.so to the LD_LIBRARY_PATH, in my case:

    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib

Installing locally without root access
--------------------------------------

If you don't have root access, you can still compile and use Open Babel.

(B1) Follow Step A1 above

(B2) Make a local directory to install everything into. In this example, I will use the folder “tree” in my home directory:

    mkdir /home/noel/tree

(B3) Instead of Step A2 above, use the 'prefix' option of configure as follows:

    ./configure --prefix=/home/noel/tree 2>&1 | tee configure.out
    make 2>&1 | tee make.out

(B4) You can now install without root permissions using the following command:

    make install

Note: This will take about 5 minutes, and will display a large amount of output on the screen.

This installs the babel executable (and related tools) to /home/noel/tree/bin so you need to add this directory to your PATH in your startup scripts (that is, .bashrc, or whatever):

    export PATH=$PATH:/home/noel/tree/bin

(B5) Add the location of the installed libopenbabel.so to the LD_LIBRARY_PATH, in my case:

    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/noel/tree/lib

Compile bindings for Java, .NET, Perl, Python or Ruby
-----------------------------------------------------

To compile and install the bindings for the various languages supported, please see the appropriate page for [Java](/Java "wikilink"), [.NET](/OBDotNet "wikilink"), [Perl](/Perl "wikilink"), [Python](/Python "wikilink"), [Ruby](/Ruby "wikilink").

Compile the development code
----------------------------

For information on compiling our development code, please see the [CMake](/CMake "wikilink") page.

[Category:Installation](/Category:Installation "wikilink")
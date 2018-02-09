---
title: Install (source code)
permalink: /Install_(source_code)/
---

Introduction and requirements
-----------------------------

Here we describe the compilation and installation procedure for OpenBabel 2.3.0 or newer. For information on installing Open Babel 2.2 series, see [Install Open Babel 2.2](/Install_Open_Babel_2.2 "wikilink").

The following are **required** to compile Open Babel:



The latest version of the [Open Babel source code](http://sourceforge.net/project/showfiles.php?group_id=40728&package_id=32894)

A **C++ compiler** (like GNU g++ or Intel Compiler icc)

A makefile system (like GNU make)

**CMake 2.4** or newer (available as the *cmake* package in Ubuntu, or from the [CMake website](http://cmake.org/cmake/resources/software.html))

The following are **optional** when compiling Open Babel, but if not installed, fewer features will be available:



**libxml2** development headers are required to read/write CML files (the *libxml2-dev* package in Ubuntu)

**zlib.h** is required to support reading gzipped files (the *zlib1g-dev* package in Ubuntu)

If using GCC 3.x to compile (and not GCC 4.x), then the Boost headers are required for certain formats (CML, Chemkin, Chemdraw CDX, MDL RXN and RSMI)

**Eigen** version 2 is required for some API classes (OBAlign, OBConformerSearch) and plugins (the QEq and QTPIE charge models, the conformer operation). These will not be available otherwise.


Eigen may be available through your package manager (the *libeigen2-dev* package in Ubuntu). Alternatively, Eigen is available from <http://eigen.tuxfamily.org>. It doesn’t need to be compiled or installed. Just unzip it and specify its location when configuring cmake (see below) using *-DEIGEN2_INCLUDE_DIR=whereever*.

If you want to build the **GUI** (Graphical User Interface), you need the following:



**wxWidgets** 2.8 (or newer)



Binary packages may be available through your package manager (*wx-common* and *wx2.8-headers* on Ubuntu) or from <http://www.wxwidgets.org/downloads/>. Otherwise, you could try compiling it yourself from the source code.

If you want to use Open Babel using one of the supported **language bindings**, then the following notes may apply:



You need the the Python development libraries to compile the Python bindings (package *python-dev* in Ubuntu)

You need the the Perl development libraries to compile the Perl bindings (package *libperl-dev* in Ubuntu)

*Developer note*: If you are compiling directly from the Subversion repository, then you need to create the Python/Perl bindings yourself. To do so you need to install the latest version of SWIG (at the time of writing, 2.0.1, but there may be a new version).

If you want to install globally on your system, you will need root access, and should follow [these instructions](/Install_(source_code)#Installing_globally_with_root_access "wikilink"). If you don't have root access or if you simply wish to install in your 'home' area, see [Installing locally without root access](/Install_(source_code)#Installing_locally_without_root_access "wikilink").

Installing globally with root access
------------------------------------

(A1) Open a command window, and decompress the downloaded file with the following command:

    tar zxvf openbabel-2.3.0.tar.gz

This will create a folder called *openbabel-2.3.0* containing the Open Babel source code.

The recommended way of building Open Babel is to use separate source and build folders. Let's call them *ob-src* and *ob-build*:

    mv openbabel-2.3.0 ob-src
    mkdir ob-build

(A2) You now need to configure and compile openbabel. To do this, change directory into *ob-src*. Run the following commands, one after the other:

    cd ob-build
    cmake ../ob-src 2>&1 | tee cmake.out
    make 2>&1 | tee make.out

If there are any errors at this point, send an email to the [openbabel-discuss](mailto:openbabel-discuss@lists.sourceforge.net) mailing list and attach the files *cmake.out* and *make.out*.

If you look at the output of CMake you can see whether CML and gzip support will be included in Open Babel (see the optional dependencies above).

    #FIXME - INSERT EXAMPLE HERE

(A3) If you have root permissions, you can install Open Babel globally. As root, run the following command:

    make install

(A4) If necessary (e.g. *obabel* doesn't work), add the location of the installed *libopenbabel.so* to the *LD_LIBRARY_PATH*, in my case:

    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib

Installing locally without root access
--------------------------------------

If you don't have root access, you can still compile and use Open Babel.

(B1) Follow Step A1 above

(B2) Make a local directory to install everything into. In this example, I will use the folder *tree* in my home directory:

    mkdir /home/noel/tree

(B3) Instead of Step A2 above, specify the install directory using the CMake option *CMAKE_INSTALL_PREFIX*:

    cmake ../ob-src -DCMAKE_INSTALL_PREFIX=/home/noel/tree 2>&1 | tee cmake.out
    make 2>&1 | tee make.out

(B4) You can now install without root permissions using the following command:

    make install

This installs the *obabel* executable (and related tools) to */home/noel/tree/bin* so you need to add this directory to your *PATH* in your startup scripts (that is, *.bashrc*, or whatever):

    export PATH=$PATH:/home/noel/tree/bin

(B5) Add the location of the installed *libopenbabel.so* to the *LD_LIBRARY_PATH*, in my case:

    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/noel/tree/lib

Compile bindings for Java, .NET, Perl, Python or Ruby
-----------------------------------------------------

To compile and install the bindings for the various languages supported, please see the appropriate page for [Java](/Java "wikilink"), [.NET](/OBDotNet "wikilink"), [Perl](/Perl "wikilink"), [Python](/Python "wikilink"), [Ruby](/Ruby "wikilink").

Compile the development code
----------------------------

For information on compiling our development code, please see the [CMake](/CMake "wikilink") page.

[Category:Installation](/Category:Installation "wikilink")
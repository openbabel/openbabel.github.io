---
title: CMake
permalink: /CMake/
---

Open Babel trunk (destined to become openbabel-2.3) will use CMake as its primary build system. Cmake is available in many Linux distributions or from [www.cmake.org](http://www.cmake.org/cmake/resources/software.html).

Building OpenBabel
==================

CMake version 2.6.3 or newer is required to build OpenBabel.

The preferred method of building Open Babel with CMake is to use “out of source” builds. This means that no generated files are placed in the source directory. This ensures good separation between source and build files. You can use whatever directory structure you prefer, one possible directory layout is:

    ~/src/openbabel
    ~/build/openbabel

So, if you want to build the source code directly from our subversion repository, you would first check out the code as follows:

    mkdir ~/src
    cd ~/src
    svn co https://openbabel.svn.sourceforge.net/svnroot/openbabel/openbabel/trunk openbabel

And to compile the code:

    mkdir ~/build
    mkdir ~/build/openbabel
    cd ~/build/openbabel
    cmake -DCMAKE_INSTALL_PREFIX=/usr/local/openbabel ~/src/openbabel
    make
    sudo make install

This would configure OpenBabel in the build directory, make all files and install them to the specified prefix. The CMakeCache.txt file contains most stored settings, erasing that will allow you to configure again.

To run the tests, first set BABEL_DATADIR=~/src/openbabel/data and BABEL_LIBDIR=~/build/openbabel/lib. Then run “make test”.

### Building the Python bindings

To build the Python bindings you need to specify “-DPYTHON_BINDINGS=ON”. If you are compiling from the subversion repository, you will also need to specify “-DRUN_SWIG=ON” to generate the bindings (note: this requires SWIG 1.3.40, which should either be on the PATH or specified with “-DSWIG_EXECUTABLE=/my/path”).

The installation directory will be the global site-packages if neither PYTHON_PREFIX nor CMAKE_INSTALL_PREFIX is specified (i.e. “-DPYTHON_PREFIX=/my/path”). If PYTHON_PREFIX is specified, then this will be used to install the bindings. Finally, if CMAKE_INSTALL_PREFIX is specified but PYTHON_PREFIX is not, then PYTHON_PREFIX is set to CMAKE_INSTALL_PREFIX.

Notes for developers
====================

### Make Individual Targets

CMake has good dependency tracking, but it uses timestamps (as most build systems do) to indicate a file has changed. As such anytime that the openbabel library is rebuilt all of the plugins/executables that link to it are relinked. This can lead to excessive amounts of time spent waiting for everything to relink, when the ABI has in fact not changed. By making individual parts of the project these relinks can be avoided.

    make openbabel       # Rebuild the openbabel libary
    make help            # List available build targets

The dependency tracking can also take time when building plugins. CMake adds an additional target that has no dependency tracking, and can be used if working on the CML format for example,

    make cmlformat/fast

This can be used for all targets by appending '/fast' to the target name.

### Target Naming Conventions

Formats are named after their source files, e.g. cmlformat.\[h|cpp\] -&gt; cmlformat. The openbabel library target is named openbabel (currently openbabel-2 on Windows). The executable targets are named after the corresponding executable, e.g. babel. Any of these target names can be used as shown above to rebuild specific parts, this can save a lot of time when working on one specific aspect of Open Babel.

### Useful Cmake Options

-   To see the actual commands used to compile the code (on Linux), run 'make VERBOSE=1'
-   You can build in debug mode with “-DCMAKE_BUILD_TYPE=Debug”.
-   On occasion, developers may find it useful to use the option -DMINIMAL_BUILD=ON. This option just compiles the Smiles and SDF formats, and of the tools just babel.

### OpenBabel GUI

The OpenBabel GUI is built by default if the wxWidgets development libraries are available (on Ubuntu 9.04, libwxgtk2.8-dev; Fedora, wxGTK-devel). On Windows, the WXWIN environment variable should be defined.

The GUI build can be explicitly disabled using -DBUILD_GUI=OFF.

### Building on Windows

There is a batch file, default_build.bat, in the windows-vc2008 folder that runs cmake. Other .bat files called default_build with additional options, e.g. to enable the tests.

Static builds
=============

A static OpenBabel library can be build by setting BUILD_SHARED to OFF when running cmake.

`cd openbabel-2.x`
`mkdir build`
`cd build`
`cmake -DBUILD_SHARED=OFF ..`
`make`

The static libopenbabel.a is now in the build/src directory. This static library archive contains all plugins

Plugins
-------

The static libopenbabel.a archive contains all plugins but these are not automatically included in an executable linked against libopenbabel.a. The plugin classes are never referenced directly and the linker removes all unreferenced symbols from the final executable. A simple approach that works for all compilers is to add the plugin source files to the executable sources. However, almost all compilers allow for symbols to be undefined at link time which is equivalent to using the symbol from inside the executable source. These symbols are the [mangled names](http://en.wikipedia.org/wiki/Name_mangling) for the plugin classes. An example is provided to make it easy to do this when developing executables that link to openbabel statically.

Creating custom static binaries
-------------------------------

In the **openbabel-2.3.0/doc/examples/static_executable/** directory there is an example CMakeLists.txt file to build custom static binraries. There are only two files:

`doc/examples/static_executable/myexe.cpp`
`doc/examples/static_executable/CMakeLists/txt`

In most cases, only 3 lines in the **CMakeLists.txt** file have to be changed:

`#`
`# This script can be used to create static executables linking to the static`
`# OpenBabel2 library.`
`#`
`# This script requires OpenBabel to be build and installed. For example:`
`#`
`#  cd openbabel-2.3`
`#  mkdir build`
`#  cd build`
`#  cmake -DBUILD_SHARED=OFF -DCMAKE_INSTALL_PREFIX=/home/me/some/path ..`
`#  make`
`#  make install`
`#`
`# To compile your static executable:`
`#`
`#  cd myproject`
`#  mkdir build`
`#  cd build`
`#  cmake -DOpenBabel2_DIR=/home/me/some/path/lib/openbabel ..`
`#  make`
`#`
`# All plugins are inside the static libopenbabel.a but the symbols for the`
`# plugin classes have to be undefined. Plugins can be disabled by removing`
`# the class names from the format_classes, descriptor_classes, ... lists below.`
`#`
`# Compilers:`
`# - GNU GCC: tested on linux`
`# - Intel ICC: not tested, should be the same as gcc`
`# - MSVC: not tested, uses different name mangling`
`# - MinGW: not tested, should be the same as gcc`
`#`
`# This line is required for cmake backwards compatibility.`
`cmake_minimum_required(VERSION 2.6)`
`# Name of your project`
`project(`**`myproject`**`)`
`# Create a list of source files (easier to maintain)`
`set(sources `**`myexe.cpp`**`)`
`# Set the name for the executable`
`set(executable_target `**`myexe`**`)`
`#`
`# The plugin class names to include in the executable.`
`#`
`set(format_classes`
`    ACRFormat`
`    ADFOutputFormat`
`    ADFInputFormat`
`    OBT41Format`
`    AlchemyFormat`
`    ...`
`################################################################################`
`... CMake code to build the executable ...`

Formats or other plugins can be excluded by removing the classes from the lists in the CMakeLists.txt file.

Creating linux relocatable binaries
-----------------------------------

### Introduction

**UNDER CONSTRUCTION** The aim of the following sections is to build linux binaries that can be distributed and will (hopefully) work on a wide variety of linux systems (including older versions). A full static build

The BUILD_SHARED=OFF option alone is not enough to produce linux binaries that can be run on a variety of linux distributions. The reason for this is that there might be code in the executable build with the -static compiler flag that is not compatible with the linux kernel on another linux machine. The list of shared libraries might look like:

`$ ldd bin/babel`
`       `**`linux-gate.so`**`.1 =>  (0xf774c000)`
`       libc.so.6 => /lib32/libc.so.6 (0xf75e3000)`
`       libopenbabel.so.4 => not found`
`       libdl.so.2 => /lib32/libdl.so.2 (0xf75de000)`
`       libz.so.1 => /usr/lib32/libz.so.1 (0xf75c8000)`
`       libstdc++.so.5 => not found`
`       libm.so.6 => /lib32/libm.so.6 (0xf75a2000)`
`       libgcc_s.so.1 => /usr/lib32/libgcc_s.so.1 (0xf7583000)`
`       `**`/lib/ld-linux.so`**`.2 (0xf774d000)`

-   The first and last shared library have are kernel specific and the minumum version can be seen by using the file command.

`$ file `**`...chroot...`**`/bin/babel`
`bin/babel: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux `**`2.2.0`**`, not stripped`

In this case the minimum kernel version is 2.2.0. However, when compiling on a recent linux distribution, the minimum required version will be newer. This would mean that the static executable might not work on older systems. For example:

`$ uname -a`
`Linux timvdm-desktop 2.6.31-16-generic #53-Ubuntu SMP Tue Dec 8 04:02:15 UTC 2009 x86_64 GNU/Linux`
`$ file bin/babel`
`bin/babel: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux `**`2.6.15`**`, not stripped`

Users downloading the binary using linux 2.6.10 might not be able to run the executable. Backwards compatibility is good though so a 2.2.0 or 2.4.0 minimum version will work on 2.6.x. To compile for an older kernel version can be done by using an older linux distribution.

-   libc.so:
-   libopenbabel.so: Will be replaced with symbols taken static libopenbabel.a
-   libdl.so: Only needed when using shared libraries (to load plugins)
-   libz.so: gzip compression, will be replaced with static libz.a
-   libm.so: math library, will be replaced with static libm.a
-   libgcc_s.so, libstdc++.so: GCC runtime libraries, see -static-libgcc below

To ensure the executable will run on most linux distributions, a **mixed** static/dymamic build can be done. The kernel dependent libraries and some system libraries will be linked shared and the openbabel, z, m and xml2 libraries will be linked statically (including all plugins). Although any linux distribution with an acceptable minimum kernel can be used, a chroot environment is often easier. Debian/Ubuntu provide utilities to make this process easy and will be used here. Sarge is the release name for debian 3.1 which results in a 2.2.0 minimum kernel version. For newer minimum versions, try etch or lenny.

`$ sudo apt-get install dchroot debootstrap`
`$ sudo mkdir sarge-chroot/`
`$ sudo debootstrap --arch i386 sarge sarge-chroot/ `[`http://archive.debian.org/debian`](http://archive.debian.org/debian)
`...performs installation in sarge-chroot...`
`$ sudo cp -r openbabel-2.2.1/ sarge-chroot/root/`

The boost libraries that can be installed for debian sarge are to old to compile OpenBabel. Only headers are used and the easiest way to solve this issue is to copy the headers to the chroot.

`$ sudo cp -R /usr/include/boost sarge-chroot/usr/include`
`$ sudo chroot sarge-chroot/`

CMake is not available for debian sarge but binaries can be downloaded:

`# cd root`
`# wget `[`http://www.cmake.org/files/v2.8/cmake-2.8.2-Linux-i386.sh`](http://www.cmake.org/files/v2.8/cmake-2.8.2-Linux-i386.sh)
`# chmod 755 cmake-2.8.2-Linux-i386.sh`
`# cd /usr/local`
`# /root/cmake-2.8.2-Linux-i386.sh`
`...`
`Do you accept the license? [yN]: `
`y`
`By default the CMake will be installed in:`
`  `“`/usr/local/cmake-2.8.2-Linux-i386`”
`Do you want to include the subdirectory cmake-2.8.2-Linux-i386?`
`Saying no will install in: `“`/usr/local`”` [Yn]: `
`n`
`Using target directory: /usr/local`
`Extracting, please wait...`
`Unpacking finished successfully`

A few packages need to be installed to be able to compile C++ code.

`# apt-get install g++ libz-dev libxml2-dev make`

OpenBabel can now be compiled inside the chroot environment:

`# cd /root/openbabel-2.3.0`
`# mkdir build`
`# cd build`
`# cmake -DBUILD_SHARED=OFF -DBUILD_MIXED=ON ..`
`# make`

Details
-------

### GNU GCC and Intel ICC

Both gcc and icc use the same name mangling scheme and compiler option **-u**. All symbols have the same structure

`_ZTVN9OpenBabel${length}${plugin_class}E`

where ${length} is the length of the ${plugin_class} string. For example, the SMIFormat class in the OpenBabel namespace becomes:

`_ZTVN9OpenBabel9SMIFormatE`

These symbols are used together with the **-u** compiler option:

`c++ myexe.cpp -o myexe -static -u  _ZTVN9OpenBabel9SMIFormatE  -u _ZTVN9OpenBabel9PDBFormatE -u ... /usr/local/lib/libopenbabel.a -Wl,-Bstatic -lxml2 -lm -lz`

### Microsoft Visual C++

The name mangling for MSVC produces symbols like:

`???OpenBabel???SMIFormat??? `**`(FIXME)`**

These symbols are used together with the **/U** compiler option:

`cl.exe myexe.cpp /MT /U ??? /U ???? /U ... `

### LibXML linker warnings on linux

The XML formats are build and inluded in the libopenbabel.a archive but including them in an executable requires a static libxml2. However, on linux at least, libxml2 uses functions from glibc that require other shared libraries (e.g. /lib64/ld-linux-x86-64.so.2). As a result, it is not possible to do a full static (-static) build linked against this version of glibc. A static libxml2 could be build and linked against a custom build libc. It's only a waning though and depending on the use case it might work fine.

`` /usr/lib/gcc/x86_64-linux-gnu/4.4.1/../../../../lib/libxml2.a(nanohttp.o): In function `xmlNanoHTTPConnectHost': ``
`(.text+0xe50): warning: Using 'getaddrinfo' in statically linked applications requires at runtime the shared libraries from the glibc version used for linking`
`` /usr/lib/gcc/x86_64-linux-gnu/4.4.1/../../../../lib/libxml2.a(nanohttp.o): In function `xmlNanoHTTPConnectHost': ``
`(.text+0xf64): warning: Using 'gethostbyname' in statically linked applications requires at runtime the shared libraries from the glibc version used for linking`
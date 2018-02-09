---
title: Install (MinGW)
permalink: /Install_(MinGW)/
---

This document contains instructions for building OpenBabel (OB) on Windows with [MinGW](http://www.mingw.org/). The resulting DLL (libopenbabel-3.dll) may be linked directly from Windows applications compiled with MinGW, so there is no need to deal with (import) libraries created with Microsoft Visual C++. This is especially useful if your existing software uses a GNU make based build system. Binaries created with MinGW are native and do not need an emulation layer, such as [Cygwin](http://www.cygwin.com/).

Date: October, 1010, Tested with OB 2.2.99 on Windows XP.

Current and Development versions
================================

Building OpenBabel 2.3.0 using CMake
------------------------------------

Install CMake 2.6 or newer. Install MSYS/MinGW using the installer and make sure to install the c++ compiler and developement tools. Download and install the **msys zlib-dev** and **libxml2-dev (optional)** packages when using the “MSYS Makefiles” or the **mingw32 zlib-dev** package for “MinGW Makefiles”.

### Shared Library Build

In the MSYS command prompt:

`cmake -G `“`MSYS`` ``Makefiles`”` -DCMAKE_INSTALL_PREFIX=/where/to/install -DZLIB_INCLUDE_DIR=/include -DZLIB_LIBRARY=/lib/`**`libz.dll.a`**` -DLIBXML2_INCLUDE_DIR=/include -DLIBXML2_LIBRARIES=/lib/`**`libxml2.dll.a`**` ..`
`make`
`make install`

### “Static” Library Build

Executables created using this method **depend** on kernel32.dll and the native **MSVCRT.dll**. The kernel32.dll dependency is not an issue since this is available on all windows machines. The C runtime (MSVCRT.dll) would have to be included with your executable though. AFAIK, it is not possible to use the static version of the runtime library. However, the formats and other plugins will be inside the executable.

In the MSYS command prompt:

`cmake -G `“**`MSYS`**` ``Makefiles`”` `**`-DBUILD_SHARED=OFF`**` -DCMAKE_INSTALL_PREFIX=/where/to/install -DZLIB_INCLUDE_DIR=/include -DZLIB_LIBRARY=/lib/`**`libz.a`**` -DLIBXML2_INCLUDE_DIR=/include -DLIBXML2_LIBRARIES=/lib/`**`libxml2.a`**` ..`
`make`
`make install`

Building OpenBabel 2.2.2 using CMake
------------------------------------

### Installing MinGW

Install MinGW with gcc 4. I used the manual install since the automated installer only allowed me to install gcc 3.4. Regardless of the install method, make sure to have at least these packages installed (i.e. extracted) to *C:/MinGW*

-   MinGW Runtime (mingwrt-3.15.2-mingw32-dev.tar.gz)
-   Windows 32 API (w32api-3.13-mingw32-dev-tar.gz)
-   GNU Binutils (binutils-2.19.1-mingw32-bin.tar.gz)
-   GCC 4 (gcc-core-4.4.0-mingw32-bin.tar.gz, gcc-core-4.4.0-mingw-dll.tar.gz, gcc-g++-4.4.0-mingw32-bin.tar.gz,

gcc-g++-4.4.0-mingw32-dll.tar.gz, gmp-4.2.4-mingw32-dll.tar.gzi, mpfr-2.4.1-mingw32-dll.tar.gz)

Install MSYS using the installer (MSYS-1.0.10.exe). Start the msys prompt using **Start &gt; Programs &gt; MinGW &gt; MSYS &gt; msys** and verify the g++ version.

`$ g++ -v`
`...`
`gcc version 4.4.0 (GCC)`

It is also possible to use the automated installer and only add the g++ 4.4 packages later. See the [<http://www.mingw.org/> MinGW Website](/http://www.mingw.org/_MinGW_Website "wikilink") for more information.

Some tips:

-   work in your MinGW **home directory**. I tried to build from a /z/... drive and didn't have much success this way.
-   Using MinGW, make sure to **link directly to the dll files**

### Shared Library Build

Install CMake 2.6, an installer for the latest version is available on the [<http://www.cmake.org/> CMake Website](/http://www.cmake.org/_CMake_Website "wikilink") (note: this is the normal windows CMake installer, you can use it from the MSYS prompt. For cygwin, the cygwin cmake package is needed.)

`$ export PATH=$PATH:/c/Program\ Files/CMake\ 2.6/bin`
`$ cd ~/openbabel-2-2-x`
`$ mkdir build`
`$ cd build`
`$ cmake -G `“`MSYS`` ``Makefiles`”` -DCMAKE_INSTALL_PREFIX=install_dir -DZLIB_INCLUDE_DIR=../include -DZLIB_LIBRARY=../windows-vc2005/`**`zlib1.dll`**`  -DLIBXML2_INCLUDE_DIR=../include -DLIBXML2_LIBRARIES=../windows-vc2005/`**`libxml2.dll`**` ..`
`$ make `
`$ make install`

All files should now be installed to **~/openbabel-2-2-x/build/install_dir**. However, you still need to copy **zlib1.dll, iconv.dll & libxml2.dll to .../install_dir/bin**.

`$ cp ../windows-vc2005/zlib1.dll install_dir/bin`
`$ cp ../windows-vc2005/libxml2.dll install_dir/bin`
`$ cp ../windows-vc2005/iconv.dll install_dir/bin`
`$ export PATH=$PATH:install_dir/bin`
`$ babel -H`
`...`

Old releases
============

Date: March 31, 2009, Tested with OB 2.1.1 and 2.2.1 on Windows Vista.

Preliminaries:
--------------

OB requires libxml2; libxml can be found \[<http://xmlsoft.org/>, here\]. Specifically, this requires you to edit the xml2-config script. I recommend you directly link a test application against libxml2.dll and insert the respective -I and -L flags into xml2-config. The relevant section of mine looks like this:

        --cflags)
            echo -I/home/libxml2-2.7.3.win32/include/libxml -I/home/libxml2-2.7.3.win32/include

and

        --libs)
            echo /c/Windows/System32/libxml2.dll -liconv -lm -Wl,-s -lwsock32 -liberty

OB requires zlib; zlib can be found [here](http://gnuwin32.sourceforge.net/packages/zlib.htm). Make sure OB can find the header files and DLL during configuration by prior adding the respective directories to your $PATH environment variable.

[Install](http://www.mingw.org/wiki/Getting_Started) current Msys and MinGW version. Unpack OB source, start Msys and change to OB directory. **Warning:** I experienced “object name conflicts” during compilation when the $PATH contained the windows\\system32 directory at the beginning.

Build OB 2.2.1:
---------------

[Update](http://sourceforge.net/project/showfiles.php?group_id=2435&package_id=241304) the g++ compiler to version 4 (g++-sjlj, see also the [release notes](http://downloads.sourceforge.net/mingw/gcc-4.2.1-sjlj-2-release_notes.txt?use_mirror=freefr)). Unpack gcc-g++-4.2.1-sjlj-2.tar.gz and gcc-core-4.2.1-sjlj-2.tar.gz in your MinGW root directory

    ./configure CXX=g++-sjlj

You may want to leave out boost and/or loading of dynamic modules by adding this to the configure command: `--without-boost --disable-dynamic-modules`.

    make

Compilation of libopenbabel-3.dll breaks due to missing zlib support. You may manually fix this by repeating the last failed command and adding the file path to `zlib.dll`.

--[Amaunz](/User:Amaunz "wikilink") 07:18, 31 March 2009 (PDT)

Build OB 2.1.1:
---------------

    ./configure

You may want to leave out boost and/or loading of dynamic modules: `./configure --without-boost --disable-dynamic-modules`.

    cd src/formats/inchi
    make
    cd ../../../tools

Edit the Makefile and exchange the following lines

    babel_DEPENDENCIES = ../src/libopenbabel.la
    babel_LDADD = ../src/libopenbabel.la

with

    babel_DEPENDENCIES = ../src/libopenbabel.la $(formats_objects)
    babel_LDADD = ../src/libopenbabel.la $(formats_objects)

Repeat the editing for the rest of the executables if you need more than babel.exe. Then continue to build and install OB. The tools as well as the DLL will be placed in /local/bin (C:\\Msys\\local\\bin).

    cd ..
    make
    make install

[Category:Installation](/Category:Installation "wikilink")
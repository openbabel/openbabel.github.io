---
title: Install (Cygwin)
permalink: /Install_(Cygwin)/
---

The [Cygwin](http://www.cygwin.com/) environment allows running UNIX tools (such as Open Babel) from a command-line, much like Linux.

There are some slight differences between running Open Babel on Cygwin and other environments.

-   Currently, dynamic loading of file format modules is not possible on Cygwin.
-   DLLs generated by Cygwin are not compatible with those distributed with conventional [Windows](/Windows "wikilink") installations.

If you encounter other problems, please [report a bug](http://sourceforge.net/tracker/?group_id=40728&atid=428740) and contact the [openbabel-devel mailing list](mailto:openbabel-devel@lists.sourceforge.net).

Cygwin installation has caused some users problems. See [here](http://sourceforge.net/tracker/index.php?func=detail&aid=1867368&group_id=40728&atid=428740) how igor_filippov overcame them.

### Step-by-step Installation Instructions for OpenBabel on Cygwin

Before installing, these instructions assume that you have installed GCC and G++ packages using Cygwin's setup tool.

These instructions describe the installation procedure for OpenBabel 2.2.0. For more different releases, the version number will be different and you should take this in account when reading the instructions below. In addition, these instructions assume that you have root access.

(1) [Download](http://sourceforge.net/project/showfiles.php?group_id=40728&package_id=32894&release_id=434410) the latest version (2.2.0, currently)

(2) Open a command window, change directory into 'openbabel', and decompress the downloaded file with following command:

    tar zxvf openbabel-2.2.0.tar.gz

This will create a folder called 'openbabel-2.2.0'.

(3) You now need to configure and compile openbabel. To do this, change directory into 'openbabel-2.2.0'. Run the following commands, one after the other

    ./configure | tee configure.out
    make | tee make.out

If there are any errors at this point, send an email to the [openbabel-discuss](mailto:openbabel-discuss@lists.sourceforge.net) mailing list and attach the files 'configure.out' and 'make.out'.

(4) If you have root permissions, you should install openbabel globally. As root, run the following command:

    make install

Build OB 2.2.2 (svn: branches/openbabel-2-2-x -- 7 July 2009)
=============================================================

Installing Cygwin
-----------------

Install Cygwin with gcc 4. Use the installer to select the packages you want to install. Make sure to have at least these packages installed from the **Devel category**:

-   binutils (&gt;=20080624-2)
-   boost-devel (&gt;=1.33.1-4)
-   cmake (&gt;=2.6.4-1)
-   gcc4, gcc4-core, gcc4-g++ (&gt;=4.3.2-2)
-   libiconv (&gt;=1.13-1)
-   libxml2-devel (&gt;=2.7.3-1)
-   make (&gt;=3.81-2)
-   zlib-devel (&gt;=1.2.3-3)

Any dependency problems will be resolved by the installer.

Start the msys prompt using **Start &gt; Programs &gt; Cygwin &gt; Cygwin Bash Shell** and verify the g++ version.

`$ g++ -v`
`...`
`gcc version 4.3.2 20080827 (beta) 2 (GCC)`

Tip: work in your cygwin **home directory**. I tried to build from a /cygwin/z/... drive and didn't have much success this way.

Building OpenBabel using CMake 2.6
----------------------------------

Install the Cygwin packages libxml2-devel, zlib-devel and cmake. Once this is done, the build process for cygwin is very straightforward:

`$ cd ~/openbabel-2-2-x`
`$ mkdir build`
`$ cd build`
`$ cmake .. -DLIBXML2_LIBRARIES=/usr/lib/libxml2.dll.a`
`$ make`
`$ make install`
`$ babel -H`
`...`

[Category:Installation](/Category:Installation "wikilink")[Category:Windows](/Category:Windows "wikilink")
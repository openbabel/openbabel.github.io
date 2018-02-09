---
title: Compile from source with MS Visual Studio
permalink: /Compile_from_source_with_MS_Visual_Studio/
---

Compiling OpenBabel versions 2.3.0 and later
--------------------------------------------

See [Install (MSVC)](/Install_(MSVC) "wikilink") for earlier versions.

### Build system and compiler

OpenBabel is built with the cross-platform CMake (version 2.4.8 and later) available from

-   <http://www.cmake.org/cmake/resources/software.html>.

The CMake setup currently produces project files for the freely available Visual C++ 2008 Express

-   <http://www.microsoft.com/express/Downloads/#2008-Visual-CPP>.

Since April 2010 \[<http://www.microsoft.com/express/Downloads/#2008-Visual-CPP>, Visual C++ 2010\] is available. It uses different project files but those from earlier versions are painlessly converted, and it would be the choice for a new Visual Studio installation.

Microsoft have made it much easier than it used to be to build 'native' C++ code for 32 bit Windows with their free compilers.

### OpenBabel source code

Although the source code package from the SourceForge download page has all the OpenBabel code, it may not have some of the ancillary files, since it is really intended for UNIX(Linux) systems. If you intend to compile under Windows it is much better to download the code from SVN. [Tortoise SVN](http://tortoisesvn.tigris.org/) is a very convenient client for SVN - it operates from Windows explorer - and is easy to install. Then make a directory for the OpenBabel file, right click and select SVN Checkout. For a released version of OpenBabel enter something like:

-   <https://openbabel.svn.sourceforge.net/svnroot/openbabel/openbabel/tags/openbabel-2-3-0>

or for the development code:

-   <https://openbabel.svn.sourceforge.net/svnroot/openbabel/openbabel/trunk>

Click OK and all the code and required external DLLs (e.g. for InChI and libxml2) are downloaded.

The GUI uses wxWidgets, and the CMake configuration will not build the GUI unless wxWidgets has been installed. See some notes on doing this (which has rather more pitfalls than the other build process on this page) are [here](/Install_(MSVC)#wxWidgets "wikilink").

### Build

Double click windows-vc2008\\default_build.bat. This will produce, among other things, a Visual Studio file windows-vc2008\\build\\openbabel.sln. Open this in Visual Studio, select the either the Debug or Release Builds and build the solution.

### Environment Variable

Make an environment variable BABEL_DATADIR to point to OpenBabel's /data folder. This needed for functions like logP, although the basic data, like atomic weights, are also compiled into the program and will be found even if this variable is not set.

### Debugging with Visual Studio

If you do a significant amount of debugging of OpenBabel code, you may wish to have the OpenBabel objects appear in the the Autos or Locals debugging windows in a more useful form. There is a lot that can be done but the simple suggestion here is a start.

Edit the file C:\\Program Files\\Microsoft Visual Studio 9\\Common7\\Packages\\Debugger\\autoexp.dat
In the \[AutoExpand\] section add the following text

    ; OpenBabel
    OpenBabel::OBMol =<_title> <_natoms> atoms, <_nbonds> bonds
    OpenBabel::OBAtom =index=<_idx> <_type> charge=<_fcharge>
    wxString=<m_pchData,st>

and restart Visual Studio.
In the debugger OBMol, OBAtom and wxString objects will be easier to identify.

### Building the Windows Installer

The Windows installer uses a script compiled by [NSIS](http://nsis.sourceforge.net/Main_Page). All the above projects, including the GUI and scripting, need to have been built. [Download](http://www.microsoft.com/downloads/details.aspx?familyid=200B2FD9-AE1A-4A14-984D-389C36F85647&displaylang=en) the Visual C++ Redistributable and put the file vcredist_x86.exe into windows-vc2005/Distribution. Right click the script file in that folder to compile it.
---
title: Install (MSVC)
permalink: /Install_(MSVC)/
---

Here we describe how to compile OpenBabel on Windows using the Microsoft Visual C++ compiler (MSVC).

Compiling the 2.2.x series
--------------------------

### Compiler

We recommend the following compiler which is available for free:

-   [Visual C++ 2005 (8.0) Express Edition](http://www.microsoft.com/express/2005/)

Microsoft would prefer you use the .NET framework, but they also support “native” code - it's just that they don't make it *too* easy.

You also need to install the Platform SDK to provide the Windows files. Follow the step 1 to 3 in the instructions in [1](http://msdn2.microsoft.com/en-us/library/ms235626(VS.80).aspx). At Step 3 when updating the corewin_express.vsprops file, the list of libraries should be “kernel32.lib user32.lib gdi32.lib winspool.lib comdlg32.lib advapi32.lib shell32.lib ole32.lib oleaut32.lib uuid.lib comctl32.lib rpcrt4.lib”. Also just before this add a section:

      <Tool
        Name="VCCLCompilerTool"
        PreprocessorDefinitions=
        "_CRT_SECURE_NO_DEPRECATE;_CRT_NONSTDC_NO_DEPRECATE;_CRT_SECURE_CPP_OVERLOAD_STANDARD_NAMES"
        "_CRT_SECURE_NO_DEPRECATE;_CRT_NONSTDC_NO_DEPRECATE;_CRT_SECURE_CPP_OVERLOAD_STANDARD_NAMES;
         _SCL_SECURE_NO_DEPRECATE"
      />

This (usually) avoids warnings about unsafe functions like sprintf for which Microsoft have provided “safe” alternatives. Read a critique of these [here](http://www.informit.com/guides/content.asp?g=cplusplus&seqNum=259&rl=1). They are not usable in cross-platform code because they are non-standard. Ignore any such warnings that have failed to be supressed.

### OpenBabel source code

Although the source code package from the SourceForge download page has all the OpenBabel code, it may not have some of the ancillary files, since it is really intended for UNIX(Linux) systems. If you intend to compile under Windows it is much better to download the code from SVN. [Tortoise SVN](http://tortoisesvn.tigris.org/) is a very convenient client for SVN - it operates from Windows explorer - and is easy to install. Then make a directory for the OpenBabel file, right click and select SVN Checkout. For a released version of OpenBabel enter something like:

-   <https://openbabel.svn.sourceforge.net/svnroot/openbabel/openbabel/tags/openbabel-2-1-1>

or for the development code:

-   <https://openbabel.svn.sourceforge.net/svnroot/openbabel/openbabel/trunk>

Click OK and all the code and required external DLLs (e.g. for InChI and libxml2) are downloaded.

### Boost

You need to install some elements of the Boost Library. This is done as follows:

-   Download and run the [BoostPro 1.34.1 Installer](http://www.boost-consulting.com/products/free)
-   Choose the Visual Studio 2005 version
-   Choose both of the single thread variants
-   On the next screen, choose just the Boost header files and deselect everything else
-   Complete the installation
-   Open windows-vc2005/OpenBabelOBF.sln with Visual Studio and from the Menu choose Project, Properties, C/C++, Additional Include Directories and add C:\\Program Files\\boost\\boost_1_34_1 (or whereever you installed Boost)

### Environment Variable

Make an environment variable BABEL_DATADIR to point to OpenBabel's /data folder. This needed for functions like logP, although the basic data, like atomic weights, are also compiled into the program and will be found even if this variable is not set.

### Basic build

At this stage you should be able to compile the command-line version of OpenBabel. Open windows-vc2005/OpenBabelOBF.sln and build all the projects except OBPythonOBF, OBJava, OBCSharp and OBGUI. In this build, the core is contained in multiple DLLs, and formats and extensions as plugin \*.obf files. This allows the package to be expanded or slimmed after compilation by adding or removing obf files. In the Release build these files are in the window-vc2005 folder and in the Debug build in windows-vc2005/debug.

### Compiling your own programs

There is an example program in window-vc2005/examples which is usable as a template for application programs. It has a Debug build which eases the development of such programs and can also assist in understanding the workings of API calls. It expects the main OpenBabel lib files to be where they were built during the main build. If you want to build your program elsewhere you will need to adjust the Additional Library Directories in the Linker section of the project properties.

window-vc2005/Tools.sln has projects for several small programs based on the OpenBabel API to do useful things, and may also be a model for further applications. There is a brief description of these in window-vc2005/OBTools/Projects in OBTools.txt and [Guides](/Guides "wikilink") and [Tutorial:Other_Tools](/Tutorial:Other_Tools "wikilink").

### Compiling wxWidgets

To compile the Windows GUI, you will need to install and compile [wxWidgets](http://www.wxwidgets.org/). We are currently using [wxWidgets 2.8.3](http://downloads.sourceforge.net/wxwindows/wxWidgets-2.8.3.zip). To compile it...

-   Unzip it into a folder that doesn't contain spaces
-   Read the install notes in the distribution
-   Read more [install notes](http://www.wxwidgets.org/wiki/index.php/MSVC_.NET_Setup_Guide) on the web site
-   Set the environment variable WXWIN to the installation directory of wxWidgets, e.g. E:\\wxWidgets-2.8.3, and restart MSVC.
-   In the file$(WXWIN)/include/wx/msw/setup.h change

<!-- -->

    #define wxUSE_STD_IOSTREAM  0

to

    #define wxUSE_STD_IOSTREAM  1

-   In the file $(WXWIN)/include/wx/msw/wx.rc find the section “Manifest file for Windows XP” and add immediately after it:

<!-- -->

    //For Visual Studio 2005
    #define wxUSE_NO_MANIFEST 1
    #if defined(__WXMSW__) && !defined(__WXWINCE__)
    #pragma comment(linker, "\"/manifestdependency:type='Win32' name='Microsoft.Windows.Common-Controls' version='6.0.0.0' processorArchitecture='X86' publicKeyToken='6595b64144ccf1df'\"")
    #endif
    //

This ensures that the latest version of Common Controls is used.

-   Open “build\\msw\\wx.dsw” and answer “Yes to All” for the format conversion. (There is no need to save the converted project files.)
-   On the menu, choose “Batch Build”, and sort by “Configuration”. Select only those configurations of type “Release” and, possibly “Debug”, and click on Build All.

The GUI can be built by opening OpenBabelOBF.sln and building the project OBGUI.

### Debugging with Visual Studio

If you do a significant amount of debugging of OpenBabel code, you may wish to have the OpenBabel objects appear in the the Autos or Locals debugging windows in a more useful form. There is a lot that can be done but the simple suggestion here is a start.

Edit the file C:\\Program Files\\Microsoft Visual Studio 8\\Common7\\Packages\\Debugger\\autoexp.dat
In the \[AutoExpand\] section add the following text

    ; OpenBabel
    OpenBabel::OBMol =<_title> <_natoms> atoms, <_nbonds> bonds
    OpenBabel::OBAtom =index=<_idx> <_type> charge=<_fcharge>
    wxString=<m_pchData,st>

and restart Visual Studio.
In the debugger OBMol, OBAtom and wxString objects will be easier to identify.

### Scripting Interfaces

As downloaded from SVN, the solution has the projects for the scripting interfaces, OBPythonOBF, OBJava and OBCSharp, disabled so that they are not built by Build Solution. To build them you need to first install [SWIG](http://www.swig.org/). Use the latest release of SWIG.

OBJava and OBCSharp built in the release configuration. The OBPythonOBF project has several configurations corresponding to different versions of Python (the default Release configuration will fail with an error).

To configure for version(s) of Python on your computer:

-   Edit windows-vc2005/setenv.txt so that the environment variable(s) correspond to your system. The irrelevant environment variables can be ignored.
-   Save as windows-vc2005/setenv.bat
-   Double click on setenv.bat to start MSVC++ with the variables set.
-   Set the Solution Configuration to Release (on the toolbar).
-   In the Configuration Manager (on the Build menu) set the Configuration of the OBPythonOBF project to the version you wish to build.

Build OBPythonOBF, OBJava or OBCSharp. If necessary, OBPython can be rebuilt with additional configurations.

### Building the Windows Installer

The Windows installer uses a script compiled by [NSIS](http://nsis.sourceforge.net/Main_Page). All the above projects, including the GUI and scripting, need to have been built. [Download](http://www.microsoft.com/downloads/details.aspx?familyid=200B2FD9-AE1A-4A14-984D-389C36F85647&displaylang=en) the Visual C++ Redistributable and put the file vcredist_x86.exe into windows-vc2005/Distribution. Right click the script file in that folder to compile it.

Compiling the 2.3.x series (subversion trunk)
---------------------------------------------

### Compiler and Build System

We recommend the following compiler which is available for free:

-   [Visual C++ 2008 (9.0) Express Edition](http://www.microsoft.com/Express/VC/)

You also need to install [CMake 2.6.x](http://www.cmake.org/cmake/resources/software.html). Install into the default location.

### Compiling wxWidgets

If you are not interested in compiling the OpenBabel GUI, you can skip this section.

To compile the Windows GUI, you will need to install and compile [wxWidgets](http://www.wxwidgets.org/). We are currently using [wxWidgets 2.8.3](http://downloads.sourceforge.net/wxwindows/wxWidgets-2.8.3.zip). To compile it...

-   Unzip it into a folder that doesn't contain spaces
-   Read the install notes in the distribution
-   Read more [install notes](http://www.wxwidgets.org/wiki/index.php/MSVC_.NET_Setup_Guide) on the web site
-   Set the environment variable WXWIN to the installation directory of wxWidgets, e.g. E:\\wxWidgets-2.8.3, and restart MSVC.
-   In the file$(WXWIN)/include/wx/msw/setup.h change

<!-- -->

    #define wxUSE_STD_IOSTREAM  0

to

    #define wxUSE_STD_IOSTREAM  1

-   In the file $(WXWIN)/include/wx/msw/wx.rc find the section “Manifest file for Windows XP” and add immediately after it:

<!-- -->

    //For Visual Studio 2005
    #define wxUSE_NO_MANIFEST 1
    #if defined(__WXMSW__) && !defined(__WXWINCE__)
    #pragma comment(linker, "\"/manifestdependency:type='Win32' name='Microsoft.Windows.Common-Controls' version='6.0.0.0' processorArchitecture='X86' publicKeyToken='6595b64144ccf1df'\"")
    #endif
    //

This ensures that the latest version of Common Controls is used.

-   Open “build\\msw\\wx.dsw” and answer “Yes to All” for the format conversion. (There is no need to save the converted project files.)
-   On the menu, choose “Batch Build”, and sort by “Configuration”. Select only those configurations of type “Release” and, possibly “Debug”, and click on Build All.

### Get the OpenBabel source code

The OpenBabel source code should be checked out of the Subversion (SVN) repository. Install [Tortoise SVN](http://tortoisesvn.tigris.org/). Then make a directory for the OpenBabel files, right click on it and select SVN Checkout. Enter

-   <https://openbabel.svn.sourceforge.net/svnroot/openbabel/openbabel/trunk>

Click OK and all the code and required external DLLs (e.g. for InChI and libxml2) are downloaded.

### Compile OpenBabel

Open a command windows in windows-vc2008 and run default_build.bat (if you don't want to compile the GUI, use “-DBUILD_GUI=OFF”). This creates windows-vc2008/build/openbabel.sln. Open this file in Visual Studio and build the target “BUILD ALL”.
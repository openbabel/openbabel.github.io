---
title: OpenBabel on Windows
permalink: /OpenBabel_on_Windows/
---

*If you're looking for information on how to get Open Babel, see the [Install](/Install "wikilink") page.*

Overview
--------

Open Babel on Windows provides two programs for the price of one:

-   **babel**, a command-line program for converting file formats, filtering using SMARTS strings, and so on. The Open Babel installer adds the install folder to the Windows Path. This means you can just type “babel” at the Command Prompt to run **babel**, no matter what your current directory is.
    -   [Full description](/Babel "wikilink")
    -   [Examples](/Tutorial:Basic_Usage "wikilink")

<!-- -->

-   **Open Babel GUI**, a graphical user interface to **babel**'s functionality. You can start **Open Babel GUI** using the shortcut in the Start Menu. You can copy this onto your desktop to make it easier to access it.
    -   [Documentation](/OpenBabelGUI "wikilink")

Automating file conversions using Drag'n'Drop
---------------------------------------------

This section describes how automate file format conversion simply by dragging an input file onto a target on your desktop.

(1) Start Notepad, and enter the following text:

    @echo off
    set convertto=sdf
    echo Converting %~nx1 to %convertto% format
    set outputfilename="%~ndp1.%convertto%"
    babel.exe %1 %outputfilename%
    pause

(2) Save this file on your desktop as *babel2sdf.bat*. Make sure that the file extension is .bat and not .txt.

(3) If you drag and drop an inputfile onto *babel2sdf.bat*, **babel** will create an SDF output file of the same name. The output file will be created in the same directory as the inputfile.

(4) If you don't like 'pressing any key to continue', remove the “pause” line in *babel2sdf.bat*.

(5) It may be more convenient to have a copy of the bat file in the folder where your chemical files are. Dropping a chemical file on the bat file still works in all Windows Explorer modes - including Details, List, Icons, etc.

(6) As an alternative to (1), use just a single line of text:

    @babel.exe %1 "%~ndp1.%~n0"

and save it as *sdf.bat*. This will behave the same as *babel2sdf.bat* above. But, if you copy it and rename it *cml.bat*, it will convert dropped files to Chemical Markup Language instead. Similarly with any other OpenBabel format.
---
title: Windows GUI
permalink: /Windows_GUI/
---

[Image:WinGUI.gif](/Image:WinGUI.gif "wikilink")

This interface helps to make OpenBabel more natural for Windows users than using the command line interface. It is entirely text-based, and does not have (as yet) graphical representations of molecules etc. It's main features are displaying the content of the input and output files, and presenting the options as checkboxes, etc.

It (along with the command line version) is available in compiled form, ready to run without any installation, in the [download area](http://sourceforge.net/project/showfiles.php?group_id=40728&package_id=32894&release_id=374001). It is written in MFC and the source code is included in the normal OpenBabel distribution.

Its use is fairly obvious, but the steps are described, with some details, below.

Choose an input format
----------------------

Select from the dropdown list, which contains all the input formats that are loaded. Further information on the selected format is available in a dialog box by clicking the FormatInfo button.

Specify an input file
---------------------

The name can be typed into the edit box, or more usually, selected from a FileOpen Dialog by clicking the ... button. By default, the files are filtered by the file extension of the selected format, but All Chemical Formats is also available. When a file is selected, its first 8000 characters are displayed. Currently, the file should have Windows type newlines (CRLF) and those with UNIX type (LF) are not displayed properly. Files with both types are however converted ok. Multiple input files can be specified, either from the OpenFile Dialog or manually, when the names are separated by a semicolon. A single input filename can contain a \* wildcard character, when the names of the matching files will be displayed, rather than any content.

Data can be entered manually if the appropriate checkbox is clicked. The file name is then ignored. To move to a new line when entering data uses CNTL Enter, since Enter carries out the conversion. Typing in SMILES like this is probably the quickest way to prepare a chemical format file for a small molecule.

Choose an output format and output file
---------------------------------------

After conversion the first 8000 characters of the output file are displayed, as a guide to whether the conversion went ok. The display also contains error messages (which do not appear in the output file). For an output with multiple molecules, all the error messages are displayed before any of the content, rather than being interleaved as in the commandline version output.

If the appropriate checkbox is checked or if no filename is given, then the content is displayed only and not written to a file.

Select the required Options
---------------------------

The check and edit boxes appropriate to the requested conversion are displayed in the centre. The ones at the top are general and relate to the type of chemical object (molecule or reaction) being converted. Below these are options specific to the input and the output formats.

These options are generated from the help text in a way described in About OBGUI accessed from the Control Menu (top left hand corner of the title bar). The command line interface has been developing fairly quickly recently and the GUI has not always been able to keep up, so that there are some features which are not available (audit messages, using a molecule in a file as a target in fastsearch format) or a bit cumbersome to use (batch conversion).

Click Convert to carry out the conversion
-----------------------------------------

The number of objects (molecules or reactions) converted is shown next to the button. OpenBabel has rather sparse error messages and the GUI isn't completely updated to show some of the lesser warnings. So if nothing appears to happen, there is probably something wrong with the data or with how you are asking it to be converted.
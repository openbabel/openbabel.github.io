---
title: What's available? Online help
permalink: /What's_available_Online_help/
---

### Getting help information from the command line

Typing

` babel -H`

will produce a large page on the basic usage of OpenBabel, with many command-line options. To see a list of the file formats that are supported, see below. (The commands are identical for the alternative obabel interface.)

Many features of OpenBabel are provided by *plugins*, which are independent pieces of code which in some cases may be added after the program has been compiled or installed. To see a list of the plugin categories that are present:

` babel -L`

These will probably include:

|                  |                                                                    |
|------------------|--------------------------------------------------------------------|
| **formats**      | file formats, such as smiles, pdb, sdf and many more.              |
| **descriptors**  | numerical or text properties of molecules, e.g. logP, inchi        |
| **ops**          | command-line options, e.g. --gen3D, --sort                         |
| **fingerprints** | binary representation of molecules for sub-structure searches etc. |
| **charges**      | models for assigning partial charges to atoms, e.g. gasteiger      |

To see a list of the plugins within a particular category add the name of the category, for instance:

` babel -L formats`

To see only formats for reading files:

` babel -L formats read    OR`
` babel -L formats input`

And similarly for write or output formats.

To get more details about a particular format (or any other plugin), use its ID (name), for instance:

` babel -L sdf`

This will provide the command-line options specific to that format and sometimes other information.

To get a detailed description of all the types within a category, use:

` babel -L ops verbose`

### Getting help information in the GUI

The available formats are shown in dropdown boxes and the available options in the middle panel.

Detailed information on the selected format can be shown with the Format Info buttons.

A list of the plugin categories is under a Plugins menu entry. Clicking the the name for a particular type provides its details and also puts its ID on the clipboard so it can be pasted into an editbox in the options panel.

[Category:Guides](/Category:Guides "wikilink")

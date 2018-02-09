---
title: IBabel
permalink: /IBabel/
---

**Note \[13/03/11\]:** The following page is out of date (last updated 2007). The **[iBabel3 website](http://www.macinchem.org/ibabel/)** has the latest information.

Overview
--------

iBabel is an alternative graphical interface to Open Babel for Macintosh OS X.

It is an AppleScript Studio application that provides a front-end for a variety of cheminformatics tools. To date these include: file conversion (between a vast range of chemical file formats), SMARTS-based substructure searching, similarity searching, list manipulation, overlaying using OpenBabel, a 2D viewer using [JChemPaint](http://jchempaint.sourceforge.net/), a 3D molecule viewer using [Jmol](http://jmol.sourceforge.net/), which are now included in the iBabel application. As an alternative [Marvin](http://www.chemaxon.com/marvin/) can be used for both 2D and 3D display.

Installation
------------

iBabel can be downloaded [here](http://www.macinchem.org/ibabel/): the expanded zip file contains an application called iBabel. Simply create a folder on Macintosh HD called Public and a folder within Public called Structures (if you forget, iBabel should create them for you the first time it runs).

The iBabel application can be in the applications folder. You also need to install OpenBabel, if you compile and install using the default instructions the babel application should be installed in usr/local/bin.

If you want to have things in different locations you will need to download the iBabel source and edit it.

You should end up with this folder structure:

[Image:Structures.png](/Image:Structures.png "wikilink")

The folder Structures is where temporary structures are stored for visualisation, and may need to be emptied occasionally.

The iBabel application can be moved to your applications folder, double click on it to open the application.

Tour of iBabel
--------------

### File Conversion

[Image:Convert.png](/Image:Convert.png "wikilink")

The “Convert” tab is a GUI for OpenBabel allowing file conversion for a wide variety of formats including CML. On all tabs the “Use Terminal” check box is available if you want to see the script run. To convert a file click the input button and chose the input file, select the input and output file types and click convert. The dropdown menus allow change the explicit hydrogens. By default all molecules are converted but a subset can be selected. You can convert a subset based on a SMARTS string, split the output into individual molecule files or join them all into a single molecule. The default location for the output is the desktop; the user can change this by simply typing the desired destination into the output file text box.

### SMARTS Searching

[Image:Search.png](/Image:Search.png "wikilink")

This is the search tab, here you can run searches using SMARTS based queries, the Classes and groups dropdown menus contain a variety of canned SMARTS queries. You can of course simply type in a SMARTS query or use Marvin as the editor to generate the SMARTS string. Simply fill the SMILES/SMARTS string box choose an option from the dropdown menu then click add (this allows the user to concatenate options). Either JChemPaint, Marvin or JME applets can be used for editing (set in Preferences).

The results of a search can be viewed in the viewer tab but you must have first imported the structures in the viewer tab. The select or unselect dropdown menu allows you to change the selection in the Viewer.

### Molecular Similarity

[Image:Similar.png](/Image:Similar.png "wikilink")

The “Similar” tab gives access to the new fastsearch and similarity searching options, you can do searching of moderately sized files (&lt;10,000 structures) directly but for larger files (or faster responses) it is advisable to first create an index file (output.fs) and then run the searches against the index. You can enter a similarity limit or number of records to return, or if left blank it will run a sub-structure search. The query can either be a SMILES or a file. At present there are two types of fingerprints, FP2 The other fingerprint type FP3 uses a series of SMARTS queries that are stored in /usr/local/share/openbabel/patterns.txt (You can add your own SMARTS queries to this file). Again you can view the results in the viewer tab.

### Tools

[Image:Tools.png](/Image:Tools.png "wikilink")

The tools menu gives access to a couple of other features, property calculation and superimposition onto a template based on SMARTS matching. More tools will be added as they become available.

### Viewing

[Image:Viewer.png](/Image:Viewer.png "wikilink")

This is the “Viewer” tab, select a file to view using the “input” button then click “import” a list of molecules in the file will be displayed in the table. This can be sorted by clicking on the column headers. Clicking on a molecule name will display a 2D or 3D structure depending on which of the radio buttons are selected. (Note display is limited to the abilities of the applets).

The viewer tab allows the user to browse through a multi-molecular file and then sort and select compounds and export a subset. The structures can be displayed as either 2D of 3D structures using a Java applet (JChempaint, Jmol, or Marvin). “Name list” exports a text list of the selected compounds, “count” gives the total of selected compounds, “invert” inverts the selection, “none” and “all” either unselect or select all. You can import more then one structure file and then export selections from one or more of the imported files using the multi or single buttons. (If you have only imported one file the single file export is faster).

### Spotlight

[Image:Spotlight.png](/Image:Spotlight.png "wikilink")

The Spotlight tab allows you to search your hard drive for chemical content, this requires [ChemSpotlight](/ChemSpotlight "wikilink") be installed. You can search by molecular weight, chirality, exact SMILES etc. the results of the search can then be viewed in the Viewer pane.

Acknowledgements
----------------

This work is only possible due to the outstanding efforts of others, in particular:

-   OpenBabel: &lt;<http://openbabel.sourceforge.net/>&gt;
-   ChemSpotlight: &lt;<http://geoffhutchison.net/projects/chem/>&gt;
-   Jmol: &lt;<http://jmol.sourceforge.net/>)
-   JChemPaint &lt;<http://jchempaint.sourceforge.net>&gt;
-   AppleScript Studio mailing list &lt;<http://lists.apple.com/mailman/listinfo/applescript-studio>&gt;
-   Marvin &lt;<http://www.chemaxon.com/>&gt;
-   JME courtesy of Peter Ertl, Novartis &lt;<http://www.molinspiration.com/jme/>&gt;

[Category:Macintosh](/Category:Macintosh "wikilink")
---
title: OBEP 1
permalink: /OBEP_1/
---

Open Babel Enhancement Proposal 1 concerns the replacement of the current system for managing data read from file formats.

The essence of the proposal is that:

1.  All data read from a file format should be stored and accessed in the same way, using a key/value system
2.  When writing a particular file format, the values of particular keys may be handled in a special way

For example, an SD file contains a title, information on the program that created the file, a comment, and optionally several user-defined data items such as 'Melting Pt', 'Number of H bonds'. This data would be read into some type of data structure, for example a std::map, where the keys would be “Title”, “CreatedBy”, “Comment”, “Melting Pt”, “Number of H bonds”. Additional data fields could be added, and the current ones could be deleted or altered.

When writing this molecule to an SD file, the fields with names “Title”, “CreatedBy” and “Comment” would be treated as corresponding to these areas in the SD file. The remainder of the key/values would be written as additional data fields. When writing this molecule to a file format that does not handle additional data fields, this data is simply ignored.

Advantages of this system:

1.  Preserves the most information possible, so that conversion from a Gaussian output file to an SD file would in theory retain the basis set information as additional field “Basis Set”, for example.
2.  One system for all data - there's no need to treat special key values differently except at the time of writing

[Category:Enhancement Proposals](/Category:Enhancement_Proposals "wikilink")
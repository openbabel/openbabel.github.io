---
title: Blue Obelisk
permalink: /Blue_Obelisk/
---

The Blue Obelisk project is a loose affiliation of multiple open-source chemistry packages.

The Internet has brought together a group of chemists/programmers/informaticians who find themselves working together using collaborative tools and sharing commonality of vision. They are driven by wanting to do things better, but are frustrated with the Closed systems that chemists currently have to work with. And they express this in code, data, algorithms, specifications, tutorials, demonstrations, articles and anything that helps get the message across.

Activities have included:

-   In-person meetings at a variety of scientific conferences
-   Discussion on common cheminformatics algorithms, including a dictionary of independent implementations
-   A repository of common chemical information, including atomic radii, elemental information, etc.
-   Shared, open source webservices

For more information, see [BlueObelisk.org](http://blueobelisk.org/)

Blue Obelisk Algorithm Dictionary
---------------------------------

The following table provides a mapping between calls in Open Babel to algorithms in the Blue Obelisk Dictionary. The list is currently incomplete and does not yet link directly to the [API Documentation](http://openbabel.sourceforge.net/api/).

|                                                         |                                                                                                                                |
|---------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| blue-obelisk:convertCartesianIntoNotionalCoordinates    | [OBUnitCell::SetData(v1, v2, v3)](http://openbabel.sourceforge.net/api/classOpenBabel_1_1OBUnitCell.shtml)                     |
| blue-obelisk:convertNotionalIntoCartesianCoordinates    | [OBUnitCell::GetCellVectors()](http://openbabel.sourceforge.net/api/classOpenBabel_1_1OBUnitCell.shtml)                        |
| blue-obelisk:calculateOrthogonalisationMatrix           | [OBUnitCell::GetOrthoMatrix()](http://openbabel.sourceforge.net/api/classOpenBabel_1_1OBUnitCell.shtml)                        |
| blue-obelisk:convertCartesianIntoFractionalCoordinates  | [OBUnitCell::GetFractionalMatrix()](http://openbabel.sourceforge.net/api/classOpenBabel_1_1OBUnitCell.shtml)                   |
| blue-obelisk:findSmallestSetOfSmallestRings             | [OBMol::GetSSSR()](http://openbabel.sourceforge.net/api/classOpenBabel_1_1OBMol.shtml#0f6bce457ef6f963b8e4ba7c4be23775)        |
| blue-obelisk:rebondFrom3DCoordinates                    | [OBMol::ConnectTheDots()](http://openbabel.sourceforge.net/api/classOpenBabel_1_1OBMol.shtml#31d05972f7454e791641c4a7d0071d12) |
| blue-obelisk:zmatrixCoordinatesIntoCartesianCoordinates | [InternalToCartesian()](http://openbabel.sourceforge.net/api/namespaceOpenBabel.shtml#0bc6cfbc4adcb9d4c39c8c2acec9e982)        |
| blue-obelisk:cartesianCoordinatesIntoZmatrixCoordinates | [CartesianToInternal()](http://openbabel.sourceforge.net/api/namespaceOpenBabel.shtml#9c68f56ae8adc8af0c2e8acce4422e8f)        |
||

[Category:Developer](/Category:Developer "wikilink")
---
title: FP2
permalink: /FP2/
---

FP2 indexes small molecule fragments based on linear segments of up to 7 atoms in length.

A molecule structure is analysed to identify linear fragments of length from 1-7 atoms. Single atom fragments of C, N,and O are ignored. A fragment is terminated when the atoms form a ring.

For each of these fragments the atoms, bonding and whether they constitute a complete ring is recorded and saved in a set so that there is only one of each fragment type. Chemically identical versions, (i.e. ones with the atoms listed in reverse order and rings listed starting at different atoms) are identified and only a single canonical fragment is retained.

Each remaining fragment is assigned a hash number from 0 to 1020 which is used to set a bit in a 1024 bit vector

[Category:Fingerprints](/Category:Fingerprints "wikilink")[Category:Developer](/Category:Developer "wikilink")
---
title: Code Standards
permalink: /Code_Standards/
---

Several important goals have been adopted for version 3.0:

1.  Headers must use forward declarations. For example, if you use OBAtom, you should \#include <openbabel/atom.h> not mol.h.
2.  Deprecated code, headers, classes will be removed. Gone.
3.  Use of “const” declarations
4.  Use of “unsigned” where appropriate
5.  Using hidden data pointers where appropriate to allow future expansion while preserving API and ABI (i.e., v3.1 will be binary compatible)
6.  Moving functions to protected and private which should not be public.
7.  Moving classes from public headers to implementation which should not be public (see parsmart.h for some horrible examples)
8.  Use the normal C++ standard file/class organization, that is, the class OBAtom should be defined in atom.cpp and atom.h. One class ONLY per .h/.cpp file pair.

External Sources
----------------

Several excellent sources exist for high-quality C++ code.

-   The KDE Project [Library Code Policy](http://techbase.kde.org/Policies/Library_Code_Policy) will be adopted in some form for Open Babel
-   The Google [C++ Style Guide](http://google-styleguide.googlecode.com/svn/trunk/cppguide.xml) has other useful suggestions
-   The [C++ FAQ](http://www.parashift.com/c++-faq-lite/)
-   [C++ Reference](http://www.cppreference.com/)
-   [C++ Library Reference](http://www.cplusplus.com/reference/)

[Category:Projects](/Category:Projects "wikilink")
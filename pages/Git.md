---
title: Git
permalink: /Git/
---

[Git](https://git-scm.com/) is the name of the software used to maintain the Open Babel version control repository. There are many clients for Git, including command-line and GUI applications. For more links, see the [Git website](http://git-scm.com/).

Keeping up to date with the latest Open Babel code with Git
-----------------------------------------------------------

(1) Make a clone of the latest development version (read-only):

    git clone git://github.com/openbabel/openbabel.git

This creates a directory called 'openbabel', which contains the latest source code from Open Babel.

(2) Configure and compile this using CMake, as described on the [CMake](/CMake "wikilink") page.

(3) After some time passes, and you want the latest bug fixes or new features, you may want to update your source code. To do this, go into the 'openbabel' directory you created above, and type:

    git pull
    git update

(4) Do step (2) again.

(5) If, after updating, the compilation fails please report it to the Open Babel [mailing list](mailto:openbabel-discuss@lists.sourceforge.net). In the meanwhile, if you want to go back to a particular revision (that is, if you don't want to use the latest one), just use 'git info' to find the details of the current revision, and update to an earlier revision either by revision checksum or by a certain number of commits:

    $ git log -1
    ...
    $ git reset --hard 4a843bef
    $ git reset --hard HEAD~10

Information for Developers
--------------------------

...coming soon?

[Category:Contribute](/Category:Contribute "wikilink")
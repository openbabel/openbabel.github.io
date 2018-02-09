---
title: Developer:Best Practices
permalink: /Developer:Best_Practices/
---

As an open source project, Open Babel has a very open development process. This means that many [contributors](/THANKS "wikilink") have helped with the project with a variety of help -- some for long periods of time, and some with small, single changes. All types of assistance has been valuable to the growth of the project over the years.

This document is aimed at itemizing a list of “best practices,” particularly for code developers.

Grabbing the Development Code
-----------------------------

The source code for Open Babel is maintained via the [Git](/Git "wikilink") version control system. You can browse the latest source code via [Github](https://github.com/openbabel/openbabel).

To download and update the source code itself, please see the instructions on using [Git](/Git "wikilink") with Open Babel.

Monitoring Progress
-------------------

Developers should keep track of changes made by others. Like most open source projects, development occurs in many places by many contributors. Therefore it is important to keep up-to-date with your code repository and keep on top of changes made by others. A bug you just found in the latest release may have already been fixed by someone else.

-   [CIA Stats on Open Babel](http://cia.navi.cx/stats/project/OpenBabel) (webpage and RSS updates for every change)
-   [OpenBabel-Updates](http://lists.sourceforge.net/lists/listinfo/openbabel-updates) (receives an e-mail message on every change)

In general, if you find that a recent update by other developer has introduced bugs or broken the code, please bring it up with them ASAP. We have a policy of “if you break it, you fix it” to keep the source code repository always in a working state.

Many of the developers use the current development snapshots for their daily use. This is sometimes called [eating your dog food](http://en.wikipedia.org/wiki/Eat_one%27s_own_dog_food) and is part of the general testing procedures for Open Babel.

Documentation
-------------

As an open source project, code **must** be documented, both for other developers to use the [API](http://openbabel.sourceforge.net/api/) and for others to follow your code.

For more information, please see tips on [adding documentation](/Developer:Documentation "wikilink").

Testing
-------

Testing is extremely important. New functions should have individual [unit tests](http://en.wikipedia.org/wiki/Unit_test) as older code is slowly added to the test suite. Because of the wide use of Open Babel, code is (and should be) thoroughly tested before release.

Releases may be imperfect and will likely contain bugs. However, increased testing improves code quality and makes life easier for everyone. For more information, see the guide on [testing](/Developer:Testing "wikilink") practices.

Code Formatting
---------------

It seems like a minor point, but the format of your code is important. As open source software, your code is read by *many*, many people.

Different contributions have often had different indentation styles. Simply making the code indentation **consistent** across an entire file makes the code easier to read.

Error Handling
--------------

The general philosophy of the Open Babel project is to attempt to gracefully recover from error conditions. Depending on the severity of the error, a message may or may not be sent to the user -- users can filter out developer debugging messages and minor errors, but should be notified of significant problems.

For more information, please see the documentation on [Handling Errors](/Errors "wikilink").

Patches and Changesets
----------------------

We're human--it's much easier to understand exactly what a patch is doing if it's not trying to add 20 features or fix 20 bugs at once. (Hopefully there won't be a need to fix 20 bugs!) If you want to add several features or fix several bugs, break the patch up into one for each request. The faster someone can understand your patch, the faster it will go into the source. Everyone benefits from faster, quality development.

Similarly, it's sometimes necessary to revert the code to an older version because of bugs. Each set of changes should only touch as few files as are needed. This makes it easier for others to review your changes and undo them if necessarily. (Again, hopefully there's never a need, but this is certainly a “best practice” to make life easier for everyone.)

The ChangeLog
-------------

The [ChangeLog](http://en.wikipedia.org/wiki/Changelog) file is used to maintain an abbreviated history of changes to the code by all users. Please add a ChangeLog entry to any patch and make sure to keep it up to date as you commit changes to the source code. The <http://www.gnu.org/software/guile/changelogs/guile-changelogs_3.html%7Cformat>\] should be mostly self-explanatory.

In particular, please include a notation of *any* file you have changed. This makes it easy for others to track which changes may have added new functionality, fixed bugs, or inadvertently caused errors.

[Category:Contribute](/Category:Contribute "wikilink")
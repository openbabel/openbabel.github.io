---
title: Ruby
permalink: /Ruby/
---

Starting with Open Babel 2.1, an experimental Ruby interface to the Open Babel library is available.

Compilation
-----------

The Ruby interface is auto-generated, including a Makefile which uses `extconf.rb`.

To generate the Makefile:

    % ruby extconf.rb --with-openbabel-include=/usr/local/include/openbabel-2.0
    % make

Running
-------

The Ruby interface can be run via `ruby` or interactive use via `irb`

    % irb
    require 'openbabel'

More Info
---------

Rich Apodaca has blogged about the Ruby interface:

-   [Painless Installation](http://depth-first.com/articles/2007/04/09/painless-installation-of-ruby-open-babel)

[Category:Developer](/Category:Developer "wikilink")
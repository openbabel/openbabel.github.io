---
title: Developer:Testing
permalink: /Developer:Testing/
---

Testing (and documenting) Open Babel is an important, and never-ending task. The following documentation is intended to give some idea as to the types of tests used by Open Babel and various tools available for debugging and testing.

Types of Tests
--------------

-   Unit tests - These are run under the UNIX build environment by calling `make check` and include a variety of tests
    -   Ideally these tests should cover every public function in the [Open Babel API](http://openbabel.sourceforge.net/api/). Adding more tests to provide greater coverage is a *high* priority.
    -   The tests attempt to show that functions work as indicated (i.e. pass) and fail properly on unacceptable input.
-   Roundtrip tests - These are run from the test file [repository](/repository "wikilink") and test file translation to/from all file formats.
-   “Dogfood” tests - Many of the developers use the current development snapshots for their daily use. This is sometimes called [eating your dog food](http://en.wikipedia.org/wiki/Eat_one%27s_own_dog_food) and ensures that bugs which impact common functionality are caught quickly.
-   Scripting language tests -- Both the [Perl](/Perl "wikilink") and [Python](/Python "wikilink") language bindings have additional tests to ensure that these scripting language modules work.
    -   These tests not only stress the scripting modules themselves, but also the underlying library.

UNIX/Linux/Mac OS X
-------------------

A variety of tools can be used to help diagnose problems and debug errors:

### Debuggers

-   [gdb](http://www.gnu.org/software/gdb/) - the GNU project debugger is a basic debugger on UNIX systems.
    -   GDB can be run on the babel program like so: `./libtool gdb src/babel`
    -   Several GDB commands are highly useful, including `bt` which gives a full backtrace of program execution upon error.
    -   The use of code optimization when compiling can make debugging with GDB and other debuggers extremely difficult. If needed, make sure Open Babel has been compiled, e.g. with CXXFLAGS=“-g -O0” on UNIX.

### Memory Checkers

Unlike languages like Java, which handle memory allocation and deletion, C++ requires that all code handle memory. In particular, this means if you use `new` or `malloc` or similar calls, you must be sure the memory will be properly freed when no longer needed. So-called “memory leaks” are cases where memory has been allocated, but never properly freed and are significant bugs in Open Babel.

Several tools can help find such errors:

-   [Valgrind](http://www.valgrind.org/) - Works on several platforms by carefully monitoring each memory access and allocation.
-   [LeakTracer](http://www.andreasen.org/LeakTracer/) - Works on a range of platforms by using C++ operator overloading.
-   [MallocDebug](http://developer.apple.com/documentation/Performance/Conceptual/ManagingMemory/Articles/FindingLeaks.html) (Mac OS X only) - Graphic front-end to monitor memory use and incorrect memory usage.

### Code Profiling

To improve the speed of execution, it is often helpful to rely on tools which can

-   [gprof](http://www.gnu.org/software/gprof/) - Used with the GCC compilers to produce profiling data including the number of calls to routines and the amount of time spent executing.
-   Shark / Saturn (Mac OS X only) - Graphical front-ends to gprof and can sample programs while running.

### C++ Unscrambler

The symbols used by C++ compilers and exposed by debugging, profiling, and memory tools are “scrambled.” The `c++filt` program can be used to decode the symbol to a human-readable form:

[c++filt](http://www.gnu.org/software/binutils/manual/html_chapter/binutils_9.html)

Windows
-------

Using the Visual C++ project files for Open Babel, the Microsoft tools offer debugging and profiling options.

[Category:Developer](/Category:Developer "wikilink")
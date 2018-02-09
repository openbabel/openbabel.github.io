---
title: Install (Android)
permalink: /Install_(Android)/
---

This document contains instructions for building OpenBabel (OB) on the Google Android platform using a JNI C++ wrapper.

Date: October, 1010, Tested with OB 2.2.99 on Android.

Current and Development versions
================================

Building OpenBabel 2.3.0 using CMake
------------------------------------

1. You will need Android SDK and a modified NDK which supports RTTI, STL, and exceptions. You can get the modified NDK here: <http://www.crystax.net/android/ndk-r4.php>

2. Android runs Java programs, libopenbabel provides C++ API. In order to connect the two you will need to write JNI C++ wrapper. Programming for Android with and without JNI is described in detail elsewhere, please be aware that there will be quite a few things to do even after libopenbabel is compiled. Create the Java project first, even if it is empty for the moment.

3. Unzip openbabel source. You might have to patch file src/locale.cpp, the patch was submitted here: <http://openbabel.svn.sourceforge.net/viewvc/openbabel?view=revision&revision=4050> (should be included in 2.3.0 release)

4. Put the attached babelconfig.h into include/openbabel. [babelconfig.h](http://gist.github.com/raw/626488/ddc42f1e117f63c7397c826917e06bdc3d0c035d/babelconfig.h)

5. Copy InChI headers: from include/inchi103/\*.h to src/formats/inchi103/

6. Create directory jni in top level openbabel source folder and put attached Android.mk and Application.mk there. [Android.mk](http://gist.github.com/raw/626490/60c1a61556a1cb4961054e9c67055acd26c1d997/Android.mk) [Application.mk](http://gist.github.com/raw/626490/ced5e34387c1a12cd22d2160d93b2582e2649b15/Application.mk)

7. Edit Application.mk to modify the locations in APP_PROJECT_PATH (should point to your Java Android project) and APP_BUILD_SCRIPT (should point to the aforementioned Android.mk script). You can also uncomment APP_ABI line to have both armeabi and armeabi-v7a executables. The latter allows for floating point unit on the target device.

8. Edit Android.mk if you'd like to have access to more formats - by default I included only SMILES and InChI. It should be trivial to include more formats. Note that I had problems with reaction formats, such as rsmilesformat, those that include reaction.h header. Avoid those unless necessary, otherwise you're on your own.

9. Run ndk-build script from the NDK you downloaded in step 1. It will compile libopenbabel.so and put it into your Android Java project directory. Remember that you will have to load libopenbabel.so in your Java program prior to any other C++ code which will use OpenBabel functions.

[Category:Installation](/Category:Installation "wikilink")
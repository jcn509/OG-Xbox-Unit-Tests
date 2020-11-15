# OG Xbox Unit Test example
A very simple example that shows you how you can run unit tests for original Xbox code inside xqemu using pyxboxtest.

[Unity](https://github.com/ThrowTheSwitch/Unity) is used in this example as it is lightweight and because it is easy to use on embedded systems.
I had initially wanted to use lest, but the lack of exception support in the NXDK made that impossible.

## Why?
You may have code that talks directly with the Xbox hardware that you wish to test.
Unfortunately, you can't test this code by running a unit testing framework on your PC as it doesn't have the right hardware.
You could use pyxboxtest on its own but as its designed to be an end to end framework it may not be ideal.

I of course would not recommend that you test hardware-independent code in this way. If you can run the tests on your PC they will execute much more quickly.

## Caveats
You may have to split up your tests into multiple executables as you will only have access to a maximum of 128mb of RAM.
Doing so is likely a good idea anyway if you have a large number of tests as then you can run multiple tests in parallel.

## TODO
- Split this repo up to into several modules
    - A C library that you can use to setup your tests
    - A python library (published on pypy) that includes the test runner
    - An example repo
- Investigate the use of a more feature-rich C++ framework
    - You likely wouldn't pick Unity for a C++ project
    - If the NXDK doesn't allow for exceptions, it may be possible to get doctest to work (although it doesn't work out of the box)
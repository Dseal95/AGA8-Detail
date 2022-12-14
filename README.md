# AGA8_Detail
Python Implementation of **AGA8 DETAIL** method for calculating gas compressibility factor, **Z** from **P**, **T** and **gas composition**.

**Notes:**

- Code refactored from the **C++** DETAIL code in file `Detail.cpp` from this repository - https://github.com/usnistgov/AGA8

- Implementation is tested on the same TEST inputs used in the **C++** code, see `main.py` input P, T and x.

- Python implementation of `DensityDetail()` only and not `PropertiesDetail()`. For this work, I only wanted to calculate the compressibility factor, **Z**.

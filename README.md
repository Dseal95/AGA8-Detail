# AGA8_Detail
Python Implementation of **AGA8 DETAIL** method for calculating gas compressibility factor, **Z** from **P**, **T** and **gas composition**.

**Notes:**

- Code refactored from the **C++** DETAIL code in file `Detail.cpp` from this repository - https://github.com/usnistgov/AGA8

- Implementation is tested on the same TEST inputs used in the **C++** code, see `main.py` input **P**, **T** and **x**.

- Python implementation of `DensityDetail()` only and not `PropertiesDetail()`. For this work, I only wanted to calculate the compressibility factor, **Z**.


## Setup
1. create `.venv` using the `setup_venv.sh` script 
2. run command `pip install -e ./src` to install the AGA8 package (in editable mode)
3. Choose what inputs, **P**, **T** and **x** you want to run the AGA8 Detail method on and add them to the `main.py`
4. Run `main.py` and output Z and approximated P are printed to the screen 







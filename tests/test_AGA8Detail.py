"""Test AGA8 Detail implementation."""

from modules.AGA8Detail import AGA8Detail

import pytest


def test_aga8_detail_compressibility_factor_against_c():
    """Test the Python implementation of AGA8 Detail for approximating Z on the C++ example."""
    # inputs
    P = 50000  # Kpa
    T = 400  # K
    x = [
        0.0,
        0.77824,
        0.02,
        0.06,
        0.08,
        0.03,
        0.0015,
        0.003,
        0.0005,
        0.00165,
        0.00215,
        0.00088,
        0.00024,
        0.00015,
        0.00009,
        0.004,
        0.005,
        0.002,
        0.0001,
        0.0025,
        0.007,
        0.001,
    ]

    # instantiate and run the AGA8 class
    AGA8 = AGA8Detail(p=P, t=T, x=x).run()

    actual = (AGA8.zd, AGA8.z)  # (density, properties)
    desired = (1.1738013826890625, 1.1738013641473262)

    assert actual == desired


def test_aga8_detail_properties_agaisnt_c():
    """Test the Python implementation of AGA8 Detail properties method agaisnt C++ example.

    Note: There are some minor differences at higher precision due to the difference in instantiaion between C and Python.
    """
    # inputs
    P = 50000  # Kpa
    T = 400  # K
    x = [
        0.0,
        0.77824,
        0.02,
        0.06,
        0.08,
        0.03,
        0.0015,
        0.003,
        0.0005,
        0.00165,
        0.00215,
        0.00088,
        0.00024,
        0.00015,
        0.00009,
        0.004,
        0.005,
        0.002,
        0.0001,
        0.0025,
        0.007,
        0.001,
    ]

    # instantiate and run the AGA8 class
    AGA8 = AGA8Detail(p=P, t=T, x=x).run()

    actual = [
        AGA8.MM,
        AGA8.D,
        AGA8.dpdd,
        AGA8.dpdt,
        AGA8.U,
        AGA8.H,
        AGA8.S,
        AGA8.cv,
        AGA8.cp,
        AGA8.W,
        AGA8.G,
        AGA8.JT,
        AGA8.kappa,
    ]
    desired = [
        20.54333051,
        12.807924036488005,
        6971.387690924084,
        235.66414930682123,
        -2739.134175817224,
        1164.6990962694103,
        -38.54882684677112,
        39.12076154430332,
        58.54617672380668,
        712.63936840579,
        16584.229834977858,
        7.432969304794694e-05,
        2.6725092251846054,
    ]

    assert actual == desired

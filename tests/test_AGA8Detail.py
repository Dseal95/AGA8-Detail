"""Test AGA8 Detail implementation."""

from modules.AGA8Detail import AGA8Detail

import pytest


def test_aga8_detail_compressibility_factor_method_against_c():
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


def test_aga8_detail_properties_method_against_c():
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


def test_aga8detail_z_approximation_example_1():
    """Test AGA8Detail() approximation of z for a known example (from UniSim simulation) of P, T and x."""
    # create test case
    P = 11672.30591
    T = 329.1959501
    x = [
        0.0,
        0.8605181275,
        0.00468943511,
        0.021032297039999998,
        0.0830931073,
        0.024005787129999998,
        0.00266965599,
        0.00310500342,
        0.00039002352999999997,
        0.00023977192000000002,
        3.197816e-05,
        4.9399800000000004e-06,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
    ]

    # instantiate AGA8Detail class
    AGA8 = AGA8Detail(p=P, t=T, x=x)

    actual = AGA8.run().z
    desired = 0.8453387504349907

    assert actual == desired


def test_aga8detail_z_approximation_example_2():
    """Test AGA8Detail() approximation of z for a known example (from UniSim simulation) of P, T and x."""
    # create test case
    P = 11778.85981
    T = 331.3596863
    x = [
        0.0,
        0.8645574829,
        0.00471616099,
        0.02077505707,
        0.08100759773,
        0.02299965451,
        0.0024834801,
        0.00286307457,
        0.00035400357,
        0.00021567912000000001,
        2.520598e-05,
        2.6290599999999997e-06,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
    ]

    # instantiate AGA8Detail class
    AGA8 = AGA8Detail(p=P, t=T, x=x)

    actual = AGA8.run().z
    desired = 0.8508947480602581

    assert actual == desired


def test_aga8detail_z_approximation_example_3():
    """Test AGA8Detail() approximation of z for a known example (from UniSim simulation) of P, T and x."""
    # create test case
    P = 11133.88937
    T = 331.0980687
    x = [
        0.0,
        0.8616455105,
        0.00469811792,
        0.021060977329999998,
        0.08256866667000001,
        0.02373943755,
        0.0026173493199999997,
        0.0030427240999999997,
        0.00037079653999999996,
        0.00022267528000000002,
        3.035669e-05,
        3.37521e-06,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
    ]

    # instantiate AGA8Detail class
    AGA8 = AGA8Detail(p=P, t=T, x=x)

    actual = AGA8.run().z
    desired = 0.853840503325755

    assert actual == desired


def test_aga8detail_z_approximation_example_4():
    """Test AGA8Detail() approximation of z for a known example (from UniSim simulation) of P, T and x."""
    # create test case
    P = 11845.12799
    T = 331.11875
    x = [
        0.0,
        0.8627619880999999,
        0.00491112452,
        0.02085074657,
        0.08144546933999999,
        0.02354307161,
        0.0026650497,
        0.00307708257,
        0.00039213710999999997,
        0.00024061062,
        3.428013e-05,
        6.89542e-06,
        8.67e-07,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
    ]

    # instantiate AGA8Detail class
    AGA8 = AGA8Detail(p=P, t=T, x=x)

    actual = AGA8.run().z
    desired = 0.8490470421250338

    assert actual == desired


def test_aga8detail_z_approximation_example_5():
    """Test AGA8Detail() approximation of z for a known example (from UniSim simulation) of P, T and x."""
    # create test case
    P = 11188.62433
    T = 328.6182424000824
    x = [
        0.0,
        0.8618463533,
        0.00470927796,
        0.02033212472,
        0.08267388868999999,
        0.02401060257,
        0.0026570938599999997,
        0.00309789558,
        0.0003977758,
        0.00023328679000000002,
        3.573006e-05,
        5.96658e-06,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
    ]

    # instantiate AGA8Detail class
    AGA8 = AGA8Detail(p=P, t=T, x=x)

    actual = AGA8.run().z
    desired = 0.8482020334710543

    assert actual == desired

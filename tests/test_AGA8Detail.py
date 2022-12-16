import pytest
from modules.AGA8Detail import AGA8Detail


def test_AGA8_DETAIL_C_Example():
    """Test the Python implementation of AGA8 Detail method on the C++ example."""
    # inputs
    P = 50000  # Kpa
    T = 400  # K
    x = [0.0, 0.77824, 0.02, 0.06, 0.08, 0.03, 0.0015, 0.003, 0.0005, 0.00165, 0.00215, 0.00088, 0.00024, 0.00015, 0.00009, 0.004, 0.005, 0.002, 0.0001, 0.0025, 0.007, 0.001]

    actual = AGA8Detail(P=P, T=T, x=x).run().Z
    desired = 1.1738013826890625

    assert actual == desired

from AGA8Detail import AGA8Detail

if "__main__" == __name__:
    # set initial values
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
    Z, P2, D, _, _ = AGA8Detail(x, P=P, T=T)

    print(
        "\n------------------------------------------ AGA8 DETAIL ------------------------------------------"
    )
    print(
        f"\nCalculaing compressibility factor, Z for P={P} (Kpa), T={T} (K) and x using AGA8 DETAIL method:\n"
    )
    print(f"Z = {Z}\nP2(Kpa) = {P2}\nP2(barg) = {(P2/100)+1.01325}\n\u03c1 = {D}\n")
    print(
        "-------------------------------------------------------------------------------------------------\n"
    )

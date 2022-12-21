"""Program to approximate gas compressibility factors, Z using AGA8 Detail method."""

from modules.AGA8Detail import AGA8Detail

if "__main__" == __name__:
    # set initial values
    P = 50000  # Kpa
    T = 400  # K
    x = [0.0, 0.77824, 0.02, 0.06, 0.08, 0.03, 0.0015, 0.003, 0.0005, 0.00165, 0.00215, 0.00088, 0.00024, 0.00015, 0.00009, 0.004, 0.005, 0.002, 0.0001, 0.0025, 0.007, 0.001]

    # run AGA8 method
    AGA8D = AGA8Detail(P=P, T=T, x=x).run()

    print("\n-----------------------------------AGA8 DETAIL-------------------------------------")
    print(f"Calculaing Z for P={P} (Kpa), T={T} (K) and gas comp, x using AGA8 DETAIL method:\n")
    print(f"Z = {AGA8D.Z}\nP2 = {AGA8D.P2} (Kpa)\nP2(barg) = {(AGA8D.P2/100)+1.01325} (barg)\n\u03c1 = {AGA8D.D}")
    print("-----------------------------------------------------------------------------------\n")
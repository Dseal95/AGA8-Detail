"""Program to approximate gas compressibility factors, Z using AGA8 Detail method."""

from modules.AGA8Detail import AGA8Detail

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

    # run AGA8 method
    AGA8D = AGA8Detail(p=P, t=T, x=x).run()

    print(
        "\n-----------------------------------AGA8 DETAIL-------------------------------------"
    )
    print(
        f"Calculaing Z for [P={P} (Kpa), T={T} (K) and gas comp, x] using AGA8 DETAIL method:\n"
    )
    print(
        f"\t     Z (PropertiesDetail) = {AGA8D.z}\n \
            Zd (DensityDetail) = {AGA8D.zd}\n \
            P2 (DensityDetail) [Kpa] = {AGA8D.P2}\n \
            P2 (DensityDetail) [barg] = {(AGA8D.P2/100)+1.01325}\n \
            P3 (PropertiesDetail) [Kpa] = {AGA8D.P3}\n \
            P3 (PropertiesDetail) [barg] = {(AGA8D.P3/100)+1.01325}\n \
            Molar Mass (MM) [g/mol] = {AGA8D.MM}\n \
            \u03c1 (Molar Density) [mol/l] = {AGA8D.D}\n \
            d(P)/d(rho) [kPa/(mol/l)] = {AGA8D.dpdd}\n \
            d^2(P)/d(rho)^2 [kPa/(mol/l)^2] = {AGA8D.dpdd2}\n \
            d(P)/d(T) [kPa/K] = {AGA8D.dpdt}\n \
            Energy [J/mol] = {AGA8D.U}\n \
            Enthalpy [J/mol] = {AGA8D.H}\n \
            Entropy [J/mol-K] = {AGA8D.S}\n \
            Isochoric heat capacity [J/mol-K] = {AGA8D.cv}\n \
            Isobaric heat capacity [J/mol-K] = {AGA8D.cp}\n \
            Speed of sound [m/s] = {AGA8D.W}\n \
            Gibbs energy [J/mol] = {AGA8D.G}\n \
            Joule-Thomson coefficient [K/kPa] = {AGA8D.JT}\n \
            Isentropic exponent = {AGA8D.kappa}\n"
    )
    print(
        "-----------------------------------------------------------------------------------\n"
    )

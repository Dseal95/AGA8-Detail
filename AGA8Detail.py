"""AGA8Detail.py module contains the functionality used in the DETAIL method."""

import math

import numpy as np

from initialise import (initialise_an, initialise_bn, initialise_Bs,
                        initialise_Bsnij2, initialise_Csn, initialise_Ei,
                        initialise_Fi, initialise_fn, initialise_Gi,
                        initialise_gn, initialise_i25_arrays,
                        initialise_ij5_arrays, initialise_ij_arrays,
                        initialise_Ki, initialise_kn, initialise_n0i,
                        initialise_Qi, initialise_qn, initialise_Si,
                        initialise_sn, initialise_th0i, initialise_Tun,
                        initialise_un, initialise_Wi, initialise_wn)
from static import MaxFlds, MmDetail, NcDetail, NTerms, R, epsilon, tolr


def SetupDetail():
    """Initialize all the constants and parameters in the DETAIL model."""
    global K3, U, G, Q, F, Told, D, P2, MM, Bs, an, bn, kn, un, fn, gn, qn, sn, wn, Ei, Eij, Ki, Kij, Gi, Gij, Qi, Fi, Si, Wi, Uij, n0i, th0i, Ki25, Ei25, Bsnij2, Csn, Kij5, Uij5, Gij5, Tun

    K3 = 0
    U = 0
    G = 0
    Q = 0
    F = 0

    Told = 0  # initial Told set @ 0
    D = 1e10  # initial D
    P2 = 0  # initial approximated P @ 0
    MM = 0

    # initialise arrays
    Bs = initialise_Bs()
    Bsnij2 = initialise_Bsnij2(MaxFlds)

    an = initialise_an(NTerms)
    bn = initialise_bn(NTerms)
    kn = initialise_kn(NTerms)
    un = initialise_un(NTerms)
    fn = initialise_fn(NTerms)
    gn = initialise_gn(NTerms)
    qn = initialise_qn(NTerms)
    sn = initialise_sn(NTerms)
    wn = initialise_wn(NTerms)

    Ei = initialise_Ei(MaxFlds)  # energy params
    Ki = initialise_Ki(MaxFlds)  # size params
    Gi = initialise_Gi(MaxFlds)  # orientation params

    Eij, Uij, Kij, Gij = initialise_ij_arrays(MaxFlds)

    # quadrupole params
    Qi = initialise_Qi(MaxFlds)
    Fi = initialise_Fi(MaxFlds)
    Si = initialise_Si(MaxFlds)
    Wi = initialise_Wi(MaxFlds)

    # ideal gas params
    n0i = initialise_n0i(MaxFlds)
    th0i = initialise_th0i(MaxFlds)

    # precalculation of constants
    Ki25, Ei25 = initialise_i25_arrays(MaxFlds)
    Kij5, Uij5, Gij5 = initialise_ij5_arrays(MaxFlds)

    for i in range(1, MaxFlds + 1):
        Ki25[i] = math.pow(Ki[i], 2.5)
        Ei25[i] = math.pow(Ei[i], 2.5)

    for i in range(1, MaxFlds + 1):
        for j in range(1, MaxFlds + 1):
            for n in range(1, 18 + 1):
                Bsnij = 1  # initialise Bs_nij @ 1
                if gn[n] == 1:
                    Bsnij = Gij[i][j] * (Gi[i] + Gi[j]) / 2
                if qn[n] == 1:
                    Bsnij = Bsnij * Qi[i] * Qi[j]
                if fn[n] == 1:
                    Bsnij = Bsnij * Fi[i] * Fi[j]
                if sn[n] == 1:
                    Bsnij = Bsnij * Si[i] * Si[j]
                if wn[n] == 1:
                    Bsnij = Bsnij * Wi[i] * Wi[j]

                Bsnij2[i][j][n] = (
                    an[n]
                    * math.pow(Eij[i][j] * math.sqrt(Ei[i] * Ei[j]), un[n])
                    * math.pow(Ki[i] * Ki[j], 1.5)
                    * Bsnij
                )

            Kij5[i][j] = (math.pow(Kij[i][j], 5) - 1) * Ki25[i] * Ki25[j]
            Uij5[i][j] = (math.pow(Uij[i][j], 5) - 1) * Ei25[i] * Ei25[j]
            Gij5[i][j] = (Gij[i][j] - 1) * (Gi[i] + Gi[j]) / 2

    # Ideal gas terms
    d0 = 101.325 / R / 298.15  # P=100(bar), T=25(DegC)

    for i in range(1, MaxFlds + 1):
        n0i[i][3] = n0i[i][3] - 1
        n0i[i][1] = n0i[i][1] - math.log(d0)

    Csn = initialise_Csn(NTerms)
    Tun = initialise_Tun(NTerms)


def MolarMassDetail(x: list, MmDetail: dict):
    """Calculate the molar mass using: M = Σ mi * xi where,
    xi = Mole fraction of ith component in gas mixture
    mi = Molar mass of ith component
    i = 21 (gas components)

    Updates the global variable MM.
    """
    global MM
    for xi in x:
        MM += xi[0] * MmDetail[xi[1]]


def xTermsDetail(x):
    """Calculate all of the variables related to the input gas composition."""
    global K3, U, Ei25, G, Gi, Q, Qi, F, Fi, Bs, Bsnij2, Kij5, Uij5, Gij5, Q2, Csn, gn, qn, fn

    # Calculate pure fluid contributions
    for i in range(1, NcDetail + 1):
        if x[i] > 0:
            xi2 = math.pow(x[i], 2)
            K3 += (
                x[i] * Ki25[i]
            )  # K, U, and G are the sums of a pure fluid contribution and a
            U += x[i] * Ei25[i]  # binary pair contribution
            G += x[i] * Gi[i]
            Q += x[i] * Qi[i]  # Q and F depend only on the pure fluid parts
            F += xi2 * Fi[i]

            for n in range(1, 18 + 1):
                Bs[n] = (
                    Bs[n] + xi2 * Bsnij2[i][i][n]
                )  #  Pure fluid contributions to second virial coefficient

    K3 = math.pow(K3, 2)
    U = math.pow(U, 2)

    # Binary pair contributions
    for i in range(1, NcDetail + 1):
        if x[i] > 0:
            for j in range(i + 1, NcDetail + 1):
                if x[j] > 0:
                    xij = 2 * x[i] * x[j]
                    K3 += xij * Kij5[i][j]
                    U += xij * Uij5[i][j]
                    G += xij * Gij5[i][j]

                    for n in range(1, 18 + 1):
                        Bs[n] = (
                            Bs[n] + xij * Bsnij2[i][j][n]
                        )  # Second virial coefficients of mixture

    K3 = math.pow(K3, 0.6)
    U = math.pow(U, 0.2)

    # Third virial and higher coefficients
    Q2 = math.pow(Q, 2)

    for n in range(13, NTerms + 1):
        Csn[n] = an[n] * math.pow(U, un[n])
        if gn[n] == 1:
            Csn[n] = Csn[n] * G
        if qn[n] == 1:
            Csn[n] = Csn[n] * Q2
        if fn[n] == 1:
            Csn[n] = Csn[n] * F


def AlphaRDetail(T, itau):
    """Calculate the derivatives of the residual Helmholtz energy (ar) with respect to T and D.

    Return ar array containing the derivatives.
    """
    global un, Told, Tun, K3, D, Bs, Csn, kn

    ar = [[0 for _ in range(4)] for _ in range(4)]  # reset ar @ 0

    if np.abs(T - Told) > 0.0000001:
        for n in range(1, NTerms + 1):
            Tun[n] = math.pow(T, -un[n])

    Told = T

    # Precalculation of common powers and exponents of density
    Dred = K3 * D
    Dknn = [0] * (9 + 1)  # create a an array Dknn (10, 1)
    Dknn[0] = 1
    for n in range(1, len(Dknn)):
        Dknn[n] = Dred * Dknn[n - 1]

    Expn = [0] * (5)  # create an array (5, 1) for exponents
    Expn[0] = 1
    for n in range(1, len(Expn)):
        Expn[n] = math.exp(-1 * Dknn[n])

    # initialise arrays
    Sum0 = [0] * (NTerms + 1)
    SumB = [0] * (NTerms + 1)
    CoefD1 = [0] * (NTerms + 1)
    CoefD2 = [0] * (NTerms + 1)
    CoefD3 = [0] * (NTerms + 1)
    CoefT1 = [0] * (NTerms + 1)
    CoefT2 = [0] * (NTerms + 1)

    for n in range(1, NTerms + 1):
        # Contributions to the Helmholtz energy and its derivatives with respect to temperature
        CoefT1[n] = R * (un[n] - 1)
        CoefT2[n] = CoefT1[n] * un[n]

        # Contributions to the virial coefficients
        SumB[n] = 0
        Sum0[n] = 0

        if n <= 18:
            Sum = Bs[n] * D
            if n >= 13:
                Sum += -Csn[n] * Dred
            SumB[n] = Sum * Tun[n]

        if n >= 13:
            # Contributions to the residual part of the Helmholtz energy
            Sum0[n] = Csn[n] * Dknn[int(bn[n])] * Tun[n] * Expn[int(kn[n])]

            # Contributions to the derivatives of the Helmholtz energy with respect to density
            bkd = bn[n] - kn[n] * Dknn[int(kn[n])]
            ckd = kn[n] * kn[n] * Dknn[int(kn[n])]
            CoefD1[n] = bkd
            CoefD2[n] = bkd * (bkd - 1) - ckd
            CoefD3[n] = (bkd - 2) * CoefD2[n] + ckd * (1 - kn[n] - 2 * bkd)

        else:
            CoefD1[n] = 0
            CoefD2[n] = 0
            CoefD3[n] = 0

    for n in range(1, NTerms + 1):
        # Density derivatives
        s0 = Sum0[n] + SumB[n]
        s1 = Sum0[n] * CoefD1[n] + SumB[n]
        s2 = Sum0[n] * CoefD2[n]
        s3 = Sum0[n] * CoefD3[n]
        ar[0][0] = ar[0][0] + (R * T) * s0
        ar[0][1] = ar[0][1] + (R * T) * s1
        ar[0][2] = ar[0][2] + (R * T) * s2
        ar[0][3] = ar[0][3] + (R * T) * s3

        # Temperature derivatives
        if itau > 0:
            ar[1][0] = ar[1][0] - CoefT1[n] * s0
            ar[1][1] = ar[1][1] - CoefT1[n] * s1
            ar[2][0] = ar[2][0] + CoefT2[n] * s0

    return ar


def PressureDetail(T):
    """Calculate pressure as a function of temperature and density.  The derivative d(P)/d(D) is also calculated."""
    global dPdDsave, D

    ar = AlphaRDetail(T, itau=0)
    Z = (
        1 + ar[0][1] / R / T
    )  # ar[0][1] is the first derivative of alpha(r) with respect to density
    P2 = D * R * T * Z
    dPdDsave = R * T + 2 * ar[0][1] + ar[0][2]  # d(P)/d(D) for use in density iteration

    return Z, P2


def DensityDetail(P, T):
    """Calculate density as a function of temperature, T and pressure, P. This is an iterative routine that calls PressureDetail()."""
    global P2, D

    if np.abs(P) < epsilon:
        D = 0
        return -1, -1, D, ierr, herr

    # initial density estimates
    if D > ((-1) * epsilon):
        D = P / R / T  # start with Ideal gas estimate

    else:
        D = abs(D)  # If D<0 then use asbolute value (itself) as initial estimate

    plog = math.log(P)
    vlog = (-1) * math.log(D)

    for it in range(1, 20 + 1):
        if (vlog < -7) | (vlog > 100):
            # fail to converge
            D = P / R / T  # return ideal gas estimate
            ierr = 1
            herr = "Calculation failed to converge in DETAIL method, ideal gas density returned."

            return -1, -1, D, ierr, herr

        D = math.exp(-vlog)

        # run pressure calculations
        Z, P2 = PressureDetail(T)

        if (dPdDsave < epsilon) | (P2 < epsilon):
            vlog += 0.1
        else:
            # Find the next density with a first order Newton's type iterative scheme, with
            # log(P) as the known variable and log(v) as the unknown property.
            dpdlv = -D * dPdDsave  # d(p)/d[log(v)]
            vdiff = (math.log(P2) - plog) * P2 / dpdlv
            vlog = vlog - vdiff
            if np.abs(vdiff) < tolr:
                # iteration converged
                D = math.exp(-vlog)
                ierr = 0
                herr = ""

                return Z, P2, D, ierr, herr

    # failed to converge (reset D back to ideal gas density)
    D = P / R / T
    ierr = 1
    herr = (
        "Calculation failed to converge in DETAIL method, ideal gas density returned."
    )

    return -1, -1, D, ierr, herr


def AGA8Detail(x, P, T):
    """Wrapper function to call the AGA8 DETAIL method for a given P, T and x.

    Input P needs to be in units Kpa.
    Input T needs to be in units K.

    """
    # 1. Initialise constants and parameters for DETAIL
    SetupDetail()

    # 2. Calculate the molar mass from the input gas composition
    MolarMassDetail(x=list(zip(x[1:], list(MmDetail.keys()))), MmDetail=MmDetail)

    # 3. Calculate terms dependent only on gas composition (only need to run once as gas comp doesn't change)
    xTermsDetail(x)

    # 4. Calculate density as a function of temperature and pressure and return approximated P and compressibility factor, Z
    Z, P2, D, ierr, herr = DensityDetail(P, T)

    return Z, P2, D, ierr, herr

"""AGA8Detail.py module contains the functionality used in the DETAIL method."""

import math

import numpy as np

from modules.initialise import (initialise_an, initialise_bn, initialise_Bs,
                                initialise_Bsnij2, initialise_Csn,
                                initialise_Ei, initialise_Fi, initialise_fn,
                                initialise_Gi, initialise_gn,
                                initialise_i25_arrays, initialise_ij5_arrays,
                                initialise_ij_arrays, initialise_Ki,
                                initialise_kn, initialise_n0i, initialise_Qi,
                                initialise_qn, initialise_Si, initialise_sn,
                                initialise_th0i, initialise_Tun, initialise_un,
                                initialise_Wi, initialise_wn)
from modules.molecule import MmDetail


class AGA8Detail:
    """Class to approximate the compressibility factor, Z for a gas given its composition x, Pressure, P and temperature, T using AGA8 Detail method."""

    def __init__(self, P, T, x):
        """Initialisation."""
        # constant terms
        self.NTerms = 58
        self.NcDetail = 21
        self.MaxFlds = 21
        self.epsilon = 1e-15
        self.tolr = 0.0000001
        self.R = 8.31451
        self.itau = 0
        self.MmDetail = MmDetail

        # inputs
        self.P = P
        self.T = T
        self.x = x

        # outputs
        self.P2 = 0
        self.Z = None
        self.D = 1e10

        # dynamic terms
        self.ar = None
        self.dPdDsave = None
        self.MM = 0
        self.K3 = 0
        self.U = 0
        self.G = 0
        self.F = 0
        self.Q = 0
        self.Told = 0
        self.Q2 = None

        # initialise arrays
        self.Bs = initialise_Bs()
        self.Bsnij2 = initialise_Bsnij2(n=self.MaxFlds)
        self.an = initialise_an(n=self.NTerms)
        self.bn = initialise_bn(n=self.NTerms)
        self.kn = initialise_kn(n=self.NTerms)
        self.un = initialise_un(n=self.NTerms)
        self.fn = initialise_fn(n=self.NTerms)
        self.gn = initialise_gn(n=self.NTerms)
        self.qn = initialise_qn(n=self.NTerms)
        self.sn = initialise_sn(n=self.NTerms)
        self.wn = initialise_wn(n=self.NTerms)
        self.Ei = initialise_Ei(n=self.MaxFlds)  # energy params
        self.Ki = initialise_Ki(n=self.MaxFlds)  # size params
        self.Gi = initialise_Gi(n=self.MaxFlds)  # orientation params
        self.Eij, self.Uij, self.Kij, self.Gij = initialise_ij_arrays(n=self.MaxFlds)
        # quadrupole params
        self.Qi = initialise_Qi(n=self.MaxFlds)
        self.Fi = initialise_Fi(n=self.MaxFlds)
        self.Si = initialise_Si(n=self.MaxFlds)
        self.Wi = initialise_Wi(n=self.MaxFlds)
        # ideal gas params
        self.n0i = initialise_n0i(n=self.MaxFlds)
        self.th0i = initialise_th0i(n=self.MaxFlds)
        # precalculation of constants
        self.Ki25, self.Ei25 = initialise_i25_arrays(n=self.MaxFlds)
        self.Kij5, self.Uij5, self.Gij5 = initialise_ij5_arrays(n=self.MaxFlds)
        self.Csn = initialise_Csn(n=self.NTerms)
        self.Tun = initialise_Tun(n=self.NTerms)

    def SetupDetail(self):
        """Initialize all the constants and parameters in the DETAIL model."""
        for i in range(1, self.MaxFlds + 1):
            self.Ki25[i] = math.pow(self.Ki[i], 2.5)
            self.Ei25[i] = math.pow(self.Ei[i], 2.5)

        for i in range(1, self.MaxFlds + 1):
            for j in range(1, self.MaxFlds + 1):
                for n in range(1, 18 + 1):
                    Bsnij = 1  # initialise Bs_nij @ 1
                    if self.gn[n] == 1:
                        Bsnij = self.Gij[i][j] * (self.Gi[i] + self.Gi[j]) / 2
                    if self.qn[n] == 1:
                        Bsnij = Bsnij * self.Qi[i] * self.Qi[j]
                    if self.fn[n] == 1:
                        Bsnij = Bsnij * self.Fi[i] * self.Fi[j]
                    if self.sn[n] == 1:
                        Bsnij = Bsnij * self.Si[i] * self.Si[j]
                    if self.wn[n] == 1:
                        Bsnij = Bsnij * self.Wi[i] * self.Wi[j]

                    self.Bsnij2[i][j][n] = (
                        self.an[n]
                        * math.pow(
                            self.Eij[i][j] * math.sqrt(self.Ei[i] * self.Ei[j]),
                            self.un[n],
                        )
                        * math.pow(self.Ki[i] * self.Ki[j], 1.5)
                        * Bsnij
                    )

                self.Kij5[i][j] = (
                    (math.pow(self.Kij[i][j], 5) - 1) * self.Ki25[i] * self.Ki25[j]
                )
                self.Uij5[i][j] = (
                    (math.pow(self.Uij[i][j], 5) - 1) * self.Ei25[i] * self.Ei25[j]
                )
                self.Gij5[i][j] = (self.Gij[i][j] - 1) * (self.Gi[i] + self.Gi[j]) / 2

        # Ideal gas terms
        d0 = 101.325 / self.R / 298.15  # P=100(bar), T=25(DegC)

        for i in range(1, self.MaxFlds + 1):
            self.n0i[i][3] = self.n0i[i][3] - 1
            self.n0i[i][1] = self.n0i[i][1] - math.log(d0)

        return self

    def MolarMassDetail(self):
        """Calculate the M using (M = Σ mi * xi) where xi = mole fraction of ith component in gas mixture and mi = molar mass of ith component."""
        for xi in list(
            zip(self.x[1:], self.MmDetail.keys())
        ):  # [:1] to avoid considering dummy 0 at index 0 in list
            self.MM += xi[0] * self.MmDetail[xi[1]]

        return self

    def xTermsDetail(self):
        """Calculate all of the variables related to the input gas composition."""
        # Calculate pure fluid contributions
        for i in range(1, self.NcDetail + 1):
            if self.x[i] > 0:
                xi2 = math.pow(self.x[i], 2)
                self.K3 += (
                    self.x[i] * self.Ki25[i]
                )  # K, U, and G are the sums of a pure fluid contribution and a
                self.U += self.x[i] * self.Ei25[i]  # binary pair contribution
                self.G += self.x[i] * self.Gi[i]
                self.Q += (
                    self.x[i] * self.Qi[i]
                )  # Q and F depend only on the pure fluid parts
                self.F += xi2 * self.Fi[i]

                for n in range(1, 18 + 1):
                    self.Bs[n] = (
                        self.Bs[n] + xi2 * self.Bsnij2[i][i][n]
                    )  # Pure fluid contributions to second virial coefficient

        self.K3 = math.pow(self.K3, 2)
        self.U = math.pow(self.U, 2)

        # Binary pair contributions
        for i in range(1, self.NcDetail + 1):
            if self.x[i] > 0:
                for j in range(i + 1, self.NcDetail + 1):
                    if self.x[j] > 0:
                        xij = 2 * self.x[i] * self.x[j]
                        self.K3 += xij * self.Kij5[i][j]
                        self.U += xij * self.Uij5[i][j]
                        self.G += xij * self.Gij5[i][j]

                        for n in range(1, 18 + 1):
                            self.Bs[n] = (
                                self.Bs[n] + xij * self.Bsnij2[i][j][n]
                            )  # Second virial coefficients of mixture

        self.K3 = math.pow(self.K3, 0.6)
        self.U = math.pow(self.U, 0.2)

        # Third virial and higher coefficients
        self.Q2 = math.pow(self.Q, 2)

        for n in range(13, self.NTerms + 1):
            self.Csn[n] = self.an[n] * math.pow(self.U, self.un[n])
            if self.gn[n] == 1:
                self.Csn[n] = self.Csn[n] * self.G
            if self.qn[n] == 1:
                self.Csn[n] = self.Csn[n] * self.Q2
            if self.fn[n] == 1:
                self.Csn[n] = self.Csn[n] * self.F

        return self

    def AlphaRDetail(self):
        """Calculate the derivatives of the residual Helmholtz energy (ar) with respect to T and D."""
        # reset ar @ 0 each call
        self.ar = [[0 for _ in range(4)] for _ in range(4)]

        if np.abs(self.T - self.Told) > 0.0000001:
            for n in range(1, self.NTerms + 1):
                self.Tun[n] = math.pow(self.T, (-1) * self.un[n])

        self.Told = self.T

        # Precalculation of common powers and exponents of density
        Dred = self.K3 * self.D
        Dknn = [0] * (9 + 1)  # create a an array Dknn (10, 1)
        Dknn[0] = 1
        for n in range(1, len(Dknn)):
            Dknn[n] = Dred * Dknn[n - 1]

        Expn = [0] * (5)  # create an array (5, 1) for exponents
        Expn[0] = 1
        for n in range(1, len(Expn)):
            Expn[n] = math.exp(-1 * Dknn[n])

        Sum0 = [0] * (self.NTerms + 1)
        SumB = [0] * (self.NTerms + 1)
        CoefD1 = [0] * (self.NTerms + 1)
        CoefD2 = [0] * (self.NTerms + 1)
        CoefD3 = [0] * (self.NTerms + 1)
        CoefT1 = [0] * (self.NTerms + 1)
        CoefT2 = [0] * (self.NTerms + 1)

        for n in range(1, self.NTerms + 1):
            # Contributions to the Helmholtz energy and its derivatives with respect to temperature
            CoefT1[n] = self.R * (self.un[n] - 1)
            CoefT2[n] = CoefT1[n] * self.un[n]
            # Contributions to the virial coefficients
            SumB[n] = 0
            Sum0[n] = 0

            if n <= 18:
                Sum = self.Bs[n] * self.D
                if n >= 13:
                    Sum += (-1) * self.Csn[n] * Dred
                SumB[n] = Sum * self.Tun[n]

            if n >= 13:
                # Contributions to the residual part of the Helmholtz energy
                Sum0[n] = (
                    self.Csn[n]
                    * Dknn[int(self.bn[n])]
                    * self.Tun[n]
                    * Expn[int(self.kn[n])]
                )

                # Contributions to the derivatives of the Helmholtz energy with respect to density
                bkd = self.bn[n] - self.kn[n] * Dknn[int(self.kn[n])]
                ckd = self.kn[n] * self.kn[n] * Dknn[int(self.kn[n])]
                CoefD1[n] = bkd
                CoefD2[n] = bkd * (bkd - 1) - ckd
                CoefD3[n] = (bkd - 2) * CoefD2[n] + ckd * (1 - self.kn[n] - 2 * bkd)

            else:
                CoefD1[n] = 0
                CoefD2[n] = 0
                CoefD3[n] = 0

        for n in range(1, self.NTerms + 1):
            # Density derivatives
            s0 = Sum0[n] + SumB[n]
            s1 = Sum0[n] * CoefD1[n] + SumB[n]
            s2 = Sum0[n] * CoefD2[n]
            s3 = Sum0[n] * CoefD3[n]
            self.ar[0][0] = self.ar[0][0] + (self.R * self.T) * s0
            self.ar[0][1] = self.ar[0][1] + (self.R * self.T) * s1
            self.ar[0][2] = self.ar[0][2] + (self.R * self.T) * s2
            self.ar[0][3] = self.ar[0][3] + (self.R * self.T) * s3

        return self

    def PressureDetail(self):
        """Calculate pressure as a function of temperature and density.  The derivative d(P)/d(D) is also calculated."""
        self.AlphaRDetail()  # updates ar with new density, D
        self.Z = (
            1 + self.ar[0][1] / self.R / self.T
        )  # ar[0][1] is the first derivative of alpha(r) with respect to density
        self.P2 = self.D * self.R * self.T * self.Z
        self.dPdDsave = (
            self.R * self.T + 2 * self.ar[0][1] + self.ar[0][2]
        )  # d(P)/d(D) for use in density iteration

        return self

    def DensityDetail(self):
        """Calculate density as a function of temperature, T and pressure, P. This is an iterative routine that calls PressureDetail()."""
        if np.abs(self.P) < self.epsilon:
            # failed to converge
            self.Z = None
            self.P2 = None
            self.D = 0
            self.ierr = 1
            self.herr = "Calculation failed to converge in DETAIL method, ideal gas density returned."

            return self

        # initial density estimates
        if self.D > ((-1) * self.epsilon):
            self.D = self.P / self.R / self.T  # start with Ideal gas estimate

        else:
            self.D = abs(
                self.D
            )  # If D<0 then use asbolute value (itself) as initial estimate

        plog = math.log(self.P)
        vlog = (-1) * math.log(self.D)

        for _ in range(1, 20 + 1):
            if (vlog < -7) | (vlog > 100):
                # fail to converge
                self.Z = None
                self.P2 = None
                self.D = self.P / self.R / self.T  # return ideal gas estimate
                self.ierr = 1
                self.herr = "Calculation failed to converge in DETAIL method, ideal gas density returned."

                return self

            self.D = math.exp(-vlog)  # update the density

            # run pressure calculations
            self.PressureDetail()

            if (self.dPdDsave < self.epsilon) | (self.P2 < self.epsilon):
                vlog += 0.1
            else:
                # Find the next density with a first order Newton's type iterative scheme, with
                # log(P) as the known variable and log(v) as the unknown property.
                dpdlv = -self.D * self.dPdDsave  # d(p)/d[log(v)]
                vdiff = (math.log(self.P2) - plog) * self.P2 / dpdlv
                vlog = vlog - vdiff
                if np.abs(vdiff) < self.tolr:
                    # iteration converged
                    self.D = math.exp(-vlog)
                    self.ierr = 0
                    self.herr = ""

                    return self

        # failed to converge (reset D back to ideal gas density)
        self.Z = None
        self.P2 = None
        self.D = self.P / self.R / self.T
        self.ierr = 1
        self.herr = "Calculation failed to converge in DETAIL method, ideal gas density returned."

        return self

    def run(self):
        """Call the AGA8 DETAIL method for a given P, T and x."""
        # 1. Initialise constants and parameters for DETAIL
        self.SetupDetail()
        # 2. Calculate the molar mass from the input gas composition
        self.MolarMassDetail()
        # 3. Calculate terms dependent only on gas composition (only need to run once as gas comp doesn't change)
        self.xTermsDetail()
        # 4. Calculate density as a function of temperature and pressure and return approximated P and compressibility factor, Z
        self.DensityDetail()

        return self

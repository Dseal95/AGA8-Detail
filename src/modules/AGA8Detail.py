"""AGA8Detail.py module contains the functionality used in the DETAIL method."""

import math

from modules.initialise import (
    initialise_an,
    initialise_bn,
    initialise_bs,
    initialise_bsnij2,
    initialise_csn,
    initialise_ei,
    initialise_fi,
    initialise_fn,
    initialise_gi,
    initialise_gn,
    initialise_i25_arrays,
    initialise_ij5_arrays,
    initialise_ij_arrays,
    initialise_ki,
    initialise_kn,
    initialise_n0i,
    initialise_qi,
    initialise_qn,
    initialise_si,
    initialise_sn,
    initialise_th0i,
    initialise_tun,
    initialise_un,
    initialise_wi,
    initialise_wn,
)
from modules.molecule import MmDetail

import numpy as np


class AGA8Detail:
    """Class to approximate the compressibility factor, Z for a gas given its composition x, Pressure, P and temperature, T using AGA8 Detail method."""

    def __init__(self, p, t, x):
        """Initialisation."""
        # constant terms
        self.nterms = 58
        self.ncdetail = 21
        self.maxflds = 21
        self.epsilon = 1e-15
        self.tolr = 0.0000001
        self.R = 8.31451
        self.itau = 0
        self.mmdetail = MmDetail

        # inputs
        self.P = p  # raw initial P (kPa)
        self.T = t  # raw inital T (K)
        self.x = x

        # outputs
        self.P2 = 0  # approximated P from DensityDetail() (Kpa)
        self.P3 = 0  # approximated P from PropertiesDetail() (Kpa)
        self.z = None  # (no units)
        self.zd = None  # (no units)
        self.D = 1e10  # molar density (mol/l)
        self.MM = 0  # Molar Mass (g/mol)
        self.ar = None
        self.dpddsave = None  # d(P)/d(D) (kPa/(mol/l)) (at constant temperature)
        self.K3 = 0
        self.F = 0
        self.Q = 0
        self.told = 0  # (K)
        self.Q2 = None
        self.dpdd = 0  # kPa/(mol/l)
        self.dpdd2 = 0  # kPa/(mol/l)^2
        self.dpdt = 0  # kPa/K
        self.A = 0
        self.U = 0  # Energy (J/mol)
        self.H = 0  # Enthalpy (J/mol)
        self.S = 0  # Entropy (Jmol-1K-1)
        self.cv = 0  # Isochoric heat capacity (Jmol-1K-1)
        self.cp = 0  # Isobaric heat capacity (Jmol-1-K-1)
        self.d2pdd2 = 0
        self.d2pdtd = 0
        self.W = 0  # Speed of sound (m/s)
        self.G = 0  # Gibbs energy (J/mol)
        self.JT = 0  # Joule-Thomson coefficient (K/kPa)
        self.kappa = 0  # Isentropic exponent

        # initialise arrays
        self.bs = initialise_bs()
        self.bsnij2 = initialise_bsnij2(n=self.maxflds)
        self.an = initialise_an(n=self.nterms)
        self.bn = initialise_bn(n=self.nterms)
        self.kn = initialise_kn(n=self.nterms)
        self.un = initialise_un(n=self.nterms)
        self.fn = initialise_fn(n=self.nterms)
        self.gn = initialise_gn(n=self.nterms)
        self.qn = initialise_qn(n=self.nterms)
        self.sn = initialise_sn(n=self.nterms)
        self.wn = initialise_wn(n=self.nterms)
        self.ei = initialise_ei(n=self.maxflds)  # energy params
        self.ki = initialise_ki(n=self.maxflds)  # size params
        self.gi = initialise_gi(n=self.maxflds)  # orientation params
        self.eij, self.uij, self.kij, self.gij = initialise_ij_arrays(n=self.maxflds)
        # quadrupole params
        self.qi = initialise_qi(n=self.maxflds)
        self.fi = initialise_fi(n=self.maxflds)
        self.si = initialise_si(n=self.maxflds)
        self.wi = initialise_wi(n=self.maxflds)
        # ideal gas params
        self.n0i = initialise_n0i(n=self.maxflds)
        self.th0i = initialise_th0i(n=self.maxflds)
        # precalculation of constants
        self.ki25, self.ei25 = initialise_i25_arrays(n=self.maxflds)
        self.kij5, self.uij5, self.gij5 = initialise_ij5_arrays(n=self.maxflds)
        self.csn = initialise_csn(n=self.nterms)
        self.tun = initialise_tun(n=self.nterms)

    def setup_detail(self):
        """Initialize all the constants and parameters in the DETAIL model."""
        for i in range(1, self.maxflds + 1):
            self.ki25[i] = math.pow(self.ki[i], 2.5)
            self.ei25[i] = math.pow(self.ei[i], 2.5)

        for i in range(1, self.maxflds + 1):
            for j in range(1, self.maxflds + 1):
                for n in range(1, 18 + 1):
                    bsnij = 1  # initialise Bs_nij @ 1
                    if self.gn[n] == 1:
                        bsnij = self.gij[i][j] * (self.gi[i] + self.gi[j]) / 2
                    if self.qn[n] == 1:
                        bsnij = bsnij * self.qi[i] * self.qi[j]
                    if self.fn[n] == 1:
                        bsnij = bsnij * self.fi[i] * self.fi[j]
                    if self.sn[n] == 1:
                        bsnij = bsnij * self.si[i] * self.si[j]
                    if self.wn[n] == 1:
                        bsnij = bsnij * self.wi[i] * self.wi[j]

                    self.bsnij2[i][j][n] = (
                        self.an[n]
                        * math.pow(
                            self.eij[i][j] * math.sqrt(self.ei[i] * self.ei[j]),
                            self.un[n],
                        )
                        * math.pow(self.ki[i] * self.ki[j], 1.5)
                        * bsnij
                    )

                self.kij5[i][j] = (
                    (math.pow(self.kij[i][j], 5) - 1) * self.ki25[i] * self.ki25[j]
                )
                self.uij5[i][j] = (
                    (math.pow(self.uij[i][j], 5) - 1) * self.ei25[i] * self.ei25[j]
                )
                self.gij5[i][j] = (self.gij[i][j] - 1) * (self.gi[i] + self.gi[j]) / 2

        # Ideal gas terms
        d0 = 101.325 / self.R / 298.15

        for i in range(1, self.maxflds + 1):
            self.n0i[i][3] = self.n0i[i][3] - 1
            self.n0i[i][1] = self.n0i[i][1] - math.log(d0)

        return self

    def molar_mass_detail(self):
        """Calculate the M using (M = Σ mi * xi) where xi = mole fraction of ith component in gas mixture and mi = molar mass of ith component."""
        for xi in list(
            zip(self.x[1:], self.mmdetail.keys())
        ):  # [:1] to avoid considering dummy 0 at index 0 in list
            self.MM += xi[0] * self.mmdetail[xi[1]]

        return self

    def x_terms_detail(self):
        """Calculate all of the variables related to the input gas composition."""
        # Calculate pure fluid contributions
        for i in range(1, self.ncdetail + 1):
            if self.x[i] > 0:
                xi2 = math.pow(self.x[i], 2)
                self.K3 += (
                    self.x[i] * self.ki25[i]
                )  # K, U, and G are the sums of a pure fluid contribution and a
                self.U += self.x[i] * self.ei25[i]  # binary pair contribution
                self.G += self.x[i] * self.gi[i]
                self.Q += (
                    self.x[i] * self.qi[i]
                )  # Q and F depend only on the pure fluid parts
                self.F += xi2 * self.fi[i]

                for n in range(1, 18 + 1):
                    self.bs[n] = (
                        self.bs[n] + xi2 * self.bsnij2[i][i][n]
                    )  # Pure fluid contributions to second virial coefficient

        self.K3 = math.pow(self.K3, 2)
        self.U = math.pow(self.U, 2)

        # Binary pair contributions
        for i in range(1, self.ncdetail + 1):
            if self.x[i] > 0:
                for j in range(i + 1, self.ncdetail + 1):
                    if self.x[j] > 0:
                        xij = 2 * self.x[i] * self.x[j]
                        self.K3 += xij * self.kij5[i][j]
                        self.U += xij * self.uij5[i][j]
                        self.G += xij * self.gij5[i][j]

                        for n in range(1, 18 + 1):
                            self.bs[n] = (
                                self.bs[n] + xij * self.bsnij2[i][j][n]
                            )  # Second virial coefficients of mixture

        self.K3 = math.pow(self.K3, 0.6)
        self.U = math.pow(self.U, 0.2)

        # Third virial and higher coefficients
        self.Q2 = math.pow(self.Q, 2)

        for n in range(13, self.nterms + 1):
            self.csn[n] = self.an[n] * math.pow(self.U, self.un[n])
            if self.gn[n] == 1:
                self.csn[n] = self.csn[n] * self.G
            if self.qn[n] == 1:
                self.csn[n] = self.csn[n] * self.Q2
            if self.fn[n] == 1:
                self.csn[n] = self.csn[n] * self.F

        return self

    def alpha_r_detail(self, itau):
        """Calculate the derivatives of the residual Helmholtz energy (ar) with respect to T and D.

        Arguments:
            itau: highest derivatives needed. Set to 1 for "ar" derivatives w.r.t T, 0 otherwise.
        """
        # reset ar @ 0 each call
        self.ar = [[0 for _ in range(4)] for _ in range(4)]

        if np.abs(self.T - self.told) > 0.0000001:
            for n in range(1, self.nterms + 1):
                self.tun[n] = math.pow(self.T, (-1) * self.un[n])

        self.told = self.T

        # Precalculation of common powers and exponents of density
        dred = self.K3 * self.D
        dknn = [0] * (9 + 1)  # create a an array Dknn (10, 1)
        dknn[0] = 1
        for n in range(1, len(dknn)):
            dknn[n] = dred * dknn[n - 1]

        expn = [0] * (5)  # create an array (5, 1) for exponents
        expn[0] = 1
        for n in range(1, len(expn)):
            expn[n] = math.exp(-1 * dknn[n])

        sum0 = [0] * (self.nterms + 1)
        sumb = [0] * (self.nterms + 1)
        coefd1 = [0] * (self.nterms + 1)
        coefd2 = [0] * (self.nterms + 1)
        coefd3 = [0] * (self.nterms + 1)
        coeft1 = [0] * (self.nterms + 1)
        coeft2 = [0] * (self.nterms + 1)

        for n in range(1, self.nterms + 1):
            # Contributions to the Helmholtz energy and its derivatives with respect to temperature
            coeft1[n] = self.R * (self.un[n] - 1)
            coeft2[n] = coeft1[n] * self.un[n]
            # Contributions to the virial coefficients
            sumb[n] = 0
            sum0[n] = 0

            if n <= 18:
                _sum = self.bs[n] * self.D
                if n >= 13:
                    _sum += (-1) * self.csn[n] * dred
                sumb[n] = _sum * self.tun[n]

            if n >= 13:
                # Contributions to the residual part of the Helmholtz energy
                sum0[n] = (
                    self.csn[n]
                    * dknn[int(self.bn[n])]
                    * self.tun[n]
                    * expn[int(self.kn[n])]
                )

                # Contributions to the derivatives of the Helmholtz energy with respect to density
                bkd = self.bn[n] - self.kn[n] * dknn[int(self.kn[n])]
                ckd = self.kn[n] * self.kn[n] * dknn[int(self.kn[n])]
                coefd1[n] = bkd
                coefd2[n] = bkd * (bkd - 1) - ckd
                coefd3[n] = (bkd - 2) * coefd2[n] + ckd * (1 - self.kn[n] - 2 * bkd)

            else:
                coefd1[n] = 0
                coefd2[n] = 0
                coefd3[n] = 0

        for n in range(1, self.nterms + 1):
            # Density derivatives
            s0 = sum0[n] + sumb[n]
            s1 = sum0[n] * coefd1[n] + sumb[n]
            s2 = sum0[n] * coefd2[n]
            s3 = sum0[n] * coefd3[n]
            self.ar[0][0] = self.ar[0][0] + (self.R * self.T) * s0
            self.ar[0][1] = self.ar[0][1] + (self.R * self.T) * s1
            self.ar[0][2] = self.ar[0][2] + (self.R * self.T) * s2
            self.ar[0][3] = self.ar[0][3] + (self.R * self.T) * s3

            # temperature derivatives
            if itau > 0:
                self.ar[1][0] = self.ar[1][0] - coeft1[n] * s0
                self.ar[1][1] = self.ar[1][1] - coeft1[n] * s1
                self.ar[2][0] = self.ar[2][0] + coeft2[n] * s0
                # The following are not used, but fully functional
                self.ar[1][2] = self.ar[1][2] - coeft1[n] * s2
                self.ar[1][3] = self.ar[1][3] - coeft1[n] * s3
                self.ar[2][1] = self.ar[2][1] + coeft2[n] * s1

        return self

    def alpha_0_detail(self):
        """Calculate the ideal gas Helmholtz energy and its derivatives with respect to T and D."""
        # reset ar @ 0 each call
        self.a0 = [0, 0, 0]

        if self.D > self.epsilon:
            logd = math.log(self.D)
        else:
            logd = math.log(self.epsilon)

        logt = math.log(self.T)

        for i in range(1, self.ncdetail + 1):
            if self.x[i] > 0:
                logxd = logd + math.log(self.x[i])
                sumhyp0 = 0
                sumhyp1 = 0
                sumhyp2 = 0

                for j in range(4, 8):
                    if self.th0i[i][j] > 0:
                        th0t = self.th0i[i][j] / self.T
                        ep = math.exp(th0t)
                        em = 1 / ep
                        hsn = (ep - em) / 2
                        hcn = (ep + em) / 2

                        if (j == 4) | (j == 6):
                            loghyp = math.log(abs(hsn))
                            sumhyp0 += self.n0i[i][j] * loghyp
                            sumhyp1 += self.n0i[i][j] * (loghyp - th0t * hcn / hsn)
                            sumhyp2 += self.n0i[i][j] * (th0t / hsn) ** 2
                        else:
                            loghyp = math.log(abs(hcn))
                            sumhyp0 += (-1) * self.n0i[i][j] * loghyp
                            sumhyp1 += (
                                (-1) * self.n0i[i][j] * (loghyp - th0t * hsn / hcn)
                            )
                            sumhyp2 += self.n0i[i][j] * (th0t / hcn) ** 2

                self.a0[0] += self.x[i] * (
                    logxd
                    + self.n0i[i][1]
                    + self.n0i[i][2] / self.T
                    - self.n0i[i][3] * logt
                    + sumhyp0
                )
                self.a0[1] += self.x[i] * (
                    logxd + self.n0i[i][1] - self.n0i[i][3] * (1 + logt) + sumhyp1
                )
                self.a0[2] += (-1) * self.x[i] * (self.n0i[i][3] + sumhyp2)

        self.a0[0] = self.a0[0] * self.R * self.T
        self.a0[1] = self.a0[1] * self.R
        self.a0[2] = self.a0[2] * self.R

        return self

    def pressure_detail(self):
        """Calculate pressure as a function of temperature and density.  The derivative d(P)/d(D) is also calculated."""
        self.alpha_r_detail(itau=0)  # updates ar with new density, D
        self.z = (
            1 + self.ar[0][1] / self.R / self.T
        )  # ar[0][1] is the first derivative of alpha(r) with respect to density
        self.P2 = self.D * self.R * self.T * self.z
        self.dpddsave = (
            self.R * self.T + 2 * self.ar[0][1] + self.ar[0][2]
        )  # d(P)/d(D) for use in density iteration

        return self

    def density_detail(self):
        """Calculate density as a function of temperature, T and pressure, P. This is an iterative routine that calls PressureDetail()."""
        if np.abs(self.P) < self.epsilon:
            # failed to converge
            self.z = None
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
                self.z = None
                self.P2 = None
                self.D = self.P / self.R / self.T  # return ideal gas estimate
                self.ierr = 1
                self.herr = "Calculation failed to converge in DETAIL method, ideal gas density returned."

                return self

            self.D = math.exp(-vlog)  # update the density

            # run pressure calculations
            self.pressure_detail()

            if (self.dpddsave < self.epsilon) | (self.P2 < self.epsilon):
                vlog += 0.1
            else:
                # Find the next density with a first order Newton's type iterative scheme, with
                # log(P) as the known variable and log(v) as the unknown property.
                dpdlv = -self.D * self.dpddsave  # d(p)/d[log(v)]
                vdiff = (math.log(self.P2) - plog) * self.P2 / dpdlv
                vlog = vlog - vdiff
                if np.abs(vdiff) < self.tolr:
                    # iteration converged
                    self.D = math.exp(-vlog)
                    self.ierr = 0
                    self.herr = ""

                    return self

        # failed to converge (reset D back to ideal gas density)
        self.z = None
        self.P2 = None
        self.D = self.P / self.R / self.T
        self.ierr = 1
        self.herr = "Calculation failed to converge in DETAIL method, ideal gas density returned."

        return self

    def properties_detail(self):
        """Calculate thermodynamic properties of as gas as a function of temperature and density.

        This method should be run after apprximating the gas density using DensityDetail().
        """
        if self.z is None:
            # density_detail() failed to converge, return object
            return self

        # Calculate the ideal gas Helmholtz energy, and its first and second derivatives with respect to temperature.
        self.alpha_0_detail()
        # Calculate the real gas Helmholtz energy, and its derivatives with respect to temperature and/or density.
        self.alpha_r_detail(itau=2)

        # store the Z approximated by DensityDetail approach
        self.zd = self.z
        # overwrite Z with the new Z from properties method
        self.z = 1 + self.ar[0][1] / (self.R * self.T)
        # create a new approximated P3 from new Z
        self.P3 = self.D * self.R * self.T * self.z

        self.dpdd = (self.R * self.T) + 2 * self.ar[0][1] + self.ar[0][2]
        self.dpdt = (self.D * self.R) + (self.D * self.ar[1][1])
        self.A = self.a0[0] + self.ar[0][0]
        self.S = (-1) * self.a0[1] - self.ar[1][0]
        self.U = self.A + self.T * self.S
        self.cv = -(self.a0[2] + self.ar[2][0])

        if self.D > self.epsilon:
            self.H = self.U + self.P3 / self.D
            self.G = self.A + self.P3 / self.D
            self.cp = self.cv + self.T * (self.dpdt / self.D) ** 2 / self.dpdd
            self.d2pdd2 = (
                2 * self.ar[0][1] + 4 * self.ar[0][2] + self.ar[0][3]
            ) / self.D
            self.JT = (self.T / self.D * self.dpdt / self.dpdd - 1) / self.cp / self.D
        else:
            self.H = self.U + (self.R * self.T)
            self.G = self.A + (self.R * self.T)
            self.cp = self.cv + self.R
            self.d2pdd2 = 0
            self.JT = 1e20

        self.W = 1000 * self.cp / self.cv * self.dpdd / self.MM
        if self.W < 0:
            self.W = 0  # force >= 0

        self.W = math.sqrt(self.W)
        self.kappa = self.W**2 * self.MM / ((self.R * self.T) * 1000 * self.z)

        return self

    def run(self):
        """Call the AGA8 DETAIL method for a given P, T and x."""
        # 1. Initialise constants and parameters for DETAIL
        self.setup_detail()
        # 2. Calculate the molar mass from the input gas composition
        self.molar_mass_detail()
        # 3. Calculate terms dependent only on gas composition (only need to run once as gas comp doesn't change)
        self.x_terms_detail()
        # 4. Calculate gas density as a function of temperature and pressure and return approximated P and compressibility factor, Z
        self.density_detail()
        # 5. Calculate gas thermodynamic properties of as gas as a function of temperature and density.
        self.properties_detail()

        return self

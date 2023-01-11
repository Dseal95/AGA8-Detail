"""Initialise.py module contains all functionality to initialise the parameters and constants used in the AGA8 DETAIL method."""


def initialise_an(n):
    """Initialise an(n+1, 1) array with known initial values."""
    an = [0] * (n + 1)
    # add initial values
    an[1] = 0.1538326
    an[2] = 1.341953
    an[3] = -2.998583
    an[4] = -0.04831228
    an[5] = 0.3757965
    an[6] = -1.589575
    an[7] = -0.05358847
    an[8] = 0.88659463
    an[9] = -0.71023704
    an[10] = -1.471722
    an[11] = 1.32185035
    an[12] = -0.78665925
    an[13] = 0.00000000229129
    an[14] = 0.1576724
    an[15] = -0.4363864
    an[16] = -0.04408159
    an[17] = -0.003433888
    an[18] = 0.03205905
    an[19] = 0.02487355
    an[20] = 0.07332279
    an[21] = -0.001600573
    an[22] = 0.6424706
    an[23] = -0.4162601
    an[24] = -0.06689957
    an[25] = 0.2791795
    an[26] = -0.6966051
    an[27] = -0.002860589
    an[28] = -0.008098836
    an[29] = 3.150547
    an[30] = 0.007224479
    an[31] = -0.7057529
    an[32] = 0.5349792
    an[33] = -0.07931491
    an[34] = -1.418465
    an[35] = -5.99905e-17
    an[36] = 0.1058402
    an[37] = 0.03431729
    an[38] = -0.007022847
    an[39] = 0.02495587
    an[40] = 0.04296818
    an[41] = 0.7465453
    an[42] = -0.2919613
    an[43] = 7.294616
    an[44] = -9.936757
    an[45] = -0.005399808
    an[46] = -0.2432567
    an[47] = 0.04987016
    an[48] = 0.003733797
    an[49] = 1.874951
    an[50] = 0.002168144
    an[51] = -0.6587164
    an[52] = 0.000205518
    an[53] = 0.009776195
    an[54] = -0.02048708
    an[55] = 0.01557322
    an[56] = 0.006862415
    an[57] = -0.001226752
    an[58] = 0.002850908

    return an


def initialise_bn(n):
    """Initialise bn(n+1, 1) array with known initial values."""
    bn = [0] * (n + 1)
    # add initial values
    bn[1] = 1
    bn[2] = 1
    bn[3] = 1
    bn[4] = 1
    bn[5] = 1
    bn[6] = 1
    bn[7] = 1
    bn[8] = 1
    bn[9] = 1
    bn[10] = 1
    bn[11] = 1
    bn[12] = 1
    bn[13] = 1
    bn[14] = 1
    bn[15] = 1
    bn[16] = 1
    bn[17] = 1
    bn[18] = 1
    bn[19] = 2
    bn[20] = 2
    bn[21] = 2
    bn[22] = 2
    bn[23] = 2
    bn[24] = 2
    bn[25] = 2
    bn[26] = 2
    bn[27] = 2
    bn[28] = 3
    bn[29] = 3
    bn[30] = 3
    bn[31] = 3
    bn[32] = 3
    bn[33] = 3
    bn[34] = 3
    bn[35] = 3
    bn[36] = 3
    bn[37] = 3
    bn[38] = 4
    bn[39] = 4
    bn[40] = 4
    bn[41] = 4
    bn[42] = 4
    bn[43] = 4
    bn[44] = 4
    bn[45] = 5
    bn[46] = 5
    bn[47] = 5
    bn[48] = 5
    bn[49] = 5
    bn[50] = 6
    bn[51] = 6
    bn[52] = 7
    bn[53] = 7
    bn[54] = 8
    bn[55] = 8
    bn[56] = 8
    bn[57] = 9
    bn[58] = 9

    return bn


def initialise_kn(n):
    """Initialise kn(n+1, 1) array with known initial values."""
    kn = [0] * (n + 1)
    # add initial values
    kn[13] = 3
    kn[14] = 2
    kn[15] = 2
    kn[16] = 2
    kn[17] = 4
    kn[18] = 4
    kn[21] = 2
    kn[22] = 2
    kn[23] = 2
    kn[24] = 4
    kn[25] = 4
    kn[26] = 4
    kn[27] = 4
    kn[29] = 1
    kn[30] = 1
    kn[31] = 2
    kn[32] = 2
    kn[33] = 3
    kn[34] = 3
    kn[35] = 4
    kn[36] = 4
    kn[37] = 4
    kn[40] = 2
    kn[41] = 2
    kn[42] = 2
    kn[43] = 4
    kn[44] = 4
    kn[46] = 2
    kn[47] = 2
    kn[48] = 4
    kn[49] = 4
    kn[51] = 2
    kn[53] = 2
    kn[54] = 1
    kn[55] = 2
    kn[56] = 2
    kn[57] = 2
    kn[58] = 2

    return kn


def initialise_un(n):
    """Initialise un(n+1, 1) array with known initial values."""
    un = [0] * (n + 1)
    # add initial values
    un[1] = 0
    un[2] = 0.5
    un[3] = 1
    un[4] = 3.5
    un[5] = -0.5
    un[6] = 4.5
    un[7] = 0.5
    un[8] = 7.5
    un[9] = 9.5
    un[10] = 6
    un[11] = 12
    un[12] = 12.5
    un[13] = -6
    un[14] = 2
    un[15] = 3
    un[16] = 2
    un[17] = 2
    un[18] = 11
    un[19] = -0.5
    un[20] = 0.5
    un[21] = 0
    un[22] = 4
    un[23] = 6
    un[24] = 21
    un[25] = 23
    un[26] = 22
    un[27] = -1
    un[28] = -0.5
    un[29] = 7
    un[30] = -1
    un[31] = 6
    un[32] = 4
    un[33] = 1
    un[34] = 9
    un[35] = -13
    un[36] = 21
    un[37] = 8
    un[38] = -0.5
    un[39] = 0
    un[40] = 2
    un[41] = 7
    un[42] = 9
    un[43] = 22
    un[44] = 23
    un[45] = 1
    un[46] = 9
    un[47] = 3
    un[48] = 8
    un[49] = 23
    un[50] = 1.5
    un[51] = 5
    un[52] = -0.5
    un[53] = 4
    un[54] = 7
    un[55] = 3
    un[56] = 0
    un[57] = 1
    un[58] = 0

    return un


def initialise_fn(n):
    """Initialise fn(n+1, 1) array with known initial values."""
    fn = [0] * (n + 1)
    fn[13] = 1
    fn[27] = 1
    fn[30] = 1
    fn[35] = 1

    return fn


def initialise_gn(n):
    """Initialise gn(n+1, 1) array with known initial values."""
    gn = [0] * (n + 1)
    # add initial values
    gn[5] = 1
    gn[6] = 1
    gn[25] = 1
    gn[29] = 1
    gn[32] = 1
    gn[33] = 1
    gn[34] = 1
    gn[51] = 1
    gn[54] = 1
    gn[56] = 1

    return gn


def initialise_qn(n):
    """Initialise qn(n+1, 1) array with known initial values."""
    qn = [0] * (n + 1)
    # add initial values
    qn[7] = 1
    qn[16] = 1
    qn[26] = 1
    qn[28] = 1
    qn[37] = 1
    qn[42] = 1
    qn[47] = 1
    qn[49] = 1
    qn[52] = 1
    qn[58] = 1

    return qn


def initialise_sn(n):
    """Initialise sn(n+1, 1) array with known initial values."""
    sn = [0] * (n + 1)
    # add initial values
    sn[8] = 1
    sn[9] = 1

    return sn


def initialise_wn(n):
    """Initialise wn(n+1, 1) array with known initial values."""
    wn = [0] * (n + 1)
    # add initial values
    wn[10] = 1
    wn[11] = 1
    wn[12] = 1

    return wn


def initialise_Ei(n):
    """Initialise Ei(n+1, 1) array with known initial values."""
    Ei = [0] * (n + 1)
    # add initial values
    Ei[1] = 151.3183
    Ei[2] = 99.73778
    Ei[3] = 241.9606
    Ei[4] = 244.1667
    Ei[5] = 298.1183
    Ei[6] = 324.0689
    Ei[7] = 337.6389
    Ei[8] = 365.5999
    Ei[9] = 370.6823
    Ei[10] = 402.636293
    Ei[11] = 427.72263
    Ei[12] = 450.325022
    Ei[13] = 470.840891
    Ei[14] = 489.558373
    Ei[15] = 26.95794
    Ei[16] = 122.7667
    Ei[17] = 105.5348
    Ei[18] = 514.0156
    Ei[19] = 296.355
    Ei[20] = 2.610111
    Ei[21] = 119.6299

    return Ei


def initialise_Fi(n):
    """Initialise Fi(n+1, 1) array with zeros."""
    Fi = [0] * (n + 1)
    # add initial values
    Fi[15] = 1  # high temperature parameter

    return Fi


def initialise_Gi(n):
    """Initialise Gi(n+1, 1) array with known initial values."""
    Gi = [0] * (n + 1)
    # add initial values
    Gi[2] = 0.027815
    Gi[3] = 0.189065
    Gi[4] = 0.0793
    Gi[5] = 0.141239
    Gi[6] = 0.256692
    Gi[7] = 0.281835
    Gi[8] = 0.332267
    Gi[9] = 0.366911
    Gi[10] = 0.289731
    Gi[11] = 0.337542
    Gi[12] = 0.383381
    Gi[13] = 0.427354
    Gi[14] = 0.469659
    Gi[15] = 0.034369
    Gi[16] = 0.021
    Gi[17] = 0.038953
    Gi[18] = 0.3325
    Gi[19] = 0.0885

    return Gi


def initialise_Ki(n):
    """Initialise Ki(n+1, 1) array with known initial values."""
    Ki = [0] * (n + 1)

    Ki[1] = 0.4619255
    Ki[2] = 0.4479153
    Ki[3] = 0.4557489
    Ki[4] = 0.5279209
    Ki[5] = 0.583749
    Ki[6] = 0.6406937
    Ki[7] = 0.6341423
    Ki[8] = 0.6738577
    Ki[9] = 0.6798307
    Ki[10] = 0.7175118
    Ki[11] = 0.7525189
    Ki[12] = 0.784955
    Ki[13] = 0.8152731
    Ki[14] = 0.8437826
    Ki[15] = 0.3514916
    Ki[16] = 0.4186954
    Ki[17] = 0.4533894
    Ki[18] = 0.3825868
    Ki[19] = 0.4618263
    Ki[20] = 0.3589888
    Ki[21] = 0.4216551

    return Ki


def initialise_Qi(n):
    """Initialise Qi(n+1, 1) array with known initial values."""
    Qi = [0] * (n + 1)
    # add initial values
    Qi[3] = 0.69
    Qi[18] = 1.06775
    Qi[19] = 0.633276

    return Qi


def initialise_Si(n):
    """Initialise Si(n+1, 1) array with known initial values."""
    Si = [0] * (n + 1)
    # add initial values
    Si[18] = 1.5822  # Dipole parameter
    Si[19] = 0.39  # Dipole parameter

    return Si


def initialise_Wi(n):
    """Initialise Wi(n+1, 1) array with known initial values."""
    Wi = [0] * (n + 1)
    # add initial values
    Wi[18] = 1  # Association parameter

    return Wi


def initialise_Eij(Eij):
    """Initialise input array Eij(i, j) with known initial conditions."""
    Eij[1][2] = 0.97164
    Eij[1][3] = 0.960644
    Eij[1][5] = 0.994635
    Eij[1][6] = 1.01953
    Eij[1][7] = 0.989844
    Eij[1][8] = 1.00235
    Eij[1][9] = 0.999268
    Eij[1][10] = 1.107274
    Eij[1][11] = 0.88088
    Eij[1][12] = 0.880973
    Eij[1][13] = 0.881067
    Eij[1][14] = 0.881161
    Eij[1][15] = 1.17052
    Eij[1][17] = 0.990126
    Eij[1][18] = 0.708218
    Eij[1][19] = 0.931484
    Eij[2][3] = 1.02274
    Eij[2][4] = 0.97012
    Eij[2][5] = 0.945939
    Eij[2][6] = 0.946914
    Eij[2][7] = 0.973384
    Eij[2][8] = 0.95934
    Eij[2][9] = 0.94552
    Eij[2][15] = 1.08632
    Eij[2][16] = 1.021
    Eij[2][17] = 1.00571
    Eij[2][18] = 0.746954
    Eij[2][19] = 0.902271
    Eij[3][4] = 0.925053
    Eij[3][5] = 0.960237
    Eij[3][6] = 0.906849
    Eij[3][7] = 0.897362
    Eij[3][8] = 0.726255
    Eij[3][9] = 0.859764
    Eij[3][10] = 0.855134
    Eij[3][11] = 0.831229
    Eij[3][12] = 0.80831
    Eij[3][13] = 0.786323
    Eij[3][14] = 0.765171
    Eij[3][15] = 1.28179
    Eij[3][17] = 1.5
    Eij[3][18] = 0.849408
    Eij[3][19] = 0.955052
    Eij[4][5] = 1.02256
    Eij[4][7] = 1.01306
    Eij[4][9] = 1.00532
    Eij[4][15] = 1.16446
    Eij[4][18] = 0.693168
    Eij[4][19] = 0.946871
    Eij[5][7] = 1.0049
    Eij[5][15] = 1.034787
    Eij[6][15] = 1.3
    Eij[7][15] = 1.3
    Eij[10][19] = 1.008692
    Eij[11][19] = 1.010126
    Eij[12][19] = 1.011501
    Eij[13][19] = 1.012821
    Eij[14][19] = 1.014089
    Eij[15][17] = 1.1

    return Eij


def initialise_Kij(Kij):
    """Initialise input array Kij(i, j) with known initial conditions."""
    # size parameters
    Kij[1][2] = 1.00363
    Kij[1][3] = 0.995933
    Kij[1][5] = 1.007619
    Kij[1][7] = 0.997596
    Kij[1][9] = 1.002529
    Kij[1][10] = 0.982962
    Kij[1][11] = 0.983565
    Kij[1][12] = 0.982707
    Kij[1][13] = 0.981849
    Kij[1][14] = 0.980991
    Kij[1][15] = 1.02326
    Kij[1][19] = 1.00008
    Kij[2][3] = 0.982361
    Kij[2][4] = 1.00796
    Kij[2][15] = 1.03227
    Kij[2][19] = 0.942596
    Kij[3][4] = 1.00851
    Kij[3][10] = 0.910183
    Kij[3][11] = 0.895362
    Kij[3][12] = 0.881152
    Kij[3][13] = 0.86752
    Kij[3][14] = 0.854406
    Kij[3][19] = 1.00779
    Kij[4][5] = 0.986893
    Kij[4][15] = 1.02034
    Kij[4][19] = 0.999969
    Kij[10][19] = 0.96813
    Kij[11][19] = 0.96287
    Kij[12][19] = 0.957828
    Kij[13][19] = 0.952441
    Kij[14][19] = 0.948338

    return Kij


def initialise_Uij(Uij):
    """Initialise input array Uij(i, j) with known initial conditions."""
    # Conformal energy parameters
    Uij[1][2] = 0.886106
    Uij[1][3] = 0.963827
    Uij[1][5] = 0.990877
    Uij[1][7] = 0.992291
    Uij[1][9] = 1.00367
    Uij[1][10] = 1.302576
    Uij[1][11] = 1.191904
    Uij[1][12] = 1.205769
    Uij[1][13] = 1.219634
    Uij[1][14] = 1.233498
    Uij[1][15] = 1.15639
    Uij[1][19] = 0.736833
    Uij[2][3] = 0.835058
    Uij[2][4] = 0.816431
    Uij[2][5] = 0.915502
    Uij[2][7] = 0.993556
    Uij[2][15] = 0.408838
    Uij[2][19] = 0.993476
    Uij[3][4] = 0.96987
    Uij[3][10] = 1.066638
    Uij[3][11] = 1.077634
    Uij[3][12] = 1.088178
    Uij[3][13] = 1.098291
    Uij[3][14] = 1.108021
    Uij[3][17] = 0.9
    Uij[3][19] = 1.04529
    Uij[4][5] = 1.065173
    Uij[4][6] = 1.25
    Uij[4][7] = 1.25
    Uij[4][8] = 1.25
    Uij[4][9] = 1.25
    Uij[4][15] = 1.61666
    Uij[4][19] = 0.971926
    Uij[10][19] = 1.028973
    Uij[11][19] = 1.033754
    Uij[12][19] = 1.038338
    Uij[13][19] = 1.042735
    Uij[14][19] = 1.046966

    return Uij


def initialise_Gij(Gij):
    """Initialise input array Gij(i, j) with known initial conditions."""
    # Orientation parameters
    Gij[1][3] = 0.807653
    Gij[1][15] = 1.95731
    Gij[2][3] = 0.982746
    Gij[3][4] = 0.370296
    Gij[3][18] = 1.67309

    return Gij


def initialise_ij_arrays(n):
    """Initialise all ij shape (i, j) arrays for the AGA8 Detail method."""
    Eij = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    Uij = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    Kij = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    Gij = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    # initialise with 1s from the 1st index
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            Eij[i][j] = 1
            Uij[i][j] = 1
            Kij[i][j] = 1
            Gij[i][j] = 1

    # add initial values
    Eij = initialise_Eij(Eij)  # energy params
    Uij = initialise_Uij(Uij)  # conformal energy params
    Kij = initialise_Kij(Kij)  # size params
    Gij = initialise_Gij(Gij)  # orientation params

    return Eij, Uij, Kij, Gij


def initialise_n0i(n):
    """Initialise n0i array of shape (n+1, 7+1) for the AGA8 Detail method."""
    n0i = [[0 for _ in range(7 + 1)] for _ in range(n + 1)]
    # add initial values
    n0i[1][3] = 4.00088
    n0i[1][4] = 0.76315
    n0i[1][5] = 0.0046
    n0i[1][6] = 8.74432
    n0i[1][7] = -4.46921
    n0i[1][1] = 29.83843397
    n0i[1][2] = -15999.69151
    n0i[2][3] = 3.50031
    n0i[2][4] = 0.13732
    n0i[2][5] = -0.1466
    n0i[2][6] = 0.90066
    n0i[2][7] = 0
    n0i[2][1] = 17.56770785
    n0i[2][2] = -2801.729072
    n0i[3][3] = 3.50002
    n0i[3][4] = 2.04452
    n0i[3][5] = -1.06044
    n0i[3][6] = 2.03366
    n0i[3][7] = 0.01393
    n0i[3][1] = 20.65844696
    n0i[3][2] = -4902.171516
    n0i[4][3] = 4.00263
    n0i[4][4] = 4.33939
    n0i[4][5] = 1.23722
    n0i[4][6] = 13.1974
    n0i[4][7] = -6.01989
    n0i[4][1] = 36.73005938
    n0i[4][2] = -23639.65301
    n0i[5][3] = 4.02939
    n0i[5][4] = 6.60569
    n0i[5][5] = 3.197
    n0i[5][6] = 19.1921
    n0i[5][7] = -8.37267
    n0i[5][1] = 44.70909619
    n0i[5][2] = -31236.63551
    n0i[6][3] = 4.06714
    n0i[6][4] = 8.97575
    n0i[6][5] = 5.25156
    n0i[6][6] = 25.1423
    n0i[6][7] = 16.1388
    n0i[6][1] = 34.30180349
    n0i[6][2] = -38525.50276
    n0i[7][3] = 4.33944
    n0i[7][4] = 9.44893
    n0i[7][5] = 6.89406
    n0i[7][6] = 24.4618
    n0i[7][7] = 14.7824
    n0i[7][1] = 36.53237783
    n0i[7][2] = -38957.80933
    n0i[8][3] = 4
    n0i[8][4] = 11.7618
    n0i[8][5] = 20.1101
    n0i[8][6] = 33.1688
    n0i[8][7] = 0
    n0i[8][1] = 43.17218626
    n0i[8][2] = -51198.30946
    n0i[9][3] = 4
    n0i[9][4] = 8.95043
    n0i[9][5] = 21.836
    n0i[9][6] = 33.4032
    n0i[9][7] = 0
    n0i[9][1] = 42.67837089
    n0i[9][2] = -45215.83
    n0i[10][3] = 4
    n0i[10][4] = 11.6977
    n0i[10][5] = 26.8142
    n0i[10][6] = 38.6164
    n0i[10][7] = 0
    n0i[10][1] = 46.99717188
    n0i[10][2] = -52746.83318
    n0i[11][3] = 4
    n0i[11][4] = 13.7266
    n0i[11][5] = 30.4707
    n0i[11][6] = 43.5561
    n0i[11][7] = 0
    n0i[11][1] = 52.07631631
    n0i[11][2] = -57104.81056
    n0i[12][3] = 4
    n0i[12][4] = 15.6865
    n0i[12][5] = 33.8029
    n0i[12][6] = 48.1731
    n0i[12][7] = 0
    n0i[12][1] = 57.25830934
    n0i[12][2] = -60546.76385
    n0i[13][3] = 4
    n0i[13][4] = 18.0241
    n0i[13][5] = 38.1235
    n0i[13][6] = 53.3415
    n0i[13][7] = 0
    n0i[13][1] = 62.09646901
    n0i[13][2] = -66600.12837
    n0i[14][3] = 4
    n0i[14][4] = 21.0069
    n0i[14][5] = 43.4931
    n0i[14][6] = 58.3657
    n0i[14][7] = 0
    n0i[14][1] = 65.93909154
    n0i[14][2] = -74131.45483
    n0i[15][3] = 2.47906
    n0i[15][4] = 0.95806
    n0i[15][5] = 0.45444
    n0i[15][6] = 1.56039
    n0i[15][7] = -1.3756
    n0i[15][1] = 13.07520288
    n0i[15][2] = -5836.943696
    n0i[16][3] = 3.50146
    n0i[16][4] = 1.07558
    n0i[16][5] = 1.01334
    n0i[16][6] = 0
    n0i[16][7] = 0
    n0i[16][1] = 16.8017173
    n0i[16][2] = -2318.32269
    n0i[17][3] = 3.50055
    n0i[17][4] = 1.02865
    n0i[17][5] = 0.00493
    n0i[17][6] = 0
    n0i[17][7] = 0
    n0i[17][1] = 17.45786899
    n0i[17][2] = -2635.244116
    n0i[18][3] = 4.00392
    n0i[18][4] = 0.01059
    n0i[18][5] = 0.98763
    n0i[18][6] = 3.06904
    n0i[18][7] = 0
    n0i[18][1] = 21.57882705
    n0i[18][2] = -7766.733078
    n0i[19][3] = 4
    n0i[19][4] = 3.11942
    n0i[19][5] = 1.00243
    n0i[19][6] = 0
    n0i[19][7] = 0
    n0i[19][1] = 21.5830944
    n0i[19][2] = -6069.035869
    n0i[20][3] = 2.5
    n0i[20][4] = 0
    n0i[20][5] = 0
    n0i[20][6] = 0
    n0i[20][7] = 0
    n0i[20][1] = 10.04639507
    n0i[20][2] = -745.375
    n0i[21][3] = 2.5
    n0i[21][4] = 0
    n0i[21][5] = 0
    n0i[21][6] = 0
    n0i[21][7] = 0
    n0i[21][1] = 10.04639507
    n0i[21][2] = -745.375

    return n0i


def initialise_th0i(n):
    """Initialise th0i array of shape (n+1, 7+1) for the AGA8 Detail method."""
    th0i = [[0 for _ in range(7 + 1)] for _ in range(n + 1)]
    # add initial values
    th0i[1][4] = 820.659
    th0i[1][5] = 178.41
    th0i[1][6] = 1062.82
    th0i[1][7] = 1090.53
    th0i[2][4] = 662.738
    th0i[2][5] = 680.562
    th0i[2][6] = 1740.06
    th0i[2][7] = 0
    th0i[3][4] = 919.306
    th0i[3][5] = 865.07
    th0i[3][6] = 483.553
    th0i[3][7] = 341.109
    th0i[4][4] = 559.314
    th0i[4][5] = 223.284
    th0i[4][6] = 1031.38
    th0i[4][7] = 1071.29
    th0i[5][4] = 479.856
    th0i[5][5] = 200.893
    th0i[5][6] = 955.312
    th0i[5][7] = 1027.29
    th0i[6][4] = 438.27
    th0i[6][5] = 198.018
    th0i[6][6] = 1905.02
    th0i[6][7] = 893.765
    th0i[7][4] = 468.27
    th0i[7][5] = 183.636
    th0i[7][6] = 1914.1
    th0i[7][7] = 903.185
    th0i[8][4] = 292.503
    th0i[8][5] = 910.237
    th0i[8][6] = 1919.37
    th0i[8][7] = 0
    th0i[9][4] = 178.67
    th0i[9][5] = 840.538
    th0i[9][6] = 1774.25
    th0i[9][7] = 0
    th0i[10][4] = 182.326
    th0i[10][5] = 859.207
    th0i[10][6] = 1826.59
    th0i[10][7] = 0
    th0i[11][4] = 169.789
    th0i[11][5] = 836.195
    th0i[11][6] = 1760.46
    th0i[11][7] = 0
    th0i[12][4] = 158.922
    th0i[12][5] = 815.064
    th0i[12][6] = 1693.07
    th0i[12][7] = 0
    th0i[13][4] = 156.854
    th0i[13][5] = 814.882
    th0i[13][6] = 1693.79
    th0i[13][7] = 0
    th0i[14][4] = 164.947
    th0i[14][5] = 836.264
    th0i[14][6] = 1750.24
    th0i[14][7] = 0
    th0i[15][4] = 228.734
    th0i[15][5] = 326.843
    th0i[15][6] = 1651.71
    th0i[15][7] = 1671.69
    th0i[16][4] = 2235.71
    th0i[16][5] = 1116.69
    th0i[16][6] = 0
    th0i[16][7] = 0
    th0i[17][4] = 1550.45
    th0i[17][5] = 704.525
    th0i[17][6] = 0
    th0i[17][7] = 0
    th0i[18][4] = 268.795
    th0i[18][5] = 1141.41
    th0i[18][6] = 2507.37
    th0i[18][7] = 0
    th0i[19][4] = 1833.63
    th0i[19][5] = 847.181
    th0i[19][6] = 0
    th0i[19][7] = 0
    th0i[20][4] = 0
    th0i[20][5] = 0
    th0i[20][6] = 0
    th0i[20][7] = 0
    th0i[21][4] = 0
    th0i[21][5] = 0
    th0i[21][6] = 0
    th0i[21][7] = 0

    return th0i


def initialise_Bs():
    """Initialise Bs array(18+1, 1) with zeros."""
    return [0] * (18 + 1)


def initialise_Bsnij2(n):
    """Initialise Bsnij2 array (n, n 18+1) with zeros."""
    return [
        [[0 for _ in range(18 + 1)] for _ in range(n + 1)]
        for _ in range(n + 1)
    ]


def initialise_i25_arrays(n):
    """Initialise i25 array(n+1, 1) with zeros."""
    Ki25 = [0] * (n + 1)
    Ei25 = [0] * (n + 1)

    return Ki25, Ei25


def initialise_ij5_arrays(n):
    """Initialise ij5 arrays shape (n+1, n+1) with zeros."""
    Kij5 = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    Uij5 = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    Gij5 = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    return Kij5, Uij5, Gij5


def initialise_Csn(n):
    """Initialise Csn array(n+1, 1) with zeros."""
    return [0] * (n + 1)


def initialise_Tun(n):
    """Initialise Tun array(n+1, 1) with zeros."""
    return [0] * (n + 1)

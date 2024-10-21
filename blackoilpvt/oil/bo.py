import numpy as np
from .co import vazquez_beggs_Undersat_co, gas_gravity_100
from ..commons import Black_oil_corr


def compute_bo(blackoilcorr: Black_oil_corr, P: float, T: float, API: float, gas_gravity: float, P_sep: float, T_sep: float, Pb: float, Rs: float, Rsb: float, cp1: float = 1.0, cp2: float = 0.0, cp3: float = 1.0, cp4: float = 0.0) -> float:
    if blackoilcorr == Black_oil_corr.GLASO:
        return glaso_bo(P, T, API, gas_gravity, Pb, Rs, Rsb, P_sep, T_sep, cp1, cp2, cp3, cp4)
    elif blackoilcorr == Black_oil_corr.VAZQUEZ_BEGGS:
        return vazquez_beggs_bo(P, T, API, gas_gravity, Pb, Rs, Rsb, P_sep, T_sep, cp1, cp2, cp3, cp4)
    elif blackoilcorr == Black_oil_corr.STANDING:
        return standing_bo(P, T, API, gas_gravity, Pb, Rs, Rsb, P_sep, T_sep, cp1, cp2, cp3, cp4)
    elif blackoilcorr == Black_oil_corr.PETROSKEY:
        return petroskey_bo(P, T, API, gas_gravity, Pb, Rs, Rsb, P_sep, T_sep, cp1, cp2, cp3, cp4)
    elif blackoilcorr == Black_oil_corr.ALMARHOUN:
        return almarhoun_bo(P, T, API, gas_gravity, Pb, Rs, Rsb, P_sep, T_sep, cp1, cp2, cp3, cp4)
    else:
        return -99


# region Glaso_Bo
def glaso_bo(P: float, T: float, API: float, gas_gravity: float, Pb: float, Rs: float, Rsb: float, P_sep: float, T_sep: float, cp1: float = 1.0, cp2: float = 0.0, cp3: float = 1.0, cp4: float = 0.0) -> float:
    bo = glaso_bo_func(T, API, gas_gravity, Rs)
    if P <= Pb:
        return cp1 * bo + cp2
    else:
        ave_co = vazquez_beggs_Undersat_co(P, T, API, gas_gravity, Rsb, P_sep, T_sep)
        boo = bo * (1.0 - ave_co * (P - Pb))
        return cp3 * boo + cp4

def glaso_bo_func(T: float, API: float, gas_gravity: float, Rs: float) -> float:
    yo = 141.5/(131.5 + API)
    B = Rs * np.power((gas_gravity/yo), 0.526) + (0.968 * T)
    A = -6.58511 + 2.91329 * np.log10(B) - 0.27683 * np.power(np.log10(B), 2)
    Bo = 1 + np.power(10, A)
    return Bo
# endregion

# region Vazquez_Beggs
def vazquez_beggs_bo(P: float, T: float, API: float, gasgravity: float, Pb: float, Rs: float, Rsb: float, P_sep: float, T_sep: float, cp1: float = 1.0, cp2: float = 0.0, cp3: float = 1.0, cp4: float = 0.0) -> float:
    if P <= Pb:
        bo = vazquez_beggs_bofunc(T, API, gasgravity, Rs, P_sep, T_sep)
        return cp1 * bo + cp2
    else:
        co_ave = vazquez_beggs_Undersat_co(P, T, API, gasgravity, Rsb, P_sep, T_sep)
        bo = vazquez_beggs_bofunc(T, API, gasgravity, Rsb, P_sep, T_sep)
        bo = bo * (1 - co_ave * (P - Pb))
        return cp3 * bo + cp4

def vazquez_beggs_bofunc(T: float, API: float, gasgravity: float, Rs: float, P_sep: float, T_sep: float):
    yg100 = gas_gravity_100(gasgravity, API, P_sep, T_sep)
    c1 = 4.67e-4
    c2 = 1.1e-5
    c3 = 1.337e-9
    if API <= 30:
        c1 = 4.677e-4
        c2 = 1.751e-5
        c3 = -1.811e-8
    bo = 1 + c1 * Rs + (T - 60) * (API / yg100) * (c2 + c3 * Rs)
    return bo

# endregion

# region Standing_Bo
def standing_bo(P: float, T: float, API: float, gasgravity: float, Pb: float, Rs: float, Rsb: float, P_sep: float, T_sep: float, cp1: float = 1.0, cp2: float = 0.0, cp3: float = 1.0, cp4: float = 0.0) -> float:
    yo = 141.5 / (131.5 + API)
    Bo = 0.972 + 0.000147 * np.power((Rs * np.power((gasgravity / yo), 0.5) + (1.25 * T)), 1.175)
    if P <= Pb:
        return cp1 * Bo + cp2
    co_ave = vazquez_beggs_Undersat_co(P, T, API, gasgravity, Rsb, P_sep, T_sep)
    Bo = Bo * (1 - co_ave * (P - Pb))

    return cp3 * Bo + cp4

# endregion

# region Petroskey_Bo
def petroskey_bo(P: float, T: float, API: float, gasgravity: float, Pb: float, Rs: float, Rsb: float, P_sep: float, T_sep: float, cp1: float = 1.0, cp2: float = 0.0, cp3: float = 1.0, cp4: float = 0.0) -> float:
    yo = 141.5/(131.5 + API)
    A = np.power(((np.power(Rs, 0.3738) * (np.power(gasgravity, 0.2914) / np.power(yo, 0.6265))) + (0.24626 * np.power(T, 0.5371))), 3.0936)
    Bo = 1.0113 + (0.000072046 * A)
    if P <= Pb:
        return cp1 * Bo + cp2
    else:
        co_ave = vazquez_beggs_Undersat_co(P, T, API, gasgravity, Rsb, P_sep, T_sep)
        Bo = Bo * (1 - co_ave * (P - Pb))
        return cp3 * Bo + cp4

# endregion

# region Almarhoun_Bo
def almarhoun_bo(P: float, T: float, API: float, gasgravity: float, Pb: float, Rs: float, Rsb: float, Psep: float, Tsep: float, cp1: float = 1.0, cp2: float = 0.0, cp3: float = 1.0, cp4: float = 0.0) -> float:
    yo = 141.5 / (131.5 + API)
    f = np.power(Rs, 0.74239) * np.power(gasgravity, 0.323294) * np.power(yo, -1.20204)
    Bo = 0.497069 + (0.000862963 * (T + 460)) + (0.00182594 * f) + (0.00000318099 * np.power(f, 2))
    if P <= Pb:
        return cp1 * Bo + cp2
    else:
        co_ave = vazquez_beggs_Undersat_co(P, T, API, gasgravity, Rsb, Psep, Tsep)
        Bo = Bo * (1 - co_ave * (P - Pb))
        return cp3 * Bo + cp4

# endregion


if __name__ == "__main__":
    bo_1 = glaso_bo(1500, 180, 35, 0.75, 14.7, 60, 1800, 700, 800)
    print(bo_1)
    bo_2 = glaso_bo(1800, 180, 35, 0.75, 14.7, 60, 1800, 780, 800)
    print(bo_2)
    bo_3 = glaso_bo(2000, 180, 35, 0.75, 14.7, 60, 1800, 800, 800)
    print(bo_3)
    bo_4 = glaso_bo(2400, 180, 35, 0.75, 14.7, 60, 1800, 800, 800)
    print(bo_4)







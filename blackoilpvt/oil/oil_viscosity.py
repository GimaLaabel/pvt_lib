import numpy as np
from ..commons import Oil_viscosity_corr

def compute_oil_viscosity(oil_visc_corr: Oil_viscosity_corr,  P: float, T: float, API: float, Pb: float, Rs: float, Rsb: float, cp1: float = 1.0, cp2: float = 0.0, cp3: float = 1.0, cp4: float = 0.0) -> float:
    if oil_visc_corr == Oil_viscosity_corr.BEAL:
        return beal_oil_viscosity(P, T, API, Pb, Rs, Rsb, cp1, cp2, cp3, cp4)
    elif oil_visc_corr == Oil_viscosity_corr.BEGGS_ROBINSON:
        return beggs_robinson_oil_viscosity(P, T, API, Pb, Rs, Rsb, cp1, cp2, cp3, cp4)
    else:
        return -99.9


# region Beal
def beal_oil_viscosity(P: float, T: float, API: float, Pb: float, Rs: float, Rsb: float, cp1: float = 1.0, cp2: float = 0.0, cp3: float = 1.0, cp4: float = 0.0) -> float:
    muo_dead = beal_dead_oil_viscosity(T, API)
    if P < Pb:
        muo_sat = beal_saturated_viscosity(muo_dead, Rs)
        return cp1 * muo_sat + cp2
    else:
        muo_Pb = beal_saturated_viscosity(muo_dead, Rsb)
        muo_under_sat = beal_undersat_viscosity(P, Pb, muo_Pb)
        return cp3 * muo_under_sat + cp4 


def beal_undersat_viscosity(P: float, Pb: float, muo_Pb: float) -> float:
    muo = muo_Pb + 0.001 * (P -  Pb) * (0.024 * np.power(muo_Pb, 1.6) + 0.038 * np.power(muo_Pb, 0.56))
    return muo 

def beal_saturated_viscosity(muo_dead: float, Rs: float) -> float:
    A1 = np.power(10.0, (-7.4 * np.power(10.0, -4) * Rs + 2.2 * np.power(10.0, -7) * np.power(Rs, 2)))
    A2 = 0.68 / np.power(10.0, (8.62 * np.power(10.0, -5) * Rs)) + 0.25 / np.power(10.0, (1.1 * np.power(10.0, -3) * Rs)) + 0.062 / np.power(10.0, (3.74 * np.power(10.0, -3) * Rs))
    muo = A1 * np.power(muo_dead, A2)
    return muo

def beal_dead_oil_viscosity(T: float, API: float) -> float:
    A = np.power(10, (0.43 + (8.33/API)))
    muo_dead = (0.32 + (1.8e7 / np.power(API, 4.53))) * np.power((360/(T + 200)), A)
    return muo_dead

# endregion

# region BeggsRobinson
def beggs_robinson_oil_viscosity(P: float, T: float, API: float, Pb: float, Rs: float, Rsb: float, cp1: float = 1.0, cp2: float = 0.0, cp3: float = 1.0, cp4: float = 0.0) -> float:
    muo_dead = beggs_robinson_dead(API, T)
    if P < Pb:
        muo_sat = beggs_robinson_saturated(muo_dead, Rs)
        return cp1 * muo_sat + cp2
    else:
        muo_Pb = beggs_robinson_saturated(muo_dead, Rsb)
        muo_under = beggs_robinson_undersat(P, Pb, muo_Pb)
        return cp3 * muo_under + cp4

def beggs_robinson_undersat(P: float, Pb: float, muo_Pb: float) -> float:
    A = 2.6 * np.power(P, 1.187) * np.exp(-11.513 - 8.98 * np.power(10.0, -5) * P)
    muo = muo_Pb * np.power((P/Pb), A)
    return muo

def beggs_robinson_saturated(muo_dead: float, Rs: float) -> float:
    A1 = 10.715 * np.power((Rs + 100), -0.515)
    A2 = 5.44 * np.power((Rs + 150), -0.338)
    muo = A1 * np.power(muo_dead, A2)
    return muo

def beggs_robinson_dead(API: float, T: float) -> float:
    A = np.power(10.0, (3.0324 - 0.02023 * API))
    muo_dead = np.power(10.0, (A * np.power(T, -1.163))) - 1.0
    return muo_dead

# endregion


if __name__ == "__main__":
    beal1 = beal_oil_viscosity(2000, 180, 35, 1800, 700, 800)
    print(f"Beal viscosity: {beal1}")

    beal2 = beggs_robinson_oil_viscosity(2000, 180, 35, 1800, 700, 800)     # 2000, 180, 35, 1800, 700, 800
    print(f"Beal viscosity: {beal2}")



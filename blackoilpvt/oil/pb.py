import numpy as np
from blackoilpvt.commons import Black_oil_corr
from blackoilpvt.oil.co import gas_gravity_100


def compute_Pb(blackoil_corr: Black_oil_corr, T: float, Api: float, gas_gravity: float, Rsb: float, yco2: float, yh2s: float, yn2: float, Pb_impurity_correct: bool, cp1 = 1.0, cp2 = 0.0) -> float:
    """
    Calculates the bubble point pressure of the fluid using the given correlation.

    Args:
        blackoil_corr (Black_oil_corr): The choice of blackoil correlation
        T (float): Fluid temperature (degF)
        Api (float): Oil gravity (API)
        gas_gravity (float): Gas gravity
        Rsb (float): Gas oil ration of fluid
        yco2 (float): Mole fraction of CO2
        yh2s (float): Mole fraction of H2S
        yn2 (float): Mole fraction of N2
        Pb_impurity_correct (bool): Bubble point pressure impurity correction
        cp1 (float): Matching parameter 1
        cp2 (float): Matching parameter 2
           
    Returns:
        float: The bubble point pressure (psia)
    """
    if blackoil_corr == Black_oil_corr.GLASO:
        return glaso_Pb(T, Api, gas_gravity, Rsb, yco2, yh2s, yn2, Pb_impurity_correct, cp1, cp2)
    elif blackoil_corr == Black_oil_corr.VAZQUEZ_BEGGS:
        return vazquez_beggs_Pb(T, Api, gas_gravity, Rsb, yn2, Pb_impurity_correct, cp1, cp2)
    elif blackoil_corr == Black_oil_corr.STANDING:
        return standing_Pb(T, Api, gas_gravity, Rsb, yn2, Pb_impurity_correct, cp1, cp2)
    elif blackoil_corr == Black_oil_corr.PETROSKEY:
        return petrosky_Pb(T, Api, gas_gravity, Rsb, yn2, Pb_impurity_correct, cp1, cp2)
    elif blackoil_corr == Black_oil_corr.ALMARHOUN:
        return almarhoun_Pb(T, Api, gas_gravity, Rsb, Pb_impurity_correct, yn2, cp1, cp2)
    else:
        return -99

        
# region Glaso_Pb
def glaso_Pb(T: float, API: float, gas_gravity: float, Rsb: float, yco2: float, yh2s: float, yn2: float, Pb_impurity_correct: bool, cp1 = 1.0, cp2 = 0.0) -> float:
    pbs = 0.0
    if Rsb <= 1500: # for typical black oil
        a = 0.816; b = 0.172; c = 0.989
        pbs = np.power((Rsb / gas_gravity), a) * (np.power(T, b)/np.power(API, c))
    else:   # for volatile oil
        a = 0.816; b = 0.130;  c = 0.989
        pbs = np.power((Rsb / gas_gravity), a) * (np.power(T, b)/np.power(API, c))

    logPb = 1.7669 + (1.7447 * np.log10(pbs)) - (0.30218 * np.power(np.log10(pbs), 2))
    Pb = np.power(10.0, logPb)

    if Pb_impurity_correct:
        pass
        # co2_correction = 1.0 - 693.8 * yco2 * np.power(T, -1.553) 
        # # co2_correction = 1.0 - 593.8 * yco2 * np.power(T, -1.553) 

        # h2s_correction = 1.0 - (0.9035 + 0.0015 * API) * yh2s + 0.019 * (45 - API) * np.power(yh2s, 2)

        # # a1 = -2.65e-4; a2 = 5.5e-3; a3 = 0.0391; a4 = 0.8295; a5 = 1.954e-11; a6 = -4.699; a7 = 0.027; a8 = 2.366

        # a1 = -2.65e-4; a2 = 5.5e-3; a3 = 0.0931; a4 = 0.8295; a5 = 1.954e-11; a6 = 4.699; a7 = 0.027; a8 = 2.366
        # # a1 = -2.65e-4; a2 = 5.5e-3; a3 = 0.0391; a4 = 0.8295; a5 = 1.954e-11; a6 = 4.699; a7 = 0.027; a8 = 2.366

        # # n2_correction = 1.0 + ((a1 * API + a2) * T + a3 * API - a4) * yn2 + ((a5 * np.power(API, a6)) * T + (a6 * np.power(API, a7)) - a8) * np.power(yn2, 2)   # This was correctly programmed, but result differs from PETEX
        # n2_correction = 1.0 + ((a1 * API + a2) * T + (a3 * API - a4)) * yn2 + ((a5 * np.power(API, a6)) * T + (a7 * API - a8)) * np.power(yn2, 2)
        # # n2_correction = 1.0 + ((-2.65e-4 * API + 5.5e-3) * T + (0.0931 * API - 0.8295)) * yn2 + ((1.954e-11 * np.power(API, 2)) * T + (0.027 * API - 2.366)) * np.power(yn2, 2)
        # correction = co2_correction * h2s_correction * n2_correction 
        # Pb = Pb * correction  
    
    return cp1 * Pb + cp2
# endregion

# region Vazquez_beggs_Pb
def vazquez_beggs_Pb(T: float, API: float, gasgravity: float, Rsb: float, yN2: float, Pb_impurity_correction: bool, cp1: float = 1.0, cp2: float = 0.0) -> float:
    c1 = 27.64
    c2 = 1.0937
    c3 = 11.172
    gasgravity_100 = gasgravity_100_vazquez_beggs(API, gasgravity)
    if API > 30.0:
        c1 = 56.06
        c2 = 1.1870
        c3 = 10.393
    term1 = np.power(10.0, -c3 * API/(T + 459.67))          #459.67
    Pb = np.power((c1 * Rsb/gasgravity_100)* term1, 1/c2)
    
    return cp1 * Pb + cp2


def jacobson_nitrogen_correction(yN2: float, T: float) -> float:
    if yN2 == 0.0: return 1.0
    return 1.1585 + 2.86 * yN2 - 0.00107 * T

# endregion

# region Standing Pb

def standing_Pb(T: float, API: float, gas_gravity: float, Rsb: float, yN2: float, pb_impurity_correction: bool, cp1: float = 1.0, cp2: float = 0.0) -> float:
    """
    Calculates the bubble point pressure of the fluid using the Standing correlation.

    Args:
        Temperature (float): Temperature (degF)
    Returns:
        float: The bubble point pressure (psia)
    """
    A = 0.00091 * T - 0.0125 * API
    term1 = np.power((Rsb / gas_gravity), 0.83)
    term2 = term1 * np.power(10.0, A)
    Pb = 18.2 * (term2 - 1.4)    
    return cp1 * Pb + cp2

# endregion

# region Petrosky_Farshard
def petrosky_Pb(T: float, API: float, gas_gravity: float, Rsb: float, yN2: float, pb_impuritycorrection: bool, cp1: float = 1.0, cp2: float = 0.0) -> float:
    x = 4.561e-5 * np.power(T, 1.3911) - 7.916e-4 * np.power(API, 1.541)
    # x = 7.916e-4* np.power(API, 1.541) - 4.561e-5 * np.power(T, 1.3911)
    pb = 112.727 * ((np.power(Rsb, 0.5774)/np.power(gas_gravity, 0.8439)) * np.power(10.0, x) - 12.34)
    # pb = 112.727 * (np.power(Rsb, 0.577421)/np.power(gas_gravity, 0.8439) * np.power(10.0, x) - 12.34)
    # if pb_impuritycorrection:
    #     pb = pb * jacobson_nitrogen_correction(yN2, T)
    return cp1 * pb + cp2

# endregion

# region Almarhoun_Pb
def almarhoun_Pb(T: float, API: float, gasgravity: float, Rsb: float, pb_impuritycorrection: bool, yN2: float, cp1: float = 1.0, cp2: float = 0.0) -> float:
    yo = 141.5 / (131.5 + API)
    pb = 0.00538088 * np.power(Rsb, 0.715082) * np.power(gasgravity, -1.87784) * np.power(yo, 3.1437) * np.power((T + 459.67), 1.32657)
    return cp1 * pb + cp2

# endregion

def gasgravity_100_vazquez_beggs(API: float, gasgravity: float, P_sep: float = 14.7, T_sep: float = 60) -> float:
    term1 = (1.0 + 5.912e-5 * API * T_sep * np.log10(P_sep/114.7))
    return (gasgravity * term1)

def jacobson_nitrogen_correction(yN2: float, T: float) -> float:
    if yN2 == 0.0:
        return 1.0
    factor = 1.1585 + 2.86 * yN2 - 0.00107 * T
    return factor

if __name__ == "__main__":
    pass
  
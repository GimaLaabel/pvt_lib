import numpy as np
from ..commons import Black_oil_corr

def compute_Rs(blackoil_corr: Black_oil_corr, P: float, T: float, Api: float, gas_gravity: float, Pb: float, Rsb: float, pst: float, P_sep: float, T_sep: float, cp1: float = 1.0, cp2: float = 0.0 ) -> float:
    """
    Calculates and returns the solution gas oil ration of the fluid from a given blackoil correlation
    Args:
        blackoil_corr (Black_oil_corr): The choice of blackoil correlation
        P (float): Fluid pressure (psia)
        T (float): Fluid temperature (degF)
        Api (float): Oil gravity (API)
        gas_gravity (float): Gas gravity
        Pb (float): Bubble point pressure of fluid (psia)
        Rsb (float): Gas oil ration of fluid
        pst (float): standard surface pressure (psia)
        P_sep (float): Primary separator pressure (psia)
        T_sep (float): Primary separator temperature (deg F)
        cp1 (float): Matching parameter 1
        cp2 (float): Matching parameter 2
        
    Returns:
        float: The calculated solution gas oil ratio
    """
    if blackoil_corr == Black_oil_corr.GLASO:
        return glaso_Rs(P, T, Api, gas_gravity, Pb, Rsb, pst, cp1, cp2)
    elif blackoil_corr == Black_oil_corr.VAZQUEZ_BEGGS:
        return vazquez_beggs_Rs(P, T, Api, gas_gravity, Pb, Rsb, P_sep, T_sep, cp1, cp2)
    elif blackoil_corr == Black_oil_corr.STANDING:
        return standing_Rs(P, T, Api, gas_gravity, Pb, Rsb, pst, cp1, cp2)
    elif blackoil_corr == Black_oil_corr.PETROSKEY:
        return petrosky_Rs(P, T, Api, gas_gravity, Pb, Rsb, pst, cp1, cp2)
    elif blackoil_corr == Black_oil_corr.ALMARHOUN:
        return almarhoun_Rs(P, T, Api, gas_gravity,Pb, Rsb, pst, cp1, cp2)
    else:
        return -99

# region Glaso_Rs
def glaso_Rs(P: float, T: float, api: float, gasgrav: float, Pb: float, Rsb: float, pst: float, cp1: float = 1.0, cp2: float = 0.0) -> float:
    Rs = 0.0
    if P < Pb:
        if P < pst: return Rs
        x = 2.8869 - np.power((14.1811 - 3.3093 * np.log10(P)), 0.5)
        A = np.power(10, x)
        if Rsb <= 1500:
            Rs = gasgrav * np.power(((np.power(api, 0.989)/np.power(T, 0.172))*A), 1.2255)
        else:
            Rs = gasgrav * np.power(((np.power(api, 0.989) / np.power(T, 0.1302)) * A), 1.2255)
    else:
        Rs = Rsb        

    Rs = rs_value_check(Rs, Rsb)
    return cp1 * Rs + cp2

# endregion

# region Vazquez_Rs
def vazquez_beggs_Rs(P: float, T: float, API: float, gasgravity: float, Pb: float, Rsb: float, P_sep: float, T_sep: float, cp1: float = 1.0, cp2: float = 0.0) -> float:
    Rs: float = 0.0
    c1 = 0.0
    c2 = 0.0
    c3 = 0.0
    if P < Pb:
        if API <= 30.0:
            c1 = 0.0362
            c2 = 1.0937
            c3 = 25.724
        else:
            c1 = 0.0178
            c2 = 1.187
            c3 = 23.931        
    
        yg100 = gasgravity * (1 + 0.00005912 * API * T_sep * np.log10(P_sep/114.7))
        
        Rs = c1 * yg100 * np.power(P, c2) * np.exp((c3 * API)/(T + 460))
        Rs = max(0.0, Rs)
    else:
        Rs = Rsb

    Rs = rs_value_check(Rs, Rsb)
    return cp1 * Rs + cp2

# endregion

# region Standing_Rs
def standing_Rs(P: float, T: float, API: float, gas_gravity: float, Pb: float, Rsb: float, pst: float, cp1: float = 1.0, cp2: float = 0.0) -> float:
    Rs = Rsb
    if P < Pb:
        if P < pst:
            return 0.0
        x = (0.0125 * API) - (0.00091 * T)
        Rs = gas_gravity * np.power((((P / 18.2) + 1.4) * np.power(10.0, x)), 1.2048)
    
    return cp1 * Rs + cp2

# endregion

# region Petrosky_Farshard_RS
def petrosky_Rs(P: float, T: float, API: float, gasgravity: float, Pb: float, Rsb: float, pst: float, cp1: float = 1.0, cp2: float = 0.0) -> float:
    Rs = Rsb
    if P < Pb:
        if P < pst:
            return 0.0
        x = 7.916e-4 * np.power(API, 1.5410) - 4.561e-5 * np.power(T, 1.3911)
        Rs = np.power(((P / 112.727 + 12.340) * np.power(gasgravity, 0.8439) * np.power(10.0, x)), 1.73190162)
    
    return cp1 * Rs + cp2

# endregion

# region Almarhoun_Rs
def almarhoun_Rs(P: float, T: float, API: float, gasgravity: float, Pb: float, Rsb: float, pst: float, cp1: float = 1.0, cp2: float = 0.0) -> float:
    Rs = Rsb
    if P < Pb:
        if P < pst:
            return 0.0
        yo = 141.5 / (131.5 + API)
        Rs = np.power((185.843208 * np.power(gasgravity, 1.8774) * np.power(yo, -3.1437) * (np.power((T + 459.67), -1.32657))* P), 1.398441)
    
    return cp1 * Rs + cp2

# endregion

# region Sanity check on Rs
def rs_value_check(Rs: float, Rsb: float) -> float:
    if Rs < 0.0:
        return 0.0
    elif Rs > Rsb:
        return Rsb
    else:
        return Rs

# endregion


if __name__ == "__main__":
    rs_1 = glaso_Rs(14.5, 180, 2200, 40, 800, 14.7, 0.75)
    print(rs_1)
    rs_2 = glaso_Rs(1800, 180, 2200, 40, 800, 14.7, 0.75)
    print(rs_2)
    rs_3 = glaso_Rs(2500, 180, 2200, 40, 800, 14.7, 0.75)
    print(rs_3)

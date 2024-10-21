import numpy as np
from scipy.optimize import fsolve
from typing import List
from ..commons import Gas_Type, Pseudocritical_Props, Z_Factor_corr


#region z factor
def compute_zfactor(tpr: float, ppr: float, zfactor_corr: Z_Factor_corr = Z_Factor_corr.DAK) -> float:
    Z = 0.0
    if zfactor_corr == Z_Factor_corr.BEGGS_BRILL:
        Z = Beggs_Brill_zfactor(tpr, ppr)
    elif zfactor_corr == Z_Factor_corr.HALLYARBOROUGH:
        Z = Z_factor_hall_yarborough(tpr, ppr)
    elif zfactor_corr == Z_Factor_corr.WANG:
        Z = wang_z_factor(tpr, ppr)
    elif zfactor_corr == Z_Factor_corr.DAK:
        Z = Z_factor_DAK(tpr, ppr)
    
    return Z

def Z_factor_DAK(tpr: float, ppr: float) -> float:
    z = 1.0
    if ppr != 0:
        tpr2 = tpr * tpr
        tpr3 = tpr2 * tpr 
        tpr4 = tpr3 * tpr
        tpr5 = tpr4 * tpr
        A1 = 0.3265; A2 = -1.0700; A3 = -0.5339; 
        A4 = 0.01569; A5 = -0.05165; A6 = 0.5475 
        A7 = -0.7361; A8 = 0.1844; A9 = 0.1056 
        A10 = 0.6134; A11 = 0.7210
        term1 = A1 + A2/tpr + A3/tpr3 + A4/tpr4 + A5/tpr5
        term2 = A6 + A7/tpr +A8/tpr2 
        term3 = A9 * (A7/tpr + A8/tpr2)
        termz = 0.27*ppr/tpr
        def func(y):
            y2 = y*y; y5 = y2 * y2 * y
            return 1.0 + term1*y + term2*y2 - term3*y5 + A10*(1+A11*y2)*(y2/tpr3)*np.exp(-A11*y2) - termz/y
        
        if tpr < 1.25:
            if ppr > 0.8 and ppr < 4.0:
                termz = termz * 3
        root = fsolve(func, termz)
        z = 0.27 * ppr/(tpr*root[0])

    return z


def Z_factor_hall_yarborough(tpr: float, ppr: float) -> float:
    if tpr < 1.01: 
        tpr = 1.0
    rT = 1.0/tpr
    A =  0.06125 * rT * np.exp(-1.2 * np.power(1.0 - rT, 2))
    B = rT * (14.76 - 9.76 * rT + 4.58 * rT * rT)
    C = rT * (90.7 - 242.2 * rT + 42.4 * rT * rT)
    D = 2.18 + 2.82 * rT
    def f(x):
        res = -A * ppr + (x + x * x + np.power(x, 3) - np.power(x, 4)) / np.power(1.0 - x, 3) - B * x * x + C * np.power(x, D)
        return res
    
    def dydx(x):
        df = (1.0 + 4.0 * x + 4.0 * x * x - 4.0 * np.power(x, 3) + np.power(x, 4)) / np.power(1.0 - x, 4) - 2.0 * B * x + D * C * np.power(x, D - 1.0)
        return df

    y = 0.001   # y is reduced density
    converged = False
    for i in range(25):
        if y > 1.0:
            y = 0.6
        f_val = f(y)
        if abs(f_val) <= 1e-8:
            converged = True
            break
        df_val = dydx(y)
        y = y - f_val/df_val
    
    z = 0.0
    if converged:
        z = A * ppr/y
    
    return z

def Beggs_Brill_zfactor(tpr: float, ppr: float) -> float:
    A = 1.39 * np.power(tpr - 0.92, 0.5) - 0.36 * tpr - 0.101
    B = ppr * (0.62 - 0.23 * tpr) + np.power(ppr, 2) * (0.066 / (tpr - 0.86) - 0.037) + 0.32 * np.power(ppr, 6) / np.exp(20.723 * (tpr - 1))
    C = 0.132 - 0.32 * np.log10(tpr)
    D = np.exp(0.715 - 1.128 * tpr + 0.42 * np.power(tpr, 2))
    z = A + (1 - A) * np.exp(-B) + C * np.power(ppr, D)
    
    return z


def wang_z_factor(tpr: float, ppr: float) -> float:
    A1 = 256.41675; A2 = 7.18202; A3 = -178.57250; A4 = 182.98704; A5 = -40.74427
    A6 = 2.24427; A7 = 47.44825; A8 = 5.28520; A9 = -0.14914; A10 = 271.50446
    A11 = 16.26940; A12 = -121.51728; A13 = 167.71477; A14 = -81.73093; A15 = 20.36191
    A16 = -2.11770; A17 = 124.64444; A18 = -6.74331; A19 = 0.20897; A20 = -0.00314
    
    tpr2 = tpr * tpr; tpr3 = tpr2 * tpr; tpr4 = tpr3 * tpr; tpr5 = tpr4 * tpr
    ppr2 = ppr * ppr; ppr3 = ppr2 * ppr; ppr4 = ppr3 * ppr; ppr5 = ppr4 * ppr
    num = A1 + A2*(1 + A3*tpr + A4*tpr2 + A5*tpr3 + A6*tpr4)*ppr + A7*ppr2 + A8*ppr3 + A9*ppr4
    denom = A10 + A11*(1 + A12*tpr + A13*tpr2 + A14*tpr3 + A15*tpr4 + A16*tpr5)*ppr + A17*ppr2 + A18*ppr3 + A19*ppr4 + A20*ppr5

    z = num /denom
    return z

#endregion


#region Pseudocritical Properties
def compute_pseudocritical_props(gas_gravity: float, yco2: float, yh2s: float, gas_type: Gas_Type = Gas_Type.NATURAL, pseudo_corr: Pseudocritical_Props = Pseudocritical_Props.STANDING) -> List[float]:
    if pseudo_corr == Pseudocritical_Props.STANDING:
        return pseudocrit_pT_standing(gas_gravity, yco2, yh2s, gas_type)
    elif pseudo_corr == Pseudocritical_Props.SUTTON:
        return pseudocrit_pT_sutton(gas_gravity, yco2, yh2s, gas_type)


def pseudocrit_pT_standing(gas_gravity: float, yco2: float, yh2s: float, gastype: Gas_Type = Gas_Type.NATURAL) -> List[float]:
    ppc = 0.0; tpc = 0.0
    gas_gravity2 = gas_gravity*gas_gravity
    if gastype == Gas_Type.NATURAL:
        ppc = 677.0 + 15.0 * gas_gravity - 37.5 * gas_gravity2
        tpc = 168.0 + 325.0 * gas_gravity - 12.5 * gas_gravity2
    elif gastype == Gas_Type.CONDENSATE:
        ppc = 706.0 - 51.7 * gas_gravity - 11.1 * gas_gravity2
        tpc = 187.0 + 330 * gas_gravity - 71.5 * gas_gravity2
    if yh2s*100 > 5 and yco2*100 > 5:
        tpc, ppc = wichert_aziz_nonhydrocarbon_correction(tpc, ppc, yco2, yh2s)
    return [tpc, ppc]


def pseudocrit_pT_sutton(gas_gravity: float, yco2: float, yh2s: float, gastype: Gas_Type = Gas_Type.NATURAL) -> List[float]:
    ppc = 0.0; tpc = 0.0
    gas_gravity2 = gas_gravity * gas_gravity
    if gastype == Gas_Type.NATURAL:
        ppc = 120.1 + 425.0 * gas_gravity - 62.9 * gas_gravity2
        tpc = 671.1 + 14.0 * gas_gravity - 34.3 * gas_gravity2
    elif gastype == Gas_Type.CONDENSATE:
        ppc = 164.3 + 357.7 * gas_gravity - 67.7 * gas_gravity2
        tpc = 706.0 - 51.70 * gas_gravity - 11.1 * gas_gravity2
    
    corr_tpc, corr_ppc = wichert_aziz_nonhydrocarbon_correction(tpc, ppc, yco2, yh2s)
    return [corr_tpc, corr_ppc]
    

def wichert_aziz_nonhydrocarbon_correction(tpc: float, ppc: float, yco2: float, yh2s: float) -> List[float]:
    new_ppc = ppc
    new_tpc = tpc

    if yco2 != 0.0 and yh2s != 0.0:
        # yh2s = yh2s*100
        # yco2 = yco2*100
        A = yh2s + yco2
        eps = 120.0 * (np.power(A, 0.9) - np.power(A, 1.6)) + 15.0 * (np.power(yh2s, 0.5) - np.power(yh2s, 4.0))
        new_tpc = tpc - eps
        new_ppc = ppc * new_tpc/(tpc + yh2s * (1 - yh2s) * eps)
    
    return [new_tpc, new_ppc]



#endregion
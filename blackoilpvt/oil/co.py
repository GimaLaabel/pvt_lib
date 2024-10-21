import numpy as np

def vazquez_beggs_Undersat_co(P: float, T: float, API: float, gasgravity: float, Rsb: float, P_sep: float, T_sep: float)->float:
    yg100 = gas_gravity_100(gasgravity, API, P_sep, T_sep)
    A = np.power(10.0, -5) * (5 *Rsb + 17.2 * T - 1180 * yg100 + 12.61 * API - 1433)
    return A/P

def gas_gravity_100(gasgravity: float, API: float, P_sep: float, T_sep: float) -> float:
    yg100 = gasgravity * (1 + 0.00005912 * API * T_sep * np.log10(P_sep/114.7))
    return yg100
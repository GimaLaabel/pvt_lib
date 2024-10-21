import numpy as np


def gas_gravity_100(gasgravity: float, API: float, P_sep: float, T_sep: float) -> float:
    yg100 = gasgravity * (1 + 0.00005912 * API * T_sep * np.log10(P_sep/114.7))
    return yg100


if __name__ == "__main__":
    pass
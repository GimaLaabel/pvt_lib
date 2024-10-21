
def gas_density(P: float, T: float, gas_gravity: float, Z: float) -> float:
    Z = round(Z, 5)
    rhoG = 2.7 * gas_gravity * P/(Z * (T + 459.67))
    return rhoG





def oil_density(API: float, gas_gravity: float,  rs: float, bo: float) -> float:
    yo = 141.5/(131.5 + API)
    rhoO = (62.4 * yo + 0.0136 * rs * gas_gravity)/bo
    return rhoO
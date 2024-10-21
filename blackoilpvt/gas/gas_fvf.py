def gas_fvf(P: float, T: float, Z: float) -> float:
    bg = 0.0283 * Z * (T + 459.67)/P
    return bg
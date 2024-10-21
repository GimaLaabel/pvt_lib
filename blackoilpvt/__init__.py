# import oil
# import commons
from blackoilpvt.oil.pb import compute_Pb
from blackoilpvt.oil.rs import compute_Rs
from blackoilpvt.oil.bo import compute_bo
from .commons import Black_oil_corr, Oil_viscosity_corr, Separator_Stage, Series_Type, get_series

from blackoilpvt.oil.oil_viscosity import compute_oil_viscosity, beal_oil_viscosity, beggs_robinson_oil_viscosity

from .oil import oil_density

from .gas.z_factor import compute_zfactor, compute_pseudocritical_props

from .gas.gas_density import gas_density
from .gas.gas_fvf import gas_fvf


# __all__ = ["oil", "gas", "commons"]
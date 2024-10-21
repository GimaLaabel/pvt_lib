from enum import Enum, auto


class Black_oil_corr(Enum):
    ALMARHOUN = auto()
    GLASO = auto()
    # LASATER = auto()
    PETROSKEY = auto()
    STANDING = auto()
    VAZQUEZ_BEGGS = auto()

class Fluid_Type(Enum):
    OIL = auto()
    GAS = auto()
    CONDENSATE = auto()

class Gas_Type(Enum):
    NATURAL = auto()
    CONDENSATE = auto()

class Oil_viscosity_corr(Enum):
    BEAL = auto()
    BEGGS_ROBINSON = auto()
    BERGMAN_SUTTON = auto()

class Pseudocritical_Props(Enum):
    STANDING = auto()
    SUTTON = auto()

class Separator_Stage(Enum):
    ONE_STAGE = auto()
    TWO_STAGE = auto()
    THREE_STAGE = auto()

class Series_Type(Enum):
    LINEAR = auto()
    GEOMETRIC = auto()

class Z_Factor_corr(Enum):
    BEGGS_BRILL = auto()
    DAK = auto()
    HALLYARBOROUGH = auto()
    WANG = auto()

if __name__ == "__main__":
    print(Fluid_Type.CONDENSATE.value)


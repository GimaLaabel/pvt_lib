from blackoilpvt import Black_oil_corr, Oil_viscosity_corr, Separator_Stage
from blackoilpvt import compute_Pb, compute_Rs, compute_bo
from blackoilpvt import compute_oil_viscosity, oil_density
from blackoilpvt import compute_pseudocritical_props, compute_zfactor, gas_density, gas_fvf

# from blackoilpvt.oil.rs import compute_Rs
# from blackoilpvt.oil.bo import compute_bo
# from fluid import Fluid_Properties


class Fluid_Properties:
    pressure: float = -99.9
    temperature: float = -99.9
    Pb: float = -99.9
    Bo: float = -99.9
    Rs: float = -99.9
    muO: float = -99.9
    muG: float = -99.9
    rhoO: float = -99.9
    rhoG: float = -99.9
    z_factor: float = -99.9
    Tpr: float = -99.9
    Ppr: float = -99.9
    rhoG: float = -99.9
    bg: float = -99.9

    def __init__(self) -> None:
        pass


class Fluid:
    blackoil_corr: Black_oil_corr = Black_oil_corr.GLASO
    oil_viscosity_corr: Oil_viscosity_corr = Oil_viscosity_corr.BEAL
    water_gravity: float = 1.0
    pst: float = 14.7
    tst: float = 60
    P_sep: float = 14.7
    T_sep: float = 60
    fluid_properties: Fluid_Properties = Fluid_Properties()

    _pb_impurity_correction: bool = False
    # _yCO2 = 0.0
    # _yH2S = 0.0
    # _yN2 = 0.0

    yCO2 = 0.0
    yH2S = 0.0
    yN2 = 0.0

    
    def pb_impurity_correction(self):
        if self.yCO2 == 0 and self.yH2S == 0 and self.yN2 == 0:
            self._pb_impurity_correction = False
        else:
            self._pb_impurity_correction = True

    def __init__(self, API: float, gasgravity: float, watercut: float, GOR: float, salinity: float, 
                 watergravity: float = 1.0, yco2: float = 0.0, yh2s: float = 0.0, yn2: float = 0.0, 
                 sep_press: float = 14.7, CGR: float = 0.0, sep_stage: Separator_Stage = Separator_Stage.ONE_STAGE):
        self.Api = API
        self.gas_gravity = gasgravity
        self.wcut = watercut
        self.Rsb = GOR
        self.salinity = salinity
        self.water_gravity = watergravity
        self.yCO2 = yco2/100
        self.yH2S = yh2s/100
        self.yN2 = yn2/100
        self.P_sep = sep_press
        self.CGR = CGR
        self.sep_stage = sep_stage
        self.pb_impurity_correction()
        

    def set_blackoil_corr(self, blackoilcorr: Black_oil_corr) -> None:
        self.blackoil_corr = blackoilcorr
    
    def set_oil_viscosity_corr(self, oilviscositycorr: Oil_viscosity_corr) -> None:
        self.oil_viscosity_corr = oilviscositycorr
    
    def get_local_properties(self, P: float, T: float) -> Fluid_Properties:
        pvt_result = Fluid_Properties()
        API = self.Api
        gas_grav = self.gas_gravity
        rsb = self.Rsb
        yco2 = self.yCO2
        yh2s = self.yH2S
        yn2 = self.yN2
        psep = self.P_sep
        tsep = self.T_sep
        pst = self.pst
        pb_impurity = self._pb_impurity_correction
        blackoilcorr = self.blackoil_corr

        pvt_result.Pb = compute_Pb(blackoilcorr, T, API, gas_grav, rsb, yco2, yh2s, yn2, pb_impurity)
        
        pvt_result.Rs = compute_Rs(blackoilcorr, P, T, API, gas_grav, pvt_result.Pb , rsb, pst, psep, tsep)

        pvt_result.Bo = compute_bo(blackoilcorr, P, T, API, gas_grav, psep, tsep, pvt_result.Pb, pvt_result.Rs, rsb,)

        pvt_result.muO = compute_oil_viscosity(self.oil_viscosity_corr, P, T, API, pvt_result.Pb, pvt_result.Rs, rsb)

        pvt_result.rhoO = oil_density(API, gas_grav, pvt_result.Rs, pvt_result.Bo)

        tpc, ppc = compute_pseudocritical_props(gas_grav, yco2, yh2s)
        tpr = (T + 460) / (tpc-6)
        ppr = P / (ppc-5)        
        pvt_result.Tpr = tpr
        pvt_result.Ppr = ppr
        pvt_result.z_factor = compute_zfactor(tpr, ppr)
        pvt_result.rhoG = gas_density(P, T, gas_grav, pvt_result.z_factor)
        pvt_result.bg = gas_fvf(P, T, pvt_result.z_factor)

        self.fluid_properties.Pb = pvt_result.Pb
        self.fluid_properties.Rs = pvt_result.Rs
        self.fluid_properties.Bo = pvt_result.Bo
        self.fluid_properties.muO = pvt_result.muO
        self.fluid_properties.z_factor = pvt_result.z_factor

        return pvt_result


if __name__ == "__main__":
    pass






    

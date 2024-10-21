from blackoilpvt import Black_oil_corr
from blackoilpvt.fluid import Fluid


Api1 = 20.651
GOR1 = 154
gas_gravity1 = 0.65
yCO21 = 1.04
yH2S1 = 0.0
yN21 = 0.21
wcut1 = 0.0
salinity1 = 0.39
water_grav1 = 1.0

print("===============  Sample1  =======================")
print("==  Below Bubble point  ==")

fluid1 = Fluid(Api1, gas_gravity1, wcut1, GOR1, salinity1, water_grav1, yCO21, yH2S1, yN21)
P1, T1 = 15, 141
fluid1.set_blackoil_corr(Black_oil_corr.VAZQUEZ_BEGGS)
fluid1.get_local_properties(P1, T1)
print(f""" 
    For Pressure = {P1}, Temperature = {T1} and Correlation = {fluid1.blackoil_corr} :  
    Pb = {fluid1.fluid_properties.Pb}       1461.62	
    Rs = {fluid1.fluid_properties.Rs}       1.02904	
    Bo = {fluid1.fluid_properties.Bo}       1.04864
""")

fluid1 = Fluid(Api1, gas_gravity1, wcut1, GOR1, salinity1, water_grav1, yCO21, yH2S1, yN21)
P1, T1 = 67.275, 141
fluid1.set_blackoil_corr(Black_oil_corr.VAZQUEZ_BEGGS)
fluid1.get_local_properties(P1, T1)
print(f""" 
    For Pressure = {P1}, Temperature = {T1} and Correlation = {fluid1.blackoil_corr} :  
    Pb = {fluid1.fluid_properties.Pb}       1461.62	
    Rs = {fluid1.fluid_properties.Rs}       5.31208	
    Bo = {fluid1.fluid_properties.Bo}       1.05043
""")

print("==  Above Bubble point  ==")

fluid1 = Fluid(Api1, gas_gravity1, wcut1, GOR1, salinity1, water_grav1, yCO21, yH2S1, yN21)
P1, T1 = 2106, 141
fluid1.set_blackoil_corr(Black_oil_corr.VAZQUEZ_BEGGS)
fluid1.get_local_properties(P1, T1)
print(f""" 
    For Pressure = {P1}, Temperature = {T1} and Correlation = {fluid1.blackoil_corr} :  
    Pb = {fluid1.fluid_properties.Pb}       1461.62
    Rs = {fluid1.fluid_properties.Rs}       154
    Bo = {fluid1.fluid_properties.Bo}       1.10829
""")

fluid1 = Fluid(Api1, gas_gravity1, wcut1, GOR1, salinity1, water_grav1, yCO21, yH2S1, yN21)
P1, T1 = 3500, 141
fluid1.set_blackoil_corr(Black_oil_corr.VAZQUEZ_BEGGS)
fluid1.get_local_properties(P1, T1)
print(f""" 
    For Pressure = {P1}, Temperature = {T1} and Correlation = {fluid1.blackoil_corr} :  
    Pb = {fluid1.fluid_properties.Pb}       1461.62
    Rs = {fluid1.fluid_properties.Rs}       154
    Bo = {fluid1.fluid_properties.Bo}       1.10445
""")

print("===============  Sample 2  =======================")
print("==  Below Bubble point  ==")

Api = 19.5
GOR = 197
gas_gravity = 0.571914
yCO2 = 0.38  # percent
yH2S = 0.0
yN2 = 0.11
wcut = 0.0
salinity = 0.35
water_grav = 1.0

fluid2 = Fluid(Api, gas_gravity, wcut, GOR, salinity, water_grav,yCO2, yH2S, yN2,)
P, T = 15, 139
fluid2.set_blackoil_corr(Black_oil_corr.VAZQUEZ_BEGGS)
fluid2.get_local_properties(P, T)
print(f"""  
    For Pressure = {P}, Temperature = {T} and Correlation = {fluid2.blackoil_corr} :
    Pb = {fluid2.fluid_properties.Pb}       2139.69	
    Rs = {fluid2.fluid_properties.Rs}       0.86767
    Bo = {fluid2.fluid_properties.Bo}       1.05063
""")

fluid2 = Fluid(Api, gas_gravity, wcut, GOR, salinity, water_grav,yCO2, yH2S, yN2,)
P, T = 69.85, 139
fluid2.set_blackoil_corr(Black_oil_corr.VAZQUEZ_BEGGS)
fluid2.get_local_properties(P, T)
print(f"""  
    For Pressure = {P}, Temperature = {T} and Correlation = {fluid2.blackoil_corr} :
    Pb = {fluid2.fluid_properties.Pb}       2139.69	
    Rs = {fluid2.fluid_properties.Rs}       4.66688
    Bo = {fluid2.fluid_properties.Bo}       1.05221
""")

print("==  Above Bubble point  ==")
fluid2 = Fluid(Api, gas_gravity, wcut, GOR, salinity, water_grav,yCO2, yH2S, yN2,)
P, T = 2209, 139
fluid2.set_blackoil_corr(Black_oil_corr.VAZQUEZ_BEGGS)
fluid2.get_local_properties(P, T)
print(f"""  
    For Pressure = {P}, Temperature = {T} and Correlation = {fluid2.blackoil_corr} :
    Pb = {fluid2.fluid_properties.Pb}       2139.69
    Rs = {fluid2.fluid_properties.Rs}       197
    Bo = {fluid2.fluid_properties.Bo}       1.13162
""")

fluid2 = Fluid(Api, gas_gravity, wcut, GOR, salinity, water_grav,yCO2, yH2S, yN2,)
P, T = 3500, 139
fluid2.set_blackoil_corr(Black_oil_corr.VAZQUEZ_BEGGS)
fluid2.get_local_properties(P, T)
print(f"""  
    For Pressure = {P}, Temperature = {T} and Correlation = {fluid2.blackoil_corr} :
    Pb = {fluid2.fluid_properties.Pb}       2139.69
    Rs = {fluid2.fluid_properties.Rs}       197
    Bo = {fluid2.fluid_properties.Bo}       1.12174
""")

# print("===============  Test  =======================")

# Api = 36.4
# GOR = 594
# gas_gravity = 0.878
# yCO2 = 0.17  # percent
# yH2S = 0.0
# yN2 = 0.22
# wcut = 0.0
# salinity = 1.0
# water_grav = 1.0

# fluid2 = Fluid(Api, gas_gravity, wcut, GOR, salinity, water_grav,yCO2, yH2S, yN2,)
# Ps, Ts = 2000, 150
# fluid2.set_blackoil_corr(Black_oil_corr.VAZQUEZ_BEGGS)
# fluid2.get_local_properties(Ps, Ts)
# print(f"""  
#     For Pressure = {Ps}, Temperature = {Ts} and Correlation = {fluid2.blackoil_corr} :
#     Pb = {fluid2.fluid_properties.Pb}
#     Rs = {fluid2.fluid_properties.Rs} 
#     Bo = {fluid2.fluid_properties.Bo}
# """)



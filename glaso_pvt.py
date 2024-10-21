from blackoilpvt.fluid import Fluid
from blackoilpvt.commons import Black_oil_corr


Api1 = 20.651
GOR1 = 154
gas_gravity1 = 0.65
yCO21 = 1.04
yH2S1 = 0.0
yN21 = 0.21
wcut1 = 0.0
salinity1 = 0.39
water_grav1 = 1.0

print("===============  Sample 1  =======================")
print("==  Below Bubble point  ==")

fluid1 = Fluid(Api1, gas_gravity1, wcut1, GOR1, salinity1, water_grav1,yCO21, yH2S1, yN21)
P1, T1 = 15, 141
fluid1.set_blackoil_corr(Black_oil_corr.GLASO)
fluid1.get_local_properties(P1, T1)
print(f""" 
    For Pressure = {P1}, Temperature = {T1} and Correlation = {fluid1.blackoil_corr} :  
    Pb = {fluid1.fluid_properties.Pb}       1649.07  
    Rs = {fluid1.fluid_properties.Rs}       3.63526
    Bo = {fluid1.fluid_properties.Bo}       1.02452
    Z = {fluid1.fluid_properties.z_factor}
""")

fluid1 = Fluid(Api1, gas_gravity1, wcut1, GOR1, salinity1, water_grav1,yCO21, yH2S1, yN21)
P1, T1 = 67.275, 141
fluid1.set_blackoil_corr(Black_oil_corr.GLASO)
fluid1.get_local_properties(P1, T1)
print(f""" 
    For Pressure = {P1}, Temperature = {T1} and Correlation = {fluid1.blackoil_corr} :  
    Pb = {fluid1.fluid_properties.Pb}       1649.07  
    Rs = {fluid1.fluid_properties.Rs}       9.92572
    Bo = {fluid1.fluid_properties.Bo}       1.02611
    Z = {fluid1.fluid_properties.z_factor}
""")
    
print("==  Above Bubble point  ==")

fluid1 = Fluid(Api1, gas_gravity1, wcut1, GOR1, salinity1, water_grav1,yCO21, yH2S1, yN21)
P1, T1 = 2106, 141
fluid1.set_blackoil_corr(Black_oil_corr.GLASO)
fluid1.get_local_properties(P1, T1)
print(f""" 
    For Pressure = {P1}, Temperature = {T1} and Correlation = {fluid1.blackoil_corr} :  
    Pb = {fluid1.fluid_properties.Pb}       1649.07
    Rs = {fluid1.fluid_properties.Rs}       154
    Bo = {fluid1.fluid_properties.Bo}       1.06731
    Z = {fluid1.fluid_properties.z_factor}
""")

fluid1 = Fluid(Api1, gas_gravity1, wcut1, GOR1, salinity1, water_grav1,yCO21, yH2S1, yN21)
P1, T1 = 3500, 141
fluid1.set_blackoil_corr(Black_oil_corr.GLASO)
fluid1.get_local_properties(P1, T1)
print(f""" 
    For Pressure = {P1}, Temperature = {T1} and Correlation = {fluid1.blackoil_corr} :  
    Pb = {fluid1.fluid_properties.Pb}       1649.07
    Rs = {fluid1.fluid_properties.Rs}       154
    Bo = {fluid1.fluid_properties.Bo}       1.06314
    Z = {fluid1.fluid_properties.z_factor}
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
P, T =  15, 139
fluid2.set_blackoil_corr(Black_oil_corr.GLASO)
fluid2.get_local_properties(P, T)
print(f"""  
    For Pressure = {P}, Temperature = {T} and Correlation = {fluid2.blackoil_corr} :
    Pb = {fluid2.fluid_properties.Pb}       2439.64
    Rs = {fluid2.fluid_properties.Rs}       2.99277
    Bo = {fluid2.fluid_properties.Bo}       1.02372
    Z = {fluid2.fluid_properties.z_factor}
""")

fluid2 = Fluid(Api, gas_gravity, wcut, GOR, salinity, water_grav,yCO2, yH2S, yN2,)
P, T =  69.85, 139
fluid2.set_blackoil_corr(Black_oil_corr.GLASO)
fluid2.get_local_properties(P, T)
print(f"""  
    For Pressure = {P}, Temperature = {T} and Correlation = {fluid2.blackoil_corr} :
    Pb = {fluid2.fluid_properties.Pb}       2439.64
    Rs = {fluid2.fluid_properties.Rs}       8.39303
    Bo = {fluid2.fluid_properties.Bo}       1.02498
    Z = {fluid2.fluid_properties.z_factor}
""")

print("==  Above Bubble point  ==")
fluid2 = Fluid(Api, gas_gravity, wcut, GOR, salinity, water_grav,yCO2, yH2S, yN2,)
P, T =  2538.1, 139
fluid2.set_blackoil_corr(Black_oil_corr.GLASO)
fluid2.get_local_properties(P, T)
print(f"""  
    For Pressure = {P}, Temperature = {T} and Correlation = {fluid2.blackoil_corr} :
    Pb = {fluid2.fluid_properties.Pb}       2439.64
    Rs = {fluid2.fluid_properties.Rs}       197
    Bo = {fluid2.fluid_properties.Bo}       1.07913
    Z = {fluid2.fluid_properties.z_factor}
""")

fluid2 = Fluid(Api, gas_gravity, wcut, GOR, salinity, water_grav,yCO2, yH2S, yN2,)
P, T =  5500, 139
fluid2.set_blackoil_corr(Black_oil_corr.GLASO)
fluid2.get_local_properties(P, T)
print(f"""  
    For Pressure = {P}, Temperature = {T} and Correlation = {fluid2.blackoil_corr} :
    Pb = {fluid2.fluid_properties.Pb}       2439.64
    Rs = {fluid2.fluid_properties.Rs}       197
    Bo = {fluid2.fluid_properties.Bo}       1.07071
    Z = {fluid2.fluid_properties.z_factor}
""")


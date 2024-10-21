from blackoilpvt import Black_oil_corr, Oil_viscosity_corr, Series_Type, get_series
from blackoilpvt.fluid import Fluid
import csv


#region Sample1
Api1 = 20.651
GOR1 = 154
gas_gravity1 = 0.65
yCO21 = 1.04
yH2S1 = 0.0
yN21 = 0.21
wcut1 = 0.0
salinity1 = 0.39
water_grav1 = 1.0
# set pressures and temperatures
p_start, p_end, T = 15, 3500, 141
num_elements = 201
#endregion

#region Sample2
# Api1 = 19.5
# GOR1 = 197
# gas_gravity1 = 0.571914
# yCO21 = 0.38
# yH2S1 = 0.0
# yN21 = 0.11
# wcut1 = 0.0
# salinity1 = 0.35
# water_grav1 = 1.0
# # set pressures and temperatures
# p_start, p_end, T = 15, 5500, 139
# num_elements = 201
#endregion


fluid1 = Fluid(Api1, gas_gravity1, wcut1, GOR1, salinity1, water_grav1,yCO21, yH2S1, yN21)
fluid1.set_blackoil_corr(Black_oil_corr.GLASO)
fluid1.set_oil_viscosity_corr(Oil_viscosity_corr.BEAL)


series = Series_Type.LINEAR
P_series = get_series(series, p_start, p_end, num_elements)
# print(f"{P_series = }")

blackoil_enum_names = [member.name for member in Black_oil_corr ]
# print(blackoil_enum_names)
oilviscosity_enum_names = [member.name for member in Oil_viscosity_corr]
# print(oilviscosity_enum_names)

for oil_visc in oilviscosity_enum_names:
    fluid1.set_oil_viscosity_corr(Oil_viscosity_corr[oil_visc])

    for oil_corr in blackoil_enum_names:
        fluid1.set_blackoil_corr(Black_oil_corr[oil_corr])
        file_path = "./results/sample1/"+ str.lower(fluid1.oil_viscosity_corr.name)  +"_"+ str.lower(fluid1.blackoil_corr.name)+ ".csv"

        file = open(file_path, mode='w', newline='')
        writer = csv.writer(file)
        header = [["Temperature", "Pressure", "Bubble point", "Gas oil ratio", 
                   "Oil FVF", "Oil Viscosity", "Z Factor", "Gas FVF", "Oil Density", "Gas density"],
                  ["(deg F)", "(psia)", "(psia)", "(Scf/STB)", "(RB/STB)", "(cp)", "", "RB/Scf", "Kg/m3", "Kg/m3"]]
        writer.writerows(header)

        for p in P_series:
            pvt_result = fluid1.get_local_properties(p, T)
            result_row = [[T, p, round(pvt_result.Pb, 2), round(pvt_result.Rs, 5), round(pvt_result.Bo, 5), round(pvt_result.muO, 4), round(pvt_result.z_factor, 5), round(pvt_result.bg * 0.1781076067, 5), round(pvt_result.rhoO * 16.0185, 3), round(pvt_result.rhoG * 16.0185, 5)]]
            writer.writerows(result_row)
            # print(f""" 
            #     For Pressure = {p}, Temperature = {T}:  
            #     Pb = {pvt_result.Pb}   
            #     Rs = {pvt_result.Rs}  
            #     Bo = {pvt_result.Bo}   
            #     muO = {pvt_result.muO}
            # """)
        file.close()
        print("Pvt results written to file")        


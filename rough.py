import numpy as np
from scipy.optimize import fsolve

def func(x:float):
    return x**4 - 3/x - 2

root = fsolve(func, 1.5)
print(root)




# from enum import Enum, auto

# pressure = []
# pressure.append(15)
# print(pressure)

# a, b = [3,4]
# print(f"{a} and {b}")
# import pandas as pd

# # Data for different sheets
# data1 = {
#     'Name': ['Alice', 'Bob', 'Charlie'],
#     'Age': [30, 25, 35],
#     'City': ['New York', 'Los Angeles', 'Chicago']
# }

# data2 = {
#     'Product': ['Apples', 'Bananas', 'Cherries'],
#     'Quantity': [10, 20, 30],
#     'Price': [1.5, 0.5, 2.0]
# }

# data3 = {
#     'Country': ['USA', 'Canada', 'Mexico'],
#     'Capital': ['Washington D.C.', 'Ottawa', 'Mexico City'],
#     'Population': [331, 38, 128]  # in millions
# }

# # Create DataFrames
# df1 = pd.DataFrame(data1)
# df2 = pd.DataFrame(data2)
# df3 = pd.DataFrame(data3)

# # File path
# file_path = './results/output.xlsx'

# # Write data to multiple sheets
# with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
#     df1.to_excel(writer, sheet_name='Sheet1', index=False)
#     df2.to_excel(writer, sheet_name='Sheet2', index=False)
#     df3.to_excel(writer, sheet_name='Sheet3', index=False)

# print(f"Data has been written to {file_path}")




# import csv

# # Data to be written to the CSV file
# data = [
#     ['Name', 'Age', 'City'],
#     ['Alice', 30, 'New York'],
#     ['Bob', 25, 'Los Angeles'],
#     ['Charlie', 35, 'Chicago']
# ]

# # File path
# file_path = './results/output.csv'

# # Open the file in write mode
# file = open(file_path, mode='w', newline='')

# # Create a CSV writer object
# writer = csv.writer(file)

# # Write the data to the CSV file
# writer.writerows(data)

# # Close the file
# file.close()

# print(f"Data has been written to {file_path}")

# import csv

# # Perform calculations and store results
# results = []
# for i in range(10):
#     calculation = i ** 2
#     results.append({'Index': i, 'Square': calculation})

# # Specify the CSV file name
# csv_file = 'results.csv'

# # Write results to CSV file
# with open(csv_file, mode='w', newline='') as file:
#     fieldnames = ['Index', 'Square']
#     writer = csv.DictWriter(file, fieldnames=fieldnames)
    
#     writer.writeheader()  # Write the header row
#     writer.writerows(results)  # Write the data rows

# print(f'Results have been written to {csv_file}')

# import csv

# # Perform calculations and store results
# results = []
# for i in range(10):
#     calculation = i ** 2
#     results.append((i, calculation))

# # Specify the CSV file name
# csv_file = 'results2.csv'

# # Write results to CSV file
# with open(csv_file, mode='w', newline='') as file:
#     writer = csv.writer(file)
    
#     writer.writerow(['Index', 'Square'])  # Write the header row
#     writer.writerows(results)  # Write the data rows

# print(f'Results have been written to {csv_file}')

# class Oil_corr(Enum):
#     ALMARHOUN = auto()
#     GLASO = auto()
#     PETROSKEY = auto()
#     STANDING = auto()
#     VAZQUEZ_BEGGS = auto()

# members = [member.name for member in Oil_corr]
# print(members)
# print(Oil_corr["ALMARHOUN"])
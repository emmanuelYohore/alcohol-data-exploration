import numpy as np


world_alcohol = np.genfromtxt("world_alcohol.csv",delimiter=",",dtype="U75", skip_header=1)

world_alcohol_2 = world_alcohol.copy()
is_canada_1986 = (world_alcohol_2[:,0] == "1986") & (world_alcohol_2[:,2] == "Canada")
canada_1986 = world_alcohol_2[is_canada_1986,:]

value_col_d = (canada_1986[:,4])
empty = value_col_d == ''
value_col_d[empty] = '0'
conv = value_col_d.astype(float)
print(conv)
print(conv.sum())


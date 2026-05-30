import numpy as np


world_alcohol = np.genfromtxt("world_alcohol.csv",delimiter=",",dtype="U75", skip_header=1)

world_alcohol_2 = world_alcohol.copy()
is_e = (world_alcohol_2[:,4] == '')
world_alcohol_2[is_e,4] = '0'

alco_consum = world_alcohol_2[:,4]
conv = alco_consum.astype(float)
print(conv.sum())
print(conv.mean())

import numpy as np


world_alcohol = np.genfromtxt("world_alcohol.csv",delimiter=",",dtype="U75", skip_header=1)

world_alcohol_2 = world_alcohol.copy()

total = {}
highest_value = 0
highest_key = None

is_1989 = world_alcohol_2[:,0] == "1989"
year = world_alcohol_2[is_1989,:]


countries = world_alcohol_2[:,2]

for country in countries:
   is_country = year[:,2] == country
   country_consum = year[is_country,:]
   col_consum = country_consum[:,4]
   is_empty = col_consum == ''
   col_consum[is_empty] = '0'
   conv = col_consum.astype(float)
   sum_col = conv.sum()
   total[str(country)] = float(sum_col)

highest_key =max(total,key=total.get)
highest_value = total[highest_key]
print(highest_value)



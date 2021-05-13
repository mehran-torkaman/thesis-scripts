import numpy as np
import math
#================================
# Inputs
#================================
min_deg = 0
max_deg = 181
data = np.loadtxt('dipole.in')
#======================
# Calculate Dipoles
#======================
rad = list()
result = list()
for i in range(len(data)):
    gamma = np.arccos(data[i][3]/data[i][4])
    rad.append(gamma)
for i in rad:
    result.append(np.degrees(i))
obj = dict()
for i in np.arange(min_deg,max_deg):
    obj[str(i)+'degree'] = []
for i in np.arange(min_deg,max_deg):
    for j in result:
        if j >= i and j < i+1:
            obj[str(i)+'degree'].append(1)
#======================
# OutPuts
#======================
degree = list()
for i in range(min_deg,max_deg):
    degree.append(i)
with open('degrees.txt', 'w') as f1:
    for item in degree:
        f1.write('%s\n' % item)
numbers = list()
for k,v in obj.items():
#    print(k,len(v))
    numbers.append(len(v))
with open('dipoles.txt', 'w') as f2:
    for item in numbers:
        f2.write('%s\n' % item)

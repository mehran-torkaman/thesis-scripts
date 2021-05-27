import numpy as np
import matplotlib.pyplot as plt
#===========================================
# Inputs
#===========================================
min_h = 0 #float(input('Enter your Minimum Height:'))
max_h = 44 #float(input('Enter your Maximum Height:'))
tickness = 44 #float(input('Enter your Bin Tickness:'))
#===================================================
# Load xyz file and create layering in z Axis
#===================================================
result = list()
for file in range(251):
    atom = np.loadtxt('0')
    obj = dict()
    obj['snap'+str(file)] = {}
    for j in np.arange(min_h,max_h,tickness):
        obj['snap'+str(file)]['chunk'+str(j)+'-'+str(j+tickness)] = []
    for k in np.arange(min_h,max_h,tickness):
        for i in range(len(atom)):
            if atom[i][3] >= k and atom[i][3] < k+tickness:
                if atom[i][0] == 2:
                    obj['snap'+str(file)]['chunk'+str(k)+'-'+str(k+tickness)].append(1)
#==============================================
# Calculating Atom numbers in Every z-layer
#==============================================
    for key,value in obj.items():
        for k,v in value.items():
            print(key,':',len(v))
            result.append(len(v))

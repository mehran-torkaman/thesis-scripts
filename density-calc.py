import numpy as np
import matplotlib.pyplot as plt
#===========================================
# Inputs
#===========================================
min_h = 0 #float(input('Enter your Minimum Height:'))
max_h = 44 #float(input('Enter your Maximum Height:'))
tickness = 0.25 #float(input('Enter your Bin Tickness:'))
channel_materials = 'phosphorene'
#============================================
# Coordination OutPuts
#============================================
z = list()
for i in np.arange(min_h,max_h,tickness):
    count = i + (tickness/2)
    z.append(count)
with open('z-dens.txt', 'w') as zout:
    for item in z:
        zout.write('%s\n' % item)
#===================================================
# Load xyz file and create layering in z Axis
#===================================================
atom = np.loadtxt('dump.xyz')
obj = dict()
for j in np.arange(min_h,max_h,tickness):
    obj['chunk'+str(j)+'-'+str(j+tickness)] = []
for k in np.arange(min_h,max_h,tickness):
    for i in range(len(atom)):
        if atom[i][3] >= k and atom[i][3] < k+tickness:
            if atom[i][0] == 2:
                obj['chunk'+str(k)+'-'+str(k+tickness)].append(1)
#==============================================
# Calculating Atom numbers in Every z-layer
#==============================================
result = list()
for k,v in obj.items():
    print(k,':',len(v))
    result.append(len(v))
with open('AtomNumbers.txt', 'w') as f:
    for item in result:
        f.write("%s\n" % item)
#================================================
# Calculating Atom Density in Every z-layer
#================================================
print('==================================================================')
volume = 57*58*tickness*10**(-30) # 57(A)*58(A)*2(A) 1(A^3) = 10^(-30)(m^3)
snapshots = 250
watermass = 2.9915*10**(-26) # kg
dens = list()
for item in result:
    d = ((item/volume)/snapshots)*watermass # kg/m3
    dens.append(d)
with open('Density.txt', 'w') as fout:
    for item in dens:
        fout.write("%s\n" % item)
#====================
# Plot Sides
#====================
x = list()
y = list()

for item in z:
    x.append(item)

for item in dens:
    y.append(item)
ticks = list()
for i in range(min_h,max_h+2,2):
    ticks.append(i)
plt.style.use('fivethirtyeight')
plt.plot(x,y,color='g',linestyle='-',marker='o',linewidth=2,label=channel_materials)
plt.title('Density Profile for Channel 40A')
plt.xlabel('Z (A)')
plt.xticks(ticks)
plt.ylabel('d (kg/m**3)')
plt.legend(loc=2)
plt.tight_layout()
plt.show()

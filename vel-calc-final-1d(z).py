from statistics import mean
import matplotlib.pyplot as plt
import numpy as np
#=======================================================================
#Calculate Velocity Profile
#=======================================================================
min_h = 0 #float(input('Enetr Your Minimum Height:'))
max_h = 44 #float(input('Enter Your Maximum Height:'))
tickness = 2 #float(input('Enter Your Bin Tickness:'))
channel_materials = 'phosphorene'
z = list()
for i in np.arange(min_h,max_h,tickness):
    count = i+(tickness/2)
    z.append(count)
with open('z-velocity.txt', 'w') as zout:
    for item in z:
        zout.write('%s\n' % item)
atom = np.loadtxt('veldump')
obj = dict()
for j in np.arange(min_h,max_h,tickness):
    obj['chunk'+str(j)+'-'+str(j+tickness)] = []
for k in np.arange(min_h,max_h,tickness):
    for i in range(len(atom)):
        if atom[i][8] >= k and atom[i][8] < k+tickness:
            if atom[i][2] == 2:
                obj['chunk'+str(k)+'-'+str(k+tickness)].append(atom[i][3])
results = list()
for j in np.arange(min_h,max_h,tickness):
    jam = sum(obj['chunk'+str(j)+'-'+str(j+tickness)])
    tedad = len(obj['chunk'+str(j)+'-'+str(j+tickness)])
    if tedad == 0:
        average =  0
    else:
        average = jam / tedad
    results.append(average)
    print('chunk'+str(j)+':',average)
with open('Vx-z.txt', 'w') as fout:
    for item in results:
        fout.write("%s\n" % item)
#=======================
# Plot Sides
#=======================
x = list()
y = list()

for item in z:
    x.append(item)

for item in results:
    y.append(item)
ticks = list()
for i in range(min_h,max_h+2,2):
    ticks.append(i)
plt.style.use('fivethirtyeight')
plt.plot(x,y,color='k',linestyle='-',marker='o',linewidth=2,label=channel_materials)
plt.title('Velocity Profile for Channel 40A')
plt.xlabel('Z (A)')
plt.xticks(ticks)
plt.ylabel('Vx (A/fs)')
plt.legend(loc=2)
plt.tight_layout()
plt.show()

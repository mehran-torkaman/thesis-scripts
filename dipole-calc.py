import numpy as np
from matplotlib import pyplot as plt
import matplotlib.mlab as mlab
from scipy.stats import norm
from math import sqrt
#=======================================
# Inputs
#=======================================
min_h = 0
max_h = 44
tickness = 44
Molecule_num = 4017
num = Molecule_num + 1
charge = 0.417
data = np.loadtxt('sample.txt')
#========================================
# Adding Atoms to their Molecules
#========================================
mols = dict()
for i in range(1,num):
    mols['molecule'+str(i)] = []
for j in range(len(data)):
    for i in range(1,num):
        if data[j][1] == i:
            mols['molecule'+str(i)].append(data[j][0])
for k,v in mols.items():
    v.sort(reverse=False)
#===============================================
# Adding Every Atom Coordinates in Molecules
#===============================================
obj = dict()
for i in range(1,num):
    obj['molecule'+str(i)] = {'H1':[],'O':[],'H2':[]}

for j in range(len(data)):
    for i in range(1,num):
        if data[j][0] == mols['molecule'+str(i)][0]:
            obj['molecule'+str(i)]['H1'].append(data[j][6])
            obj['molecule'+str(i)]['H1'].append(data[j][7])
            obj['molecule'+str(i)]['H1'].append(data[j][8])
        elif data[j][0] == mols['molecule'+str(i)][1]:
            obj['molecule'+str(i)]['H2'].append(data[j][6])
            obj['molecule'+str(i)]['H2'].append(data[j][7])
            obj['molecule'+str(i)]['H2'].append(data[j][8])
        elif data[j][0] == mols['molecule'+str(i)][2]:
            obj['molecule'+str(i)]['O'].append(data[j][6])
            obj['molecule'+str(i)]['O'].append(data[j][7])
            obj['molecule'+str(i)]['O'].append(data[j][8])
#======================================================
# Creating Dipole Vectors for every H-O Bond
#======================================================
dipoles = dict()
for i in range(1,num):
    dipoles['molecule'+str(i)] = []
for i in range(1,num):
    vector1 = list()
    vector2 = list()
    x1 = obj['molecule'+str(i)]['O'][0]-obj['molecule'+str(i)]['H1'][0]
    if sqrt(x1**2) > 1:
        if obj['molecule'+str(i)]['O'][0] > obj['molecule'+str(i)]['H1'][0]:
            obj['molecule'+str(i)]['O'][0] = obj['molecule'+str(i)]['O'][0] - 56.727
        elif obj['molecule'+str(i)]['H1'][0] > obj['molecule'+str(i)]['O'][0]:
            obj['molecule'+str(i)]['H1'][0] = obj['molecule'+str(i)]['H1'][0] - 56.727
        x1 = obj['molecule'+str(i)]['O'][0]-obj['molecule'+str(i)]['H1'][0]
    vector1.append(x1)
    y1 = obj['molecule'+str(i)]['O'][1]-obj['molecule'+str(i)]['H1'][1]
    if sqrt(y1**2) > 1:
        if obj['molecule'+str(i)]['O'][1] > obj['molecule'+str(i)]['H1'][1]:
            obj['molecule'+str(i)]['O'][1] = obj['molecule'+str(i)]['O'][1] - 56.916
        elif obj['molecule'+str(i)]['H1'][1] > obj['molecule'+str(i)]['O'][1]:
            obj['molecule'+str(i)]['H1'][1] = obj['molecule'+str(i)]['H1'][1] - 56.916
        y1 = obj['molecule'+str(i)]['O'][1]-obj['molecule'+str(i)]['H1'][1]
    vector1.append(y1)
    z1 = obj['molecule'+str(i)]['O'][2]-obj['molecule'+str(i)]['H1'][2]
    vector1.append(z1)
    x2 = obj['molecule'+str(i)]['O'][0]-obj['molecule'+str(i)]['H2'][0]
    if sqrt(x2**2) > 1:
        if obj['molecule'+str(i)]['O'][0] > obj['molecule'+str(i)]['H2'][0]:
            obj['molecule'+str(i)]['O'][0] = obj['molecule'+str(i)]['O'][0] - 56.727
        elif obj['molecule'+str(i)]['H2'][0] > obj['molecule'+str(i)]['O'][0]:
            obj['molecule'+str(i)]['H2'][0] = obj['molecule'+str(i)]['H2'][0] - 56.727
        x2 = obj['molecule'+str(i)]['O'][0]-obj['molecule'+str(i)]['H2'][0]
    vector2.append(x2)
    y2 = obj['molecule'+str(i)]['O'][1]-obj['molecule'+str(i)]['H2'][1]
    if sqrt(y2**2) > 1:
        if obj['molecule'+str(i)]['O'][1] > obj['molecule'+str(i)]['H2'][1]:
            obj['molecule'+str(i)]['O'][1] = obj['molecule'+str(i)]['O'][1] - 56.916
        elif obj['molecule'+str(i)]['H2'][1] > obj['molecule'+str(i)]['O'][1]:
            obj['molecule'+str(i)]['H2'][1] = obj['molecule'+str(i)]['H2'][1] - 56.916
        y2 = obj['molecule'+str(i)]['O'][1]-obj['molecule'+str(i)]['H2'][1]
    vector2.append(y2)
    z2 = obj['molecule'+str(i)]['O'][2]-obj['molecule'+str(i)]['H2'][2]
    vector2.append(z2)
    dipoles['molecule'+str(i)].append(charge*(vector1[0]+vector2[0]))
    dipoles['molecule'+str(i)].append(charge*(vector1[1]+vector2[1]))
    dipoles['molecule'+str(i)].append(charge*(vector1[2]+vector2[2]))
#===========================================
# Calculating magnitude of Dipole Vector
#===========================================
for i in range(1,num):
    x = dipoles['molecule'+str(i)][0]
    y = dipoles['molecule'+str(i)][1]
    z = dipoles['molecule'+str(i)][2]
    magnitude = sqrt((x**2)+(y**2)+(z**2))
    dipoles['molecule'+str(i)].append(magnitude)
#for i in range(1,num):
#    print(dipoles['molecule'+str(i)][3])
#===============================================
# Calculating Degree of Dipoles
#===============================================
rad = list()
for i in range(1,num):
    gamma = np.arccos(dipoles['molecule'+str(i)][2]/dipoles['molecule'+str(i)][3])
    rad.append(gamma)
result = list()
for i in rad:
    result.append(np.degrees(i))
degree = dict()
for i in range(1,num):
    degree['molecule'+str(i)]=result[i-1]
#=====================================
# Creating Chunks in z direction
#=====================================
z_chunks = dict()
for i in np.arange(min_h,max_h,tickness):
    z_chunks['chunk'+str(i)+'-'+str(i+tickness)] = {}
for i in np.arange(min_h,max_h,tickness):
    for j in range(0,181):
        z_chunks['chunk'+str(i)+'-'+str(i+tickness)]['degree'+str(j)] = []
#===============================================
# Adding every dipole degree to it's chunk
#===============================================
for i in np.arange(min_h,max_h,tickness):
    for j in range(1,num):
        if obj['molecule'+str(j)]['O'][2] >= i and obj['molecule'+str(j)]['O'][2] < i+tickness:
             for k in range(0,181):
                 if degree['molecule'+str(j)] >= k and degree['molecule'+str(j)] < k+1:
                     z_chunks['chunk'+str(i)+'-'+str(i+tickness)]['degree'+str(k)].append(1)
#========================
# Outputs
#========================
with open('dipole1.dat', 'w') as f:
    for key,value in z_chunks.items():
        for k,v in value.items():
            f.write('%s %s %s\n' % (key,k,len(v)))
#========================
# Plots
#========================
if tickness == max_h:
    numbers = list()
    bins = list()
    for i in range(0,181):
        bins.append(i)
    for k,value in z_chunks.items():
        for k,v in value.items():
            numbers.append(len(v))
    plot = list()
    for i in range(len(numbers)):
        tick = numbers[i]
        for j in range(tick):
            plot.append(bins[i])
    plt.style.use('fivethirtyeight')
    ticks=list()
    for i in range(0,181,10):
        ticks.append(i)
    _, bins, _ = plt.hist(plot, 180,facecolor='green',density = 1 ,alpha=0.5 ,edgecolor='black')
    mu, sigma = norm.fit(plot)
    best_fit_line = norm.pdf(bins, mu, sigma)
    plt.plot(bins, best_fit_line)
    plt.title('Distributions Of the Dipole Moment Orientation')
    plt.xlabel('Dipole Moment Orientation Angle')
    plt.xticks(ticks)
    plt.grid(True)
    plt.show()

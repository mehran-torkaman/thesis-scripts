import numpy as np
#==========================
# Inputs
#==========================
min_h = 0
max_h = 44
tickness = 1
min_y = 1.337
max_y = 58.253
#========================================
# Creating Steps in Y-Axis
#========================================
j = 0
step = min_y
l = list()
while True:
    l.append(step)
    if step > max_y:
        break
    elif j%2 == 0:
        j += 1
        step += 3.3
    else:
        j += 1
        step += 3.3
with open('y.txt', 'w') as yf:
    for i in l:
        yf.write('%s\n' % i)
#===================================================================
# Creating Bins and Putting Atom's Vx and Vy to their Bins
#===================================================================
vx = dict()
for z in np.arange(min_h,max_h,tickness):
    vx['chunk'+str(z)+'-'+str(z+tickness)] = {}
for z in np.arange(min_h,max_h,tickness):
    for j in range(1,19):
        vx['chunk'+str(z)+'-'+str(z+tickness)]['bin'+str(j)] = []
vy = dict()
for z in np.arange(min_h,max_h,tickness):
    vy['chunk'+str(z)+'-'+str(z+tickness)] = {}
for z in np.arange(min_h,max_h,tickness):
    for j in range(1,19):
        vy['chunk'+str(z)+'-'+str(z+tickness)]['bin'+str(j)] = []

atom = np.loadtxt('veldump')
for z in np.arange(min_h,max_h,tickness):
    for i in range(len(atom)):
        if z<=atom[i][6]<z+tickness:
            if atom[i][0] == 2:
                if l[0]<=atom[i][5]<l[1]:
                    vx['chunk'+str(z)+'-'+str(z+tickness)]['bin1'].append(atom[i][1])
                    vy['chunk'+str(z)+'-'+str(z+tickness)]['bin1'].append(atom[i][2])
                elif l[1]<=atom[i][5]<l[2]:
                    vx['chunk'+str(z)+'-'+str(z+tickness)]['bin2'].append(atom[i][1])
                    vy['chunk'+str(z)+'-'+str(z+tickness)]['bin2'].append(atom[i][2])
                elif l[2]<=atom[i][5]<l[3]:
                    vx['chunk'+str(z)+'-'+str(z+tickness)]['bin3'].append(atom[i][1])
                    vy['chunk'+str(z)+'-'+str(z+tickness)]['bin3'].append(atom[i][2])
                elif l[3]<=atom[i][5]<l[4]:
                    vx['chunk'+str(z)+'-'+str(z+tickness)]['bin4'].append(atom[i][1])
                    vy['chunk'+str(z)+'-'+str(z+tickness)]['bin4'].append(atom[i][2])
                elif l[4]<=atom[i][5]<l[5]:
                    vx['chunk'+str(z)+'-'+str(z+tickness)]['bin5'].append(atom[i][1])
                    vy['chunk'+str(z)+'-'+str(z+tickness)]['bin5'].append(atom[i][2])
                elif l[5]<=atom[i][5]<l[6]:
                    vx['chunk'+str(z)+'-'+str(z+tickness)]['bin6'].append(atom[i][1])
                    vy['chunk'+str(z)+'-'+str(z+tickness)]['bin6'].append(atom[i][2])
                elif l[6]<=atom[i][5]<l[7]:
                    vx['chunk'+str(z)+'-'+str(z+tickness)]['bin7'].append(atom[i][1])
                    vy['chunk'+str(z)+'-'+str(z+tickness)]['bin7'].append(atom[i][2])
                elif l[7]<=atom[i][5]<l[8]:
                    vx['chunk'+str(z)+'-'+str(z+tickness)]['bin8'].append(atom[i][1])
                    vy['chunk'+str(z)+'-'+str(z+tickness)]['bin8'].append(atom[i][2])
                elif l[8]<=atom[i][5]<l[9]:
                    vx['chunk'+str(z)+'-'+str(z+tickness)]['bin9'].append(atom[i][1])
                    vy['chunk'+str(z)+'-'+str(z+tickness)]['bin9'].append(atom[i][2])
                elif l[9]<=atom[i][5]<l[10]:
                    vx['chunk'+str(z)+'-'+str(z+tickness)]['bin10'].append(atom[i][1])
                    vy['chunk'+str(z)+'-'+str(z+tickness)]['bin10'].append(atom[i][2])
                elif l[10]<=atom[i][5]<l[11]:
                    vx['chunk'+str(z)+'-'+str(z+tickness)]['bin11'].append(atom[i][1])
                    vy['chunk'+str(z)+'-'+str(z+tickness)]['bin11'].append(atom[i][2])
                elif l[11]<=atom[i][5]<l[12]:
                    vx['chunk'+str(z)+'-'+str(z+tickness)]['bin12'].append(atom[i][1])
                    vy['chunk'+str(z)+'-'+str(z+tickness)]['bin12'].append(atom[i][2])
                elif l[12]<=atom[i][5]<l[13]:
                    vx['chunk'+str(z)+'-'+str(z+tickness)]['bin13'].append(atom[i][1])
                    vy['chunk'+str(z)+'-'+str(z+tickness)]['bin13'].append(atom[i][2])
                elif l[13]<=atom[i][5]<l[14]:
                    vx['chunk'+str(z)+'-'+str(z+tickness)]['bin14'].append(atom[i][1])
                    vy['chunk'+str(z)+'-'+str(z+tickness)]['bin14'].append(atom[i][2])
                elif l[14]<=atom[i][5]<l[15]:
                    vx['chunk'+str(z)+'-'+str(z+tickness)]['bin15'].append(atom[i][1])
                    vy['chunk'+str(z)+'-'+str(z+tickness)]['bin15'].append(atom[i][2])
                elif l[15]<=atom[i][5]<l[16]:
                    vx['chunk'+str(z)+'-'+str(z+tickness)]['bin16'].append(atom[i][1])
                    vy['chunk'+str(z)+'-'+str(z+tickness)]['bin16'].append(atom[i][2])
                elif l[16]<=atom[i][5]<l[17]:
                    vx['chunk'+str(z)+'-'+str(z+tickness)]['bin17'].append(atom[i][1])
                    vy['chunk'+str(z)+'-'+str(z+tickness)]['bin17'].append(atom[i][2])
                elif l[17]<=atom[i][5]<l[18]:
                    vx['chunk'+str(z)+'-'+str(z+tickness)]['bin18'].append(atom[i][1])
                    vy['chunk'+str(z)+'-'+str(z+tickness)]['bin18'].append(atom[i][2])
#==============================================================================
# Calculating Average Velocities for every bin in every z-chunk
#==============================================================================
vx_results = dict()
for z in np.arange(min_h,max_h,tickness):
    vx_results['chunk'+str(z)+'-'+str(z+tickness)] = {}

vy_results = dict()
for z in np.arange(min_h,max_h,tickness):
    vy_results['chunk'+str(z)+'-'+str(z+tickness)] = {}
#==============================================================================
# Compute Vx Averages
#==============================================================================
for z in np.arange(min_h,max_h,tickness):
    temp = dict()
    for k,v in vx['chunk'+str(z)+'-'+str(z+tickness)].items():
        jam = sum(v)
        tedad = len(v)
        if tedad == 0:
            average = 0
        else:
            average = jam / tedad
        temp[k] = average
    vx_results['chunk'+str(z)+'-'+str(z+tickness)] = temp
#=============================================================================
# Compute Vy Averages
#=============================================================================
for z in np.arange(min_h,max_h,tickness):
    temp = dict()
    for k,v in vy['chunk'+str(z)+'-'+str(z+tickness)].items():
        jam = sum(v)
        tedad = len(v)
        if tedad == 0:
            average = 0
        else:
            average = jam / tedad
        temp[k] = average
    vy_results['chunk'+str(z)+'-'+str(z+tickness)] = temp

#for k,v in vx_results.items():
#    print(k,':',v)
#==============================================================
# OutPuts
#==============================================================
with open('Vx-Y.txt','w') as foutx:
    for key,value in vx_results.items():
        for k,v in value.items():
            foutx.write("%s:%s\n" % (key,v))

with open('Vy-Y.txt','w') as fouty:
    for key,value in vy_results.items():
        for k,v in value.items():
            fouty.write("%s:%s\n" % (key,v))

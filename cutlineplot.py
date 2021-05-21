import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from scipy.interpolate import make_interp_spline, BSpline
from scipy.stats import norm
from statistics import mean
from math import sqrt
from math import cos
#=========================
# split Z layers
#=========================
min_h = 0
max_h = 44
tickness = 2
channel_width = max_h-min_h


lines_per_file = 37
smallfile = None
l = list()
for i in range(200):
    l.append(i)
i=0
with open('alpha_averages') as bigfile:
    for lineno, line in enumerate(bigfile):
        if lineno % lines_per_file == 0 :
            if smallfile:
                smallfile.close()
            small_filename = str(l[i])
            i+=1
            smallfile = open(small_filename, 'w')
        smallfile.write(line)
    if smallfile:
        smallfile.close()
#=================
# Plot Part
#=================
file_numbers = int(channel_width/tickness)
deg_averages = list()
layer = list()
layer_plt = list()
for file in range(2,19):
    file_name = str(file)
    angle = 'alpha'
    dig_step = 5
    numbers = list()
    degrees = list()
    data = np.loadtxt(file_name)
    layer_num = int(data[0][0])
    layer.append(layer_num)
    layer_plt.append(layer_num)
    for i in range(0,181,dig_step):
        degrees.append(i)
    for j in range(len(data)):
        if data[j][2] > int(data[j][2])+0.5:
            numbers.append(int(data[j][2])+1)
        else:
            numbers.append(int(data[j][2]))
#**********************************
# Calculate Standard Diviation
#**********************************
    plot = list()
    for i in range(len(numbers)):
        tick = numbers[i]
        for j in range(tick):
            plot.append(degrees[i])
    if len(plot)==0:
        mu = 0
    else:
        mu=sum(plot)/len(plot)
    deg_averages.append(mu)
    div = list()
    for item in plot:
        div.append((item-mu)**2)
    summ = sum(div)
    if len(plot)==0:
        sumation = 0
    else:
        sumation = summ/len(plot)
    sigma = sqrt(sumation)
#**********************************
    plt.style.use('fivethirtyeight')
    ticks=list()
    for j in range(0,181,10):
        ticks.append(j)
    plt.figure(figsize=(14,8))
    plt.hist(plot,bins=degrees,density=True, alpha=0.8,color='g',edgecolor='black')
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, sigma)
    plt.plot(x, p, 'r--', linewidth=2,label='layer'+str(layer_num))
    plt.title('Distributions Of the Dipole Moment Orientation')
    plt.xlabel('Dipole Moment Orientation Angle(%s)' % angle)
    plt.legend(loc=2)
    plt.xticks(ticks)
    plt.grid(True)
    plt.savefig('%s.png' % file)
#===================================
# Calculate second_Legendre
#===================================
plt.close('all')
second_Legendre = list()
for i in deg_averages:
    P2=(3/2)*((cos(i))**2)-(1/2)
    second_Legendre.append(P2)
plt.style.use('fivethirtyeight')
layernew = np.linspace(min(layer), max(layer), 300)
spl = make_interp_spline(layer, second_Legendre, k=3)
Legendre_smooth = spl(layernew)
plt.figure(figsize=(14,8))
plt.plot(layernew,Legendre_smooth,'k',linewidth=2,label='dipole orientation')
plt.xlabel('Z')
ticks = list()
for j in range(min_h,max_h,tickness):
    ticks.append(j)
plt.xticks(ticks)
plt.title('second_Legendre')
plt.legend(loc=3)
plt.savefig('second_Legendre.png')
#print(second_Legendre)
#print(layer)

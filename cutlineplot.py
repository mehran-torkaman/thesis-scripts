import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
from math import sqrt
from scipy.interpolate import make_interp_spline, BSpline
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
        numbers.append(data[j][2])
#**********************************
# Calculate Standard Diviation
#**********************************
    total = list()
    for i in range(len(numbers)):
        total.append(numbers[i]*degrees[i])
    if sum(numbers)==0:
        mu = 0
    else:
        mu=sum(total)/sum(numbers)
    deg_averages.append(mu)
    div = list()
    for item in degrees:
        div.append((item-mu)**2)
    summ = sum(div)
    sumation = summ/len(degrees)
    sigma = sqrt(sumation)
#**********************************
    plt.style.use('fivethirtyeight')
    ticks=list()
    for j in range(0,181,10):
        ticks.append(j)
    df = pd.DataFrame({'Deg':degrees, 'Num':numbers})
    plt.figure(figsize=(14,8))
    plt.hist(df.Deg, bins=36, weights=df.Num,density=True, alpha=0.8,color='g',edgecolor='black')
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, sigma)
    plt.plot(x, p, 'r--', linewidth=2,label='layer'+str(layer_num))
    plt.title('Histogram of Dipoles Orientation: $\mu=%.2f, \sigma=%.2f$' % (mu,sigma))
    plt.xlabel('Dipole Moment Orientation Angle(%s)' % angle)
    plt.ylabel('Probability Density')
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

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from scipy.stats import norm
from statistics import mean
from math import sqrt
#=========================
# split Z layers
#=========================
lines_per_file = 37
smallfile = None
l = list()
for i in range(200):
    l.append(i)
i=0
with open('gamma_averages') as bigfile:
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
min_h = 0
max_h = 44
tickness = 2
channel_width = max_h-min_h
file_numbers = int(channel_width/tickness)
for file in range(file_numbers):
    file_name = str(file)
    angle = 'gamma'
    dig_step = 5
    numbers = list()
    degrees = list()
    data = np.loadtxt(file_name)
    layer_num = int(data[0][0])
    for i in range(0,181,dig_step):
        degrees.append(i)
    for j in range(len(data)):
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
    plt.hist(plot,bins=degrees,density=True, alpha=0.6,color='g',edgecolor='black')
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

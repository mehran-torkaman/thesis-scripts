#========================
# Plots
#========================
import numpy as np
import matplotlib as plt

file_name = 'alpha_averages.txt'
angle = 'alpha'
dig_step = 5
numbers = list()
bins = list()
data = np.loadtxt(file_name)
for i in range(0,181,dig_step):
    bins.append(i)
for i in range(len(data)):
    numbers.append(int(data[i][2]))
plot = list()
for i in range(len(numbers)):
    tick = numbers[i]
    for j in range(tick):
        plot.append(bins[i])
plt.style.use('fivethirtyeight')
ticks=list()
for i in range(0,181,dig_step):
    ticks.append(i)
_, bins, _ = plt.hist(plot, 180,facecolor='green',density = 1 ,alpha=0.5 ,edgecolor='black')
mu, sigma = norm.fit(plot)
best_fit_line = norm.pdf(bins, mu, sigma)
plt.plot(bins, best_fit_line)
plt.title('Distributions Of the Dipole Moment Orientation')
plt.xlabel('Dipole Moment Orientation Angle(%s)' % angle)
plt.xticks(ticks)
plt.grid(True)
plt.show()

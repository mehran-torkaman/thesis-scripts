import numpy as np
from statistics import mean

file_numbers = 100
linesno = 209
tot_alpha = dict()
for j in range(linesno):
    tot_alpha['line'+str(j)] = []
tot_betta = dict()
for j in range(linesno):
    tot_betta['line'+str(j)] = []
tot_gamma = dict()
for j in range(linesno):
    tot_gamma['line'+str(j)] = []
for i in range(file_numbers):
    file_alpha = 'dipole-alpha'+str(i)
    file_betta = 'dipole-betta'+str(i)
    file_gamma = 'dipole-gamma'+str(i)
    data_a = np.loadtxt(file_alpha)
    data_b = np.loadtxt(file_betta)
    data_g = np.loadtxt(file_gamma)
    for j in range(len(data_a)):
        tot_alpha['line'+str(j)].append(data_a[j][2])
    for j in range(len(data_b)):
        tot_betta['line'+str(j)].append(data_b[j][2])
    for j in range(len(data_g)):
        tot_gamma['line'+str(j)].append(data_g[j][2])
ave_alpha = list()
ave_betta = list()
ave_gamma = list()
for i in range(linesno):
    temp_a = tot_alpha['line'+str(i)]
    ave_alpha.append(mean(temp_a))
    temp_b = tot_betta['line'+str(i)]
    ave_betta.append(mean(temp_b))
    temp_g = tot_gamma['line'+str(i)]
    ave_gamma.append(mean(temp_g))

with open('alpha_averages.txt', 'w') as fa:
    for item in ave_alpha:
        fa.write('%s\n' % item)

with open('betta_averages.txt', 'w') as fb:
    for item in ave_betta:
        fb.write('%s\n' % item)

with open('gamma_averages.txt', 'w') as fg:
    for item in ave_gamma:
        fg.write('%s\n' % item)

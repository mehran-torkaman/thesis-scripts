lines_per_file = 13828
smallfile = None
l = list()
for i in range(200):
    l.append(i)
i=0
with open('1700') as bigfile:
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

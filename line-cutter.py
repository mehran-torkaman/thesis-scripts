import os

n = 9
for j in range(100):
    with open(str(j)) as f:
        mylist = f.read().splitlines()

    newlist = mylist[:n]
    os.remove(str(j))

    thefile = open(str(j), 'w')

    del mylist[:n]

    for item in mylist:
        thefile.write('%s\n' % item)

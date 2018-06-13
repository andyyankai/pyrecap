import numpy as np
import math

def sqdist(p1,p2):
    dist = math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2+(p1[2]-p2[2])**2)
    return dist

f = open("tri.obj","r")
d = f.readlines()
vdata = {}
fdata = []
count = 1
for i in d:
    if i[0] == "v":
        vdata[str(count)] = str(i[2:]).split()
        vdata[str(count)][0] = float(vdata[str(count)][0])
        vdata[str(count)][1] = float(vdata[str(count)][1])
        vdata[str(count)][2] = float(vdata[str(count)][2])
    if i[0] == "f":
        fdata.append(str(i[2:]).split())

    count += 1
f.close()
print(vdata)
print(fdata)

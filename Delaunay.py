#Delaunay before
import numpy as np
import math

def sqdist(p1,p2):
    dist = math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2+(p1[2]-p2[2])**2)
    return dist

f = open("e.obj","r")
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
f = open("e.obj","r+")
d = f.readlines()
f.seek(0)
count = 0
deletelist = []
for i in fdata:
    if sqdist(np.array(vdata[i[0]]), np.array(vdata[i[1]])) > 100 or sqdist(np.array(vdata[i[0]]), np.array(vdata[i[2]])) > 100 or sqdist(np.array(vdata[i[1]]), np.array(vdata[i[2]])) > 100:
        deletelist.append(count)
        pass
    count += 1
    
for i in reversed(deletelist):
    del fdata[i]


count = 0
count2 = 0
for i in d:
    if i[0] == "v":
        f.write(i)
    elif i[0] == "f" and count < len(fdata):
        f.write("f "+fdata[count][0]+" "+fdata[count][1]+" "+fdata[count][2]+"\n")
        count += 1
    elif i[0] == "\n":
        pass
    else:
        break


f.truncate()
f.close()

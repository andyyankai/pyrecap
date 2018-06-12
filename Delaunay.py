#Delaunay before
import numpy as np


'''def cutF(fstr):
    a = 0
    b = 0
    rs = "f"
    for i in range(0,len(fstr)):
        if fstr[i] == " ":
            a = i
        if fstr[i] == "/" and fstr[i-1] != "/":
            b = i
            rs += fstr[a:b]
    return rs

f = open("triout.obj","r+")
d = f.readlines()
f.seek(0)
count = 1
for i in d:
    if i[0] == "v":
        f.write(str(i[:-1])+" #"+str(count)+"\n")
        count += 1
    else:
        f.write(cutF(i)+"\n")

f.truncate()
f.close()'''

def sqdist(p1,p2):
    squared_dist = np.sum(p1**2 + p2**2, axis=0)
    dist = np.sqrt(squared_dist)
    return dist

f = open("triout.obj","r")
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


print(vdata)
print(fdata)

for i in fdata:
    print(vdata[i[1]])
    print(vdata[i[2]])
    print(sqdist(np.array(vdata[i[1]]), np.array(vdata[i[2]])))



f.close()

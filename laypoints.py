import numpy as np
import math
import readobj

vdata, fdata = readobj.readdata("result.obj")

print(vdata)



f = open("e.obj","r+")
d = f.readlines()
f.seek(0)
for v in vdata:
    f.write("v " + " " + str(vdata[v][0]) +  " " + str(int(vdata[v][1]/20)*20) +  " " + str(vdata[v][2]) + "\n")

f.truncate()
f.close()

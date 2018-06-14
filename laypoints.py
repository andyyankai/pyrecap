import numpy as np
import math
import readobj


def clean(src,dest):
    vdata, fdata = readobj.readdata(src)

    f = open(dest,"r+")
    d = f.readlines()
    f.seek(0)
    for v in vdata:
        f.write("v " + " " + str(vdata[v][0]) +  " " + str(int(vdata[v][1]/100)*100) +  " " + str(vdata[v][2]) + "\n")

    f.truncate()
    f.close()

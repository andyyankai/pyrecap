import numpy as np
import math

def readdata(filename):
    f = open(filename,"r")
    d = f.readlines()
    vdata = {}
    fdata = []
    count = 1
    for i in d:
        if i[0] == "v" and i[1] != "n":
            vdata[str(count)] = str(i[2:]).split()
            vdata[str(count)][0] = float(vdata[str(count)][0])
            vdata[str(count)][1] = float(vdata[str(count)][1])
            vdata[str(count)][2] = float(vdata[str(count)][2])
        if i[0] == "f":
            fdata.append(str(i[2:]).split())

        count += 1
    f.close()
    return (vdata, fdata)

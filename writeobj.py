def writein(filename,vdata,fdata):


    z = open(filename,"w+")

    for count in vdata:
        z.write("v "+str(vdata[str(count)][0])+" "+str(vdata[str(count)][1])+" "+str(vdata[str(count)][2])+"\n")


    for f in fdata:
        z.write("f "+str(f[0])+" "+str(f[1])+" "+str(f[2])+"\n")

    z.close()

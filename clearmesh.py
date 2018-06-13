import readobj

(vdata, fdata) = readobj.readdata("triout.obj")
deletelist = []
count = 1

average = 0
for i in vdata:
    average += vdata[i][1]
average = average/len(vdata)
print(average)


#delete bound
rig = 857
lef = 16
bot = 39
top = 644

for f in fdata:
    if vdata[f[0]][0] < bot or vdata[f[0]][0] > top or vdata[f[0]][1] < lef or vdata[f[0]][1] > rig or vdata[f[1]][0] < bot or vdata[f[1]][0] > top or vdata[f[1]][1] < lef or vdata[f[1]][1] > rig or vdata[f[2]][0] < bot or vdata[f[2]][0] > top or vdata[f[2]][1] < lef or vdata[f[2]][1] > rig:
        deletelist.append(count)
    count += 1



for i in reversed(deletelist):
    del fdata[i-1]
    
    
z = open("e.obj","w+")


for count in range(1,len(vdata)):
    z.write("v "+str(vdata[str(count)][0])+" "+str(vdata[str(count)][1])+" "+str(vdata[str(count)][2])+"\n")
    
for f in fdata:
    z.write("f "+str(f[0])+" "+str(f[1])+" "+str(f[2])+"\n")
    
z.close()

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
bound = [644,39,16,857]

for f in fdata:
    if vdata[f[0]][0] < bound[1] or vdata[f[0]][0] > bound[0] or vdata[f[0]][1] < bound[2] or vdata[f[0]][1] > bound[3] or vdata[f[1]][0] < bound[1] or vdata[f[1]][0] > bound[0] or vdata[f[1]][1] < bound[2] or vdata[f[1]][1] > bound[3] or vdata[f[2]][0] < bound[1] or vdata[f[2]][0] > bound[0] or vdata[f[2]][1] < bound[2] or vdata[f[2]][1] > bound[3]:
        deletelist.append(count)
    count += 1
    
#delete box
deletebox = [[100,200,300,500]]

#two situation, one vertex in the box: easy!! no vertex in the box but a line in: emmmm...
for box in deletebox:
    



for i in reversed(deletelist):
    del fdata[i-1]
    
    
z = open("e.obj","w+")


for count in range(1,len(vdata)):
    z.write("v "+str(vdata[str(count)][0])+" "+str(vdata[str(count)][1])+" "+str(vdata[str(count)][2])+"\n")
    
for f in fdata:
    z.write("f "+str(f[0])+" "+str(f[1])+" "+str(f[2])+"\n")
    
z.close()

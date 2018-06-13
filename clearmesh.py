import readobj


# Liang-Barsky line clipping algorithm
def collides(x1,y1,x2,y2,box):
    t = [-1,-1,-1,-1]
    dx = x2-x1
    dy = y2-y1
    p = [-1,-1,-1,-1]
    q = [-1,-1,-1,-1]
    p[0]=-dx
    p[1]=dx
    p[2]=-dy
    p[3]=dy
    q[0]=x1-box[0]
    q[1]=box[2]-x1
    q[2]=y1-box[1]
    q[3]=box[3]-y1
    for i in range(0,4):
        if p[i] != 0:
            t[i]=q[i]/p[i]
        else:
            if p[i] != 0:
                t[i]=q[i]/p[i]
            else:
                if p[i]==0 and q[i] < 0:
                    return False
                else:
                    if p[i]==0 and q[i] >= 0:
                        return False
    if t[0] > t[2]:
        t1=t[0]
    else:
        t1=t[2]
        
    if t[1] < t[3]:
        t2=t[1]
    else:
        t2=t[3]
        
        
    if t1 < t2:
        return True
    else:
        return False


(vdata, fdata) = readobj.readdata("triout.obj")
deletelist = []
count = 1

'''average = 0
for i in vdata:
    average += vdata[i][1]
average = average/len(vdata)
print(average)'''


#delete bound
bound = [644,39,16,957] #[left,right,top,bot]

#delete box
deletebox = [[200,200,400,400]]

for f in fdata:
    if vdata[f[0]][0] < bound[1] or vdata[f[0]][0] > bound[0] or vdata[f[0]][1] < bound[2] or vdata[f[0]][1] > bound[3] or vdata[f[1]][0] < bound[1] or vdata[f[1]][0] > bound[0] or vdata[f[1]][1] < bound[2] or vdata[f[1]][1] > bound[3] or vdata[f[2]][0] < bound[1] or vdata[f[2]][0] > bound[0] or vdata[f[2]][1] < bound[2] or vdata[f[2]][1] > bound[3]:
        deletelist.append(count)
    else:
        for box in deletebox:
            if (int(vdata[f[0]][0]) in range(box[0],box[2]) and int(vdata[f[0]][1]) in range(box[1],box[3])) or (int(vdata[f[1]][0]) in range(box[0],box[2]) and int(vdata[f[1]][1]) in range(box[1],box[3])) or (int(vdata[f[2]][0]) in range(box[0],box[2]) and int(vdata[f[2]][1]) in range(box[1],box[3])):
                deletelist.append(count)
            else:
                if collides(vdata[f[0]][0],vdata[f[0]][1],vdata[f[1]][0],vdata[f[1]][1],box) or collides(vdata[f[0]][0],vdata[f[0]][1],vdata[f[2]][0],vdata[f[2]][1],box) or collides(vdata[f[1]][0],vdata[f[1]][1],vdata[f[2]][0],vdata[f[2]][1],box):
                    deletelist.append(count)
        
    count += 1
    

#two situation, one vertex in the box: easy!! no vertex in the box but a line in: emmmm...

print(len(deletelist))


for i in reversed(deletelist):
    del fdata[i-1]
    
    
z = open("e.obj","w+")
z.truncate()

for count in range(1,len(vdata)):
    z.write("v "+str(vdata[str(count)][0])+" "+str(vdata[str(count)][1])+" "+str(vdata[str(count)][2])+"\n")
    
for f in fdata:
    z.write("f "+str(f[0])+" "+str(f[1])+" "+str(f[2])+"\n")
    
z.close()

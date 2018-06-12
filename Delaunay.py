f = open("square.obj","r+")
d = f.readlines()
f.seek(0)
count = 1
for i in d:
    f.write(i+"#"+str(i))

f.truncate()
f.close()

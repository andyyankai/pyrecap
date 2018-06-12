def cutF(fstr):
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

f = open("tri.obj","r+")
d = f.readlines()
f.seek(0)
for i in d:
    if i[0] == "v" and i[1] != "n":
        f.write(i)
    elif i[0] == "f":
        f.write(cutF(i)+"\n")

f.truncate()
f.close()

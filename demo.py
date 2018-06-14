import objectmaker
import clearmesh
import Delaunay
import laypoints
import convexhull



print("Scanning images to build 3d point cloud...")
objectmaker.run()
print("Done! Check out.obj for result!")

f = open("out.obj","r+")
d = f.readlines()
f.seek(0)
f.writelines([item for item in d[1:-1]])

f.truncate()
f.close()


print("Mesh cleaning...chop and cut using the mask...")
clearmesh.clear()
print("Done! Check e.obj for result!")


print("Now removing the exceed long edges...")
Delaunay.tri("triout.obj","Delresult.obj")
print("Done! Check Delresult.obj for result!")

print("Now triangulate using the box chopped model...")
Delaunay.tri("e.obj","result.obj")
print("Done! Check result.obj for result!")

print("Layering the points....")
laypoints.clean("result.obj", "cleanpoints.obj")
print("Done! Check cleanpoints.obj for result!")


print("Building convexhull...")
convexhull.main()
print("Done! Check convexhull.obj for result!")

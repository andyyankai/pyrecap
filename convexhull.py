from collections import namedtuple  
import matplotlib.pyplot as plt  
import random
import readobj
import writeobj

Point = namedtuple('Point', 'x y')


class ConvexHull(object):  


    def __init__(self):
        self._points = []
        self._hull_points = []

    def add(self, point):
        self._points.append(point)
    def clear(self):
        self._points = []
        self._hull_points = []
    
    
    def _get_orientation(self, origin, p1, p2):
        difference = (
            ((p2.x - origin.x) * (p1.y - origin.y))
            - ((p1.x - origin.x) * (p2.y - origin.y))
        )

        return difference

    def compute_hull(self):
        '''
        Computes the points that make up the convex hull.
        :return: NOne
        '''
        points = self._points

        # get leftmost point
        start = points[0]
        min_x = start.x
        for p in points[1:]:
            if p.x < min_x:
                min_x = p.x
                start = p

        point = start
        self._hull_points.append(start)

        far_point = None
        while far_point is not start:

            # get the first point (initial max) to use to compare with others
            p1 = None
            for p in points:
                if p is point:
                    continue
                else:
                    p1 = p
                    break

            far_point = p1

            for p2 in points:
                # ensure we aren't comparing to self or pivot point
                if p2 is point or p2 is p1:
                    continue
                else:
                    direction = self._get_orientation(point, far_point, p2)
                    if direction > 0:
                        far_point = p2

            self._hull_points.append(far_point)
            point = far_point

    def get_hull_points(self):
        if self._points and not self._hull_points:
            self.compute_hull()

        return self._hull_points

    def display(self):
        # all points
        x = [p.x for p in self._points]
        y = [p.y for p in self._points]
        plt.plot(x, y, marker='D', linestyle='None')

        # hull points
        hx = [p.x for p in self._hull_points]
        hy = [p.y for p in self._hull_points]
        plt.plot(hx, hy)

        plt.title('Convex Hull')
        plt.show()


def main():
    deletelist = []
    resultlist = []
    for i in range(0,950,20):
    
        vdata, fdata = readobj.readdata("e.obj")
        ch = ConvexHull()
        for v in vdata: #0 to 840
            if vdata[v][1] == i:
                ch.add(Point(vdata[v][0], vdata[v][2]))
    
        ch.get_hull_points()
        for rs in ch._hull_points:
            resultlist.append([rs[0],i,rs[1]])
        print("Points on hull:", len(ch._hull_points))
        #ch.display()
        ch.clear()
        
    outdata = {}
    for i in range(0,len(resultlist)):
        outdata[str(i)] = resultlist[i]
    


    writeobj.writein("convexhull.obj",outdata,fdata)


if __name__ == '__main__':  
    main()

"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Solution:
    """
    @param n: An integer
    @param m: An integer
    @param operators: an array of point
    @return: an integer array
    """
    def numIslands2(self, n, m, operators):
        disjointSet = [-1] * (n*m)
        def find(i):
            while disjointSet[i] >= 0: 
                i = disjointSet[i]
            return i

        def merge(i, j):
            i = find(i)
            j = find(j)
            if i == j:
                return False
            disjointSet[i] = j
            return True
           
        count, ret = 0, []
        land = set()
        for point in operators:
            x, y = point.x, point.y
            if x*m + y not in land:
                land.add(x*m + y)
                count += 1
                for i, j in ((x+1, y), (x, y+1), (x-1, y), (x, y-1)):
                    if 0 <= i < n and 0 <= j < m and i*m + j in land:
                        if merge(x*m + y, i*m + j):
                            count -= 1
            ret.append(count)
        return ret
                
    def test(self):
        class Point:
            def __init__(self, a=0, b=0):
                self.x = a
                self.y = b
        #print self.numIslands2(3, 3, [Point(0, 0), Point(0, 1), Point(2, 2), Point(2, 1)])
        #print self.numIslands2(2, 2, [Point(0, 0), Point(0, 1), Point(1, 0), Point(1, 1)])
        print self.numIslands2(2, 2, [Point(0, 0), Point(1, 1), Point(1, 0), Point(0, 1)])

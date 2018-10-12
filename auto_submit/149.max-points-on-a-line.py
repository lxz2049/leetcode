#
# [149] Max Points on a Line
#
# https://leetcode.com/problems/max-points-on-a-line/description/
#
# algorithms
# Hard (15.27%)
# Total Accepted:    102.9K
# Total Submissions: 673.5K
# Testcase Example:  '[[1,1],[2,2],[3,3]]'
#
# Given n points on a 2D plane, find the maximum number of points that lie on
# the same straight line.
# 
# Example 1:
# 
# 
# Input: [[1,1],[2,2],[3,3]]
# Output: 3
# Explanation:
# ^
# |
# |        o
# |     o
# |  o  
# +------------->
# 0  1  2  3  4
# 
# 
# Example 2:
# 
# 
# Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# Output: 4
# Explanation:
# ^
# |
# |  o
# |     o        o
# |        o
# |  o        o
# +------------------->
# 0  1  2  3  4  5  6
# 
# 
#
# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b
from collections import defaultdict
class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if len(points) <= 2:
            return len(points)

        def gcdtuple(a, b):
            def gcd(x, y):
                if y == 0:
                    return x
                return gcd(y, x%y)
            g = gcd(a,b)
            return a/g, b/g

        lines = defaultdict(set)
        ret = 0
        for i in xrange(len(points)):
            for j in xrange(i+1, len(points)):
                x1, y1 = points[i].x, points[i].y
                x2, y2 = points[j].x, points[j].y
                if (x1 != x2):
                    tan, b = gcdtuple(y2 - y1 ,x2 - x1), gcdtuple(y1*x2 - y2*x1, x2 - x1)
                    key = (tan, b)
                    lines[key].add(i)
                    lines[key].add(j)
                    ret = max(len(lines[key]), ret)
                else:
                    key = x1
                    lines[key].add(i)
                    lines[key].add(j)
                    ret = max(len(lines[key]), ret)

        return ret

    def test(self):
        print self.maxPoints([[1,1],[2,2],[0,0]])
        print self.maxPoints([[1,1],[2,2],[0,0]])
        print self.maxPoints([[1,1],[0,0],[0,0]])
        print self.maxPoints([[0,0],[0,0],[0,0]])
        print self.maxPoints([[0,0],[94911151,94911150],[94911152,94911151]])
        print self.maxPoints([[3,2],[4,1],[2,3],[1,4]])
        print self.maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]])

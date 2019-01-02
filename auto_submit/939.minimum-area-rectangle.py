#
# [976] Minimum Area Rectangle
#
# https://leetcode.com/problems/minimum-area-rectangle/description/
#
# algorithms
# Medium (43.47%)
# Total Accepted:    7.1K
# Total Submissions: 15.4K
# Testcase Example:  '[[1,1],[1,3],[3,1],[3,3],[2,2]]'
#
# Given a set of points in the xy-plane, determine the minimum area of a
# rectangle formed from these points, with sides parallel to the x and y axes.
# 
# If there isn't any rectangle, return 0.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [[1,1],[1,3],[3,1],[3,3],[2,2]]
# Output: 4
# 
# 
# 
# Example 2:
# 
# 
# Input: [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
# Output: 2
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= points.length <= 500
# 0 <= points[i][0] <= 40000
# 0 <= points[i][1] <= 40000
# All points are distinct.
# 
# 
# 
#
class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        ret = 40000 ** 2
        lookup = set((x, y) for x, y in points)
        for i in xrange(len(points)):
            for j in xrange(i):
                x1, y1 = points[i]
                x2, y2 = points[j]
                if x1 != x2 and y1 != y2 and (x1, y2) in lookup and (x2, y1) in lookup:
                    ret = min(ret, abs(x1 - x2) * abs(y1 - y2))

        return ret if ret < 40000 ** 2 else 0

    def test(self):
        print self.minAreaRect([[1,1],[1,3],[3,1],[3,3],[2,2]])
        print self.minAreaRect([[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]])

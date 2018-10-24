#
# [391] Perfect Rectangle
#
# https://leetcode.com/problems/perfect-rectangle/description/
#
# algorithms
# Hard (27.55%)
# Total Accepted:    16.2K
# Total Submissions: 58.7K
# Testcase Example:  '[[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]'
#
# Given N axis-aligned rectangles where N > 0, determine if they all together
# form an exact cover of a rectangular region.
# 
# Each rectangle is represented as a bottom-left point and a top-right point.
# For example, a unit square is represented as [1,1,2,2]. (coordinate of
# bottom-left point is (1, 1) and top-right point is (2, 2)).
# 
# 
# 
# Example 1:
# 
# 
# rectangles = [
# ⁠ [1,1,3,3],
# ⁠ [3,1,4,2],
# ⁠ [3,2,4,4],
# ⁠ [1,3,2,4],
# ⁠ [2,3,3,4]
# ]
# 
# Return true. All 5 rectangles together form an exact cover of a rectangular
# region.
# 
# 
# 
# 
# 
# 
# 
# 
# Example 2:
# 
# 
# rectangles = [
# ⁠ [1,1,2,3],
# ⁠ [1,3,2,4],
# ⁠ [3,1,4,2],
# ⁠ [3,2,4,4]
# ]
# 
# Return false. Because there is a gap between the two rectangular
# regions.
# 
# 
# 
# 
# 
# 
# 
# 
# Example 3:
# 
# 
# rectangles = [
# ⁠ [1,1,3,3],
# ⁠ [3,1,4,2],
# ⁠ [1,3,2,4],
# ⁠ [3,2,4,4]
# ]
# 
# Return false. Because there is a gap in the top center.
# 
# 
# 
# 
# 
# 
# 
# 
# Example 4:
# 
# 
# rectangles = [
# ⁠ [1,1,3,3],
# ⁠ [3,1,4,2],
# ⁠ [1,3,2,4],
# ⁠ [2,2,4,4]
# ]
# 
# Return false. Because two of the rectangles overlap with each other.
# 
# 
# 
# 
#
class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        m = set()
        area = 0
        for rect in rectangles:
            bl = (rect[0], rect[1])
            br = (rect[0], rect[3])
            tl = (rect[2], rect[1])
            tr = (rect[2], rect[3])
            points = (bl, br, tl, tr)
            for i, p in enumerate(points):
                if p in m:
                    m.remove(p)
                else:
                    m.add(p)
            area += (rect[2] - rect[0]) * (rect[3] - rect[1])
        if len(m) != 4:
            return False
        marea = (max(x for x, _ in m) - min(x for x, _ in m)) * (max(y for _, y in m) - min(y for _, y in m))
        return area == marea

    def test(self):
        print self.isRectangleCover([ [1,1,3,3], [3,1,4,2], [3,2,4,4], [1,3,2,4], [2,3,3,4] ])
        print self.isRectangleCover([ [1,1,3,3], [1,1,3,3], [1,1,3,3], [3,1,4,2], [3,2,4,4], [1,3,2,4], [2,3,3,4] ])
        print self.isRectangleCover([ [1,1,2,3], [1,3,2,4], [3,1,4,2], [3,2,4,4] ])
        print self.isRectangleCover([ [1,1,3,3], [3,1,4,2], [1,3,2,4], [3,2,4,4] ])
        print self.isRectangleCover([ [1,1,3,3], [3,1,4,2], [1,3,2,4], [2,2,4,4] ])
        print self.isRectangleCover([ [0,0,1,1], [0,0,2,1], [1,0,2,1], [0,2,2,3] ])
        print self.isRectangleCover([ [0,0,1,1], [0,2,1,3], [1,1,2,2], [2,0,3,1], [2,2,3,3], [1,0,2,3], [0,1,3,2] ])
        print self.isRectangleCover([ [0,0,4,1], [0,0,4,1]])

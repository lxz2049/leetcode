#
# [223] Rectangle Area
#
# https://leetcode.com/problems/rectangle-area/description/
#
# algorithms
# Medium (33.63%)
# Total Accepted:    69.7K
# Total Submissions: 207.2K
# Testcase Example:  '-2\n-2\n2\n2\n-2\n-2\n2\n2'
#
# Find the total area covered by two rectilinear rectangles in a 2D plane.
# Each rectangle is defined by its bottom left corner and top right corner as
# shown in the figure.
# 
# 
# 
# 
# Assume that the total area is never beyond the maximum possible value of
# int.
# 
# 
# Credits:Special thanks to @mithmatt for adding this problem, creating the
# above image and all test cases.
#
class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        area1 = (A - C) * (B - D) 
        area2 = (E - G) * (F - H)
        overlap_width = max(0, min(C, G) - max(A, E))
        overlap_height = max(0, min(D, H) - max(B, F))
        return area1 + area2 - overlap_height * overlap_width

    def test(self):
        print self.computeArea(-3, 0, 3, 4, 0, -1, 9, 2)

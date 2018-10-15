#
# [84] Largest Rectangle in Histogram
#
# https://leetcode.com/problems/largest-rectangle-in-histogram/description/
#
# algorithms
# Hard (28.87%)
# Total Accepted:    138.3K
# Total Submissions: 478.2K
# Testcase Example:  '[2,1,5,6,2,3]'
#
# Given n non-negative integers representing the histogram's bar height where
# the width of each bar is 1, find the area of largest rectangle in the
# histogram.
# 
# 
# 
# 
# Above is a histogram where width of each bar is 1, given height =
# [2,1,5,6,2,3].
# 
# 
# 
# 
# The largest rectangle is shown in the shaded area, which has area = 10
# unit.
# 
# 
# 
# Example:
# 
# 
# Input: [2,1,5,6,2,3]
# Output: 10
# 
# 
#
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        ret = 0
        stack = [(0, -1)]
        heights.append(0)
        for i, h in enumerate(heights):
            while h < stack[-1][0]:
                height, index = stack.pop()
                area = (i - stack[-1][1] - 1) * height
                ret = max(ret, area)
            stack.append((h, i))
        return ret

    def test(self):
        print self.largestRectangleArea([2,1,5,6,2,3])

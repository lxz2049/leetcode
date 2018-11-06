#
# [11] Container With Most Water
#
# https://leetcode.com/problems/container-with-most-water/description/
#
# algorithms
# Medium (39.74%)
# Total Accepted:    262.4K
# Total Submissions: 659.5K
# Testcase Example:  '[1,8,6,2,5,4,8,3,7]'
#
# Given n non-negative integers a1, a2, ..., an , where each represents a point
# at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
# of line i is at (i, ai) and (i, 0). Find two lines, which together with
# x-axis forms a container, such that the container contains the most water.
# 
# Note: You may not slant the container and n is at least 2.
# 
# 
# 
# 
# 
# The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In
# this case, the max area of water (blue section) the container can contain is
# 49. 
# 
# 
# 
# Example:
# 
# 
# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49
# 
#
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ret = 0
        lo, hi = 0, len(height) - 1
        while lo < hi:
            ret = max(ret, min(height[lo], height[hi]) * (hi - lo))
            if height[lo] < height[hi]:
                lo += 1
            else:
                hi -= 1
        return ret

    def test(self):
        print self.maxArea([1,8,6,2,5,4,8,3,7])

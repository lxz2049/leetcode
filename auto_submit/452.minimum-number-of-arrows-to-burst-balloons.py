#
# [452] Minimum Number of Arrows to Burst Balloons
#
# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/
#
# algorithms
# Medium (44.38%)
# Total Accepted:    21.3K
# Total Submissions: 47.9K
# Testcase Example:  '[[10,16],[2,8],[1,6],[7,12]]'
#
# There are a number of spherical balloons spread in two-dimensional space. For
# each balloon, provided input is the start and end coordinates of the
# horizontal diameter. Since it's horizontal, y-coordinates don't matter and
# hence the x-coordinates of start and end of the diameter suffice. Start is
# always smaller than end. There will be at most 104 balloons.
# 
# An arrow can be shot up exactly vertically from different points along the
# x-axis. A balloon with xstart and xend bursts by an arrow shot at x if xstart
# ≤ x ≤ xend. There is no limit to the number of arrows that can be shot. An
# arrow once shot keeps travelling up infinitely. The problem is to find the
# minimum number of arrows that must be shot to burst all balloons. 
# 
# Example:
# 
# Input:
# [[10,16], [2,8], [1,6], [7,12]]
# 
# Output:
# 2
# 
# Explanation:
# One way is to shoot one arrow for example at x = 6 (bursting the balloons
# [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two
# balloons).
# 
# 
#
class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        from operator import itemgetter
        shots = 0
        right = None
        for p in sorted(points, key=itemgetter(1, 0)):
            if not right or p[0] > right:
                shots += 1
                right = p[1]
        return shots

    def test(self):
        print self.findMinArrowShots([[10,16], [2,8], [1,6], [7,12]])
        print self.findMinArrowShots([[-2147483648, 2147483647]])

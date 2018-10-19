#
# [796] Reaching Points
#
# https://leetcode.com/problems/reaching-points/description/
#
# algorithms
# Hard (24.93%)
# Total Accepted:    4.9K
# Total Submissions: 19.6K
# Testcase Example:  '9\n5\n12\n8'
#
# A move consists of taking a point (x, y) and transforming it to either (x,
# x+y) or (x+y, y).
# 
# Given a starting point (sx, sy) and a target point (tx, ty), return True if
# and only if a sequence of moves exists to transform the point (sx, sy) to
# (tx, ty). Otherwise, return False.
# 
# 
# Examples:
# Input: sx = 1, sy = 1, tx = 3, ty = 5
# Output: True
# Explanation:
# One series of moves that transforms the starting point to the target is:
# (1, 1) -> (1, 2)
# (1, 2) -> (3, 2)
# (3, 2) -> (3, 5)
# 
# Input: sx = 1, sy = 1, tx = 2, ty = 2
# Output: False
# 
# Input: sx = 1, sy = 1, tx = 1, ty = 1
# Output: True
# 
# 
# 
# Note:
# 
# 
# sx, sy, tx, ty will all be integers in the range [1, 10^9].
# 
# 
#
class Solution(object):
    def reachingPoints(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        """
        while tx > sx and ty > sy and tx != ty:
            if tx > ty:
                tx = tx - ((tx-1) / ty) * ty
            else:
                ty = ty - ((ty-1) / tx) * tx
            #print tx, ty
        if tx == sx:
            return ty % tx == sy % sx
        if ty == sy:
            return tx % ty == sx % sy
        return False

    def test(self):
        print self.reachingPoints(1,1,1,1)
        print self.reachingPoints(1,1,2,2)
        print self.reachingPoints(3,3,12,9)
        print self.reachingPoints(9,10,9,19)
        print self.reachingPoints(1,1,1000000,1)

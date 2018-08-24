#
# [335] Self Crossing
#
# https://leetcode.com/problems/self-crossing/description/
#
# algorithms
# Hard (26.13%)
# Total Accepted:    17.4K
# Total Submissions: 65.7K
# Testcase Example:  '[2,1,1,2]'
#
# You are given an array x of n positive numbers. You start at point (0,0) and
# moves x[0] metres to the north, then x[1] metres to the west, x[2] metres to
# the south, x[3] metres to the east and so on. In other words, after each move
# your direction changes counter-clockwise.
# 
# Write a one-pass algorithm with O(1) extra space to determine, if your path
# crosses itself, or not.
# 
# Example 1:
# 
# 
# Input: [2,1,1,2]
# 
# ?????
# ?   ?
# ???????>
# ⁠   ?
# 
# Input: true 
# Explanation: self crossing
# 
# 
# Example 2:
# 
# 
# Input: [1,2,3,4]
# 
# ????????
# ?      ?
# ?
# ?
# ?????????????>
# 
# Output: false 
# Explanation: not self crossing
# 
# 
# Example 3:
# 
# 
# Input: [1,1,1,1]
# 
# ?????
# ?   ?
# ?????>
# 
# Output: true 
# Explanation: self crossing
# 
# 
#
from operator import sub
class Solution(object):
    def isSelfCrossing(self, l):
        """
        :type l: List[int]
        :rtype: bool
        """
        for i in xrange(len(l)):
            if i > 2 and l[i] >= l[i-2] and l[i-1] <= l[i-3]:
                return True
            if i > 3 and l[i-1] == l[i-3] and l[i] + l[i-4] >= l[i-2]:
                return True
            if i > 4 and l[i-3] >= l[i-1] >= l[i-3] - l[i-5] and l[i] + l[i-4] >= l[i-2] >= l[i-4]:
                return True
        return False

    def test(self):
        #print self.isSelfCrossing([1,1,1,1])
        #print self.isSelfCrossing([1,2,3,4])
        #print self.isSelfCrossing([2,1,1,2])
        #print self.isSelfCrossing([1,1,2,1,1])
        #print self.isSelfCrossing([1,1,2,1,1])
        #print self.isSelfCrossing([1,1,2,2,1,1])
        print self.isSelfCrossing([3,3,3,2,1,1])
        #print self.isSelfCrossing([1,1,2,2,3,3,4,4,10,4,4,3,3,2,2,1,1])


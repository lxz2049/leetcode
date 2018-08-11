#
# [633] Sum of Square Numbers
#
# https://leetcode.com/problems/sum-of-square-numbers/description/
#
# algorithms
# Easy (32.27%)
# Total Accepted:    28.7K
# Total Submissions: 88.4K
# Testcase Example:  '5'
#
# 
# Given a non-negative integer c, your task is to decide whether there're two
# integers a and b such that a2 + b2 = c.
# 
# 
# Example 1:
# 
# Input: 5
# Output: True
# Explanation: 1 * 1 + 2 * 2 = 5
# 
# 
# 
# 
# Example 2:
# 
# Input: 3
# Output: False
# 
# 
# 
#
import math
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        for n in xrange(int(math.sqrt(c))+1):
            x = int(math.sqrt(c - n*n))
            if x*x + n*n == c:
                return True
        return False

    def test(self):
        print self.judgeSquareSum(5)
        print self.judgeSquareSum(0)
        print self.judgeSquareSum(3)

#
# [233] Number of Digit One
#
# https://leetcode.com/problems/number-of-digit-one/description/
#
# algorithms
# Hard (29.46%)
# Total Accepted:    37.6K
# Total Submissions: 127.4K
# Testcase Example:  '13'
#
# Given an integer n, count the total number of digit 1 appearing in all
# non-negative integers less than or equal to n.
# 
# Example:
# 
# 
# Input: 13
# Output: 6 
# Explanation: Digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.
# 
# 
#
import math
from operator import mul
class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret = 0
        divide = 1
        while divide <= n:
            ret += (n / divide + 8) / 10 * divide
            ret += (n / divide % 10 == 1) * (n % divide + 1)
            #print n / divide / 10, n / divide % 10, n % divide
            divide *= 10
        return ret
        
    def test(self):
        print self.countDigitOne(13)
        print self.countDigitOne(101)

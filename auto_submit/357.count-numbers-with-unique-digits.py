#
# [357] Count Numbers with Unique Digits
#
# https://leetcode.com/problems/count-numbers-with-unique-digits/description/
#
# algorithms
# Medium (46.16%)
# Total Accepted:    53.1K
# Total Submissions: 115.1K
# Testcase Example:  '2'
#
# Given a non-negative integer n, count all numbers with unique digits, x,
# where 0 ≤ x < 10n.
# 
# 
# Example:
# 
# 
# Input: 2
# Output: 91 
# Explanation: The answer should be the total numbers in the range of 0 ≤ x <
# 100, 
# excluding 11,22,33,44,55,66,77,88,99
# 
# 
# 
#
from math import factorial
class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        def func(n):
            if not n:
                return 1
            ret = 9
            fact = 9
            while n-1 > 0:
                ret *= fact
                n -= 1
                fact -= 1
            return ret

        return sum(func(x) for x in xrange(0, n+1))

    def test(self):
        print self.countNumbersWithUniqueDigits(0)
        print self.countNumbersWithUniqueDigits(1)
        print self.countNumbersWithUniqueDigits(2)
        print self.countNumbersWithUniqueDigits(3)
        print self.countNumbersWithUniqueDigits(4)

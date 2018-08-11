#
# [202] Happy Number
#
# https://leetcode.com/problems/happy-number/description/
#
# algorithms
# Easy (41.47%)
# Total Accepted:    177.2K
# Total Submissions: 417K
# Testcase Example:  '19'
#
# Write an algorithm to determine if a number is "happy".
# 
# A happy number is a number defined by the following process: Starting with
# any positive integer, replace the number by the sum of the squares of its
# digits, and repeat the process until the number equals 1 (where it will
# stay), or it loops endlessly in a cycle which does not include 1. Those
# numbers for which this process ends in 1 are happy numbers.
# 
# Example: 
# 
# 
# Input: 19
# Output: true
# Explanation: 
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1
# 
# 
#
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = set()
        while n not in s:
            s.add(n)
            tmp = 0
            while n:
                digit = n%10
                n /= 10
                tmp += digit*digit
            n = tmp
        return n == 1

    def test(self):
        print self.isHappy(19)
        print self.isHappy(20)

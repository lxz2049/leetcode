#
# [263] Ugly Number
#
# https://leetcode.com/problems/ugly-number/description/
#
# algorithms
# Easy (39.64%)
# Total Accepted:    123.5K
# Total Submissions: 311K
# Testcase Example:  '6'
#
# Write a program to check whether a given number is an ugly number.
# 
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
# For example, 6, 8 are ugly while 14 is not ugly since it includes another
# prime factor 7.
# 
# Note:
# 
# 
# 1 is typically treated as an ugly number.
# Input is within the 32-bit signed integer range.
# 
# 
# 
# Credits:
# Special thanks to @jianchao.li.fighter for adding this problem and creating
# all test cases.
# 
#
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        while num:
            print num
            if num % 2 == 0:
                num /= 2
            elif num % 3 == 0:
                num /= 3
            elif num % 5 == 0:
                num /= 5
            else:
                break
        return num == 1

    def test(self):
        print self.isUgly(1)
        print self.isUgly(6)
        print self.isUgly(8)
        print self.isUgly(14)
        print self.isUgly(-2147483648)

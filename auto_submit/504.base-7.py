#
# [504] Base 7
#
# https://leetcode.com/problems/base-7/description/
#
# algorithms
# Easy (43.94%)
# Total Accepted:    28.1K
# Total Submissions: 64K
# Testcase Example:  '100'
#
# Given an integer, return its base 7 string representation.
# 
# Example 1:
# 
# Input: 100
# Output: "202"
# 
# 
# 
# Example 2:
# 
# Input: -7
# Output: "-10"
# 
# 
# 
# Note:
# The input will be in range of [-1e7, 1e7].
# 
#
class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        carry = abs(num)
        num_base7 = ""
        while carry:
            num_base7 += str(carry%7)
            carry /= 7
            
        num_base7 = num_base7[::-1]
        if num < 0:
            num_base7 = "-%s" % num_base7
        elif num == 0:
            num_base7 = "0"
        return num_base7

    def test(self):
        print self.convertToBase7(100)
        print self.convertToBase7(-7)

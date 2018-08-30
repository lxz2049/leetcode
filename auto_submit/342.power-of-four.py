#
# [342] Power of Four
#
# https://leetcode.com/problems/power-of-four/description/
#
# algorithms
# Easy (39.08%)
# Total Accepted:    93.5K
# Total Submissions: 237K
# Testcase Example:  '16'
#
# Given an integer (signed 32 bits), write a function to check whether it is a
# power of 4.
# 
# Example 1:
# 
# 
# Input: 16
# Output: true
# 
# 
# 
# Example 2:
# 
# 
# Input: 5
# Output: false
# 
# 
# Follow up: Could you solve it without loops/recursion?
# 
#
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num & (num-1) == 0 and (num - 1) % 3 == 0

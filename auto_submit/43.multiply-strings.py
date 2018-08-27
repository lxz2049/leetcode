#
# [43] Multiply Strings
#
# https://leetcode.com/problems/multiply-strings/description/
#
# algorithms
# Medium (28.16%)
# Total Accepted:    151.9K
# Total Submissions: 532.6K
# Testcase Example:  '"2"\n"3"'
#
# Given two non-negative integers num1 and num2 represented as strings, return
# the product of num1 and num2, also represented as a string.
# 
# Example 1:
# 
# 
# Input: num1 = "2", num2 = "3"
# Output: "6"
# 
# Example 2:
# 
# 
# Input: num1 = "123", num2 = "456"
# Output: "56088"
# 
# 
# Note:
# 
# 
# The length of both num1 and num2 is < 110.
# Both num1 and num2 contain only digits 0-9.
# Both num1 and num2 do not contain any leading zero, except the number 0
# itself.
# You must not use any built-in BigInteger library or convert the inputs to
# integer directly.
# 
# 
#
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num2 = int(num2)
        ans = 0
        carry = 1
        for c1 in reversed(num1):
            ans += int(c1) * int(num2) * carry
            carry *= 10
        return str(ans)

    def test(self):
        print self.multiply("2", "3")
        print self.multiply("123", "456")
            

#
# [67] Add Binary
#
# https://leetcode.com/problems/add-binary/description/
#
# algorithms
# Easy (36.36%)
# Total Accepted:    247.8K
# Total Submissions: 679.3K
# Testcase Example:  '"11"\n"1"'
#
# Given two binary strings, return their sum (also a binary string).
# 
# The input strings are both non-empty and contains only characters 1 or 0.
# 
# Example 1:
# 
# 
# Input: a = "11", b = "1"
# Output: "100"
# 
# Example 2:
# 
# 
# Input: a = "1010", b = "1011"
# Output: "10101"
# 
#
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        ret = []
        while i >= 0 or j >= 0:
            ba = int(a[i]) if i >= 0 else 0
            bb = int(b[j]) if j >= 0 else 0
            ret.append((carry + ba + bb) % 2)
            carry = (carry + ba + bb) / 2
            i -= 1
            j -= 1
        if carry:
            ret.append(1)
        return "".join(str(b) for b in reversed(ret))

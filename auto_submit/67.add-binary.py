#
# [67] Add Binary
#
# https://leetcode.com/problems/add-binary/description/
#
# algorithms
# Easy (34.53%)
# Total Accepted:    224.8K
# Total Submissions: 634.6K
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
import itertools
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        ans = []
        carry = "0"
        for t in itertools.izip_longest(reversed(a), reversed(b), fillvalue="0"):
            if t[0] == "1" and t[1] == "1":
                ans.append(carry)
                carry = "1"
            elif t[0] == "1" or t[1] == "1":
                if carry == "1":
                    ans.append("0")
                    carry = "1"
                else:
                    ans.append("1")
                    carry = "0"
            else:
                ans.append(carry)
                carry = "0"
        if carry == "1":
            ans.append(carry)
        return "".join(reversed(ans))


            
            

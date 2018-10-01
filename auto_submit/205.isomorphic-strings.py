#
# [205] Isomorphic Strings
#
# https://leetcode.com/problems/isomorphic-strings/description/
#
# algorithms
# Easy (35.49%)
# Total Accepted:    159.5K
# Total Submissions: 449.1K
# Testcase Example:  '"egg"\n"add"'
#
# Given two strings s and t, determine if they are isomorphic.
# 
# Two strings are isomorphic if the characters in s can be replaced to get t.
# 
# All occurrences of a character must be replaced with another character while
# preserving the order of characters. No two characters may map to the same
# character but a character may map to itself.
# 
# Example 1:
# 
# 
# Input: s = "egg", t = "add"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s = "foo", t = "bar"
# Output: false
# 
# Example 3:
# 
# 
# Input: s = "paper", t = "title"
# Output: true
# 
# Note:
# You may assume both s and t have the same length.
# 
#
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def util(s, t):
            m = {}
            for cs, ct in zip(s, t):
                if cs not in m:
                    m[cs] = ct
                elif m[cs] != ct:
                    return False
            return True
     
        return util(t, s) and util(s, t)

#
# [459] Repeated Substring Pattern
#
# https://leetcode.com/problems/repeated-substring-pattern/description/
#
# algorithms
# Easy (38.18%)
# Total Accepted:    52.6K
# Total Submissions: 137.8K
# Testcase Example:  '"abab"'
#
# Given a non-empty string check if it can be constructed by taking a substring
# of it and appending multiple copies of the substring together.  You may
# assume the given string consists of lowercase English letters only and its
# length  will not exceed 10000. 
# 
# Example 1:
# 
# Input: "abab"
# 
# Output: True
# 
# Explanation: It's the substring "ab" twice.
# 
# 
# 
# Example 2:
# 
# Input: "aba"
# 
# Output: False
# 
# 
# 
# Example 3:
# 
# Input: "abcabcabcabc"
# 
# Output: True
# 
# Explanation: It's the substring "abc" four times. (And the substring "abcabc"
# twice.)
# 
# 
#
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(1, len(s)/2+1):
            if len(s) % i == 0:
                sub = s[:i]
                if s[:i] * (len(s) / len(s[:i])) == s:
                    return True
        return False

    def test(self):
        print self.repeatedSubstringPattern("abab")
        print self.repeatedSubstringPattern("aba")
        print self.repeatedSubstringPattern("abcabcabc")
        print self.repeatedSubstringPattern("bb")

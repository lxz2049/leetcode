#
# [10] Regular Expression Matching
#
# https://leetcode.com/problems/regular-expression-matching/description/
#
# algorithms
# Hard (24.60%)
# Total Accepted:    261.1K
# Total Submissions: 1.1M
# Testcase Example:  '"aa"\n"a"'
#
# Given an input string (s) and a pattern (p), implement regular expression
# matching with support for '.' and '*'.
# 
# 
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# 
# 
# The matching should cover the entire input string (not partial).
# 
# Note:
# 
# 
# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like
# . or *.
# 
# 
# Example 1:
# 
# 
# Input:
# s = "aa"
# p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# 
# 
# Example 2:
# 
# 
# Input:
# s = "aa"
# p = "a*"
# Output: true
# Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore,
# by repeating 'a' once, it becomes "aa".
# 
# 
# Example 3:
# 
# 
# Input:
# s = "ab"
# p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
# 
# 
# Example 4:
# 
# 
# Input:
# s = "aab"
# p = "c*a*b"
# Output: true
# Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore
# it matches "aab".
# 
# 
# Example 5:
# 
# 
# Input:
# s = "mississippi"
# p = "mis*is*p*."
# Output: false
# 
# 
#
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = {}
        def match(i, j, matching=None):
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False

            if (i, j) in dp:
                return dp[i, j]

            #print "%s|%s" % (s[i:], p[j:])
            ret = False
            star = j + 1 < len(p) and p[j+1] == "*"
            if star and match(i, j+2, None):
                dp[i, j] = True
                return True
            if i < len(s) and (p[j].isalpha() and s[i] == p[j] or p[j] == "."): 
                if star:
                    dp[i, j] = match(i+1, j) or match(i+1, j+2)
                    return dp[i, j]
                dp[i, j] = match(i+1, j+1)
                return dp[i, j]
            dp[i, j] = False
            return False

        return match(0, 0)

    def test(self):
        print self.isMatch("aa", "a*")
        print self.isMatch("ab", ".*")
        print self.isMatch("aab", "c*a*b")
        print self.isMatch("a", "ab*")
        print self.isMatch("ab", ".*c")
        print self.isMatch("mississippi", "mis*is*p*")

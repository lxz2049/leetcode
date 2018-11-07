#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (25.66%)
# Total Accepted:    401.5K
# Total Submissions: 1.6M
# Testcase Example:  '"babad"'
#
# Given a string s, find the longest palindromic substring in s. You may assume
# that the maximum length of s is 1000.
# 
# Example 1:
# 
# 
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# 
# 
# Example 2:
# 
# 
# Input: "cbbd"
# Output: "bb"
# 
# 
#
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s

        def solve(i):
            lo = hi = i
            while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
                lo -= 1
                hi += 1
            ret = s[lo+1:hi]
            if i < len(s) - 1 and s[i] == s[i+1]:
                lo, hi = i, i + 1
                while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
                    lo -= 1
                    hi += 1
                lo += 1
                hi -= 1
                if hi - lo + 1 > len(ret):
                    ret = s[lo:hi+1]
            return ret
 
        return max((solve(i) for i in xrange(len(s))), key=len)

    def test(self):
        print self.longestPalindrome("cbbd")
        print self.longestPalindrome("babad")

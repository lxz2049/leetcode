#
# [409] Longest Palindrome
#
# https://leetcode.com/problems/longest-palindrome/description/
#
# algorithms
# Easy (45.93%)
# Total Accepted:    70.1K
# Total Submissions: 151.9K
# Testcase Example:  '"abccccdd"'
#
# Given a string which consists of lowercase or uppercase letters, find the
# length of the longest palindromes that can be built with those letters.
# 
# This is case sensitive, for example "Aa" is not considered a palindrome
# here.
# 
# Note:
# Assume the length of given string will not exceed 1,010.
# 
# 
# Example: 
# 
# Input:
# "abccccdd"
# 
# Output:
# 7
# 
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.
# 
# 
#
import collections
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = collections.Counter(s)
        ans = 0
        for key in counter:
            count = counter[key]
            ans += count - count%2
            #print key, count, ans
        return ans + (1 if ans < len(s) else 0)

    def test(self):
        print self.longestPalindrome("abccccdd")
        print self.longestPalindrome("bb")

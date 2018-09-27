#
# [131] Palindrome Partitioning
#
# https://leetcode.com/problems/palindrome-partitioning/description/
#
# algorithms
# Medium (37.16%)
# Total Accepted:    134.5K
# Total Submissions: 359.3K
# Testcase Example:  '"aab"'
#
# Given a string s, partition s such that every substring of the partition is a
# palindrome.
# 
# Return all possible palindrome partitioning of s.
# 
# Example:
# 
# 
# Input: "aab"
# Output:
# [
# ⁠ ["aa","b"],
# ⁠ ["a","a","b"]
# ]
# 
# 
#
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        return [[s[:i+1]] + rest for i in xrange(len(s)) if s[:i+1] == s[i::-1]
                for rest in self.partition(s[i+1:])] or [[]]

    def test(self):
        print self.partition("aab")

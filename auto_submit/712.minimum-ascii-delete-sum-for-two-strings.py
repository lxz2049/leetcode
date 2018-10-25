#
# [712] Minimum ASCII Delete Sum for Two Strings
#
# https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/description/
#
# algorithms
# Medium (52.05%)
# Total Accepted:    14K
# Total Submissions: 26.8K
# Testcase Example:  '"sea"\n"eat"'
#
# Given two strings s1, s2, find the lowest ASCII sum of deleted characters to
# make two strings equal.
# 
# Example 1:
# 
# Input: s1 = "sea", s2 = "eat"
# Output: 231
# Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the
# sum.
# Deleting "t" from "eat" adds 116 to the sum.
# At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum
# possible to achieve this.
# 
# 
# 
# Example 2:
# 
# Input: s1 = "delete", s2 = "leet"
# Output: 403
# Explanation: Deleting "dee" from "delete" to turn the string into "let",
# adds 100[d]+101[e]+101[e] to the sum.  Deleting "e" from "leet" adds 101[e]
# to the sum.
# At the end, both strings are equal to "let", and the answer is
# 100+101+101+101 = 403.
# If instead we turned both strings into "lee" or "eet", we would get answers
# of 433 or 417, which are higher.
# 
# 
# 
# Note:
# 0 < s1.length, s2.length .
# All elements of each string will have an ASCII value in [97, 122]. 
# 
#
class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        dp = [[0] * (len(s2)+1) for _ in xrange(len(s1)+1)]
        for i, c1 in enumerate(s1):
            dp[i][-1] = dp[i-1][-1] + ord(c1)
        for j, c2 in enumerate(s2):
            dp[-1][j] = dp[-1][j-1] + ord(c2)
        for i, c1 in enumerate(s1):
            for j, c2 in enumerate(s2):
                 dp[i][j] = min(dp[i-1][j] + ord(c1), dp[i][j-1] + ord(c2), 
                         dp[i-1][j-1] if c1 == c2 else 0x7fffffff)
        return dp[-2][-2]

    def test(self):
        print self.minimumDeleteSum('sea', 'eat')
        print self.minimumDeleteSum('delete', 'leet')

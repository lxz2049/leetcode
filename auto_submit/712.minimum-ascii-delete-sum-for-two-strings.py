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
        dp = [[-1] * (len(s2)+1) for _ in xrange(len(s1)+1)]
        def traverse(i, j):
            if dp[i][j] < 0:
                if i == len(s1) and j == len(s2):
                    dp[i][j] = 0
                elif i == len(s1):
                    dp[i][j] = ord(s2[j]) + traverse(i, j+1)
                elif j == len(s2):
                    dp[i][j] = ord(s1[i]) + traverse(i+1, j)
                elif s1[i] == s2[j]:
                    dp[i][j] = traverse(i+1, j+1) 
                else:
                    dp[i][j] = min(ord(s1[i]) + traverse(i+1, j),
                                   ord(s2[j]) + traverse(i, j+1))
            return dp[i][j]
        ret = traverse(0, 0)
        return ret

    def test(self):
        print self.minimumDeleteSum('sea', 'eat')
        print self.minimumDeleteSum('delete', 'leet')

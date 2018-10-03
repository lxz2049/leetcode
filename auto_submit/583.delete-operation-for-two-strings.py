#
# [583] Delete Operation for Two Strings
#
# https://leetcode.com/problems/delete-operation-for-two-strings/description/
#
# algorithms
# Medium (44.78%)
# Total Accepted:    22.7K
# Total Submissions: 50.5K
# Testcase Example:  '"sea"\n"eat"'
#
# 
# Given two words word1 and word2, find the minimum number of steps required to
# make word1 and word2 the same, where in each step you can delete one
# character in either string.
# 
# 
# Example 1:
# 
# Input: "sea", "eat"
# Output: 2
# Explanation: You need one step to make "sea" to "ea" and another step to make
# "eat" to "ea".
# 
# 
# 
# Note:
# 
# The length of given words won't exceed 500.
# Characters in given words can only be lower-case letters.
# 
# 
#
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if not word1 or not word2:
            return len(word2) + len(word1)

        dp = [[0] * (len(word2) + 1) for _ in xrange(len(word1) + 1)]
        for i, c1 in enumerate(word1):
            for j, c2 in enumerate(word2):
                dp[i][j] = max(dp[i-1][j], dp[i][j-1], (dp[i-1][j-1] + 1) if c1 == c2 else 0)
        return len(word1) + len(word2) - dp[-2][-2] * 2

    def test(self):
        print self.minDistance("", "eat")
        print self.minDistance("", "")
        print self.minDistance("sea", "eat")

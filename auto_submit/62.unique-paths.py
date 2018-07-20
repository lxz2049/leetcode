#
# [62] Unique Paths
#
# https://leetcode.com/problems/unique-paths/description/
#
# algorithms
# Medium (42.72%)
# Total Accepted:    204.8K
# Total Submissions: 468.9K
# Testcase Example:  '3\n2'
#
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in
# the diagram below).
# 
# The robot can only move either down or right at any point in time. The robot
# is trying to reach the bottom-right corner of the grid (marked 'Finish' in
# the diagram below).
# 
# How many possible unique paths are there?
# 
# 
# Above is a 7 x 3 grid. How many possible unique paths are there?
# 
# Note: m and n will be at most 100.
# 
# Example 1:
# 
# 
# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the
# bottom-right corner:
# 1. Right -> Right -> Down
# 2. Right -> Down -> Right
# 3. Down -> Right -> Right
# 
# 
# Example 2:
# 
# 
# Input: m = 7, n = 3
# Output: 28
# 
#
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[None]*m for _ in range(n)]
        dp[n-1][m-1] = 1
        def dfs(i, j):
            if i > n-1 or j > m-1:
                return 0

            if dp[i][j] is not None:
                return dp[i][j]
            dp[i][j] = dfs(i+1, j) + dfs(i, j+1)
            return dp[i][j]

        ans = dfs(0, 0)
        #print dp
        return ans

    def test(self):
        print self.uniquePaths(7, 3)

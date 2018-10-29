#
# [63] Unique Paths II
#
# https://leetcode.com/problems/unique-paths-ii/description/
#
# algorithms
# Medium (32.70%)
# Total Accepted:    162.2K
# Total Submissions: 496K
# Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
#
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in
# the diagram below).
# 
# The robot can only move either down or right at any point in time. The robot
# is trying to reach the bottom-right corner of the grid (marked 'Finish' in
# the diagram below).
# 
# Now consider if some obstacles are added to the grids. How many unique paths
# would there be?
# 
# 
# 
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.
# 
# Note: m and n will be at most 100.
# 
# Example 1:
# 
# 
# Input:
# [
# [0,0,0],
# [0,1,0],
# [0,0,0]
# ]
# Output: 2
# Explanation:
# There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right
# 
# 
#
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid or not obstacleGrid[0] or obstacleGrid[0][0] == 1:
            return 0
        dp = [[0] * len(row) for row in obstacleGrid]
        dp[0][0] = obstacleGrid[0][0] = 1
        for i, row in enumerate(obstacleGrid):
            for j, g in enumerate(row):
                if not g:
                    up = dp[i-1][j] if i else 0
                    left = dp[i][j-1] if j else 0
                    dp[i][j] = up + left
        return dp[-1][-1]

    def test(self):
        print self.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])
        print self.uniquePathsWithObstacles([[1]])

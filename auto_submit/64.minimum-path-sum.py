#
# [64] Minimum Path Sum
#
# https://leetcode.com/problems/minimum-path-sum/description/
#
# algorithms
# Medium (40.62%)
# Total Accepted:    161.1K
# Total Submissions: 384.3K
# Testcase Example:  '[[1,3,1],[1,5,1],[4,2,1]]'
#
# Given a m x n grid filled with non-negative numbers, find a path from top
# left to bottom right which minimizes the sum of all numbers along its path.
# 
# Note: You can only move either down or right at any point in time.
# 
# Example:
# 
# 
# Input:
# [
# [1,3,1],
# ⁠ [1,5,1],
# ⁠ [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.
# 
# 
#
import itertools
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_value = 0xffffffff
        it = itertools.product(xrange(len(grid)), xrange(len(grid[0])))
        it.next()
        for i, j in it:
            min_val = min(grid[i-1][j] if i else max_value, grid[i][j-1] if j else max_value)
            grid[i][j] += min_val if min_val < max_value else 0
        return grid[-1][-1]

    def test(self):
        print self.minPathSum([[1,3,1],[1,5,1],[4,2,1]])

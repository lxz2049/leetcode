#
# [221] Maximal Square
#
# https://leetcode.com/problems/maximal-square/description/
#
# algorithms
# Medium (31.27%)
# Total Accepted:    103.8K
# Total Submissions: 331.6K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# Given a 2D binary matrix filled with 0's and 1's, find the largest square
# containing only 1's and return its area.
# 
# Example:
# 
# 
# Input: 
# 
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# 
# Output: 4
# 
#
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0

        ret = 0
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[0])):
                if matrix[i][j] == "1":
                    matrix[i][j] = min(matrix[i-1][j] if i else 0
                            , matrix[i][j-1] if j else 0,
                            matrix[i-1][j-1] if i and j else 0) + 1
                    ret = max(ret, matrix[i][j] * matrix[i][j])
                else:
                    matrix[i][j] = 0
                
        return ret

    def test(self):
        print self.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])
        print self.maximalSquare([["1"]])

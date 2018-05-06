#
# [304] Range Sum Query 2D - Immutable
#
# https://leetcode.com/problems/range-sum-query-2d-immutable/description/
#
# algorithms
# Medium (27.18%)
# Total Accepted:    44.3K
# Total Submissions: 161.3K
# Testcase Example:  '["NumMatrix","sumRegion","sumRegion","sumRegion"]\n[[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],[2,1,4,3],[1,1,2,2],[1,2,2,4]]'
#
# Given a 2D matrix matrix, find the sum of the elements inside the rectangle
# defined by its upper left corner (row1, col1) and lower right corner (row2,
# col2).
# 
# 
# 
# The above rectangle (with the red border) is defined by (row1, col1) = (2, 1)
# and (row2, col2) = (4, 3), which contains sum = 8.
# 
# 
# Note:
# 
# You may assume that the matrix does not change.
# There are many calls to sumRegion function.
# You may assume that row1 ≤ row2 and col1 ≤ col2.
# 
# 
#
class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if i > 0:
                    matrix[i][j] += matrix[i-1][j]
                if j > 0:
                    matrix[i][j] += matrix[i][j-1]
                if i > 0 and j > 0:
                    matrix[i][j] -= matrix[i-1][j-1]

        self.matrix = matrix
        

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        s = self.matrix[row2][col2]
        s -= self.matrix[row1-1][col2] if row1 > 0 else 0
        s -= self.matrix[row2][col1-1] if col1 > 0 else 0
        s += self.matrix[row1-1][col1-1] if row1 > 0 and col1 > 0 else 0
        return s
        

class Solution:
    def test(self):
        m = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
        print 8, m.sumRegion(2, 1, 4, 3) 
        print 11, m.sumRegion(1, 1, 2, 2)
        print 12, m.sumRegion(1, 2, 2, 4)


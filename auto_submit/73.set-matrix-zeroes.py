#
# [73] Set Matrix Zeroes
#
# https://leetcode.com/problems/set-matrix-zeroes/description/
#
# algorithms
# Medium (37.74%)
# Total Accepted:    164.2K
# Total Submissions: 435K
# Testcase Example:  '[[1,1,1],[1,0,1],[1,1,1]]'
#
# Given a m x n matrix, if an element is 0, set its entire row and column to 0.
# Do it in-place.
# 
# Example 1:
# 
# 
# Input: 
# [
# [1,1,1],
# [1,0,1],
# [1,1,1]
# ]
# Output: 
# [
# [1,0,1],
# [0,0,0],
# [1,0,1]
# ]
# 
# 
# Example 2:
# 
# 
# Input: 
# [
# [0,1,2,0],
# [3,4,5,2],
# [1,3,1,5]
# ]
# Output: 
# [
# [0,0,0,0],
# [0,4,5,0],
# [0,3,1,0]
# ]
# 
# 
# Follow up:
# 
# 
# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best
# solution.
# Could you devise a constant space solution?
# 
# 
#
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        zero_first_row = any(e == 0 for e in matrix[0])
        for i in xrange(1, len(matrix)):
            zero_cur_row = any(e == 0 for e in matrix[i])
            for j in xrange(len(matrix[i])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                elif zero_cur_row:
                    matrix[i][j] = 0
        for j in xrange(len(matrix[0])):
            if matrix[0][j] == 0:
                for i in xrange(1, len(matrix)):
                    matrix[i][j] = 0
            elif zero_first_row:
                matrix[0][j] = 0
            
    def test(self):
        m = [[1,1,1], [1,0,1], [1,1,1] ]
        self.setZeroes(m)
        print m
        m = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
        self.setZeroes(m)
        print m
        m = [[0]]
        self.setZeroes(m)
        print m
 

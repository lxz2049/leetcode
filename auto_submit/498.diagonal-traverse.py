#
# [498] Diagonal Traverse
#
# https://leetcode.com/problems/diagonal-traverse/description/
#
# algorithms
# Medium (44.22%)
# Total Accepted:    30.8K
# Total Submissions: 69.6K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given a matrix of M x N elements (M rows, N columns), return all elements of
# the matrix in diagonal order as shown in the below image.
# 
# 
# 
# Example:
# 
# 
# Input:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 4, 5, 6 ],
# ⁠[ 7, 8, 9 ]
# ]
# 
# Output:  [1,2,4,7,5,3,6,8,9]
# 
# Explanation:
# 
# 
# 
# 
# 
# Note:
# 
# The total number of elements of the given matrix will not exceed 10,000.
# 
#
class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        N, M = len(matrix), len(matrix[0])
        l = [(i, j) for i in xrange(N) for j in xrange(M)]
        ret = []
        l.sort(key=lambda x: (x[0]+x[1], x[0] if (x[0]+x[1]) % 2 else x[1]))
        return [matrix[i][j] for i, j in l]

    def test(self):
        print self.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]])
        print self.findDiagonalOrder([[6,9,7]])

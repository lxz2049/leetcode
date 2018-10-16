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
        
        hori = [[int(x) for x in m] for m in matrix]
        vert = [[int(x) for x in m] for m in matrix]
        matrix = [[int(x) for x in m] for m in matrix]
        ret = matrix[0][0]
        for i in xrange(len(hori)):
            for j in xrange(1, len(hori[0])):
                if hori[i][j]:
                    ret = 1
                    hori[i][j] += hori[i][j-1]

        for i in xrange(1, len(vert)):
            for j in xrange(len(vert[0])):
                if vert[i][j]:
                    ret = 1
                    vert[i][j] += vert[i-1][j]

        for i in xrange(1, len(matrix)):
            for j in xrange(1, len(matrix[0])):
                matrix[i][j] = min(hori[i][j], vert[i][j], matrix[i-1][j-1]+1)
                ret = max(ret, matrix[i][j] * matrix[i][j])
                
        #print hori
        #print vert
        #print matrix
        return ret

    def test(self):
        print self.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])
        print self.maximalSquare([["1"]])

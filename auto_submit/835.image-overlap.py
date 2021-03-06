#
# [864] Image Overlap
#
# https://leetcode.com/problems/image-overlap/description/
#
# algorithms
# Medium (47.48%)
# Total Accepted:    7.1K
# Total Submissions: 14.8K
# Testcase Example:  '[[1,1,0],[0,1,0],[0,1,0]]\n[[0,0,0],[0,1,1],[0,0,1]]'
#
# Two images A and B are given, represented as binary, square matrices of the
# same size.  (A binary matrix has only 0s and 1s as values.)
# 
# We translate one image however we choose (sliding it left, right, up, or down
# any number of units), and place it on top of the other image.  After, the
# overlap of this translation is the number of positions that have a 1 in both
# images.
# 
# (Note also that a translation does not include any kind of rotation.)
# 
# What is the largest possible overlap?
# 
# Example 1:
# 
# 
# Input: A = [[1,1,0],
# ⁠           [0,1,0],
# [0,1,0]]
# B = [[0,0,0],
# [0,1,1],
# [0,0,1]]
# Output: 3
# Explanation: We slide A to right by 1 unit and down by 1 unit.
# 
# Notes: 
# 
# 
# 1 <= A.length = A[0].length = B.length = B[0].length <= 30
# 0 <= A[i][j], B[i][j] <= 1
# 
# 
#
class Solution(object):
    def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        def cal(x, y):
            return max(sum(A[i][j] & B[x+i][y+j] for i in xrange(len(A)-x) for j in xrange(len(A[i])-y))
            , sum(B[i][j] & A[x+i][y+j] for i in xrange(len(A)-x) for j in xrange(len(A[i])-y)))
        return max(cal(i, j) for i in xrange(len(A)) for j in xrange(len(A[i])))
                
    def test(self):
        print self.largestOverlap([[1,1,0],[0,1,0],[0,1,0]], [[0,0,0],[0,1,1],[0,0,1]])
        print self.largestOverlap([[1,0],[0,0]], [[0,1],[1,0]])
        print self.largestOverlap([[0,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,0,1],[0,1,0,0,1]], [[1,0,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[0,1,1,1,1],[1,0,1,1,1]])

#
# [378] Kth Smallest Element in a Sorted Matrix
#
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/
#
# algorithms
# Medium (46.33%)
# Total Accepted:    76.4K
# Total Submissions: 164.6K
# Testcase Example:  '[[1,5,9],[10,11,13],[12,13,15]]\n8'
#
# Given a n x n matrix where each of the rows and columns are sorted in
# ascending order, find the kth smallest element in the matrix.
# 
# 
# Note that it is the kth smallest element in the sorted order, not the kth
# distinct element.
# 
# 
# Example:
# 
# matrix = [
# ⁠  [ 1,  5,  9],
# ⁠  [10, 11, 13],
# ⁠  [12, 13, 15]
# ],
# k = 8,
# 
# return 13.
# 
# 
# 
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ n2.
#
import heapq
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        h = []
        for j, e in enumerate(matrix[0]):
            heapq.heappush(h, (e, 0, j))
        ret = None
        for _ in xrange(k):
            ret, i, j = heapq.heappop(h)
            if i < len(matrix) - 1:
                heapq.heappush(h, (matrix[i+1][j], i+1, j))
        return ret

    def test(self):
        print self.kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8)
        print self.kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 9)

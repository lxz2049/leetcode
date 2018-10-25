#
# [446] Arithmetic Slices II - Subsequence
#
# https://leetcode.com/problems/arithmetic-slices-ii-subsequence/description/
#
# algorithms
# Hard (28.33%)
# Total Accepted:    11.3K
# Total Submissions: 39.7K
# Testcase Example:  '[2,4,6,8,10]'
#
# A sequence of numbers is called arithmetic if it consists of at least three
# elements and if the difference between any two consecutive elements is the
# same.
# 
# For example, these are arithmetic sequences:
# 1, 3, 5, 7, 9
# 7, 7, 7, 7
# 3, -1, -5, -9
# 
# The following sequence is not arithmetic. 1, 1, 2, 5, 7 
# 
# 
# A zero-indexed array A consisting of N numbers is given. A subsequence slice
# of that array is any sequence of integers (P0, P1, ..., Pk) such that 0 ≤ P0
# < P1 < ... < Pk < N.
# 
# A subsequence slice (P0, P1, ..., Pk) of array A is called arithmetic if the
# sequence A[P0], A[P1], ..., A[Pk-1], A[Pk] is arithmetic. In particular, this
# means that k ≥ 2.
# 
# The function should return the number of arithmetic subsequence slices in the
# array A. 
# 
# The input contains N integers. Every integer is in the range of -231 and
# 231-1 and 0 ≤ N ≤ 1000. The output is guaranteed to be less than 231-1.
# 
# 
# Example:
# 
# Input: [2, 4, 6, 8, 10]
# 
# Output: 7
# 
# Explanation:
# All arithmetic subsequence slices are:
# [2,4,6]
# [4,6,8]
# [6,8,10]
# [2,4,6,8]
# [4,6,8,10]
# [2,4,6,8,10]
# [2,6,10]
# 
# 
#
from collections import defaultdict
class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        complete = [defaultdict(int) for _ in A]
        partial = [defaultdict(int) for _ in A]
        ret = 0
        for i, a in enumerate(A):
            for j in xrange(i):
                diff = a-A[j]
                complete[i][diff] += complete[j][diff] + partial[j][diff]
                partial[i][diff] += 1
            ret += sum(complete[i].itervalues())
            
        return ret

    def test(self):
        print self.numberOfArithmeticSlices([2,4,6,8,10])
        print self.numberOfArithmeticSlices([2,2,3,4])
        print self.numberOfArithmeticSlices([2,2,3,3,4,4,5,6])

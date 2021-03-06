#
# [303] Range Sum Query - Immutable
#
# https://leetcode.com/problems/range-sum-query-immutable/description/
#
# algorithms
# Easy (32.10%)
# Total Accepted:    95K
# Total Submissions: 292.8K
# Testcase Example:  '["NumArray","sumRange","sumRange","sumRange"]\n[[[-2,0,3,-5,2,-1]],[0,2],[2,5],[0,5]]'
#
# Given an integer array nums, find the sum of the elements between indices i
# and j (i ≤ j), inclusive.
# 
# Example:
# 
# Given nums = [-2, 0, 3, -5, 2, -1]
# 
# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3
# 
# 
# 
# Note:
# 
# You may assume that the array does not change.
# There are many calls to sumRange function.
# 
# 
#
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        def accumu(l):
            total = 0
            for x in l:
                total += x
                yield total
            yield 0
        self.sums = list(accumu(nums))
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        j = min(len(self.sums)-1, j)
        #print i, j, self.sums
        return self.sums[j] - self.sums[i-1]


class Solution:
    def test(self):
        n = NumArray([-2, 0, 3, -5, 2, -1])
        print n.sumRange(0, 2)
        print n.sumRange(2, 5)
        print n.sumRange(0, 5)
    


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

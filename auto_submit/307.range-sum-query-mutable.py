#
# [307] Range Sum Query - Mutable
#
# https://leetcode.com/problems/range-sum-query-mutable/description/
#
# algorithms
# Medium (22.47%)
# Total Accepted:    44.8K
# Total Submissions: 197K
# Testcase Example:  '["NumArray","sumRange","update","sumRange"]\n[[[1,3,5]],[0,2],[1,2],[0,2]]'
#
# Given an integer array nums, find the sum of the elements between indices i
# and j (i ≤ j), inclusive.
# 
# The update(i, val) function modifies nums by updating the element at index i
# to val.
# 
# Example:
# 
# Given nums = [1, 3, 5]
# 
# sumRange(0, 2) -> 9
# update(1, 2)
# sumRange(0, 2) -> 8
# 
# 
# 
# Note:
# 
# The array is only modifiable by the update function.
# You may assume the number of calls to update and sumRange function is
# distributed evenly.
# 
# 
#
import math
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        if not nums:
            return

        self.count = len(nums)
        self.height = int(math.ceil(math.log(len(nums), 2)))
        self.tree = [0] * ((2 << self.height) - 1)
        def build(i, l, r):
            #print 'build', i, l, r
            if l==r:
                self.tree[i] = nums[l]
                return nums[l]
            self.tree[i] = build(2*i+1, l, (l+r)/2) + build(2*i+2, (l+r)/2+1, r)
            return self.tree[i]
        build(0, 0, len(nums)-1)
        #print "build tree", self.count, self.height, self.tree
        

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        if not self.tree:
            return

        def updatetree(idx, l, r):
            #print 'update', i, idx, l, r
            if l == r:
                diff = val - self.tree[idx]
                self.tree[idx] += diff
                return diff
            mid = (l+r)/2
            if l <= i <= mid:
                diff = updatetree(2*idx+1, l, mid)
            else:
                diff = updatetree(2*idx+2, mid+1, r)
            self.tree[idx] += diff
            return diff
        updatetree(0, 0, self.count-1)
        #print self.tree
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if not self.tree:
            return 0

        def getsum(i, j, l, r, idx):
            #print "sumRange", i, j, l, r, idx
            if i > j:
                return 0
            if l == i and r == j:
                return self.tree[idx]

            mid = (l+r)/2
            sl = getsum(i, min(mid, j), l, mid, idx*2+1)
            sr = getsum(max(mid+1, i), j, mid+1, r, idx*2+2)
            return sl + sr

        return getsum(i, j, 0, self.count-1, 0)
        

class Solution:
    def test(self):
        n = NumArray([1, 3, 5])
        print n.sumRange(0, 2), 9
        n.update(1, 2)
        print n.sumRange(0, 2), 8

        n = NumArray([0, 9, 5, 7, 3])
        print n.sumRange(0, 2), 14
        n.update(1, 2)
        print n.sumRange(0, 2), 7

        n = NumArray([5, 18, 13])
        print n.sumRange(0, 2), 36
        n.update(1, -1)
        n.update(2, 3)
        n.update(0, 5)
        n.update(0, -4)
        print n.sumRange(0, 2), -2

        print "*************"
        n = NumArray([0, 9, 5, 7, 3])
        print n.sumRange(4, 4), 3
        print n.sumRange(2, 4), 15
        print n.sumRange(3, 3), 7
        n.update(4, 5)
        n.update(1, 7)
        n.update(0, 8)
        print n.sumRange(1, 2), 12
        n.update(1, 9)
        print n.sumRange(4, 4), 5
        n.update(3, 9)



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)

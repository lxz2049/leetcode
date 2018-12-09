#
# [33] Search in Rotated Sorted Array
#
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (32.31%)
# Total Accepted:    334.3K
# Total Submissions: 1M
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
# 
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
# 
# You are given a target value to search. If found in the array return its
# index, otherwise return -1.
# 
# You may assume no duplicate exists in the array.
# 
# Your algorithm's runtime complexity must be in the order of O(log n).
# 
# Example 1:
# 
# 
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# 
# 
# Example 2:
# 
# 
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# 
#
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + hi >> 1
            if nums[mid] == target:
                return mid
            if nums[mid] < target <= nums[hi] or \
                    nums[mid] > nums[hi] and (target < nums[lo] or target > nums[mid]):
                lo = mid + 1
            else:
                hi = mid - 1
        return -1

    def test(self):
        for i in xrange(8): print self.search([4,5,6,7,0,1,2], i)
        for i in xrange(4): print self.search([0, 1, 2, 3], i)
        print self.search([5, 1, 2], 5)
        print self.search([3, 5, 1], 5)


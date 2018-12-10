#
# [81] Search in Rotated Sorted Array II
#
# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/
#
# algorithms
# Medium (32.42%)
# Total Accepted:    146.8K
# Total Submissions: 452.8K
# Testcase Example:  '[2,5,6,0,0,1,2]\n0'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
# 
# (i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).
# 
# You are given a target value to search. If found in the array return true,
# otherwise return false.
# 
# Example 1:
# 
# 
# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false
# 
# Follow up:
# 
# 
# This is a follow up problem to Search in Rotated Sorted Array, where nums may
# contain duplicates.
# Would this affect the run-time complexity? How and why?
# 
# 
#
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + hi >> 1
            if nums[mid] == target:
                return True
            if nums[lo] == nums[mid] == nums[hi]:
                lo += 1
            elif nums[mid] < target <= nums[hi] or \
               target > nums[mid] >= nums[lo] or \
               target < nums[lo] <= nums[mid]:
                lo = mid + 1
            else:
                hi = mid - 1
        return False

    def test(self):
        print self.search([2,5,6,0,0,1,2], 0)
        print self.search([2,5,6,0,0,1,2], 3)
        print self.search([5,1,3], 5)

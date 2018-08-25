#
# [665] Non-decreasing Array
#
# https://leetcode.com/problems/non-decreasing-array/description/
#
# algorithms
# Easy (20.06%)
# Total Accepted:    31.5K
# Total Submissions: 158.1K
# Testcase Example:  '[4,2,3]'
#
# 
# Given an array with n integers, your task is to check if it could become
# non-decreasing by modifying at most 1 element.
# 
# 
# 
# We define an array is non-decreasing if array[i]  holds for every i (1 
# 
# Example 1:
# 
# Input: [4,2,3]
# Output: True
# Explanation: You could modify the first 4 to 1 to get a non-decreasing
# array.
# 
# 
# 
# Example 2:
# 
# Input: [4,2,1]
# Output: False
# Explanation: You can't get a non-decreasing array by modify at most one
# element.
# 
# 
# 
# Note:
# The n belongs to [1, 10,000].
# 
#
class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cnt = 0
        nums_clone = list(reversed(nums))
        for i in xrange(len(nums)-1):
            if nums[i] > nums[i+1]:
                nums[i+1] = nums[i]
                cnt += 1
        cnt_clone = 0
        for i in xrange(len(nums_clone)-1):
            if nums_clone[i] < nums_clone[i+1]:
                nums_clone[i+1] = nums_clone[i]
                cnt_clone += 1
        return cnt <= 1 or cnt_clone <= 1

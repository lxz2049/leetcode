#
# [493] Reverse Pairs
#
# https://leetcode.com/problems/reverse-pairs/description/
#
# algorithms
# Hard (21.13%)
# Total Accepted:    16.2K
# Total Submissions: 76.5K
# Testcase Example:  '[1,3,2,3,1]'
#
# Given an array nums, we call (i, j) an important reverse pair if i < j and
# nums[i] > 2*nums[j].
# 
# You need to return the number of important reverse pairs in the given array.
# 
# Example1:
# 
# Input: [1,3,2,3,1]
# Output: 2
# 
# 
# Example2:
# 
# Input: [2,4,3,5,1]
# Output: 3
# 
# 
# Note:
# 
# The length of the given array will not exceed 50,000.
# All the numbers in the input array are in the range of 32-bit integer.
# 
# 
#
from bisect import bisect_right
class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def merge(nums):
            if len(nums) < 2:
                return 0
            nums_left = nums[:len(nums)/2]
            nums_right = nums[len(nums)/2:]
            rank_left = merge(nums_left)
            rank_right = merge(nums_right)
            rank = sum(len(nums_left) - bisect_right(nums_left, 2*n) for n in nums_right)
            i = left = right = 0
            while left < len(nums_left) and right < len(nums_right):
                if nums_left[left] < nums_right[right]:
                    nums[i] = nums_left[left]
                    left += 1
                    i += 1
                else:
                    nums[i] = nums_right[right]
                    right += 1
                    i += 1
            while left < len(nums_left):
                nums[i] = nums_left[left]
                left += 1
                i += 1
            while right < len(nums_right):
                nums[i] = nums_right[right]
                right += 1
                i += 1
            rank += rank_left + rank_right
            return rank

        return merge(nums)

    def test(self):
        print self.reversePairs([1,3,2,3,1])
        print self.reversePairs([2,4,3,5,1])

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
                return 0, nums
            rank_left, nums_left = merge(nums[:len(nums)/2])
            rank_right, nums_right = merge(nums[len(nums)/2:])
            rank = sum(len(nums_left) - bisect_right(nums_left, 2*n) for n in nums_right)
            i = left = right = 0
            nums = [] 
            while left < len(nums_left) and right < len(nums_right):
                if nums_left[left] < nums_right[right]:
                    nums.append(nums_left[left])
                    left += 1
                else:
                    nums.append(nums_right[right])
                    right += 1
            nums += nums_left[left:]
            nums += nums_right[right:]
            rank += rank_left + rank_right
            #print rank, nums_left, nums_right, nums
            return rank, nums

        rank, nums = merge(nums)
        return rank

    def test(self):
        print self.reversePairs([1,3,2,3,1])
        print self.reversePairs([2,4,3,5,1])

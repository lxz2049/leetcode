#
# [581] Shortest Unsorted Continuous Subarray
#
# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/description/
#
# algorithms
# Easy (29.14%)
# Total Accepted:    35K
# Total Submissions: 119.1K
# Testcase Example:  '[2,6,4,8,10,9,15]'
#
# Given an integer array, you need to find one continuous subarray that if you
# only sort this subarray in ascending order, then the whole array will be
# sorted in ascending order, too.  
# 
# You need to find the shortest such subarray and output its length.
# 
# Example 1:
# 
# Input: [2, 6, 4, 8, 10, 9, 15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the
# whole array sorted in ascending order.
# 
# 
# 
# Note:
# 
# Then length of the input array is in range [1, 10,000].
# The input array may contain duplicates, so ascending order here means . 
# 
# 
#
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        nums_sorted = sorted(nums)
        for i in range(0, len(nums)):
            if nums[i] != nums_sorted[i]:
                break

        for j in reversed(range(0, len(nums))):
            if nums[j] != nums_sorted[j]:
                break
        
        if j <= i:
            return 0
        return j-i+1

    def test(self):
        print self.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15])
        print self.findUnsortedSubarray([2, 6, 6, 4, 8, 10, 9, 15])
        print self.findUnsortedSubarray([2, 6, 6, 4, 8, 10, 9, 9, 15])
        print self.findUnsortedSubarray([1])
        print self.findUnsortedSubarray([1, 2, 3, 4])
        print self.findUnsortedSubarray([3, 1])
        print self.findUnsortedSubarray([1, 2, 4, 5, 3])

#
# [153] Find Minimum in Rotated Sorted Array
#
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
#
# algorithms
# Medium (41.99%)
# Total Accepted:    240.6K
# Total Submissions: 572.9K
# Testcase Example:  '[3,4,5,1,2]'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
# 
# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
# 
# Find the minimum element.
# 
# You may assume no duplicate exists in the array.
# 
# Example 1:
# 
# 
# Input: [3,4,5,1,2] 
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input: [4,5,6,7,0,1,2]
# Output: 0
# 
# 
#
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return min(nums)
        if nums[0] <= nums[-1]:
            return nums[0]

        lo, hi = 0, len(nums)
        while lo < hi:
            mid = lo + hi >> 1
            if nums[mid] >= nums[0]:
                lo = mid + 1
            else:
                hi = mid
        return nums[lo]

    def test(self):
        print self.findMin([2])
        print self.findMin([1,2])
        print self.findMin([2,1])
        print self.findMin([3,4,5,1,2])
        print self.findMin([4,5,6,7,0,1,2])

#
# [540] Single Element in a Sorted Array
#
# https://leetcode.com/problems/single-element-in-a-sorted-array/description/
#
# algorithms
# Medium (55.83%)
# Total Accepted:    30.3K
# Total Submissions: 54.3K
# Testcase Example:  '[1,1,2]'
#
# 
# Given a sorted array consisting of only integers where every element appears
# twice except for one element which appears once. Find this single element
# that appears only once. 
# 
# 
# Example 1:
# 
# Input: [1,1,2,3,3,4,4,8,8]
# Output: 2
# 
# 
# 
# Example 2:
# 
# Input: [3,3,7,7,10,11,11]
# Output: 10
# 
# 
# 
# Note:
# Your solution should run in O(log n) time and O(1) space.
# 
# 
#
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l+r)//2
            #print mid
            if (mid < len(nums) - 1 and nums[mid] != nums[mid+1]) and \
               (mid > 0 and nums[mid] != nums[mid-1]) or \
               (mid == 0 and nums[0] != nums[1]) or \
               (mid == len(nums) - 1 and nums[mid] != nums[mid-1]):
                   break
            if nums[mid] == nums[mid + (-1 if mid % 2 else 1)]:
                l = mid + 1
            else:
                r = mid - 1
                
        return nums[mid]

    def test(self):
        print self.singleNonDuplicate([1,1,2,3,3,4,4,8,8])
        print self.singleNonDuplicate([3,3,7,7,10,11,11])
        print self.singleNonDuplicate([1,1,2])

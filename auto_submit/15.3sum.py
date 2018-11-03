#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum/description/
#
# algorithms
# Medium (22.25%)
# Total Accepted:    409.2K
# Total Submissions: 1.8M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an array nums of n integers, are there elements a, b, c in nums such
# that a + b + c = 0? Find all unique triplets in the array which gives the sum
# of zero.
# 
# Note:
# 
# The solution set must not contain duplicate triplets.
# 
# Example:
# 
# 
# Given array nums = [-1, 0, 1, 2, -1, -4],
# 
# A solution set is:
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
# 
# 
#
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        nums.sort()
        for i in xrange(len(nums)):
            if i and nums[i] == nums[i-1]:
                continue
            lo = i + 1
            hi = len(nums) - 1
            while lo < hi:
                three = nums[i] + nums[lo] + nums[hi]
                if three == 0:
                   ret.append([nums[i], nums[lo], nums[hi]])
                   lo += 1
                   while lo < hi and nums[lo] == nums[lo-1]:
                       lo += 1
                elif three > 0:
                    hi -= 1
                else:
                    lo += 1
        return ret

    def test(self):
        print self.threeSum([-1, 0, 1, 2, -1, -4])

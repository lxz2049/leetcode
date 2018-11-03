#
# [18] 4Sum
#
# https://leetcode.com/problems/4sum/description/
#
# algorithms
# Medium (28.55%)
# Total Accepted:    187.3K
# Total Submissions: 654.7K
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# Given an array nums of n integers and an integer target, are there elements
# a, b, c, and d in nums such that a + b + c + d = target? Find all unique
# quadruplets in the array which gives the sum of target.
# 
# Note:
# 
# The solution set must not contain duplicate quadruplets.
# 
# Example:
# 
# 
# Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
# 
# A solution set is:
# [
# ⁠ [-1,  0, 0, 1],
# ⁠ [-2, -1, 1, 2],
# ⁠ [-2,  0, 0, 2]
# ]
# 
# 
#
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret = []
        nums.sort()
        for i in xrange(len(nums)):
            if i and nums[i] == nums[i-1]:
                continue
            if nums[i] * 4 > target:
                break
            for j in xrange(i+1, len(nums)):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                lo = j+1
                hi = len(nums) - 1
                while lo < hi:
                    four = [nums[i], nums[j], nums[lo], nums[hi]]
                    fourSum = sum(four)
                    if fourSum == target:
                        ret.append(four)
                        lo += 1
                        while lo < hi and nums[lo] == nums[lo-1]:
                            lo += 1
                    elif fourSum < target:
                        lo += 1
                    else:
                        hi -= 1
        return ret

    def test(self):
        print self.fourSum([1, 0, -1, 0, -2, 2], 0)
        print self.fourSum([0, 0, 0, 0], 0)

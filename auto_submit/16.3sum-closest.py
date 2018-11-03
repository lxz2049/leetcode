#
# [16] 3Sum Closest
#
# https://leetcode.com/problems/3sum-closest/description/
#
# algorithms
# Medium (32.86%)
# Total Accepted:    210.9K
# Total Submissions: 640.9K
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# Given an array nums of n integers and an integer target, find three integers
# in nums such that the sum is closest to target. Return the sum of the three
# integers. You may assume that each input would have exactly one solution.
# 
# Example:
# 
# 
# Given array nums = [-1, 2, 1, -4], and target = 1.
# 
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# 
# 
#
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ret = nums[0] + nums[1] + nums[2]
        nums.sort()
        for i in xrange(len(nums)):
            lo = i + 1
            hi = len(nums) - 1
            while lo < hi:
                three = nums[i] + nums[lo] + nums[hi]
                if abs(three - target) < abs(ret - target):
                    ret = three
                if three == target:
                    return target
                if three < target:
                    lo += 1
                else:
                    hi -= 1
        return ret

    def test(self):
        print self.threeSumClosest([-1, 2, 1, -4], 1)
        print self.threeSumClosest([-1, 2, 1, -4], -4)
        print self.threeSumClosest([1, 1, 1, 0], -100)

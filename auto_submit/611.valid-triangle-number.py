#
# [611] Valid Triangle Number
#
# https://leetcode.com/problems/valid-triangle-number/description/
#
# algorithms
# Medium (43.37%)
# Total Accepted:    27.9K
# Total Submissions: 64.5K
# Testcase Example:  '[2,2,3,4]'
#
# Given an array consists of non-negative integers,  your task is to count the
# number of triplets chosen from the array that can make triangles if we take
# them as side lengths of a triangle.
# 
# Example 1:
# 
# Input: [2,2,3,4]
# Output: 3
# Explanation:
# Valid combinations are: 
# 2,3,4 (using the first 2)
# 2,3,4 (using the second 2)
# 2,2,3
# 
# 
# 
# Note:
# 
# The length of the given array won't exceed 1000.
# The integers in the given array are in the range of [0, 1000].
# 
# 
# 
#
class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        nums.sort()
        ret, k = 0, 2
        for i in xrange(N):
            if nums[i] == 0:
                continue
            k = i + 2
            for j in xrange(i+1, N):
                while k < N and nums[i] + nums[j] > nums[k]:
                    k += 1
                ret += k - j - 1
                #if k > j + 1: print nums[i], nums[j], nums[k] if k < N else -1
        return ret

    def test(self):
        print self.triangleNumber([2,2,3,4])
        print self.triangleNumber([0, 0, 0])
        print self.triangleNumber([1,2,3,4,5,6])

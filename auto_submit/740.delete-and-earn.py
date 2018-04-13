#
# [740] Delete and Earn
#
# https://leetcode.com/problems/delete-and-earn/description/
#
# algorithms
# Medium (43.74%)
# Total Accepted:    8K
# Total Submissions: 18.4K
# Testcase Example:  '[3,4,2]'
#
# 
# Given an array nums of integers, you can perform operations on the array.
# 
# In each operation, you pick any nums[i] and delete it to earn nums[i]
# points.  After, you must delete every element equal to nums[i] - 1 or nums[i]
# + 1.
# 
# You start with 0 points.  Return the maximum number of points you can earn by
# applying such operations.
# 
# 
# Example 1:
# 
# Input: nums = [3, 4, 2]
# Output: 6
# Explanation: 
# Delete 4 to earn 4 points, consequently 3 is also deleted.
# Then, delete 2 to earn 2 points. 6 total points are earned.
# 
# 
# 
# Example 2:
# 
# Input: nums = [2, 2, 3, 3, 3, 4]
# Output: 9
# Explanation: 
# Delete 3 to earn 3 points, deleting both 2's and the 4.
# Then, delete 3 again to earn 3 points, and 3 again to earn 3 points.
# 9 total points are earned.
# 
# 
# 
# Note:
# The length of nums is at most 20000.
# Each element nums[i] is an integer in the range [1, 10000].
# 
#
class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import collections
        c = collections.Counter(nums)
        ans = 0
        sofar_with = 0
        sofar_without = 0
        prev = 0
        for num, point in sorted(c.items()):
            if num > prev + 1:
                sofar_without = max(sofar_with, sofar_without)
                sofar_with = sofar_without + num * point
            else:
                sofar_without, sofar_with = \
                max(sofar_with, sofar_without), sofar_without + num * point
            prev = num
            ans = max(ans, sofar_with, sofar_without)
            #print c, num, point, sofar_with, sofar_without
 
        return ans

    def test(self):
        print self.deleteAndEarn([2, 2, 3, 3, 3, 4]), 9
        print self.deleteAndEarn([2, 3, 4]), 6
        print self.deleteAndEarn([3, 1]), 4
        print self.deleteAndEarn([1, 6, 3, 3, 8, 4, 8, 10, 1, 3]), 43


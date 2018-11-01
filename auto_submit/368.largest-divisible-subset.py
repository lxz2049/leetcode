#
# [368] Largest Divisible Subset
#
# https://leetcode.com/problems/largest-divisible-subset/description/
#
# algorithms
# Medium (34.11%)
# Total Accepted:    40K
# Total Submissions: 117.3K
# Testcase Example:  '[1,2,3]'
#
# Given a set of distinct positive integers, find the largest subset such that
# every pair (Si, Sj) of elements in this subset satisfies:
# 
# Si % Sj = 0 or Sj % Si = 0.
# 
# If there are multiple solutions, return any subset is fine.
# 
# Example 1:
# 
# 
# 
# Input: [1,2,3]
# Output: [1,2] (of course, [1,3] will also be ok)
# 
# 
# 
# Example 2:
# 
# 
# Input: [1,2,4,8]
# Output: [1,2,4,8]
# 
# 
# 
#
class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        ret = []
        dp = []
        for i in xrange(len(nums)):
            try:
                m = max((dp[j] for j in xrange(i) if nums[i] % nums[j] == 0), key=len)
                dp.append(m[:])
            except:
                dp.append([])
            dp[i].append(nums[i])
            if len(dp[i]) > len(ret):
                ret = dp[i]
        return ret

    def test(self):
        print self.largestDivisibleSubset([1,2,3])
        print self.largestDivisibleSubset([1,2,4,8])

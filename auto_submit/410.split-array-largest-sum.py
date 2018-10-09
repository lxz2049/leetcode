#
# [410] Split Array Largest Sum
#
# https://leetcode.com/problems/split-array-largest-sum/description/
#
# algorithms
# Hard (40.23%)
# Total Accepted:    28.7K
# Total Submissions: 71.5K
# Testcase Example:  '[7,2,5,10,8]\n2'
#
# Given an array which consists of non-negative integers and an integer m, you
# can split the array into m non-empty continuous subarrays. Write an algorithm
# to minimize the largest sum among these m subarrays.
# 
# 
# Note:
# If n is the length of array, assume the following constraints are satisfied:
# 
# 1 ≤ n ≤ 1000
# 1 ≤ m ≤ min(50, n)
# 
# 
# 
# Examples: 
# 
# Input:
# nums = [7,2,5,10,8]
# m = 2
# 
# Output:
# 18
# 
# Explanation:
# There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8],
# where the largest sum among the two subarrays is only 18.
# 
# 
#
from collections import defaultdict
class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        presum = nums[:]
        for i, n in enumerate(presum):
            presum[i] += presum[i-1] if i else 0
        subsum = lambda i, j: presum[j] - presum[i] + nums[i]

        dp = defaultdict(int)
        for i, n in enumerate(nums):
            dp[i, 1] = subsum(0, i)
            for j in xrange(2, min(i+2, m+1)):
                dp[i, j] = min(max(dp[k, j-1], subsum(k+1, i)) for k in xrange(i))
                #print "dp[%s, %s]" % (i, j), dp[i, j]
        #print dp
        return dp[len(nums)-1, m]

    def test(self):
        print self.splitArray([7,2,5,10,8], 2)
        print self.splitArray([1, 2147483647], 2)

#
# [560] Subarray Sum Equals K
#
# https://leetcode.com/problems/subarray-sum-equals-k/description/
#
# algorithms
# Medium (40.07%)
# Total Accepted:    32.3K
# Total Submissions: 80.7K
# Testcase Example:  '[1,1,1]\n2'
#
# Given an array of integers and an integer k, you need to find the total
# number of continuous subarrays whose sum equals to k.
# 
# Example 1:
# 
# Input:nums = [1,1,1], k = 2
# Output: 2
# 
# 
# 
# Note:
# 
# The length of the array is in range [1, 20,000].
# The range of numbers in the array is [-1000, 1000] and the range of the
# integer k is [-1e7, 1e7].
# 
# 
#
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import collections
        m = collections.defaultdict(int)
        m[0] = 1
        asum = 0
        ans = 0
        for n in nums:
            asum += n
            if asum - k in m:
                ans += m[asum-k]
            m[asum] += 1
        #print m
        return ans

    def test(self):
        print 2, self.subarraySum([1, 1, 1], 2)
        print 1, self.subarraySum([1, 1], 2)
        print 55, self.subarraySum([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 0)


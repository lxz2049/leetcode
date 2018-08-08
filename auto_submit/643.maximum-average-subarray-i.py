#
# [643] Maximum Average Subarray I
#
# https://leetcode.com/problems/maximum-average-subarray-i/description/
#
# algorithms
# Easy (37.49%)
# Total Accepted:    29.7K
# Total Submissions: 78.8K
# Testcase Example:  '[1,12,-5,-6,50,3]\n4'
#
# 
# Given an array consisting of n integers, find the contiguous subarray of
# given length k that has the maximum average value. And you need to output the
# maximum average value.
# 
# 
# Example 1:
# 
# Input: [1,12,-5,-6,50,3], k = 4
# Output: 12.75
# Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
# 
# 
# 
# Note:
# 
# 1 k n 
# Elements of the given array will be in the range [-10,000, 10,000].
# 
# 
#
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        max_avg = -10000
        cur_avg = 0.0
        for i, n in enumerate(nums):
            if i >= k:
                cur_avg = cur_avg - float(nums[i-k])/k + float(n)/k
                max_avg = max(cur_avg, max_avg)
            else:
                cur_avg += float(n)/k
                if i == k-1:
                    max_avg = max(cur_avg, max_avg)
            #print cur_avg
        return max_avg

    def test(self):
        print self.findMaxAverage([1,12,-5,-6,50,3], 4)

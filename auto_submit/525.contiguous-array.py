#
# [525] Contiguous Array
#
# https://leetcode.com/problems/contiguous-array/description/
#
# algorithms
# Medium (41.38%)
# Total Accepted:    23.1K
# Total Submissions: 55.9K
# Testcase Example:  '[0,1]'
#
# Given a binary array, find the maximum length of a contiguous subarray with
# equal number of 0 and 1. 
# 
# 
# Example 1:
# 
# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0
# and 1.
# 
# 
# 
# Example 2:
# 
# Input: [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal
# number of 0 and 1.
# 
# 
# 
# Note:
# The length of the given binary array will not exceed 50,000.
# 
#
class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = 0
        m = {0: -1}
        max_len = 0
        for i, n in enumerate(nums):
            if n > 0:
                s += 1
            else:
                s -= 1
            if s in m:
                max_len = max(max_len, i - m[s])
            else:
                m[s] = i
        #print m
        return max_len

    def test(self):
        print self.findMaxLength([0, 1, 0])
        print self.findMaxLength([0, 1])

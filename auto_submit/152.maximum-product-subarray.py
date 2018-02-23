#
# [152] Maximum Product Subarray
#
# https://leetcode.com/problems/maximum-product-subarray/description/
#
# algorithms
# Medium (26.59%)
# Total Accepted:    130.8K
# Total Submissions: 491.9K
# Testcase Example:  '[-2]'
#
# 
# Find the contiguous subarray within an array (containing at least one number)
# which has the largest product.
# 
# 
# 
# For example, given the array [2,3,-2,4],
# the contiguous subarray [2,3] has the largest product = 6.
# 
#
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        it = iter(nums)
        pmax = tmax = tmin = it.next()
        for n in it:
            tmax, tmin = max(n, tmax*n, tmin*n), min(n, tmax*n, tmin*n)
            pmax = max(tmax, pmax)
        return pmax

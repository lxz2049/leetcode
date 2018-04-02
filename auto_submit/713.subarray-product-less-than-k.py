#
# [713] Subarray Product Less Than K
#
# https://leetcode.com/problems/subarray-product-less-than-k/description/
#
# algorithms
# Medium (33.14%)
# Total Accepted:    9.1K
# Total Submissions: 27.4K
# Testcase Example:  '[10,5,2,6]\n100'
#
# Your are given an array of positive integers nums.
# Count and print the number of (contiguous) subarrays where the product of all
# the elements in the subarray is less than k.
# 
# Example 1:
# 
# Input: nums = [10, 5, 2, 6], k = 100
# Output: 8
# Explanation: The 8 subarrays that have product less than 100 are: [10], [5],
# [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
# Note that [10, 5, 2] is not included as the product of 100 is not strictly
# less than k.
# 
# 
# 
# Note:
# 0 < nums.length .
# 0 < nums[i] < 1000.
# 0 .
# 
#
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l = 0
        ans = 0
        prod = 1
        for i in range(0, len(nums)):
            #print nums[i], prod*nums[i]
            prod *= nums[i]
            while l < len(nums) and prod >= k:
                prod /= nums[l]
                l += 1
            ans += max(0, i-l + 1)
            #print  nums[l:i+1]
        return ans

    def test(self):
        print self.numSubarrayProductLessThanK([10, 5, 2, 6], 100)
        print self.numSubarrayProductLessThanK([10, 5, 2, 6], 0)
        print self.numSubarrayProductLessThanK([1, 1, 1, 1, 1, 1, 1, 1], 5)
                


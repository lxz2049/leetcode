#
# [209] Minimum Size Subarray Sum
#
# https://leetcode.com/problems/minimum-size-subarray-sum/description/
#
# algorithms
# Medium (32.06%)
# Total Accepted:    113K
# Total Submissions: 352.6K
# Testcase Example:  '7\n[2,3,1,2,4,3]'
#
# 
# Given an array of n positive integers and a positive integer s, find the
# minimal length of a contiguous subarray of which the sum ≥ s. If there isn't
# one, return 0 instead.
# 
# 
# For example, given the array [2,3,1,2,4,3] and s = 7,
# the subarray [4,3] has the minimal length under the problem constraint.
# 
# 
# click to show more practice.
# 
# More practice:
# 
# If you have figured out the O(n) solution, try coding another solution of
# which the time complexity is O(n log n).
# 
# 
# Credits:Special thanks to @Freezen for adding this problem and creating all
# test cases.
#
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        sumlr = ans = 0
        l = 0
        for i in range(0, len(nums)):
            sumlr += nums[i]
            while sumlr >= s:
                ans = min(ans, i-l+1) if ans > 0 else i-l+1
                sumlr -= nums[l]
                l += 1
        return ans

    def test(self):
        print self.minSubArrayLen(7, [2, 3, 1, 2, 4, 3])

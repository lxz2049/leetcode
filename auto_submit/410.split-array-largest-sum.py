#
# [410] Split Array Largest Sum
#
# https://leetcode.com/problems/split-array-largest-sum/description/
#
# algorithms
# Hard (40.20%)
# Total Accepted:    28.9K
# Total Submissions: 71.8K
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
class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        def solve(k):
            rs = rm = 0
            for n in nums:
                if rs + n > k:
                    rs = 0
                    rm += 1
                rs += n
            rm += rs > 0
            #print k, rm
            return rm <= m

        # bisect
        lo = max(nums)
        hi = sum(nums) + 1
        while lo < hi:
            #print lo, hi
            mid = (lo + hi) / 2
            if solve(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
    
    def test(self):
        print self.splitArray([7,2,5,10,8], 2)
            


#
# [416] Partition Equal Subset Sum
#
# https://leetcode.com/problems/partition-equal-subset-sum/description/
#
# algorithms
# Medium (38.76%)
# Total Accepted:    59.6K
# Total Submissions: 153.5K
# Testcase Example:  '[1,5,11,5]'
#
# Given a non-empty array containing only positive integers, find if the array
# can be partitioned into two subsets such that the sum of elements in both
# subsets is equal.
# 
# 
# Note:
# 
# Each of the array element will not exceed 100.
# The array size will not exceed 200.
# 
# 
# 
# Example 1:
# 
# Input: [1, 5, 11, 5]
# 
# Output: true
# 
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
# 
# 
# 
# Example 2:
# 
# Input: [1, 2, 3, 5]
# 
# Output: false
# 
# Explanation: The array cannot be partitioned into equal sum subsets.
# 
# 
#
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)
        if total % 2 > 0:
            return False

        target = total / 2
        sums = {0}
        for n in nums:
            sums |= {s + n for s in sums}
            #print target, sums
            if target in sums:
                return True
        return False
        
        
    def test(self):
        print self.canPartition([1,2,3,5])
        print self.canPartition([1,5,11,5])
        print self.canPartition([1,2,3,4,5,6,7])

#
# [334] Increasing Triplet Subsequence
#
# https://leetcode.com/problems/increasing-triplet-subsequence/description/
#
# algorithms
# Medium (39.31%)
# Total Accepted:    76.4K
# Total Submissions: 194.4K
# Testcase Example:  '[1,2,3,4,5]'
#
# Given an unsorted array return whether an increasing subsequence of length 3
# exists or not in the array.
# 
# Formally the function should:
# 
# Return true if there exists i, j, k 
# such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return
# false.
# 
# Note: Your algorithm should run in O(n) time complexity and O(1) space
# complexity.
# 
# 
# Example 1:
# 
# 
# Input: [1,2,3,4,5]
# Output: true
# 
# 
# 
# Example 2:
# 
# 
# Input: [5,4,3,2,1]
# Output: false
# 
# 
# 
#
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False

        one = nums[0]
        two = None
        for n in nums:
            if two is not None and n > two:
                return True
            if n > one:
                two = min(two, n) if two is not None else n
            one = min(one, n)
        return False

    def test(self):
        print self.increasingTriplet([])
        print self.increasingTriplet([1])
        print self.increasingTriplet([1,2,3,4,5])
        print self.increasingTriplet([2,2,3,4,4])
        print self.increasingTriplet([3,2,1,0])

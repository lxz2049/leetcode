#
# [137] Single Number II
#
# https://leetcode.com/problems/single-number-ii/description/
#
# algorithms
# Medium (44.41%)
# Total Accepted:    151.3K
# Total Submissions: 340.6K
# Testcase Example:  '[2,2,3,2]'
#
# Given a non-empty array of integers, every element appears three times except
# for one, which appears exactly once. Find that single one.
# 
# Note:
# 
# Your algorithm should have a linear runtime complexity. Could you implement
# it without using extra memory?
# 
# Example 1:
# 
# 
# Input: [2,2,3,2]
# Output: 3
# 
# 
# Example 2:
# 
# 
# Input: [0,1,0,1,0,1,99]
# Output: 99
# 
#
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set()
        candidates = set()
        for n in nums:
            if n not in seen:
                seen.add(n)
                candidates.add(n)
            elif n in candidates:
                candidates.remove(n)
        return candidates.pop()

    def test(self):
        print self.singleNumber([2,2,0,2])
        print self.singleNumber([2,2,3,2])
        print self.singleNumber([0,1,0,1,0,1,99])

#
# [90] Subsets II
#
# https://leetcode.com/problems/subsets-ii/description/
#
# algorithms
# Medium (39.93%)
# Total Accepted:    172.7K
# Total Submissions: 429.5K
# Testcase Example:  '[1,2,2]'
#
# Given a collection of integers that might contain duplicates, nums, return
# all possible subsets (the power set).
# 
# Note: The solution set must not contain duplicate subsets.
# 
# Example:
# 
# 
# Input: [1,2,2]
# Output:
# [
# ⁠ [2],
# ⁠ [1],
# ⁠ [1,2,2],
# ⁠ [2,2],
# ⁠ [1,2],
# ⁠ []
# ]
# 
# 
#
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ret = []
        def traverse(st, candidate):
            ret.append(candidate)
            for i in xrange(st, len(nums)):
                if i > st and nums[i-1] == nums[i]:
                    continue
                traverse(i+1, candidate + [nums[i]])
        traverse(0, [])
        return ret

    def test(self):
        print self.subsetsWithDup([1,2,2])

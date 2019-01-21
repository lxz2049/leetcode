#
# [46] Permutations
#
# https://leetcode.com/problems/permutations/description/
#
# algorithms
# Medium (51.58%)
# Total Accepted:    310.1K
# Total Submissions: 598.8K
# Testcase Example:  '[1,2,3]'
#
# Given a collection of distinct integers, return all possible permutations.
# 
# Example:
# 
# 
# Input: [1,2,3]
# Output:
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
# 
# 
#
from itertools import permutations
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        def traverse(candidates, perm):
            if len(perm) == len(nums):
                ret.append([nums[i] for i in perm])
                return
            for i in candidates:
                candidates.remove(i)
                traverse(candidates, perm + [i])
                candidates.add(i)

        traverse(set(range(len(nums))), [])
            
        return ret

    def test(self):
        print self.permute([1,2,3])

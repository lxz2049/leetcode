#
# [77] Combinations
#
# https://leetcode.com/problems/combinations/description/
#
# algorithms
# Medium (43.69%)
# Total Accepted:    164.4K
# Total Submissions: 376.2K
# Testcase Example:  '4\n2'
#
# Given two integers n and k, return all possible combinations of k numbers out
# of 1 ... n.
# 
# Example:
# 
# 
# Input: n = 4, k = 2
# Output:
# [
# ⁠ [2,4],
# ⁠ [3,4],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ [1,3],
# ⁠ [1,4],
# ]
# 
# 
#
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ret = []
        def traverse(candidate, m, s):
            if m == k:
                ret.append(list(candidate))
                return
            for i in xrange(s+1, n+1):
                candidate.append(i)
                traverse(candidate, m+1, i)
                candidate.pop()
                    
        traverse([], 0, 0)
        return ret

    def test(self):
        print self.combine(4, 2)

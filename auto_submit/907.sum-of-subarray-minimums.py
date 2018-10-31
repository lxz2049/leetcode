#
# [943] Sum of Subarray Minimums
#
# https://leetcode.com/problems/sum-of-subarray-minimums/description/
#
# algorithms
# Medium (20.68%)
# Total Accepted:    4.2K
# Total Submissions: 19.6K
# Testcase Example:  '[3,1,2,4]'
#
# Given an array of integers A, find the sum of min(B), where B ranges over
# every (contiguous) subarray of A.
# 
# Since the answer may be large, return the answer modulo 10^9 + 7.
# 
# 
# 
# Example 1:
# 
# 
# Input: [3,1,2,4]
# Output: 17
# Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2],
# [1,2,4], [3,1,2,4]. 
# Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 30000
# 1 <= A[i] <= 30000
# 
# 
# 
# 
# 
# 
#
MOD = 1000000007
class Solution(object):
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        ret = 0
        last = 0
        stack = [(0, 0, -1)]
        for i, a in enumerate(A):
            while stack and a < stack[-1][0]:
                stack.pop()
            _, val, j = stack[-1]
            val += a * (i-j)
            ret = (ret + val) % MOD
            stack.append((a, val, i))
        return ret
    
    def test(self):
        print self.sumSubarrayMins([3,1,2,4])


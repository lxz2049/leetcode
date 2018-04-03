#
# [811] Number of Subarrays with Bounded Maximum
#
# https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/description/
#
# algorithms
# Medium (39.96%)
# Total Accepted:    3.1K
# Total Submissions: 7.6K
# Testcase Example:  '[2,1,4,3]\n2\n3'
#
# We are given an array A of positive integers, and two positive integers L and
# R (L <= R).
# 
# Return the number of (contiguous, non-empty) subarrays such that the value of
# the maximum array element in that subarray is at least L and at most R.
# 
# 
# Example :
# Input: 
# A = [2, 1, 4, 3]
# L = 2
# R = 3
# Output: 3
# Explanation: There are three subarrays that meet the requirements: [2], [2,
# 1], [3].
# 
# 
# Note:
# 
# 
# L, R  and A[i] will be an integer in the range [0, 10^9].
# The length of A will be in the range of [1, 50000].
# 
# 
#
class Solution(object):
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        ans = 0
        len_fq = 0
        len_nfq = 0
        for n in A:
            len_fq += 1
            len_nfq += 1
            if n > R:
                len_nfq = len_fq = 0
            elif n >= L:
                len_nfq = 0
            #print "n", n, "delta", len_fq - len_nfq
            ans += len_fq - len_nfq
        return ans

    def test(self):
        print self.numSubarrayBoundedMax([2, 1, 4, 3], 2, 3), 3
        print self.numSubarrayBoundedMax([2, 1, 1, 1, 4, 3], 2, 3), 5
        print self.numSubarrayBoundedMax([2, 1, 1, 3, 4, 3], 2, 3), 9
                
                

        

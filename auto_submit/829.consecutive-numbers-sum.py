#
# [856] Consecutive Numbers Sum
#
# https://leetcode.com/problems/consecutive-numbers-sum/description/
#
# algorithms
# Medium (28.47%)
# Total Accepted:    5.3K
# Total Submissions: 18.6K
# Testcase Example:  '5'
#
# Given a positive integer N, how many ways can we write it as a sum of
# consecutive positive integers?
# 
# Example 1:
# 
# 
# Input: 5
# Output: 2
# Explanation: 5 = 5 = 2 + 3
# 
# Example 2:
# 
# 
# Input: 9
# Output: 3
# Explanation: 9 = 9 = 4 + 5 = 2 + 3 + 4
# 
# Example 3:
# 
# 
# Input: 15
# Output: 4
# Explanation: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
# 
# Note: 1 <= N <= 10 ^ 9.
# 
#
import math
class Solution(object):
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        ret = 0
        for k in xrange(1, N+1):
            if 2*N/k < k:
                break
            if 2*N % k == 0 and (2*N/k) >= k + 1 and ((2*N/k) - k - 1) % 2 == 0:
                #print ((2*N/k) - k - 1) / 2, k
                ret += 1
        
        return ret

    def test(self):
        print self.consecutiveNumbersSum(5)
        print self.consecutiveNumbersSum(9)
        print self.consecutiveNumbersSum(15)
        print self.consecutiveNumbersSum(3654859)

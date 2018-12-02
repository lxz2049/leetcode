#
# [204] Count Primes
#
# https://leetcode.com/problems/count-primes/description/
#
# algorithms
# Easy (27.36%)
# Total Accepted:    193.6K
# Total Submissions: 705.3K
# Testcase Example:  '10'
#
# Count the number of prime numbers less than a non-negative number, n.
# 
# Example:
# 
# 
# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
# 
#
import math
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        primes = [True for i in xrange(n)]
        i = 2
        while i * i < n:
            if primes[i]:
                j = i * i
                while j < n:
                    primes[j] = False
                    j += i
            i += 1
            
        return sum(primes[2:])
            

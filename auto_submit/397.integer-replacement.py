#
# [397] Integer Replacement
#
# https://leetcode.com/problems/integer-replacement/description/
#
# algorithms
# Medium (30.66%)
# Total Accepted:    34.4K
# Total Submissions: 112.2K
# Testcase Example:  '8'
#
# 
# Given a positive integer n and you can do operations as follow:
# 
# 
# 
# 
# If n is even, replace n with n/2.
# If n is odd, you can replace n with either n + 1 or n - 1.
# 
# 
# 
# 
# What is the minimum number of replacements needed for n to become 1?
# 
# 
# 
# 
# Example 1:
# 
# Input:
# 8
# 
# Output:
# 3
# 
# Explanation:
# 8 -> 4 -> 2 -> 1
# 
# 
# 
# Example 2:
# 
# Input:
# 7
# 
# Output:
# 4
# 
# Explanation:
# 7 -> 8 -> 4 -> 2 -> 1
# or
# 7 -> 6 -> 3 -> 2 -> 1
# 
# 
#
from collections import deque
class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        q = deque([(n, 0)])
        visited = set()
        while q:
            n, step = q.popleft()
            if n == 1:
                return step
            if n % 2 == 0 and n / 2 not in visited:
                q.append((n/2, step + 1))
                visited.add(n/2)
            elif n % 2 == 1:
                if n + 1 not in visited:
                    q.append((n + 1, step + 1))
                    visited.add(n+1)
                if n - 1 not in visited:
                    q.append((n - 1, step + 1))
                    visited.add(n-1)
        return -1

    def test(self):
        print self.integerReplacement(8)
        print self.integerReplacement(7)
        print self.integerReplacement(1234)

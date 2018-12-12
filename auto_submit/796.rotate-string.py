#
# [812] Rotate String
#
# https://leetcode.com/problems/rotate-string/description/
#
# algorithms
# Easy (48.64%)
# Total Accepted:    28.5K
# Total Submissions: 58.7K
# Testcase Example:  '"abcde"\n"cdeab"'
#
# We are given two strings, A and B.
# 
# A shift on A consists of taking string A and moving the leftmost character to
# the rightmost position. For example, if A = 'abcde', then it will be 'bcdea'
# after one shift on A. Return True if and only if A can become B after some
# number of shifts on A.
# 
# 
# Example 1:
# Input: A = 'abcde', B = 'cdeab'
# Output: true
# 
# Example 2:
# Input: A = 'abcde', B = 'abced'
# Output: false
# 
# 
# Note:
# 
# 
# A and B will have length at most 100.
# 
# 
#
class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        def test(start):
            for i in xrange(len(A)):
                if A[(i+start) % len(A)] != B[i]:
                    return False
            return True

        if len(A) != len(B):
            return False
        if not A and not B:
            return True
        for i in xrange(len(A)):
            if test(i):
                return True
        return False

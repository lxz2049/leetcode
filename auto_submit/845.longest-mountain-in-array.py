#
# [875] Longest Mountain in Array
#
# https://leetcode.com/problems/longest-mountain-in-array/description/
#
# algorithms
# Medium (31.65%)
# Total Accepted:    8.5K
# Total Submissions: 26.6K
# Testcase Example:  '[2,1,4,7,3,2,5]'
#
# Let's call any (contiguous) subarray B (of A) a mountain if the following
# properties hold:
# 
# 
# B.length >= 3
# There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] <
# B[i] > B[i+1] > ... > B[B.length - 1]
# 
# 
# (Note that B could be any subarray of A, including the entire array A.)
# 
# Given an array A of integers, return the length of the longest mountain. 
# 
# Return 0 if there is no mountain.
# 
# Example 1:
# 
# 
# Input: [2,1,4,7,3,2,5]
# Output: 5
# Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
# 
# 
# Example 2:
# 
# 
# Input: [2,2,2]
# Output: 0
# Explanation: There is no mountain.
# 
# 
# Note:
# 
# 
# 0 <= A.length <= 10000
# 0 <= A[i] <= 10000
# 
# 
# Follow up:
# 
# 
# Can you solve it using only one pass?
# Can you solve it in O(1) space?
# 
# 
#
class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A:
            return 0
        state = 0
        prev = A[0]
        ret = mountain = 0
        for a in A[1:]:
            if a > prev:
                if state != 1:
                    state = 1
                    mountain = 1
                mountain += 1
            elif a < prev:
                mountain += 1
                if state == 1:
                    state = 2
                if state == 2:
                    ret = max(ret, mountain)
                else:
                    state = 0
                    mountain = 0
            else:
                state = 0
                mountain = 0
            prev = a
            #print a, state, mountain
        return ret

    def test(self):
        print self.longestMountain([2,1,4,7,3,2,5])
        print self.longestMountain([2,1,4,4,3,2,5])
        print self.longestMountain([0,1,2,3,4,5,4,3,2,1,0])
        print self.longestMountain([0,2,1,5,4,3])
        print self.longestMountain([0,1,0])

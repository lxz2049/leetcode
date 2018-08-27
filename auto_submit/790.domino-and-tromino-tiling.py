#
# [806] Domino and Tromino Tiling
#
# https://leetcode.com/problems/domino-and-tromino-tiling/description/
#
# algorithms
# Medium (32.75%)
# Total Accepted:    4.4K
# Total Submissions: 13.1K
# Testcase Example:  '3'
#
# We have two types of tiles: a 2x1 domino shape, and an "L" tromino shape.
# These shapes may be rotated.
# 
# 
# XX  <- domino
# 
# XX  <- "L" tromino
# X
# 
# 
# Given N, how many ways are there to tile a 2 x N board? Return your answer
# modulo 10^9 + 7.
# 
# (In a tiling, every square must be covered by a tile. Two tilings are
# different if and only if there are two 4-directionally adjacent cells on the
# board such that exactly one of the tilings has both squares occupied by a
# tile.)
# 
# 
# 
# Example:
# Input: 3
# Output: 5
# Explanation: 
# The five different ways are listed below, different letters indicates
# different tiles:
# XYZ XXZ XYY XXY XYY
# XYZ YYZ XZZ XYY XXY
# 
# Note:
# 
# 
# N  will be in range [1, 1000].
# 
# 
# 
#
class Solution(object):
    def numTilings(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 1:
            return 1

        MOD_CONSTANT = 1000000007
        prev_full = 1
        cur_full = 2
        prev_half = 0
        cur_half = 2
        for n in xrange(3, N+1):
            cur_full, prev_full, cur_half, prev_half = (prev_full + cur_full + cur_half) % MOD_CONSTANT, \
                                                       cur_full, \
                                                       (prev_full * 2 + cur_half) % MOD_CONSTANT, \
                                                       cur_half
            #print n, cur_full, prev_full, cur_half, prev_half
        return cur_full

    def test(self):
        #print self.numTilings(3)
        print self.numTilings(5)
                                                       
            

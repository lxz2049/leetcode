#
# [190] Reverse Bits
#
# https://leetcode.com/problems/reverse-bits/description/
#
# algorithms
# Easy (29.37%)
# Total Accepted:    134.7K
# Total Submissions: 458.4K
# Testcase Example:  '    43261596 (00000010100101000001111010011100)'
#
# Reverse bits of a given 32 bits unsigned integer.
# 
# Example:
# 
# 
# Input: 43261596
# Output: 964176192
# Explanation: 43261596 represented in binary as
# 00000010100101000001111010011100, 
# return 964176192 represented in binary as 00111001011110000010100101000000.
# 
# 
# Follow up:
# If this function is called many times, how would you optimize it?
# 
#
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        arr = (bin(n)[:1:-1])
        return int(arr + '0' * (32-len(arr)), 2)

    def test(self):
        print bin(self.reverseBits(int('00000010100101000001111010011100', 2)))[2:], ('00000010100101000001111010011100')[::-1]
        print bin(self.reverseBits(0xffffffff))[2:]

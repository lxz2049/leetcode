#
# [639] Decode Ways II
#
# https://leetcode.com/problems/decode-ways-ii/description/
#
# algorithms
# Hard (24.35%)
# Total Accepted:    15.2K
# Total Submissions: 62.7K
# Testcase Example:  '"*"'
#
# 
# A message containing letters from A-Z is being encoded to numbers using the
# following mapping way:
# 
# 
# 
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# 
# 
# 
# Beyond that, now the encoded string can also contain the character '*', which
# can be treated as one of the numbers from 1 to 9.
# 
# 
# 
# 
# Given the encoded message containing digits and the character '*', return the
# total number of ways to decode it.
# 
# 
# 
# Also, since the answer may be very large, you should return the output mod
# 109 + 7.
# 
# 
# Example 1:
# 
# Input: "*"
# Output: 9
# Explanation: The encoded message can be decoded to the string: "A", "B", "C",
# "D", "E", "F", "G", "H", "I".
# 
# 
# 
# Example 2:
# 
# Input: "1*"
# Output: 9 + 9 = 18
# 
# 
# 
# Note:
# 
# The length of the input string will fit in range [1, 105].
# The input string will only contain the character '*' and digits '0' - '9'.
# 
# 
#
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s[0] == '0':
            return 0

        MOD = 1000000007
        prev = 1
        cur = 9 if s[0] == "*" else 1
        for i in xrange(1, len(s)):
            if s[i] == "*":
                if s[i-1] == "*":
                    cur, prev = (cur * 9 + prev * 15) % MOD, cur
                elif s[i-1] == "1":
                    cur, prev = (cur * 9 + prev * 9) % MOD, cur
                elif s[i-1] == "2":
                    cur, prev = (cur * 9 + prev * 6) % MOD, cur
                else:
                    cur, prev = (cur * 9) % MOD, cur
            elif s[i-1] == '*':
                if s[i] == "0":
                    cur, prev = (prev * 2) % MOD, cur
                elif s[i] <= "6":
                    cur, prev = (cur + prev * 2) % MOD, cur
                else:
                    cur, prev = (cur + prev) % MOD, cur
            else:
                double = (s[i-1] == "1" and s[i] >= "0" or s[i-1] == "2" and s[i] <= "6")
                if double and s[i] > "0":
                    cur, prev = (prev + cur) % MOD, cur
                elif s[i] > "0":
                    prev = cur
                elif double:
                    cur, prev = prev, cur
                else:
                    cur, prev = 0, cur
        return cur
	

    def test(self):
        print self.numDecodings("12")
        print self.numDecodings("226")
        print self.numDecodings("22626")
        print self.numDecodings("0")
        print self.numDecodings("26260")
        print self.numDecodings("101")
        print self.numDecodings("110")
        print self.numDecodings("**")
        print self.numDecodings("1*")
        print self.numDecodings("1003")
        print self.numDecodings("*10*1")

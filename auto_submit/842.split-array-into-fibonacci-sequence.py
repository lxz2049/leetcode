#
# [872] Split Array into Fibonacci Sequence
#
# https://leetcode.com/problems/split-array-into-fibonacci-sequence/description/
#
# algorithms
# Medium (33.74%)
# Total Accepted:    5.5K
# Total Submissions: 16.4K
# Testcase Example:  '"123456579"'
#
# Given a string S of digits, such as S = "123456579", we can split it into a
# Fibonacci-like sequence [123, 456, 579].
# 
# Formally, a Fibonacci-like sequence is a list F of non-negative integers such
# that:
# 
# 
# 0 <= F[i] <= 2^31 - 1, (that is, each integer fits a 32-bit signed integer
# type);
# F.length >= 3;
# and F[i] + F[i+1] = F[i+2] for all 0 <= i < F.length - 2.
# 
# 
# Also, note that when splitting the string into pieces, each piece must not
# have extra leading zeroes, except if the piece is the number 0 itself.
# 
# Return any Fibonacci-like sequence split from S, or return [] if it cannot be
# done.
# 
# Example 1:
# 
# 
# Input: "123456579"
# Output: [123,456,579]
# 
# 
# Example 2:
# 
# 
# Input: "11235813"
# Output: [1,1,2,3,5,8,13]
# 
# 
# Example 3:
# 
# 
# Input: "112358130"
# Output: []
# Explanation: The task is impossible.
# 
# 
# Example 4:
# 
# 
# Input: "0123"
# Output: []
# Explanation: Leading zeroes are not allowed, so "01", "2", "3" is not
# valid.
# 
# 
# Example 5:
# 
# 
# Input: "1101111"
# Output: [110, 1, 111]
# Explanation: The output [11, 0, 11, 11] would also be accepted.
# 
# 
# Note: 
# 
# 
# 1 <= S.length <= 200
# S contains only digits.
# 
# 
#
class Solution(object):
    def splitIntoFibonacci(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        for i in xrange(len(S)-2):
            if S[0] == '0' and i > 0:
                break
            for j in xrange(i+1, len(S)-1):
                if S[i+1] == '0' and j > i+1:
                    break
                seq = [int(S[:i+1]), int(S[i+1:j+1])]
                k = j+1
                while k < len(S):
                    #print seq
                    num = seq[-2] + seq[-1]
                    numstr = str(num)
                    if num <= 0x7fffffff and S.startswith(numstr, k):
                        seq.append(num)
                        k += len(numstr)
                    else:
                        break
                else:
                    if len(seq) > 2:
                        return seq
        return []

    def test(self):
        print self.splitIntoFibonacci('123456579')
        print self.splitIntoFibonacci('1101111')
        print self.splitIntoFibonacci('11235813')
        print self.splitIntoFibonacci('539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511')
        print self.splitIntoFibonacci('502113822114324228146342470570616913086148370223967883880490627727810157768164350462659281443027860696206741126485341822692082949177424771869507721046921249291642202139633432706879765292084310')

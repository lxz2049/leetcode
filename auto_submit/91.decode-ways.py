#
# [91] Decode Ways
#
# https://leetcode.com/problems/decode-ways/description/
#
# algorithms
# Medium (20.29%)
# Total Accepted:    192K
# Total Submissions: 921.9K
# Testcase Example:  '"12"'
#
# A message containing letters from A-Z is being encoded to numbers using the
# following mapping:
# 
# 
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# 
# 
# Given a non-empty string containing only digits, determine the total number
# of ways to decode it.
# 
# Example 1:
# 
# 
# Input: "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).
# 
# 
# Example 2:
# 
# 
# Input: "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2
# 6).
# 
#
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s[0] == "0":
            return 0
        prev = 1
        cur = 1
        for i in xrange(1, len(s)):
            #print s[i], s[i-1:i+1]
            if 26 >= int(s[i-1:i+1]) >= 10 and int(s[i]) > 0:
                cur, prev = prev + cur, cur
            elif int(s[i]) > 0:
                prev = cur
            elif 26 >= int(s[i-1:i+1]) >= 10:
                cur, prev = prev, cur
            else:
                return 0
        return cur
                
    def test(self):
        print self.numDecodings("12")
        print self.numDecodings("226")
        print self.numDecodings("22626")
        print self.numDecodings("0")
        print self.numDecodings("26260")
        print self.numDecodings("101")
        print self.numDecodings("110")

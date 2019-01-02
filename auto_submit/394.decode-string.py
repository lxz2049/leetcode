#
# [394] Decode String
#
# https://leetcode.com/problems/decode-string/description/
#
# algorithms
# Medium (42.86%)
# Total Accepted:    80K
# Total Submissions: 185.2K
# Testcase Example:  '"3[a]2[bc]"'
#
# 
# Given an encoded string, return it's decoded string.
# 
# 
# The encoding rule is: k[encoded_string], where the encoded_string inside the
# square brackets is being repeated exactly k times. Note that k is guaranteed
# to be a positive integer.
# 
# 
# You may assume that the input string is always valid; No extra white spaces,
# square brackets are well-formed, etc.
# 
# Furthermore, you may assume that the original data does not contain any
# digits and that digits are only for those repeat numbers, k. For example,
# there won't be input like 3a or 2[4].
# 
# 
# Examples:
# 
# s = "3[a]2[bc]", return "aaabcbc".
# s = "3[a2[c]]", return "accaccacc".
# s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
# 
# 
#
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        def decode(i):
            ret = []
            mul = 0
            while i < len(s):
                if s[i] == "]":
                    return ret, i+1
                if s[i].isdigit():
                    mul = mul * 10 + int(s[i])
                    i += 1
                    continue
                if s[i] == "[":
                    sub, i = decode(i+1)
                    ret.extend(mul * sub)
                    mul = 0
                    continue
                ret.append(s[i])
                i += 1
            return ret

        return "".join(decode(0))

    def test(self):
        print self.decodeString("3[a]2[bc]"), "aaabcbc"
        print self.decodeString("3[a2[c]]"), "accaccacc"
        print self.decodeString("2[abc]3[cd]ef"), "abcabccdcdcdef"
        print self.decodeString("2[abccd]"), "abccdabccd"

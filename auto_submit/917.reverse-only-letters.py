#
# @lc app=leetcode id=917 lang=python
#
# [917] Reverse Only Letters
#
# https://leetcode.com/problems/reverse-only-letters/description/
#
# algorithms
# Easy (55.97%)
# Total Accepted:    22.8K
# Total Submissions: 40.7K
# Testcase Example:  '"ab-cd"'
#
# Given a string S, return the "reversed" string where all characters that are
# not a letter stay in the same place, and all letters reverse their
# positions.
# 
# 
# Example 1:
# 
# Input: "ab-cd"
# Output: "dc-ba"
# 
# 
# Example 2:
# 
# Input: "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"
# 
# 
# Example 3:
# 
# Input: "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"
# 
# 
# Note:
# 
# 
# S.length <= 100
# 33 <= S[i].ASCIIcode <= 122 
# S doesn't contain \ or "
# 
#
class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        ret = []
        j = len(S) - 1
        for i, c in enumerate(S):
            if c.isalpha():
                while j >= 0 and not S[j].isalpha():
                    j -= 1
                ret.append(S[j])
                j -= 1
            else:
                ret.append(c)
        return "".join(ret)

    def test(self):
        print self.reverseOnlyLetters("ab-cd")
        print self.reverseOnlyLetters("a-bC-dEf-ghIj")
        print self.reverseOnlyLetters("Test1ng-Leet=code-Q!")

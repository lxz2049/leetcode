#
# [345] Reverse Vowels of a String
#
# https://leetcode.com/problems/reverse-vowels-of-a-string/description/
#
# algorithms
# Easy (39.05%)
# Total Accepted:    101.6K
# Total Submissions: 260K
# Testcase Example:  '"hello"'
#
# Write a function that takes a string as input and reverse only the vowels of
# a string.
# 
# 
# Example 1:
# Given s = "hello", return "holle".
# 
# 
# 
# Example 2:
# Given s = "leetcode", return "leotcede".
# 
# 
# 
# Note:
# The vowels does not include the letter "y".
# 
#
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        vowels = ['a', 'e', 'u', 'i', 'o', 'A', 'E', 'U', 'I', 'O']
        l = 0
        r = len(s)-1
        while l < r:
            while l < r and s[l] not in vowels:
                l += 1
            while l < r and s[r] not in vowels:
                r -= 1
            if s[l] in vowels and s[r] in vowels:
                s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return ''.join(s)

    def test(self):
        print self.reverseVowels("leetcode")
        print self.reverseVowels("hello")
        print self.reverseVowels(" ")

#
# [125] Valid Palindrome
#
# https://leetcode.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (26.95%)
# Total Accepted:    227.4K
# Total Submissions: 835K
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# Given a string, determine if it is a palindrome, considering only
# alphanumeric characters and ignoring cases.
# 
# Note: For the purpose of this problem, we define empty string as valid
# palindrome.
# 
# Example 1:
# 
# 
# Input: "A man, a plan, a canal: Panama"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: "race a car"
# Output: false
# 
# 
#
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = "".join(str(c) for c in (c.lower() for c in s if c.lower() in "0123456789abcdefghijklmnopqrstuvwxyz"))
        #print s
        for i in range(0, len(s)/2):
            if s[i] != s[len(s)-1-i]:
                return False
        return True

    def test(self):
        print self.isPalindrome("race a car")
        print self.isPalindrome("A man, a plan, a canal: Panama")

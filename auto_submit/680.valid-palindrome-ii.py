#
# [680] Valid Palindrome II
#
# https://leetcode.com/problems/valid-palindrome-ii/description/
#
# algorithms
# Easy (32.61%)
# Total Accepted:    45.9K
# Total Submissions: 140.6K
# Testcase Example:  '"aba"'
#
# 
# Given a non-empty string s, you may delete at most one character.  Judge
# whether you can make it a palindrome.
# 
# 
# Example 1:
# 
# Input: "aba"
# Output: True
# 
# 
# 
# Example 2:
# 
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.
# 
# 
# 
# Note:
# 
# The string will only contain lowercase characters a-z.
# The maximum length of the string is 50000.
# 
# 
#
class Solution(object):
    def validPalindrome(self, s, removed=False):
        """
        :type s: str
        :rtype: bool
        """
        lo = 0
        hi = len(s) - 1
        while lo <= hi:
            if s[lo] != s[hi]:
                if not removed:
                    return self.validPalindrome(s[lo+1:hi+1], removed=True) or \
                            self.validPalindrome(s[lo:hi], removed=True)
                else:
                    return False
            lo += 1
            hi -= 1
        return True

    def test(self):
        #print self.validPalindrome("aba")
        #print self.validPalindrome("abca")
        #print self.validPalindrome("abcca")
        #print self.validPalindrome("cxaca")
        print self.validPalindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga")

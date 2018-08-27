#
# [678] Valid Parenthesis String
#
# https://leetcode.com/problems/valid-parenthesis-string/description/
#
# algorithms
# Medium (29.42%)
# Total Accepted:    14.3K
# Total Submissions: 48K
# Testcase Example:  '"()"'
#
# 
# Given a string containing only three types of characters: '(', ')' and '*',
# write a function to check whether this string is valid. We define the
# validity of a string by these rules:
# 
# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left
# parenthesis '(' or an empty string.
# An empty string is also valid.
# 
# 
# 
# Example 1:
# 
# Input: "()"
# Output: True
# 
# 
# 
# Example 2:
# 
# Input: "(*)"
# Output: True
# 
# 
# 
# Example 3:
# 
# Input: "(*))"
# Output: True
# 
# 
# 
# Note:
# 
# The string size will be in the range [1, 100].
# 
# 
#
class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        score = 0
        star = 0
        for c in s:
            if c == "(":
                score += 1
            elif c == ")":
                if not score and star:
                    star -= 1
                else:
                    score -= 1
            else:        
                star += 1
            if score < 0:
                return False
            #print c, score, star
                
        score = 0
        star = 0
        for c in reversed(s):
            if c == ")":
                score += 1
            elif c == "(":
                if not score and star:
                    star -= 1
                else:
                    score -= 1
            else:        
                star += 1
            if score < 0:
                return False
            #print c, score, star
        return True

    def test(self):
        print self.checkValidString("((*")
        print self.checkValidString("((*)(*))((*")
        print self.checkValidString("(())((())()()(*)(*()(())())())()()((()())((()))(*")
        

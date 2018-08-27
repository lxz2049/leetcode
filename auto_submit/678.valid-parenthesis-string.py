#
# [678] Valid Parenthesis String
#
# https://leetcode.com/problems/valid-parenthesis-string/description/
#
# algorithms
# Medium (29.64%)
# Total Accepted:    14.3K
# Total Submissions: 47.9K
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
        dp = []
        stars = []
        for i, c in enumerate(s):
            if c == "*":
                stars.append((c, i))
            elif dp and dp[-1][0] == "(" and c == ")":
                dp.pop()
            else:
                dp.append((c, i))
        #print dp, stars
        new_dp = []
        i = j = 0
        while i < len(dp) or j < len(stars):
            if i < len(dp) and (j >= len(stars) or dp[i][1] < stars[j][1]):
                cur = dp[i][0]
                i += 1
            elif j < len(stars):
                cur = "*"
                j += 1
            if new_dp and (new_dp[-1] == "(" and cur == "*" or new_dp[-1] == "*" and cur == ")"):
                new_dp.pop()
            else:
                new_dp.append(cur)

            #print new_dp
        return ")" not in new_dp and "(" not in new_dp
            

    def test(self):
        print self.checkValidString("()")
        print self.checkValidString("(*))")
        print self.checkValidString("(())((())()()(*)(*()(())())())()()((()())((()))(*")
            

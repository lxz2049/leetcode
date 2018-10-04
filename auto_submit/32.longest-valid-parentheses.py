#
# [32] Longest Valid Parentheses
#
# https://leetcode.com/problems/longest-valid-parentheses/description/
#
# algorithms
# Hard (23.81%)
# Total Accepted:    147.2K
# Total Submissions: 616.4K
# Testcase Example:  '"(()"'
#
# Given a string containing just the characters '(' and ')', find the length of
# the longest valid (well-formed) parentheses substring.
# 
# Example 1:
# 
# 
# Input: "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()"
# 
# 
# Example 2:
# 
# 
# Input: ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()"
# 
# 
#
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        for i, c in enumerate(s):
            if c == ')' and stack and stack[-1][0] == '(':
                stack.pop()
            else:
                stack.append((c, i))

        start = ret = -1
        for _, i in stack:
            ret = max(ret, i - start - 1)   
            start = i
        ret = max(ret, len(s) - start - 1)   
        return ret

    def test(self):
        print self.longestValidParentheses(")()())")
        print self.longestValidParentheses("()(()")
        print self.longestValidParentheses("())")
        print self.longestValidParentheses("(()")
        print self.longestValidParentheses("((())((")

#
# [224] Basic Calculator
#
# https://leetcode.com/problems/basic-calculator/description/
#
# algorithms
# Hard (30.73%)
# Total Accepted:    86.9K
# Total Submissions: 282.3K
# Testcase Example:  '"1 + 1"'
#
# Implement a basic calculator to evaluate a simple expression string.
# 
# The expression string may contain open ( and closing parentheses ), the plus
# + or minus sign -, non-negative integers and empty spaces  .
# 
# Example 1:
# 
# 
# Input: "1 + 1"
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: " 2-1 + 2 "
# Output: 3
# 
# Example 3:
# 
# 
# Input: "(1+(4+5+2)-3)+(6+8)"
# Output: 23
# Note:
# 
# 
# You may assume that the given expression is always valid.
# Do not use the eval built-in library function.
# 
# 
#
from operator import add, sub
class Solution(object):
    def calculate(self, s, i=0):
        """
        :type s: str
        :rtype: int
        """
        def cal(i):
            prev, cur, op = 0, 0, add
            while i < len(s):
                #print prev, cur, op
                c = s[i]
                if c.isdigit():
                    cur = cur * 10 + int(c)
                elif c == "(":
                    cur, i = cal(i+1)
                elif c == ")":
                    return op(prev, cur), i
                elif c in "+-":
                    prev, cur = op(prev, cur), 0
                    op = add if c == "+" else sub
                i += 1
            return op(prev, cur), i
        return cal(0)[0]

    def test(self):
        print self.calculate("1 + 1")
        print self.calculate("2-1 + 2")
        print self.calculate("(1+(4+5+2)-3)+(6+8)")

#
# [227] Basic Calculator II
#
# https://leetcode.com/problems/basic-calculator-ii/description/
#
# algorithms
# Medium (29.87%)
# Total Accepted:    61.7K
# Total Submissions: 206.4K
# Testcase Example:  '"3+2*2"'
#
# Implement a basic calculator to evaluate a simple expression string.
# 
# The expression string contains only non-negative integers, +, -, *, /
# operators and empty spaces  . The integer division should truncate toward
# zero.
# 
# You may assume that the given expression is always valid.
# 
# Some examples:
# 
# "3+2*2" = 7
# " 3/2 " = 1
# " 3+5 / 2 " = 5
# 
# 
# 
# 
# Note: Do not use the eval built-in library function.
# 
# 
# Credits:Special thanks to @ts for adding this problem and creating all test
# cases.
#
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s += '#'
        a = b = carry = 0
        aop = bop = None
        for c in s:
            if c in '+-*/#':
                if aop:
                    if aop in '*/':
                        a = a * carry if aop == '*' else a / carry
                    else:
                        if bop:
                            a = b + a if bop == '+' else b - a
                        b, bop = a, aop
                        a = carry
                else:
                    a = carry
                aop = c
                carry = 0

            elif c != ' ':
                carry = carry * 10 + int(c) 
                        
        if not bop:
            return a
        return b + a if bop == '+' else b - a

    def test(self):
        print self.calculate('3+2*2')
        print self.calculate('3/2')
        print self.calculate('3+5 / 2')

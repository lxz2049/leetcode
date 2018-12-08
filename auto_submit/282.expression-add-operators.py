#
# [282] Expression Add Operators
#
# https://leetcode.com/problems/expression-add-operators/description/
#
# algorithms
# Hard (31.65%)
# Total Accepted:    58.6K
# Total Submissions: 185.2K
# Testcase Example:  '"123"\n6'
#
# Given a string that contains only digits 0-9 and a target value, return all
# possibilities to add binary operators (not unary) +, -, or * between the
# digits so they evaluate to the target value.
# 
# Example 1:
# 
# 
# Input: num = "123", target = 6
# Output: ["1+2+3", "1*2*3"] 
# 
# 
# Example 2:
# 
# 
# Input: num = "232", target = 8
# Output: ["2*3+2", "2+3*2"]
# 
# Example 3:
# 
# 
# Input: num = "105", target = 5
# Output: ["1*0+5","10-5"]
# 
# Example 4:
# 
# 
# Input: num = "00", target = 0
# Output: ["0+0", "0-0", "0*0"]
# 
# 
# Example 5:
# 
# 
# Input: num = "3456237490", target = 9191
# Output: []
# 
#
from operator import add, sub, mul
class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        if not num:
            return []

        ret = []
        def traverse(st, op, base, prev, cur, exp):
            #print exp, op, prev, cur
            if st < len(num):
                # no op
                if cur != 0:
                    traverse(st+1, op, base, prev, cur * 10 + int(num[st]) * base, exp + num[st])
                # plus
                traverse(st+1, add, 1, op(prev, cur), int(num[st]), exp + "+" + num[st])
                # minus
                traverse(st+1, sub, 1, op(prev, cur), int(num[st]), exp + "-" + num[st])
                # multiply
                traverse(st+1, op, cur, prev, cur * int(num[st]), exp + "*" + num[st])
            else:
                if op(prev, cur) == target:
                    ret.append(exp)
        traverse(1, add, 1, 0, int(num[0]), num[0])
        return ret

    def test(self):
        #print self.addOperators("1234", 1234)
        #print self.addOperators("1111", 4)
        #print self.addOperators("1111", 0)
        #print self.addOperators("232", 8)
        #print self.addOperators("105", 5)
        #print self.addOperators("00", 0)
        print self.addOperators("3456237490", 9191)

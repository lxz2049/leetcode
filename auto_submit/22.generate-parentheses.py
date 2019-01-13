#
# [22] Generate Parentheses
#
# https://leetcode.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (51.50%)
# Total Accepted:    282.6K
# Total Submissions: 542K
# Testcase Example:  '3'
#
# 
# Given n pairs of parentheses, write a function to generate all combinations
# of well-formed parentheses.
# 
# 
# 
# For example, given n = 3, a solution set is:
# 
# 
# [
# ⁠ "((()))",
# ⁠ "(()())",
# ⁠ "(())()",
# ⁠ "()(())",
# ⁠ "()()()"
# ]
# 
#
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret = []
        def gen(can, left, right):
            if left + right == n * 2:
                ret.append("".join(can))
                return
            if left < n:
                can.append("(")
                gen(can, left + 1, right)
                can.pop()
            if left > right and right < n:
                can.append(")")
                gen(can, left, right + 1)
                can.pop()
        gen([], 0, 0)
        return ret

    def test(self):
        print self.generateParenthesis(3)

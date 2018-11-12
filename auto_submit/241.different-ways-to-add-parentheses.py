#
# [241] Different Ways to Add Parentheses
#
# https://leetcode.com/problems/different-ways-to-add-parentheses/description/
#
# algorithms
# Medium (47.55%)
# Total Accepted:    64K
# Total Submissions: 133.7K
# Testcase Example:  '"2-1-1"'
#
# Given a string of numbers and operators, return all possible results from
# computing all the different possible ways to group numbers and operators. The
# valid operators are +, - and *.
# 
# Example 1:
# 
# 
# Input: "2-1-1"
# Output: [0, 2]
# Explanation: 
# ((2-1)-1) = 0 
# (2-(1-1)) = 2
# 
# Example 2:
# 
# 
# Input: "2*3-4*5"
# Output: [-34, -14, -10, -10, 10]
# Explanation: 
# (2*(3-(4*5))) = -34 
# ((2*3)-(4*5)) = -14 
# ((2*(3-4))*5) = -10 
# (2*((3-4)*5)) = -10 
# (((2*3)-4)*5) = 10
# 
#
class Solution(object):
    def diffWaysToCompute(self, s):
        def traverse(s):
            ret = []
            for i, c in enumerate(s):
                if not c.isdigit():
                    left = traverse(s[:i])
                    right = traverse(s[i+1:])
                    if c == '*':
                        ret.extend([l * r for l in left for r in right])
                    elif c == '+':
                        ret.extend([l + r for l in left for r in right])
                    else:
                        ret.extend([l - r for l in left for r in right])

            return ret or [int(s)]
        return traverse(s)

    def test(self):
        print self.diffWaysToCompute("2*3-4*5")
        print self.diffWaysToCompute("11")

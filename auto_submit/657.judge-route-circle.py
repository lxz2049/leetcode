#
# [657] Judge Route Circle
#
# https://leetcode.com/problems/judge-route-circle/description/
#
# algorithms
# Easy (68.53%)
# Total Accepted:    58K
# Total Submissions: 84.6K
# Testcase Example:  '"UD"'
#
# 
# Initially, there is a Robot at position (0, 0). Given a sequence of its
# moves, judge if this robot makes a circle, which means it moves back to the
# original place. 
# 
# 
# 
# The move sequence is represented by a string. And each move is represent by a
# character. The valid robot moves are R (Right), L (Left), U (Up) and D
# (down). The output should be true or false representing whether the robot
# makes a circle.
# 
# 
# Example 1:
# 
# Input: "UD"
# Output: true
# 
# 
# 
# Example 2:
# 
# Input: "LL"
# Output: false
# 
# 
#
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x = 0
        y = 0
        for m in moves:
            if m == 'U':
                x = x + 1
            elif m == "D":
                x = x - 1
            elif m == "R":
                y = y + 1
            elif m == "L":
                y = y - 1
        return x == 0 and y == 0

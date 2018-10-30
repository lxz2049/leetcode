#
# [868] Push Dominoes
#
# https://leetcode.com/problems/push-dominoes/description/
#
# algorithms
# Medium (41.50%)
# Total Accepted:    7.3K
# Total Submissions: 17.5K
# Testcase Example:  '".L.R...LR..L.."'
#
# There are N dominoes in a line, and we place each domino vertically upright.
# 
# In the beginning, we simultaneously push some of the dominoes either to the
# left or to the right.
# 
# 
# 
# After each second, each domino that is falling to the left pushes the
# adjacent domino on the left.
# 
# Similarly, the dominoes falling to the right push their adjacent dominoes
# standing on the right.
# 
# When a vertical domino has dominoes falling on it from both sides, it stays
# still due to the balance of the forces.
# 
# For the purposes of this question, we will consider that a falling domino
# expends no additional force to a falling or already fallen domino.
# 
# Given a string "S" representing the initial state. S[i] = 'L', if the i-th
# domino has been pushed to the left; S[i] = 'R', if the i-th domino has been
# pushed to the right; S[i] = '.', if the i-th domino has not been pushed.
# 
# Return a string representing the final state. 
# 
# Example 1:
# 
# 
# Input: ".L.R...LR..L.."
# Output: "LL.RR.LLRRLL.."
# 
# 
# Example 2:
# 
# 
# Input: "RR.L"
# Output: "RR.L"
# Explanation: The first domino expends no additional force on the second
# domino.
# 
# 
# Note:
# 
# 
# 0 <= N <= 10^5
# String dominoes contains only 'L', 'R' and '.'
# 
# 
#
class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        right = [10001] * len(dominoes)
        for i, d in enumerate(dominoes):
            if d == "R":
                right[i] = 0
            elif d == '.' and i and right[i-1] < 10001: 
                right[i] = right[i-1] + 1
        left = [10001] * len(dominoes)
        for i, d in reversed(list(enumerate(dominoes))):
            if d == 'L':
                left[i] = 0
            elif d == '.' and i < len(dominoes) - 1 and left[i+1] < 10001:
                left[i] = left[i+1] + 1
        #print left, right
        ret = []
        for l, r in zip(left, right):
            if l < r:
                ret.append('L')
            elif l > r:
                ret.append('R')
            else:
                ret.append('.')
        return "".join(ret)

    def test(self):
        print self.pushDominoes("RR.L")
        print self.pushDominoes(".L.R...LR..L..")



                

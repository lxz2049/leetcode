#
# [755] Reach a Number
#
# https://leetcode.com/problems/reach-a-number/description/
#
# algorithms
# Medium (25.13%)
# Total Accepted:    2.4K
# Total Submissions: 9.5K
# Testcase Example:  '1'
#
# 
# You are standing at position 0 on an infinite number line.  There is a goal
# at position target.
# 
# On each move, you can either go left or right.  During the n-th move
# (starting from 1), you take n steps.
# 
# Return the minimum number of steps required to reach the destination.
# 
# 
# Example 1:
# 
# Input: target = 3
# Output: 2
# Explanation:
# On the first move we step from 0 to 1.
# On the second step we step from 1 to 3.
# 
# 
# 
# Example 2:
# 
# Input: target = 2
# Output: 3
# Explanation:
# On the first move we step from 0 to 1.
# On the second move we step  from 1 to -1.
# On the third move we step from -1 to 2.
# 
# 
# 
# Note:
# target will be a non-zero integer in the range [-10^9, 10^9].
# 
#
class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        step = 0
        target = abs(target)
        while target > 0:
            step += 1
            target -= step

        if target % 2 == 0:
            return step
        return step + 1 if step % 2 == 0 else step + 2

"""
if __name__ == "__main__":
    print Solution().reachNumber(2)
    print Solution().reachNumber(10)
    """

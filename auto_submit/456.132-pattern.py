#
# [456] 132 Pattern
#
# https://leetcode.com/problems/132-pattern/description/
#
# algorithms
# Medium (27.29%)
# Total Accepted:    22.5K
# Total Submissions: 82.5K
# Testcase Example:  '[1,2,3,4]'
#
# 
# Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a
# subsequence ai, aj, ak such
# that i < j < k and ai < ak < aj. Design an algorithm that takes a list of n
# numbers as input and checks whether there is a 132 pattern in the list.
# 
# Note: n will be less than 15,000.
# 
# Example 1:
# 
# Input: [1, 2, 3, 4]
# 
# Output: False
# 
# Explanation: There is no 132 pattern in the sequence.
# 
# 
# 
# Example 2:
# 
# Input: [3, 1, 4, 2]
# 
# Output: True
# 
# Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
# 
# 
# 
# Example 3:
# 
# Input: [-1, 3, 2, 0]
# 
# Output: True
# 
# Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1,
# 3, 0] and [-1, 2, 0].
# 
# 
#
class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False

        stack = []
        last_output = None
        for n in reversed(nums):
            while stack and stack[-1] < n:
                # found the 1 in this 2 3 1 pattern
                if last_output is not None and last_output > stack[-1]:
                    return True
                last_output = stack.pop()
            stack.append(n)
        return stack and last_output > stack[-1] 


    def test(self):
        print self.find132pattern([1,2,3,4])
        print self.find132pattern([3,1,4,2])
        print self.find132pattern([-1,3,2,0])
        print self.find132pattern([5,7,2,4,6])

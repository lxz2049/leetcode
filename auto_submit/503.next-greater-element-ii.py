#
# [503] Next Greater Element II
#
# https://leetcode.com/problems/next-greater-element-ii/description/
#
# algorithms
# Medium (48.59%)
# Total Accepted:    35.8K
# Total Submissions: 73.6K
# Testcase Example:  '[1,2,1]'
#
# 
# Given a circular array (the next element of the last element is the first
# element of the array), print the Next Greater Number for every element. The
# Next Greater Number of a number x is the first greater number to its
# traversing-order next in the array, which means you could search circularly
# to find its next greater number. If it doesn't exist, output -1 for this
# number.
# 
# 
# Example 1:
# 
# Input: [1,2,1]
# Output: [2,-1,2]
# Explanation: The first 1's next greater number is 2; The number 2 can't find
# next greater number; The second 1's next greater number needs to search
# circularly, which is also 2.
# 
# 
# 
# Note:
# The length of given array won't exceed 10000.
# 
#
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = [-1] * len(nums)
        stack = []
        for i, n in enumerate(nums + nums):
            while stack and n > stack[-1][1]:
                ret[stack.pop()[0]] = n
            if i < len(nums):
                stack.append((i, n))
        return ret

    def test(self):
        print self.nextGreaterElements([1,2,1])
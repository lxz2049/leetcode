#
# [66] Plus One
#
# https://leetcode.com/problems/plus-one/description/
#
# algorithms
# Easy (39.69%)
# Total Accepted:    244.7K
# Total Submissions: 614.4K
# Testcase Example:  '[1,2,3]'
#
# Given a non-empty array of digits representing a non-negative integer, plus
# one to the integer.
# 
# The digits are stored such that the most significant digit is at the head of
# the list, and each element in the array contain a single digit.
# 
# You may assume the integer does not contain any leading zero, except the
# number 0 itself.
# 
# Example 1:
# 
# 
# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# 
# 
# Example 2:
# 
# 
# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# 
# 
#
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits) - 1
        digits[i] += 1
        while i > 0 and digits[i] == 10:
            digits[i] = 0
            i -= 1
            digits[i] += 1
        if digits[i] == 10:
            digits[i] = 0
            return [1] + digits
        return digits

    def test(self):
        print self.plusOne([1, 2, 3])
        print self.plusOne([9, 9, 9])


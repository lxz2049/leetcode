#
# [169] Majority Element
#
# https://leetcode.com/problems/majority-element/description/
#
# algorithms
# Easy (47.93%)
# Total Accepted:    261.4K
# Total Submissions: 542.6K
# Testcase Example:  '[3,2,3]'
#
# Given an array of size n, find the majority element. The majority element is
# the element that appears more than ⌊ n/2 ⌋ times.
# 
# You may assume that the array is non-empty and the majority element always
# exist in the array.
# 
# Example 1:
# 
# 
# Input: [3,2,3]
# Output: 3
# 
# Example 2:
# 
# 
# Input: [2,2,1,1,1,2,2]
# Output: 2
# 
# 
#
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = nums[0]
        cnt = 1
        for n in nums[1:]:
            if n != c:
                cnt -= 1
                if cnt == 0:
                    c = n
                    cnt = 1
            else:
                cnt += 1
        return c

    def test(self):
        print self.majorityElement([3, 2, 3])

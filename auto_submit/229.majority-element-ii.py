#
# [229] Majority Element II
#
# https://leetcode.com/problems/majority-element-ii/description/
#
# algorithms
# Medium (29.05%)
# Total Accepted:    67.2K
# Total Submissions: 231.4K
# Testcase Example:  '[]'
#
# Given an integer array of size n, find all elements that appear more than 
# n/3  times. The algorithm should run in linear time and in O(1) space.
#
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        counter1 = counter2 = 0
        num1 = 0
        num2 = 1
        for n in nums:
            if n == num1:
                counter1 += 1
            elif n == num2:
                counter2 += 1
            elif not counter1:
                num1 = n
                counter1 = 1
            elif not counter2:
                num2 = n
                counter2 = 1
            else:
                counter1 -= 1
                counter2 -= 1

        counter1 = counter2 = 0
        for n in nums:
            if n == num1:
                counter1 += 1
            elif n == num2:
                counter2 += 1
        
        ans = []
        if counter1 > len(nums)/3:
            ans.append(num1)
        if counter2 > len(nums)/3:
            ans.append(num2)

        return ans

"""
if __name__ == "__main__":
    print Solution().majorityElement([1,2,3])
    print Solution().majorityElement([1,1,3])
    print Solution().majorityElement([1,1,1,3,3,3,5,6])
    """

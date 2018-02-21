#
# [658] Find K Closest Elements
#
# https://leetcode.com/problems/find-k-closest-elements/description/
#
# algorithms
# Medium (35.38%)
# Total Accepted:    14K
# Total Submissions: 39.5K
# Testcase Example:  '[1,2,3,4,5]\n4\n3'
#
# 
# Given a sorted array, two integers k and x, find the k closest elements to x
# in the array.  The result should also be sorted in ascending order.
# If there is a tie,  the smaller elements are always preferred.
# 
# 
# Example 1:
# 
# Input: [1,2,3,4,5], k=4, x=3
# Output: [1,2,3,4]
# 
# 
# 
# 
# Example 2:
# 
# Input: [1,2,3,4,5], k=4, x=-1
# Output: [1,2,3,4]
# 
# 
# 
# Note:
# 
# The value k is positive and will always be smaller than the length of the
# sorted array.
# 
# 
# 
# 
# 
# UPDATE (2017/9/19):
# The arr parameter had been changed to an array of integers (instead of a list
# of integers). Please reload the code definition to get the latest changes.
# 
#
class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        l = 0
        r = len(arr)
        while l < r:
            mid = (r+l) / 2
            if arr[mid] < x:
                l = mid + 1
            else:
                r = mid
        while r - l < k:
            if l <= 0:
                r += 1
            elif r >= len(arr):
                l -= 1
            elif x - arr[l-1] <= arr[r] - x:
                l -= 1
            else:
                r += 1
        return arr[l:r]

    def test(self):
        print self.findClosestElements([1], 1, 1)
        print self.findClosestElements([1, 2, 3, 4, 5], 4, 3)
        print self.findClosestElements([1, 2, 3, 4, 5], 4, -1)
        print self.findClosestElements([1, 2, 5, 5, 6, 6, 7, 7, 8, 9], 7, 7)

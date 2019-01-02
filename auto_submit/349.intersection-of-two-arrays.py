#
# [349] Intersection of Two Arrays
#
# https://leetcode.com/problems/intersection-of-two-arrays/description/
#
# algorithms
# Easy (50.11%)
# Total Accepted:    181.7K
# Total Submissions: 351.4K
# Testcase Example:  '[1,2,2,1]\n[2,2]'
#
# Given two arrays, write a function to compute their intersection.
# 
# Example 1:
# 
# 
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# 
# 
# 
# Example 2:
# 
# 
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# 
# 
# Note:
# 
# 
# Each element in the result must be unique.
# The result can be in any order.
# 
# 
# 
# 
#
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        i = j = 0
        ret = []
        while i < len(nums1):
            while j < len(nums2) and nums1[i] > nums2[j]:
                j += 1
            #print i, j
            if j < len(nums2) and nums1[i] == nums2[j] and (not ret or nums1[i] != ret[-1]):
                ret.append(nums1[i])
            i += 1
        return ret

    def test(self):
        print self.intersection([1,2], [1,1])

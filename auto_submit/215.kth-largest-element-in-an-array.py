#
# [215] Kth Largest Element in an Array
#
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (41.19%)
# Total Accepted:    242.1K
# Total Submissions: 572.5K
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# Find the kth largest element in an unsorted array. Note that it is the kth
# largest element in the sorted order, not the kth distinct element.
# 
# Example 1:
# 
# 
# Input: [3,2,1,5,6,4] and k = 2
# Output: 5
# 
# 
# Example 2:
# 
# 
# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
# 
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ array's length.
# 
#
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def quickselect(left, right):
            if left > right:
                return

            #print nums[left:right+1]
            pivot = left
            nums[right], nums[pivot] = nums[pivot], nums[right]
            left_boundary = left
            for i in range(left, right):
                if nums[i] > nums[right]:
                    nums[i], nums[left_boundary] = nums[left_boundary], nums[i]
                    left_boundary += 1
                if left_boundary >= right:
                    break
            nums[left_boundary], nums[right] = nums[right], nums[left_boundary]
            #print nums[left:right+1], left_boundary, k
            if left_boundary == k:
                return nums[left_boundary]
            if left_boundary < k:
                return quickselect(left_boundary+1, right)
            return quickselect(left, left_boundary-1)

        k -= 1
        return quickselect(0, len(nums)-1)

    def test(self):
        print self.findKthLargest([3,2,1,5,6,4], 2)
        print self.findKthLargest([3,2,3,1,2,4,5,5,6], 4)

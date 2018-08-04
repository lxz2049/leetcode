#
# [31] Next Permutation
#
# https://leetcode.com/problems/next-permutation/description/
#
# algorithms
# Medium (29.12%)
# Total Accepted:    163.8K
# Total Submissions: 561.6K
# Testcase Example:  '[1,2,3]'
#
# Implement next permutation, which rearranges numbers into the
# lexicographically next greater permutation of numbers.
# 
# If such arrangement is not possible, it must rearrange it as the lowest
# possible order (ie, sorted in ascending order).
# 
# The replacement must be in-place and use only constant extra memory.
# 
# Here are some examples. Inputs are in the left-hand column and its
# corresponding outputs are in the right-hand column.
# 
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
# 
#
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def rev(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        k = None
        for i in reversed(xrange(1, len(nums))):
            if nums[i] > nums[i-1]:
                k = i
                break
        if k is not None:
            for j in xrange(i+1, len(nums)):
                if nums[j] > nums[i-1]:
                    k = j
            nums[i-1], nums[k] = nums[k], nums[i-1]
            rev(i, len(nums)-1)
        else:
            rev(0, len(nums)-1)
        #print nums
                
    def test(self):
        self.nextPermutation([1, 2, 3])
        self.nextPermutation([3, 2, 1])
        self.nextPermutation([1, 1, 5])
        self.nextPermutation([1, 3, 2, 1])

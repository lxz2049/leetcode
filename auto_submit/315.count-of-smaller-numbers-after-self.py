#
# [315] Count of Smaller Numbers After Self
#
# https://leetcode.com/problems/count-of-smaller-numbers-after-self/description/
#
# algorithms
# Hard (35.70%)
# Total Accepted:    60.1K
# Total Submissions: 167.3K
# Testcase Example:  '[5,2,6,1]'
#
# You are given an integer array nums and you have to return a new counts
# array. The counts array has the property where counts[i] is the number of
# smaller elements to the right of nums[i].
# 
# Example:
# 
# 
# Input: [5,2,6,1]
# Output: [2,1,1,0] 
# Explanation:
# To the right of 5 there are 2 smaller elements (2 and 1).
# To the right of 2 there is only 1 smaller element (1).
# To the right of 6 there is 1 smaller element (1).
# To the right of 1 there is 0 smaller element.
# 
# 
#
class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = [(n, i) for i, n in enumerate(nums)]
        smaller = [0] * len(nums)
        def merge(nums):
            if len(nums) <= 1:
                return nums

            left = merge(nums[:len(nums)/2])
            right = merge(nums[len(nums)/2:])
            ret = []
            l, r = len(left) - 1, len(right) - 1
            while l >= 0 and r >= 0:
                while r >= 0 and right[r][0] < left[l][0]:
                    ret.append(right[r])
                    r -= 1
                ret.append(left[l])
                smaller[left[l][1]] += len(right) - r - 1
                l -= 1
            while l >= 0:
                ret.append(left[l])
                smaller[left[l][1]] += len(right)
                l -= 1
            while r >= 0:
                ret.append(right[r])
                r -= 1
            ret.reverse()
            return ret

        nums = merge(nums)
        return smaller

    def test(self):
        print self.countSmaller([5,2,6,1])

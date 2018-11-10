#
# [327] Count of Range Sum
#
# https://leetcode.com/problems/count-of-range-sum/description/
#
# algorithms
# Hard (31.17%)
# Total Accepted:    26.8K
# Total Submissions: 86.1K
# Testcase Example:  '[-2,5,-1]\n-2\n2'
#
# Given an integer array nums, return the number of range sums that lie in
# [lower, upper] inclusive.
# Range sum S(i, j) is defined as the sum of the elements in nums between
# indices i and j (i ≤ j), inclusive.
# 
# Note:
# A naive algorithm of O(n2) is trivial. You MUST do better than that.
# 
# Example:
# 
# 
# Input: nums = [-2,5,-1], lower = -2, upper = 2,
# Output: 3 
# Explanation: The three ranges are : [0,0], [2,2], [0,2] and their respective
# sums are: -2, -1, 2.
# 
# 
#
class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        if not nums:
            return 0

        # calcualte prefix sum
        prefixsum = nums[:]
        for i in xrange(1, len(prefixsum)):
            prefixsum[i] += prefixsum[i-1]

        def merge(prefixsum):
            if len(prefixsum) == 1:
                return prefixsum, int(lower <= prefixsum[0] <= upper)

            # solve for left/right
            left, lcount = merge(prefixsum[:len(prefixsum)/2])
            right, rcount = merge(prefixsum[len(prefixsum)/2:])

            # calculate count for prefixsum
            count = lcount + rcount
            l = r = 0
            for n in right:
                while l < len(left) and n - upper > left[l]:
                    l += 1
                while r < len(left) and n - lower >= left[r]:
                    r += 1
                count += r - l

            # sort prefixsum
            ret = []
            l = r = 0
            while l < len(left) and r < len(right):
                if left[l] < right[r]:
                    ret.append(left[l])
                    l += 1
                else:
                    ret.append(right[r])
                    r += 1
            if l < len(left):
                ret.extend(left[l:])
            if r < len(right):
                ret.extend(right[r:])
            #print left, lcount, right, rcount, ret, count
            return ret, count

        return merge(prefixsum)[1]

    def test(self):
        print self.countRangeSum([-2,5,-1], -2, 2)
        print self.countRangeSum([-2,5,-1,2], -2, 2)
        print self.countRangeSum([4, -5, -1, 0], -1, 0)
        print self.countRangeSum([0,-3,-3,1,1,2], 3, 5)

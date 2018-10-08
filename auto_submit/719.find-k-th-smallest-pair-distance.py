#
# [719] Find K-th Smallest Pair Distance
#
# https://leetcode.com/problems/find-k-th-smallest-pair-distance/description/
#
# algorithms
# Hard (28.15%)
# Total Accepted:    12.4K
# Total Submissions: 44.1K
# Testcase Example:  '[1,3,1]\n1'
#
# Given an integer array, return the k-th smallest distance among all the
# pairs. The distance of a pair (A, B) is defined as the absolute difference
# between A and B. 
# 
# Example 1:
# 
# Input:
# nums = [1,3,1]
# k = 1
# Output: 0 
# Explanation:
# Here are all the pairs:
# (1,3) -> 2
# (1,1) -> 0
# (3,1) -> 2
# Then the 1st smallest distance pair is (1,1), and its distance is 0.
# 
# 
# 
# Note:
# 
# 2 .
# 0 .
# 1 .
# 
# 
#
class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        lo = 0
        hi = nums[-1] - nums[0]
        while lo < hi:
            mid = lo + (hi - lo) / 2
            cnt_le = 0
            j = 0
            for i in xrange(len(nums)):
                while j < len(nums) and mid >= nums[j] - nums[i]:
                    j += 1
                cnt_le += j - i - 1
            #print "mid", mid, "cnt_le", cnt_le, "k", k
            if cnt_le < k:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def test(self):
        for i in xrange(3):
            print self.smallestDistancePair([1,3,1], i+1)
        print "----"
        for i in xrange(6):
            print self.smallestDistancePair([1,2,5,7], i+1)
                

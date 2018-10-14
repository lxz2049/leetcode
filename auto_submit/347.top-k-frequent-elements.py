#
# [347] Top K Frequent Elements
#
# https://leetcode.com/problems/top-k-frequent-elements/description/
#
# algorithms
# Medium (51.12%)
# Total Accepted:    138.8K
# Total Submissions: 271.5K
# Testcase Example:  '[1,1,1,2,2,3]\n2'
#
# Given a non-empty array of integers, return the k most frequent elements.
# 
# Example 1:
# 
# 
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# 
# 
# 
# Example 2:
# 
# 
# Input: nums = [1], k = 1
# Output: [1]
# 
# 
# Note: 
# 
# 
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is
# the array's size.
# 
# 
#
from collections import defaultdict, Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter = defaultdict(list)
        for key, value in Counter(nums).iteritems():
            counter[value].append(key)
        ret = []
        for i in xrange(len(nums), 0, -1):
            if len(ret) >= k:
                break
            if i in counter:
                ret.extend(counter[i])
        return ret[:k]

    def test(self):
        print self.topKFrequent([1],1)

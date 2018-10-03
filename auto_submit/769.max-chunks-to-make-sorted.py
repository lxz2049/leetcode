#
# [780] Max Chunks To Make Sorted
#
# https://leetcode.com/problems/max-chunks-to-make-sorted/description/
#
# algorithms
# Medium (48.87%)
# Total Accepted:    14K
# Total Submissions: 28.5K
# Testcase Example:  '[4,3,2,1,0]'
#
# Given an array arr that is a permutation of [0, 1, ..., arr.length - 1], we
# split the array into some number of "chunks" (partitions), and individually
# sort each chunk.  After concatenating them, the result equals the sorted
# array.
# 
# What is the most number of chunks we could have made?
# 
# Example 1:
# 
# 
# Input: arr = [4,3,2,1,0]
# Output: 1
# Explanation:
# Splitting into two or more chunks will not return the required result.
# For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2],
# which isn't sorted.
# 
# 
# Example 2:
# 
# 
# Input: arr = [1,0,2,3,4]
# Output: 4
# Explanation:
# We can split into two chunks, such as [1, 0], [2, 3, 4].
# However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks
# possible.
# 
# 
# Note:
# 
# 
# arr will have length in range [1, 10].
# arr[i] will be a permutation of [0, 1, ..., arr.length - 1].
# 
# 
# 
#
class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        ret = 0
        chunkStart = None
        chunkMax = None
        chunkMin = None
        for i, n in enumerate(arr):
            if chunkStart is None:
                chunkStart = i
                chunkMin = arr[i]
                chunkMax = arr[i]
            else:
                chunkMin = min(chunkMin, arr[i])
                chunkMax = max(chunkMax, arr[i])

            if chunkStart == chunkMin and chunkMax == i:
                ret += 1
                chunkStart = chunkMin = chunkMax = None


        return ret

    def test(self):
        print self.maxChunksToSorted([1,0,2,3,4]);
            

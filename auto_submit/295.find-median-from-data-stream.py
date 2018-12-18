#
# [295] Find Median from Data Stream
#
# https://leetcode.com/problems/find-median-from-data-stream/description/
#
# algorithms
# Hard (33.11%)
# Total Accepted:    83.1K
# Total Submissions: 249.5K
# Testcase Example:  '["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]\n[[],[1],[2],[],[3],[]]'
#
# Median is the middle value in an ordered integer list. If the size of the
# list is even, there is no middle value. So the median is the mean of the two
# middle value.
# For example,
# 
# [2,3,4], the median is 3
# 
# [2,3], the median is (2 + 3) / 2 = 2.5
# 
# Design a data structure that supports the following two operations:
# 
# 
# void addNum(int num) - Add a integer number from the data stream to the data
# structure.
# double findMedian() - Return the median of all elements so far.
# 
# 
# 
# 
# Example:
# 
# 
# addNum(1)
# addNum(2)
# findMedian() -> 1.5
# addNum(3) 
# findMedian() -> 2
# 
# 
# 
# 
# Follow up:
# 
# 
# If all integer numbers from the stream are between 0 and 100, how would you
# optimize it?
# If 99% of all integer numbers from the stream are between 0 and 100, how
# would you optimize it?
# 
# 
#
import heapq
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minheap = []
        self.maxheap = []
        
    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if len(self.minheap) > len(self.maxheap):
            if not self.maxheap or num > -self.maxheap[0]:
                heapq.heappush(self.maxheap, -heapq.heappushpop(self.minheap, num))
            else:
                heapq.heappush(self.maxheap, -num)
        else:
            if self.minheap and num < self.minheap[0]:
                heapq.heappush(self.minheap, -heapq.heappushpop(self.maxheap, -num))
            else:
                heapq.heappush(self.minheap, num)

    def findMedian(self):
        """
        :rtype: float
        """
        #print self.minheap, self.maxheap
        if len(self.minheap) > len(self.maxheap):
            return self.minheap[0] * 1.0
        return (self.minheap[0] - self.maxheap[0]) / 2.0
        
class Solution:
    def test(self):
        finder = MedianFinder()
        finder.addNum(1)
        finder.addNum(2)
        print finder.findMedian()
        finder.addNum(3)
        print finder.findMedian()


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

#
# [406] Queue Reconstruction by Height
#
# https://leetcode.com/problems/queue-reconstruction-by-height/description/
#
# algorithms
# Medium (56.93%)
# Total Accepted:    56.6K
# Total Submissions: 99.4K
# Testcase Example:  '[[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]'
#
# Suppose you have a random list of people standing in a queue. Each person is
# described by a pair of integers (h, k), where h is the height of the person
# and k is the number of people in front of this person who have a height
# greater than or equal to h. Write an algorithm to reconstruct the queue.
# 
# 
# Note:
# The number of people is less than 1,100.
# 
# 
# 
# 
# Example
# 
# Input:
# [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
# 
# Sorted: [[7,0], [7,1], [6,1], [5,0], [5,2], [4,4]]
# Output:
# [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
# 
# 
#
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key=lambda p: (-p[0], p[1]))
        ans = []
        for height, rank in people:
            ans.insert(rank, [height, rank])
            #print ans
        return ans

    def test(self):
        print self.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]])

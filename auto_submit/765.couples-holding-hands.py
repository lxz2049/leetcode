#
# [770] Couples Holding Hands
#
# https://leetcode.com/problems/couples-holding-hands/description/
#
# algorithms
# Hard (48.83%)
# Total Accepted:    8.3K
# Total Submissions: 16.9K
# Testcase Example:  '[0,2,1,3]'
#
# 
# N couples sit in 2N seats arranged in a row and want to hold hands.  We want
# to know the minimum number of swaps so that every couple is sitting side by
# side.  A swap consists of choosing any two people, then they stand up and
# switch seats. 
# 
# The people and seats are represented by an integer from 0 to 2N-1, the
# couples are numbered in order, the first couple being (0, 1), the second
# couple being (2, 3), and so on with the last couple being (2N-2, 2N-1).
# 
# The couples' initial seating is given by row[i] being the value of the person
# who is initially sitting in the i-th seat.
# 
# Example 1:
# Input: row = [0, 2, 1, 3]
# Output: 1
# Explanation: We only need to swap the second (row[1]) and third (row[2])
# person.
# 
# 
# Example 2:
# Input: row = [3, 2, 0, 1]
# Output: 0
# Explanation: All couples are already seated side by side.
# 
# 
# 
# Note:
# ⁠
# ⁠len(row) is even and in the range of [4, 60].
# ⁠row is guaranteed to be a permutation of 0...len(row)-1.
# 
#
class Solution(object):
    def find(self, x):
        while self.disjointSet[x] is not None:
            x = self.disjointSet[x]
        return x

    def merge(self, l, r):
        lp = self.find(l)
        rp = self.find(r)
        if lp != rp:
            self.disjointSet[lp] = rp
            self.size[rp] += self.size[lp]
        #print l, lp, r, rp, self.size[rp], self.disjointSet
        
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        ret = 0
        self.disjointSet = [None] * (len(row)/2)
        self.size = [1] * (len(row)/2)
        for i in xrange(len(row)/2):
            l = row[i*2] / 2
            r = row[i*2+1] / 2
            self.merge(l, r)

        visited = [False] * (len(row)/2)
        for i in xrange(len(row)/2):
            p = self.find(i)
            if not visited[p]:
                visited[p] = True
                if (self.size[p] > 1):
                    ret += self.size[p] - 1
        return ret

    def test(self):
        print self.minSwapsCouples([0,1]), 0
        print self.minSwapsCouples([0,2,1,3]), 1
        print self.minSwapsCouples([5,4,2,6,3,1,0,7]), 2
        print self.minSwapsCouples([0,2,4,6,7,1,3,5]), 3
        print self.minSwapsCouples([1,4,0,5,8,7,7,3,2,9]), 3

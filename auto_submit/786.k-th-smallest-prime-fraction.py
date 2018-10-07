#
# [802] K-th Smallest Prime Fraction
#
# https://leetcode.com/problems/k-th-smallest-prime-fraction/description/
#
# algorithms
# Hard (34.89%)
# Total Accepted:    4.5K
# Total Submissions: 12.7K
# Testcase Example:  '[1,2,3,5]\n3'
#
# A sorted list A contains 1, plus some number of primes.  Then, for every p <
# q in the list, we consider the fraction p/q.
# 
# What is the K-th smallest fraction considered?  Return your answer as an
# array of ints, where answer[0] = p and answer[1] = q.
# 
# 
# Examples:
# Input: A = [1, 2, 3, 5], K = 3
# Output: [2, 5]
# Explanation:
# The fractions to be considered in sorted order are:
# 1/5, 1/3, 2/5, 1/2, 3/5, 2/3.
# The third fraction is 2/5.
# 
# Input: A = [1, 7], K = 1
# Output: [1, 7]
# 
# 
# Note:
# 
# 
# A will have length between 2 and 2000.
# Each A[i] will be between 1 and 30000.
# K will be between 1 and A.length * (A.length - 1) / 2.
# 
#
import heapq
class Solution(object):
    def kthSmallestPrimeFraction(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        hq = []
        for i, a in enumerate(A[1:]):
            heapq.heappush(hq, (1.0/a, 0, a))
        p = q = None
        for _ in xrange(K):
            _, p, q = heapq.heappop(hq)
            if A[p+1] < q:
                heapq.heappush(hq, (float(A[p+1])/q, p+1, q))
        return [A[p], q]

    def test(self):
        print self.kthSmallestPrimeFraction([1,2,3,5], 3)
        print self.kthSmallestPrimeFraction([1,2,3,5], 4)
        print self.kthSmallestPrimeFraction([1,2,3,5], 5)

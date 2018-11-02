#
# [966] Binary Subarrays With Sum
#
# https://leetcode.com/problems/binary-subarrays-with-sum/description/
#
# algorithms
# Medium (28.62%)
# Total Accepted:    3.4K
# Total Submissions: 10.4K
# Testcase Example:  '[1,0,1,0,1]\n2'
#
# In an array A of 0s and 1s, how many non-empty subarrays have sum S?
# 
# 
# 
# Example 1:
# 
# 
# Input: A = [1,0,1,0,1], S = 2
# Output: 4
# Explanation: 
# The 4 subarrays are bolded below:
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# 
# 
# 
# 
# Note:
# 
# 
# A.length <= 30000
# 0 <= S <= A.length
# A[i] is either 0 or 1.
# 
# 
#
from collections import defaultdict
class Solution(object):
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        for i in xrange(1, len(A)):
            A[i] += A[i-1]
        ret = 0
        lookup = defaultdict(int)
        lookup[0] = 1
        for a in A:
            #print a, a - S, lookup
            if a - S in lookup:
                ret += lookup[a - S]
            lookup[a] += 1
        return ret
    
    def test(self):
        print self.numSubarraysWithSum([1,0,1,0,1], 2)

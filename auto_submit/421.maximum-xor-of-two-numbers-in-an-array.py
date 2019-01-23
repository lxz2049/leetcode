#
# [421] Maximum XOR of Two Numbers in an Array
#
# https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/description/
#
# algorithms
# Medium (49.51%)
# Total Accepted:    30K
# Total Submissions: 60.5K
# Testcase Example:  '[3,10,5,25,2,8]'
#
# Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai <
# 231.
# 
# Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.
# 
# Could you do this in O(n) runtime?
# 
# Example:
# 
# Input: [3, 10, 5, 25, 2, 8]
# 
# Output: 28
# 
# Explanation: The maximum result is 5 ^ 25 = 28.
# 
# 
#
from collections import defaultdict

Trie = lambda: defaultdict(Trie)

class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        trie = Trie()
        for n in nums:
            node = trie
            mask = 1 << 30
            while mask:
                b = bool(n & mask)
                node = node[int(b)]
                mask = mask >> 1
            node["_"] = n
        
        ret = 0
        for n in nums:
            can = 0
            node = trie
            mask = 1 << 30
            while mask:
                can = can << 1
                b = bool(n & mask)
                if int(not b) in node:
                    b = not b
                    can += 1
                node = node[int(b)]
                mask = mask >> 1
            ret = max(ret, can)
        return ret

    def test(self):
        print self.findMaximumXOR([3,10,5,25,2,8])

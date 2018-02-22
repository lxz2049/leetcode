#
# [768] Partition Labels
#
# https://leetcode.com/problems/partition-labels/description/
#
# algorithms
# Medium (64.65%)
# Total Accepted:    6.4K
# Total Submissions: 10K
# Testcase Example:  '"ababcbacadefegdehijhklij"'
#
# 
# A string S of lowercase letters is given.  We want to partition this string
# into as many parts as possible so that each letter appears in at most one
# part, and return a list of integers representing the size of these parts.
# 
# 
# Example 1:
# 
# Input: S = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it
# splits S into less parts.
# 
# 
# 
# Note:
# S will have length in range [1, 500].
# S will consist of lowercase letters ('a' to 'z') only.
# 
#
from collections import Counter
class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        counter = Counter(S)
        counting = Counter()
        output = []
        for i, c in enumerate(S):
            counting[c] += 1
            if all(counter[k] == v for k, v in counting.iteritems()):
                output.append(i + 1 - sum(output))
        return output

    def test(self):
        print self.partitionLabels("ababcbacadefegdehijhklij")

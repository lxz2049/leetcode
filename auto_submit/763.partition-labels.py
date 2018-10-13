#
# [768] Partition Labels
#
# https://leetcode.com/problems/partition-labels/description/
#
# algorithms
# Medium (65.43%)
# Total Accepted:    25.2K
# Total Submissions: 38.6K
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
class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        partitions = {}
        for i, s in enumerate(S):
            if s not in partitions:
                partitions[s] = [i, i]
            else:
                partitions[s][1] = i
        #print partitions
        labels = []
        for st, end in sorted(partitions.values()):
            if labels and labels[-1][0] <= st <= labels[-1][1]:
               labels[-1][1] = max(labels[-1][1], end)
            else:
                labels.append([st, end])
        return [end - st + 1 for st, end in labels]
            
    def test(self):
        print self.partitionLabels("ababcbacadefegdehijhklij")

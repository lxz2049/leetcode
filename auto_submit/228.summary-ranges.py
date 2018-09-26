#
# [228] Summary Ranges
#
# https://leetcode.com/problems/summary-ranges/description/
#
# algorithms
# Medium (33.53%)
# Total Accepted:    110.2K
# Total Submissions: 328.2K
# Testcase Example:  '[0,1,2,4,5,7]'
#
# Given a sorted integer array without duplicates, return the summary of its
# ranges.
# 
# Example 1:
# 
# 
# Input:  [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
# 
# 
# Example 2:
# 
# 
# Input:  [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.
# 
# 
#
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []

        ret = []
        start = nums[0]
        last = nums[0]
        for n in nums[1:]:
            if n  > last + 1:
                if start == last:
                    ret.append(str(start))
                else:
                    ret.append("%s->%s" % (start, last))
                start = n
            last = n
        if start == last:
            ret.append(str(start))
        else:
            ret.append("%s->%s" % (start, last))
        return ret

    def test(self):
        print self.summaryRanges([0,2,3,4,6,8,9])


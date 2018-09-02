#
# [128] Longest Consecutive Sequence
#
# https://leetcode.com/problems/longest-consecutive-sequence/description/
#
# algorithms
# Hard (38.50%)
# Total Accepted:    157.7K
# Total Submissions: 402.6K
# Testcase Example:  '[100,4,200,1,3,2]'
#
# Given an unsorted array of integers, find the length of the longest
# consecutive elements sequence.
# 
# Your algorithm should run in O(n) complexity.
# 
# Example:
# 
# 
# Input: [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
# Therefore its length is 4.
# 
# 
#
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        running_size = 1
        ans = 1 if nums else 0
        for i in xrange(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            if nums[i] == nums[i-1] + 1:
                running_size += 1
            else:
                running_size = 1
            ans = max(ans, running_size)
               
        return ans
        
        self.max_size = 1 if nums else 0
        def find(x):
            if x in tree:
                while tree[x]['parent'] != x:
                    x, tree[x]['parent'] = tree[x]['parent'], tree[tree[x]['parent']]['parent']
                return x
                
        def union(a, b):
            parent_a = find(a)
            parent_b = find(b)
            #print tree
            if parent_a is not None and parent_b is not None and parent_a != parent_b:
                if tree[parent_b]['size'] > tree[parent_a]['size']:
                    tree[parent_a]['parent'] = parent_b
                    tree[parent_b]['size'] += tree[parent_a]['size']
                    self.max_size = max(self.max_size, tree[parent_b]['size'])
                else:
                    tree[parent_b]['parent'] = parent_a
                    tree[parent_a]['size'] += tree[parent_b]['size']
                    self.max_size = max(self.max_size, tree[parent_a]['size'])

        tree = {}
        for n in nums:
            tree[n] = {'parent': n, 'size': 1}
            
        for n in nums:
            union(n+1, n)
            union(n, n-1)
        return self.max_size

    def test(self):
        #print self.longestConsecutive([100,4,200,1,3,2])
        print self.longestConsecutive([0, -1])

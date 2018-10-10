#
# [797] Rabbits in Forest
#
# https://leetcode.com/problems/rabbits-in-forest/description/
#
# algorithms
# Medium (49.85%)
# Total Accepted:    8.3K
# Total Submissions: 16.6K
# Testcase Example:  '[1,0,1,0,0]'
#
# In a forest, each rabbit has some color. Some subset of rabbits (possibly all
# of them) tell you how many other rabbits have the same color as them. Those
# answers are placed in an array.
# 
# Return the minimum number of rabbits that could be in the forest.
# 
# 
# Examples:
# Input: answers = [1, 1, 2]
# Output: 5
# Explanation:
# The two rabbits that answered "1" could both be the same color, say red.
# The rabbit than answered "2" can't be red or the answers would be
# inconsistent.
# Say the rabbit that answered "2" was blue.
# Then there should be 2 other blue rabbits in the forest that didn't answer
# into the array.
# The smallest possible number of rabbits in the forest is therefore 5: 3 that
# answered plus 2 that didn't.
# 
# Input: answers = [10, 10, 10]
# Output: 11
# 
# Input: answers = []
# Output: 0
# 
# 
# Note:
# 
# 
# answers will have length at most 1000.
# Each answers[i] will be an integer in the range [0, 999].
# 
# 
#
from collections import defaultdict
class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        seen = defaultdict(int)
        ret = 0
        for a in answers:
            seen[a] += 1
            if seen[a] == a + 1:
               ret += a + 1 
               seen[a] = 0
        return ret + sum(k + 1 for k in seen if seen[k])

    def test(self):
        print self.numRabbits([1, 1, 2])
        print self.numRabbits([10, 10, 10])
        print self.numRabbits([])

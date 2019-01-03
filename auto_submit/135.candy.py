#
# [135] Candy
#
# https://leetcode.com/problems/candy/description/
#
# algorithms
# Hard (26.31%)
# Total Accepted:    92.8K
# Total Submissions: 341.5K
# Testcase Example:  '[1,0,2]'
#
# There are N children standing in a line. Each child is assigned a rating
# value.
# 
# You are giving candies to these children subjected to the following
# requirements:
# 
# 
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# 
# 
# What is the minimum candies you must give?
# 
# Example 1:
# 
# 
# Input: [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 2, 1,
# 2 candies respectively.
# 
# 
# Example 2:
# 
# 
# Input: [1,2,2]
# Output: 4
# Explanation: You can allocate to the first, second and third child with 1, 2,
# 1 candies respectively.
# ⁠            The third child gets 1 candy because it satisfies the above two
# conditions.
# 
# 
#
class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        i = candy = ret = 0
        while i < len(ratings):
            # update candy
            if i and ratings[i-1] < ratings[i]:
                candy += 1
            else:
                candy = 1
            
            # peek forward
            j = i
            while j+1 < len(ratings) and ratings[j] > ratings[j+1]:
                j += 1
            count = j-i+1
            candy = max(count, candy)
            ret += candy + count * (count-1) / 2
            if i < j:
                candy = 1
            i = j+1
            #print candy, count * (count-1) / 2, ret

        return ret

    def test(self):
        #print self.candy([1,0,2])
        #print self.candy([1,2,2])
        print self.candy([0,1,2,5,3,2,7])

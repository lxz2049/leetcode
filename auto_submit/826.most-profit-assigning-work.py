#
# [853] Most Profit Assigning Work
#
# https://leetcode.com/problems/most-profit-assigning-work/description/
#
# algorithms
# Medium (32.88%)
# Total Accepted:    6.5K
# Total Submissions: 19.6K
# Testcase Example:  '[2,4,6,8,10]\n[10,20,30,40,50]\n[4,5,6,7]'
#
# We have jobs: difficulty[i] is the difficulty of the ith job, and profit[i]
# is the profit of the ith job. 
# 
# Now we have some workers. worker[i] is the ability of the ith worker, which
# means that this worker can only complete a job with difficulty at most
# worker[i]. 
# 
# Every worker can be assigned at most one job, but one job can be completed
# multiple times.
# 
# For example, if 3 people attempt the same job that pays $1, then the total
# profit will be $3.  If a worker cannot complete any job, his profit is $0.
# 
# What is the most profit we can make?
# 
# Example 1:
# 
# 
# Input: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker =
# [4,5,6,7]
# Output: 100 
# Explanation: Workers are assigned jobs of difficulty [4,4,6,6] and they get
# profit of [20,20,30,30] seperately.
# 
# Notes:
# 
# 
# 1 <= difficulty.length = profit.length <= 10000
# 1 <= worker.length <= 10000
# difficulty[i], profit[i], worker[i]  are in range [1, 10^5]
# 
# 
#
class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        jobs = sorted([(d, p) for d, p in zip(difficulty, profit)])
        worker.sort()
        ret = 0
        st, best = 0, 0
        for w in worker:
            while st < len(jobs) and w >= jobs[st][0]:
                best = max(best, jobs[st][1])
                st += 1
            ret += best
        return ret

    def test(self):
        print self.maxProfitAssignment([2,4,6,8,10], [10,20,30,40,50], [4,5,6,7])
            

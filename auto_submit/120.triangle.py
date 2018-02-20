import copy
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        dp = copy.deepcopy(triangle[-1])
        for l in reversed(triangle[:-1]):
            for i, n in enumerate(l):
                dp[i] = min(n+dp[i], n+dp[i+1])
        return dp[0]

    def test(self):
        t = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
        return self.minimumTotal(t)

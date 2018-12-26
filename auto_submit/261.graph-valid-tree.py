class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        s = range(n)
        r = [1] * n
        def find(i):
            if s[i] != i:
                #i = s[i]
                s[i] = find(s[i])
            return s[i]
        
        def merge(i, j):
            i = find(i)
            j = find(j)
            if i == j:
                return False
            if r[i] < r[j]:
                j, i = i, j
            s[j] = i
            r[i] += r[j]
            return True
        
        for i, j in edges:
            if not merge(i, j):
                return False
        
        return n and r[find(0)] == n


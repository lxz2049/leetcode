#
# [895] Shortest Path to Get All Keys
#
# https://leetcode.com/problems/shortest-path-to-get-all-keys/description/
#
# algorithms
# Hard (32.74%)
# Total Accepted:    2.4K
# Total Submissions: 7.4K
# Testcase Example:  '["@.a.#","###.#","b.A.B"]'
#
# We are given a 2-dimensional grid. "." is an empty cell, "#" is a wall, "@"
# is the starting point, ("a", "b", ...) are keys, and ("A", "B", ...) are
# locks.
# 
# We start at the starting point, and one move consists of walking one space in
# one of the 4 cardinal directions.  We cannot walk outside the grid, or walk
# into a wall.  If we walk over a key, we pick it up.  We can't walk over a
# lock unless we have the corresponding key.
# 
# For some 1 <= K <= 6, there is exactly one lowercase and one uppercase letter
# of the first K letters of the English alphabet in the grid.  This means that
# there is exactly one key for each lock, and one lock for each key; and also
# that the letters used to represent the keys and locks were chosen in the same
# order as the English alphabet.
# 
# Return the lowest number of moves to acquire all keys.  If it's impossible,
# return -1.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: ["@.a.#","###.#","b.A.B"]
# Output: 8
# 
# 
# 
# Example 2:
# 
# 
# Input: ["@..aA","..B#.","....b"]
# Output: 6
# 
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= grid.length <= 30
# 1 <= grid[0].length <= 30
# grid[i][j] contains only '.', '#', '@', 'a'-'f' and 'A'-'F'
# The number of keys is in [1, 6].  Each key has a different letter and opens
# exactly one lock.
# 
# 
# 
#
from collections import deque
class Solution(object):
    def shortestPathAllKeys(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        sx = sy = None
        keyCnt = 0
        for i, row in enumerate(grid):
            for j, col in enumerate(grid[i]):
                if col == '@':
                    sx = i
                    sy = j
                elif col.islower():
                    keyCnt += 1

        keys = set()
        self.shortest = 30 * 30

        def traverse(x, y, dis):
            if dis >= self.shortest:
                return
            if len(keys) == keyCnt:
                self.shortest = min(self.shortest, dis)
            else:
                nextKeys = findKeys(x, y)
                for key, keyX, keyY, distance in nextKeys:
                    keys.add(key)
                    traverse(keyX, keyY, dis + distance)
                    keys.remove(key)

        def findKeys(x, y):
            foundKeys = []
            visited = [[False] * len(row) for row in grid]
            q = deque([(x, y, 0)])
            while q:
                x, y, dist = q.pop()
                noPass = x < 0 or y < 0 or \
                         x >= len(grid) or y >= len(grid[0]) or \
                         visited[x][y] or \
                         grid[x][y] == '#' or \
                         grid[x][y].isupper() and grid[x][y].lower() not in keys
                if noPass:
                    continue

                if grid[x][y].islower() and grid[x][y] not in keys:
                    foundKeys.append((grid[x][y], x, y, dist))

                visited[x][y] = True
                for x, y in ((x, y-1), (x, y+1), 
                             (x-1, y), (x+1, y)):
                    q.appendleft((x, y, dist+1))
            return foundKeys

        traverse(sx, sy, 0)
        return self.shortest if self.shortest < 900 else -1

    def test(self):
        print self.shortestPathAllKeys(["@.a.#","###.#","b.A.B"])
        print self.shortestPathAllKeys(["@..aA","..B#.","....b"])


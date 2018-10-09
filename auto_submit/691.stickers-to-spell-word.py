#
# [691] Stickers to Spell Word
#
# https://leetcode.com/problems/stickers-to-spell-word/description/
#
# algorithms
# Hard (35.94%)
# Total Accepted:    6K
# Total Submissions: 16.6K
# Testcase Example:  '["with","example","science"]\n"thehat"'
#
# 
# We are given N different types of stickers.  Each sticker has a lowercase
# English word on it.
# 
# You would like to spell out the given target string by cutting individual
# letters from your collection of stickers and rearranging them.
# 
# You can use each sticker more than once if you want, and you have infinite
# quantities of each sticker.
# 
# What is the minimum number of stickers that you need to spell out the
# target?  If the task is impossible, return -1.
# 
# 
# Example 1:
# Input:
# ["with", "example", "science"], "thehat"
# 
# 
# Output:
# 3
# 
# 
# Explanation:
# We can use 2 "with" stickers, and 1 "example" sticker.
# After cutting and rearrange the letters of those stickers, we can form the
# target "thehat".
# Also, this is the minimum number of stickers necessary to form the target
# string.
# 
# 
# Example 2:
# Input:
# ["notice", "possible"], "basicbasic"
# 
# 
# Output:
# -1
# 
# 
# Explanation:
# We can't form the target "basicbasic" from cutting letters from the given
# stickers.
# 
# 
# Note:
# stickers has length in the range [1, 50].
# stickers consists of lowercase English words (without apostrophes).
# target has length in the range [1, 15], and consists of lowercase English
# letters.
# In all test cases, all words were chosen randomly from the 1000 most common
# US English words, and the target was chosen as a concatenation of two random
# words.
# The time limit may be more challenging than usual.  It is expected that a 50
# sticker test case can be solved within 35ms on average.
# 
#
from collections import Counter, deque
class Solution(object):
    def minStickers(self, stickers, target):
        t_count = Counter(target)
        A = [Counter(sticker) & t_count
             for sticker in stickers]

        for i in range(len(A) - 1, -1, -1):
            if any(A[i] == A[i] & A[j] for j in range(len(A)) if i != j):
                A.pop(i)

        self.best = len(target) + 1
        def search(ans = 0):
            if ans >= self.best: return
            if not A:
                if all(t_count[letter] <= 0 for letter in t_count):
                    self.best = ans
                return

            sticker = A.pop()
            used = max((t_count[letter] - 1) // sticker[letter] + 1
                        for letter in sticker)
            used = max(used, 0)

            for c in sticker:
                t_count[c] -= used * sticker[c]

            search(ans + used)
            for i in range(used - 1, -1, -1):
                for letter in sticker:
                    t_count[letter] += sticker[letter]
                search(ans + i)

            A.append(sticker)

        search()
        return self.best if self.best <= len(target) else -1

    def minStickers_(self, stickers, target):
        """
        :type stickers: List[str]
        :type target: str
        :rtype: int
        """
        target = Counter(target)
        stickers = [Counter(s) & target for s in stickers]
        for i in range(len(stickers) - 1, -1, -1):
            if any(stickers[i] == stickers[i] & stickers[j] for j in range(len(stickers)) if i != j):
                stickers.pop(i)

        visited = set()
        q = deque([(target, 0)])
        cnter = 0
        while q:
            cnter += 1
            missing, ret = q.popleft()
            if not missing:
                return ret
            #key = tuple(missing.elements())
            #visited.add(key)
            for s in stickers:
                if s & missing:
                    #if tuple((missing - s).elements()) not in visited:
                    q.append((missing - s, ret+1))

        return -1
                    
    def test(self):
        print self.minStickers(["with", "example", "science"], "thehat")
        print self.minStickers(["a", "b", "c"], "thehat")
        print self.minStickers(["this","island","keep","spring","problem","subject"], "gasproper")
        print self.minStickers(["island","spring","problem"], "gasproper")
        print self.minStickers(["slave","doctor","kept","insect","an","window","she","range","post","guide"], "supportclose")
        print self.minStickers(["control","heart","interest","stream","sentence","soil","wonder","them","month","slip","table","miss","boat","speak","figure","no","perhaps","twenty","throw","rich","capital","save","method","store","meant","life","oil","string","song","food","am","who","fat","if","put","path","come","grow","box","great","word","object","stead","common","fresh","the","operate","where","road","mean"], "stoodcrease")

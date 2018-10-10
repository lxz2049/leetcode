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
from collections import Counter
import heapq
class Solution(object):
    def minStickers(self, stickers, target):
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

        q = [(0, 0, target)]
        visited = set()
        while q:
            ret, length, missing = heapq.heappop(q)
            for s in stickers:
                key = tuple((missing-s).elements())
                if not key:
                    return ret + 1
                elif key not in visited:
                    visited.add(key)
                    heapq.heappush(q, (ret+1, len(key)+1, missing - s))

        return -1

    def test(self):
        print self.minStickers(["with", "example", "science"], "thehat")
        print self.minStickers(["these", "guess", "about", "garden", "him"], "atomher")
        print self.minStickers(["a", "b", "c"], "thehat")
        print self.minStickers(["this","island","keep","spring","problem","subject"], "gasproper")
        print self.minStickers(["island","spring","problem"], "gasproper")
        print self.minStickers(["slave","doctor","kept","insect","an","window","she","range","post","guide"], "supportclose")
        print self.minStickers(["control","heart","interest","stream","sentence","soil","wonder","them","month","slip","table","miss","boat","speak","figure","no","perhaps","twenty","throw","rich","capital","save","method","store","meant","life","oil","string","song","food","am","who","fat","if","put","path","come","grow","box","great","word","object","stead","common","fresh","the","operate","where","road","mean"], "stoodcrease")
        print self.minStickers(["divide","danger","student","share","feet","say","expect","chair","special","blue","differ","thank","doctor","top","there","had","ice","mark","note","equate","basic","so","hope","happy","draw","evening","star","shall","thousand","mother","quite","letter","atom","baby","such","trouble","stand","day","room","third","level","salt","thing","shore","truck","block","time","fresh","dream","talk"], "distantcollect")

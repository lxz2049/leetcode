#
# [648] Replace Words
#
# https://leetcode.com/problems/replace-words/description/
#
# algorithms
# Medium (49.50%)
# Total Accepted:    25.4K
# Total Submissions: 51.3K
# Testcase Example:  '["cat", "bat", "rat"]\n"the cattle was rattled by the battery"'
#
# 
# In English, we have a concept called root, which can be followed by some
# other words to form another longer word - let's call this word successor. For
# example, the root an, followed by other, which can form another word
# another.
# 
# 
# 
# 
# Now, given a dictionary consisting of many roots and a sentence. You need to
# replace all the successor in the sentence with the root forming it. If a
# successor has many roots can form it, replace it with the root with the
# shortest length.
# 
# 
# 
# You need to output the sentence after the replacement.
# 
# 
# 
# Example 1:
# 
# Input: dict = ["cat", "bat", "rat"]
# sentence = "the cattle was rattled by the battery"
# Output: "the cat was rat by the bat"
# 
# 
# 
# 
# Note:
# 
# The input will only have lower-case letters.
# ⁠1 
# ⁠1 
# ⁠1 
# ⁠1 
# 
# 
#
class Solution(object):
    def replaceWords(self, d, sentence):
        d = set(d)
        ret = []
        for w in sentence.split(" "):
            ret.append(next((w[:i+1] for i in xrange(len(w)) if w[:i+1] in d), w))
        return " ".join(ret)

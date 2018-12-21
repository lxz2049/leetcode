#
# [355] Design Twitter
#
# https://leetcode.com/problems/design-twitter/description/
#
# algorithms
# Medium (26.42%)
# Total Accepted:    30.1K
# Total Submissions: 113.8K
# Testcase Example:  '["Twitter","postTweet","getNewsFeed","follow","postTweet","getNewsFeed","unfollow","getNewsFeed"]\n[[],[1,5],[1],[1,2],[2,6],[1],[1,2],[1]]'
#
# Design a simplified version of Twitter where users can post tweets,
# follow/unfollow another user and is able to see the 10 most recent tweets in
# the user's news feed. Your design should support the following methods:
# 
# 
# 
# postTweet(userId, tweetId): Compose a new tweet.
# getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news
# feed. Each item in the news feed must be posted by users who the user
# followed or by the user herself. Tweets must be ordered from most recent to
# least recent.
# follow(followerId, followeeId): Follower follows a followee.
# unfollow(followerId, followeeId): Follower unfollows a followee.
# 
# 
# 
# Example:
# 
# Twitter twitter = new Twitter();
# 
# // User 1 posts a new tweet (id = 5).
# twitter.postTweet(1, 5);
# 
# // User 1's news feed should return a list with 1 tweet id -> [5].
# twitter.getNewsFeed(1);
# 
# // User 1 follows user 2.
# twitter.follow(1, 2);
# 
# // User 2 posts a new tweet (id = 6).
# twitter.postTweet(2, 6);
# 
# // User 1's news feed should return a list with 2 tweet ids -> [6, 5].
# // Tweet id 6 should precede tweet id 5 because it is posted after tweet id
# 5.
# twitter.getNewsFeed(1);
# 
# // User 1 unfollows user 2.
# twitter.unfollow(1, 2);
# 
# // User 1's news feed should return a list with 1 tweet id -> [5],
# // since user 1 is no longer following user 2.
# twitter.getNewsFeed(1);
# 
# 
#
import heapq
from collections import defaultdict
class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.users = defaultdict(list)
        self.relationship = defaultdict(set)
        self.ts = 0
        
    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self.users[userId].append((-self.ts, tweetId))
        self.ts += 1
        
    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        lists = [self.users[i] for i in [userId] + list(self.relationship[userId])]
        heap = [(u[-1], u, -1) for u in lists if u]
        heapq.heapify(heap)
        ret = []
        while len(ret) < 10 and heap:
            t, u, i = heapq.heappop(heap)
            ret.append(t[1])
            if len(u) + i - 1 >= 0:
                heapq.heappush(heap, (u[i-1], u, i-1))
        return ret

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId != followeeId:
            self.relationship[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        self.relationship[followerId].discard(followeeId)


class Solution:
    def test(self):
        twitter = Twitter()
        twitter.postTweet(1,1)
        twitter.postTweet(1,2)
        print twitter.getNewsFeed(1)
        twitter.follow(2,1)
        print twitter.getNewsFeed(2)
        twitter.unfollow(2,1)
        print twitter.getNewsFeed(2)

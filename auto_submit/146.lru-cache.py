#
# [146] LRU Cache
#
# https://leetcode.com/problems/lru-cache/description/
#
# algorithms
# Hard (22.58%)
# Total Accepted:    235.3K
# Total Submissions: 1M
# Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
#
# 
# Design and implement a data structure for Least Recently Used (LRU) cache. It
# should support the following operations: get and put.
# 
# 
# 
# get(key) - Get the value (will always be positive) of the key if the key
# exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present.
# When the cache reached its capacity, it should invalidate the least recently
# used item before inserting a new item.
# 
# 
# Follow up:
# Could you do both operations in O(1) time complexity?
# 
# Example:
# 
# LRUCache cache = new LRUCache( 2 /* capacity */ );
# 
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4
# 
# 
#
class ListNode(object):
    def __init__(self, key=None, val=None):
        self.next = None
        self.prev = None
        self.key = key
        self.val = val


class List(object):
    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next, self.tail.prev = self.tail, self.head

    def add(self, node):
        n = self.head.next
        self.head.next = n.prev = node
        node.next, node.prev = n, self.head

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.size = 0
        self.capacity = capacity
        self.hashmap = dict()
        self.cache = List()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.hashmap:
            node = self.hashmap[key]
            self.promote(node)
            return node.val

        return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.hashmap:
            node = self.hashmap[key]
            node.val = value
            self.promote(node)
        else:
            if self.size >= self.capacity:
                self.evict()
            node = ListNode(key, value)
            self.cache.add(node)
            self.hashmap[key] = node
            self.size += 1
            
    def evict(self):
        tail = self.cache.tail.prev
        self.cache.remove(tail)
        self.hashmap.pop(tail.key)
        self.size -= 1

    def promote(self, node):
        self.cache.remove(node)
        self.cache.add(node)
            
        
class Solution:
    def test(self):
        cache = LRUCache(2)
         
        print cache.put(1, 1)
        print cache.put(2, 2)
        print cache.get(1)       # returns 1
        print cache.put(3, 3)    # evicts key 2
        print cache.get(2)       # returns -1 (not found)
        print cache.put(4, 4)    # evicts key 1
        print cache.get(1)       # returns -1 (not found)
        print cache.get(3)       # returns 3
        print cache.get(4)       # returns 4

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

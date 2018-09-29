/*
 * [432] All O`one Data Structure
 *
 * https://leetcode.com/problems/all-oone-data-structure/description/
 *
 * algorithms
 * Hard (27.71%)
 * Total Accepted:    12.2K
 * Total Submissions: 43.1K
 * Testcase Example:  '["AllOne","getMaxKey","getMinKey"]\n[[],[],[]]'
 *
 * Implement a data structure supporting the following operations:
 * 
 * 
 * 
 * Inc(Key) - Inserts a new key  with value 1. Or increments an existing key by
 * 1. Key is guaranteed to be a non-empty string.
 * Dec(Key) - If Key's value is 1, remove it from the data structure. Otherwise
 * decrements an existing key by 1. If the key does not exist, this function
 * does nothing. Key is guaranteed to be a non-empty string.
 * GetMaxKey() - Returns one of the keys with maximal value. If no element
 * exists, return an empty string "".
 * GetMinKey() - Returns one of the keys with minimal value. If no element
 * exists, return an empty string "".
 * 
 * 
 * 
 * 
 * Challenge: Perform all these in O(1) time complexity.
 * 
 */
struct Bucket {
    unordered_set<string> keys;
    int value;
    Bucket(int x) { value = x; }
};

typedef list<Bucket> BucketList;
typedef BucketList::iterator BucketIterator;
typedef unordered_map<string, BucketIterator> KeyMapping;

class AllOne {
private:
    BucketList bucketList;
    KeyMapping keyMapping;
public:
    /** Initialize your data structure here. */
    AllOne() {
    }
    
    /** Inserts a new key <Key> with value 1. Or increments an existing key by 1. */
    void inc(string key) {
        if (keyMapping.find(key) == keyMapping.end()) {
            // new key with value 1
            if (bucketList.begin() == bucketList.end() || bucketList.begin()->value > 1) {
                bucketList.push_front(Bucket(1));
            }
            BucketIterator it = bucketList.begin();
            it->keys.insert(key);
            keyMapping[key] = it;
        } else {
            // increment
            BucketIterator it = keyMapping[key];
            it->keys.erase(key);
            BucketIterator next_it = next(it);
            if (next_it == bucketList.end() || next_it->value > it->value + 1) {
                next_it = bucketList.insert(next_it, Bucket(it->value+1));
            }
            next_it->keys.insert(key);
            keyMapping[key] = next_it;
            // remove bucket from list
            if (!it->keys.size()) {
                bucketList.erase(it);
            }
        }
    }
    
    /** Decrements an existing key by 1. If Key's value is 1, remove it from the data structure. */
    void dec(string key) {
        if (keyMapping.find(key) != keyMapping.end()) {
            // decrement
            BucketIterator it = keyMapping[key];
            it->keys.erase(key);
            if (it->value > 1) {
                BucketIterator prev_it = prev(it);
                if (prev_it == bucketList.end() || prev_it->value < it->value - 1) { 
                    prev_it = bucketList.insert(it, Bucket(it->value - 1));
                }
                prev_it->keys.insert(key);
                keyMapping[key] = prev_it;
            } else {
                // remove key with value 0
                keyMapping.erase(key);
            }
            // remove bucket from list
            if (!it->keys.size()) {
                bucketList.erase(it);
            }
        }
    }
    
    /** Returns one of the keys with maximal value. */
    string getMaxKey() {
        if (bucketList.size())
            return *bucketList.back().keys.begin();
        return "";
    }
    
    /** Returns one of the keys with Minimal value. */
    string getMinKey() {
        if (bucketList.size())
            return *bucketList.front().keys.begin();
        return "";
    }
};

class Solution {
public:
    void test() {
        AllOne test;
        test.inc("a"); cout<<test.getMaxKey()<<" "<<test.getMinKey()<<endl;
        test.inc("a"); cout<<test.getMaxKey()<<" "<<test.getMinKey()<<endl;
        test.inc("b"); cout<<test.getMaxKey()<<" "<<test.getMinKey()<<endl;
        test.inc("b"); cout<<test.getMaxKey()<<" "<<test.getMinKey()<<endl; 
        test.inc("c"); cout<<test.getMaxKey()<<" "<<test.getMinKey()<<endl; 
        test.inc("c"); cout<<test.getMaxKey()<<" "<<test.getMinKey()<<endl; 
        test.inc("c"); cout<<test.getMaxKey()<<" "<<test.getMinKey()<<endl; 

        test.dec("b"); cout<<test.getMaxKey()<<" "<<test.getMinKey()<<endl; 
        test.dec("b"); cout<<test.getMaxKey()<<" "<<test.getMinKey()<<endl; 
        test.dec("a"); cout<<test.getMaxKey()<<" "<<test.getMinKey()<<endl; 
        test.dec("a"); cout<<test.getMaxKey()<<" "<<test.getMinKey()<<endl; 
    }
};

/**
 * Your AllOne object will be instantiated and called as such:
 * AllOne obj = new AllOne();
 * obj.inc(key);
 * obj.dec(key);
 * string param_3 = obj.getMaxKey();
 * string param_4 = obj.getMinKey();
 */

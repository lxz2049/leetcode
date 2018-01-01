#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
using namespace std;

const int MAX_CACHE_SIZE = 1 << 14;

struct HashNode {
	int key;
	int value;
	HashNode *prevNode;
	HashNode *nextNode;
	HashNode *prev;
	HashNode *next;
	HashNode(int k, int val) : 
		key(k),
		value(val),
		prevNode(NULL),
		nextNode(NULL),
		prev(NULL),
		next(NULL) {}
};

class LRUCache{
public:
    LRUCache(int cap) : 
		capacity(cap),
		size(0),
		head(NULL),
		tail(NULL) { 
			cache = new HashNode*[cap]; 
			memset(cache, 0, cap * sizeof(HashNode*));
		}
		
    
    int get(int key) {
		//printf("\nattemping to get key %d\n", key);
		int hashKey = hash(key);
        HashNode* entry = cache[hashKey];
		while (entry) {
			//printf("%d %d\n", entry->key, entry->value);
			if (entry->key == key) {
				// found key
				//printf("getting key %d with value %d\n", key, entry->value);
				updateLastUsed(entry);
				return entry->value;
			}
			entry = entry->nextNode;
		}
		//printf("didn't find key!\n"); 
		return -1;
    }
    
    void set(int key, int value) {
		//printf("\nattempting to set key %d to value %d\n", key, value);
		int hashKey = hash(key);
		HashNode* entry = cache[hashKey];
		while (entry) {
			if (entry->key == key) {
				// found key
				//printf("setting key %d from value %d to %d\n", key, entry->value, value);
				entry->value = value;
				updateLastUsed(entry);
				return;
			}
			entry = entry->nextNode;
		}
		// didn't find key, add to cache
		if (size >= capacity) {
			//printf("reached capacity %d removing key %d!\n", capacity, head->key);
			// remove head from cache
			int headHashKey = hash(head->key);
			if (head->nextNode) {
				head->nextNode->prevNode = head->prevNode;
			}
			if (head->prevNode) {
				head->prevNode->nextNode = head->nextNode;
			} else {
				cache[headHashKey] = head->nextNode;
				//printf("cache[%d]%lu\n", head->key, (unsigned long)cache[hash(head->key]);
			}

			// remove from lru list
			HashNode* oldHead = head;
			head = head->next;
			if (head) {
				head->prev = NULL;
			} else {
				head = NULL;
			}
			size--;
			delete(oldHead);
		}
		//printf("creating new key %d with value %d\n", key, value);
		HashNode* newNode = new HashNode(key, value);
		if (cache[hashKey]) {
			cache[hashKey]->prevNode = newNode;
		}
		newNode->nextNode = cache[hashKey];
		cache[hashKey] = newNode;
		size++;
		addLastUsed(newNode);
    }
private:
	int hash(int key) {
		int hashKey = key % capacity;
		//printf("hashing key %d into %d\n", key, hashKey);
		return hashKey;
	}
	void updateLastUsed(HashNode* node) {
		//printLRUList();
		// do nothing if already end of list
		if (!node->next) {
			return;
		}
		// remove node from current position
		if (!node->prev) {
			// update head if necessary
			head = node->next;
		} else {
			node->prev->next = node->next;
		}
		node->next->prev = node->prev;
		addLastUsed(node);
	}
	void addLastUsed(HashNode* node) {
		// add new node to end of list
		if (!head){
			tail = head = node;
		} else {
			node->prev= tail;
			node->next = NULL;
			tail->next= node;
			tail = node;
		}
		//printf("head %d tail %d\n", head ? head->key : -1, tail ? tail->key : -1);
	}
	void printLRUList() {
		printf("***DEBUG***\nPrinting LRUList\n");
		HashNode *node = head;
		while (node) {
			//printf("node->prev%lu node->next%lu\n", (unsigned long)node->prev, (unsigned long)node->next);
			printf("node key: %d ", node->key);
			node = node->next;
		}
		printf("\n");
	}
	HashNode** cache;
	HashNode* head;
	HashNode* tail;
	int capacity;
	int size;
};

void test0 () {
	printf("\n*****************\n");
	printf("executing test0\n");
	LRUCache cache(1);
	cache.get(0);
	cache.set(1, 1);
	cache.set(2, 2);
	cache.get(2);
}

void test1 () {
	printf("\n*****************\n");
	printf("executing test1\n");
	LRUCache cache(5);
	cache.get(0);
	cache.set(1, 1);
	cache.set(2, 2);
	cache.set(3, 3);
	cache.set(4, 4);
	cache.set(5, 5);
	cache.set(5, 6);
	cache.set(1, 0);
	cache.set(6, 6);
}

void test2 () {
	printf("\n*****************\n");
	printf("executing test2\n");
	LRUCache cache(1);
	cache.set(2, 1);
	cache.get(2);
	cache.set(3, 2);
	cache.get(2);
	cache.get(3);
}

void test3 () {
	printf("\n*****************\n");
	printf("executing test3\n");
	LRUCache cache(5);
	cache.set(1, 1);
	cache.set(2, 2);
	cache.set(3, 3);
	cache.set(4, 4);
	cache.set(5, 5);

	cache.get(1);
	cache.set(1, 11);
	cache.get(2);
	cache.set(2, 22);
	cache.get(3);
	cache.set(3, 33);
	cache.get(4);
	cache.set(4, 44);
	cache.get(5);
	cache.set(5, 55);
}

int main() {
	//test0();
	//test1();
	//test2();
	test3();
	return 0;
}

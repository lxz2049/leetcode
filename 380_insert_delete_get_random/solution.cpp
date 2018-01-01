#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <stdlib.h>

using namespace std;

struct HashNode {
	int value;
	int index;
	HashNode *next;
	HashNode (int val, int id) : value(val), index(id), next(NULL) {};
};

class RandomizedSet {
	public:
    /** Initialize your data structure here. */
    RandomizedSet() {
		srand (time(NULL));
		table = new HashNode*[65535];
		keySet = new int[65535];
		memset(table, 0, sizeof(HashNode*) * 65535);
		memset(keySet, 0, sizeof(int) * 65535);
		count = 0;
    }
    
    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    bool insert(int val) {
		//printf("insert %d\n", val);
		int key = hash(val);		        
		HashNode *entry = table[key];
		while (entry) {
			if (entry->value == val) {
				return false;
			}		
			entry = entry->next;
		}
		// insert into array
		int index = count++;
		keySet[index] = val;

		// insert into table
		HashNode *newEntry = new HashNode(val, index); 
		newEntry->next = table[key];
		table[key] = newEntry;

		return true;
    }
			    
    /** Removes a value from the set. Returns true if the set contained the specified element. */
    bool remove(int val) {
		//printf("remove %d\n", val);
		int key = hash(val);
		HashNode *entry = table[key];
		HashNode *prev = NULL;
		while (entry) {
			if (entry->value == val) {
				// swap and remove from array
				int last = --count;
				modifyMapping(keySet[last], entry->index);
				keySet[entry->index] = keySet[last];

				// remove from table
				if (prev) {
					prev->next = entry->next;
				} else {
					table[key] = NULL;	
				}
				delete entry;
				return true;
			}		
			entry = entry->next;
		}
		return false;
    }

	void modifyMapping(int val, int id) {
		int key = hash(val);
		HashNode *entry = table[key];
		while (entry) {
			if (entry->value == val) {
				//printf("modified from %d to %d\n", entry->index, id);
				entry->index = id;
				return;
			}		
			entry = entry->next;
		}
    }

    /** Get a random element from the set. */
    int getRandom() {
		if (count == 0) {
			return 0;
		}
		int id = rand() % count;
		/*
		printf("getting random from key set: ");
		for (int i = 0; i < count; ++i) {
			printf("%d ", keySet[i]);
		}
		printf("\n");
		*/
		return keySet[id];
    }

	private:
	int hash(int a) {
		//printf("hashing %d into %d\n", a, a&65535);
		return a & 65535;
	}
	HashNode **table;
	int *keySet;
	int count;
};

int main() {
	RandomizedSet s;
	printf("%d\n", s.insert(1));
	printf("%d\n", s.insert(10));
	printf("%d\n", s.insert(20));
	printf("%d\n", s.insert(30));
	printf("%d\n", s.getRandom());
	//printf("%d\n", s.remove(-2));
	return 0;
}

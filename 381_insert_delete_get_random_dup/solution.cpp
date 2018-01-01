#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <stdlib.h>

using namespace std;

const int TABLE_SIZE = 1024;
struct HashNode {
	int value;
	int index;
	HashNode *next;
	HashNode (int val, int id) : value(val), index(id), next(NULL) {};
};

class RandomizedCollection {
	public:
    /** Initialize your data structure here. */
    RandomizedCollection() {
		srand (time(NULL));
		table = new HashNode*[TABLE_SIZE];
		keySet = new int[TABLE_SIZE];
		memset(table, 0, sizeof(HashNode*) * TABLE_SIZE);
		memset(keySet, 0, sizeof(int) * TABLE_SIZE);
		count = 0;
    }
    
    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    bool insert(int val) {
		//printf("insert %d\n", val);
		bool ret = true;
		int key = hash(val);		        
		HashNode *entry = table[key];
		while (entry) {
			if (entry->value == val) {
				ret = false;
				break;
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

		return ret;
    }
			    
    /** Removes a value from the set. Returns true if the set contained the specified element. */
    bool remove(int val) {
		//printf("remove %d\n", val);
		int key = hash(val);
		HashNode *entry = table[key];
		HashNode *prev = NULL;
		while (entry) {
			if (entry->value == val) {
				//printf("found %d with index:%d\n", val, entry->index);
				// swap and remove from array
				int last = --count;
				modifyMapping(keySet[last], entry->index);
				keySet[entry->index] = keySet[last];

				// remove from table
				if (prev)
					prev->next = entry->next;
				else
					table[key] = entry->next;
				delete entry;
				return true;
			}		
			prev = entry;
			entry = entry->next;
		}
		return false;
    }

	void modifyMapping(int val, int id) {
		int key = hash(val);
		HashNode *entry = table[key];
		while (entry) {
			if (entry->index == count) {
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
		int modulus = TABLE_SIZE - 1;
		//printf("hashing %d into %d\n", a, a & modulus);
		return a & modulus;
	}
	HashNode **table;
	int *keySet;
	int count;
};

int main() {
	RandomizedCollection s;
	printf("%d\n", s.insert(-1));
	printf("%d\n", s.remove(-2));
	printf("%d\n", s.insert(-2));
	printf("%d\n", s.getRandom());
	return 0;
}

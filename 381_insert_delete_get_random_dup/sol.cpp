#include<map>
#include<vector>
#include<iostream>

using namespace std;

class RandomizedCollection {
private:
    map<int, vector<int> > dic;
    vector<int> arr;
    
public:
    RandomizedCollection() {
    }

    bool insert(int val) {
        arr.push_back(val);//add val in arr
        dic[val].push_back(arr.size() - 1);//add its index in dic[val]
        return dic[val].size() == 1;
    }
    
    bool remove(int val) {
        if(dic[val].size() == 0)
        {
            return false;
        }
        int idx = dic[val].back();//arr[idx] = val
        dic[val].pop_back();
       //swap arr[idx] and arr[arr.size()-1] if idx != arr.size()-1
       //modify the dic at the same time.
        if(arr.size() - 1 != idx)
        {
            int tmp = arr.back();
            arr[idx] = tmp;
     //the new index of tmp is now idx, so modify the dic accordingly.
            dic[tmp].pop_back();
            dic[tmp].push_back(idx);
        }
       //remove the last element in arr
        arr.pop_back();
        return true;
    }

    int getRandom() {
        return arr[rand()%arr.size()];
    }
};

int main() {
	RandomizedCollection s;
	printf("%d\n", s.insert(4));
	printf("%d\n", s.insert(3));
	printf("%d\n", s.insert(4));
	printf("%d\n", s.insert(2));
	printf("%d\n", s.insert(4));
	printf("%d\n", s.remove(4));
	printf("%d\n", s.remove(3));
	printf("%d\n", s.remove(4));
	printf("%d\n", s.remove(4));
	printf("%d\n", s.getRandom());
	//printf("%d\n", s.remove(-2));
	return 0;
}

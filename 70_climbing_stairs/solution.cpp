#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>

using namespace std;

class Solution {
	public:
    int climbStairs(int n) {
 		// fibonacci       
		int ans = 1;
		int prev = 0;
		for (int i = 0; i < n; ++i) {
			int tmp = ans;
			ans += prev;
			prev = tmp;
		}

		return ans;
    }
};

int main() {
	Solution sol;
	printf("%d\n", sol.climbStairs(4));
	return 0;
}

#include <iostream>                                                                                                           
#include <stdio.h>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
    public:
    int combinationSum4(vector<int>& nums, int target) {
		vector<int> dp(target + 1, 0);
		dp[0] = 1;

		for (int i = 0; i <= target ; ++i) {
			for (int j = 0; j < nums.size(); ++j) {
				if (i >= nums[j]) {
					dp[i] += dp[i-nums[j]];
				}
			}
		}

		return dp[target];
	}  
};



int main() {
	int a[] = {1,2};
	vector<int> nums(a, a+2);
	Solution sol;
	printf("%d\n", sol.combinationSum4(nums, 10));
    return 0;
}

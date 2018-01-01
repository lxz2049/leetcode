#include <iostream>                                                                                                           
#include <stdio.h>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
	public:
    vector<vector<int> > combinationSum3(int k, int n) {
		int target = n;

		// create dp array of size target
		vector<vector<vector<int> > > dp(target + 1);
		dp[0] = vector<vector<int > >(1, vector<int>());

		// begin dping
		for (int i = 1; i < 10; ++i) {
			int candidate = i;
			//printf("\ncandidate %d\n", candidate);
			for (int j = target; j >= candidate; --j) {
				//printf("j%d\n", j);
				vector<vector<int> > &ingredients = dp[j-candidate];
				//printf("ingredients size %lu\n", ingredients.size());
				for (int k = 0; k < ingredients.size(); ++k) {
					vector<int> newCandidate(ingredients[k]);
					newCandidate.push_back(candidate);
					dp[j].push_back(newCandidate);
				}
			}
		}

		// remove unqualified entries
		vector<vector<int> > ans;
		for (int i = 0; i < dp[target].size(); ++i) {
			if (dp[target][i].size() == k) {
				ans.push_back(dp[target][i]);
			}
		}

		return ans;
    }
};

int main() {
	Solution sol;
	vector<vector<int> > ans = sol.combinationSum3(3, 9);
	for (int i = 0; i < ans.size(); ++i) {
		for (int j = 0; j < ans[i].size(); ++j) {
			printf("%d ", ans[i][j]);
		}
		printf("\n");
	}
    return 0;
}

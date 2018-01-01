#include <iostream>                                                                                                           
#include <stdio.h>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
	public:
    vector<vector<int> > combinationSum2(vector<int>& candidates, int target) {
		// sort candidates
		sort(candidates.begin(), candidates.end());

		// create dp array of size target
		vector<vector<vector<int> > > dp(target + 1);
		dp[0] = vector<vector<int > >(1, vector<int>());

		// begin dping
		for (int i = 0; i < candidates.size(); ++i) {
			int candidate = candidates[i];
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

		// remove duplicates
		sort(dp[target].begin(), dp[target].end());
		vector<vector<int> > ret;
		for (int i = 0; i < dp[target].size(); ++i) {
			if (i == 0 || dp[target][i] != dp[target][i-1]) {
				ret.push_back(dp[target][i]);
			}
		}

		return ret;
    }
};

int main() {
	int ints[] = {10, 1, 2, 7, 6, 1, 5};
	vector<int> v(ints, ints+7);
	Solution sol;
	vector<vector<int> > ans = sol.combinationSum2(v, 8);
	for (int i = 0; i < ans.size(); ++i) {
		for (int j = 0; j < ans[i].size(); ++j) {
			printf("%d ", ans[i][j]);
		}
		printf("\n");
	}
    return 0;
}

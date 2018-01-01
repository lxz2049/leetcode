#include <iostream>                                                                                                           
#include <stdio.h>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
	public:
    vector<vector<int> > combinationSum(vector<int>& candidates, int target) {
		// sort candidates
		sort(candidates.begin(), candidates.end());

		// create dp array of size target
		vector<vector<vector<int> > > dp(target + 1);
		dp[0] = vector<vector<int > >(1, vector<int>());
		
		// begin dping
		for (int i = 0; i < candidates.size(); ++i) {
			int candidate = candidates[i];
			//printf("\ncandidate %d\n", candidate);
			for (int j = candidate; j <= target; ++j) {
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

		return dp[target];
    }
};

int main() {
	int ints[] = {2, 3, 6, 7};
	vector<int> v(ints, ints+4);
	Solution sol;
	vector<vector<int> > ans = sol.combinationSum(v, 7);
	for (int i = 0; i < ans.size(); ++i) {
		for (int j = 0; j < ans[i].size(); ++j) {
			printf("%d ", ans[i][j]);
		}
		printf("\n");
	}
    return 0;
}

#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <stack>

using namespace std;

class Solution {
	public:
	int titleToNumber(string s) {
		int result = 0;
		for (int i = 0; i < s.length(); ++i) {
			result = result * 26 + s[i] - 'A' + 1;
		}
		return result;
	}
};

int main() {
	string input;
	Solution sol;
	cin>>input;
	printf("%d\n", sol.titleToNumber(input));
	return 0;
}

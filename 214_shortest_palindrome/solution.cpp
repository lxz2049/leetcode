#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>

using namespace std;

class Solution {
	private:
	int t[60002];
	void buildKMPTable(string s) {
		t[0] = -1;
		t[1] = 0;
		int pos = 2;
		int cnd = 0;
		while (pos < s.size()) {
			if (s[pos - 1] == s[cnd]) {
				t[pos] = cnd + 1;
			}
		}
	}
	public:
	string shortestPalindrome(string s) {
        
    }
};

int main() {
	Solution sol;
	printf("%d\n", sol.shortestPalindrome("abcd"));
	printf("%d\n", sol.shortestPalindrome("aacecaaa"));
	return 0;
}

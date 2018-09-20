class Solution {
public:
    bool buddyStrings(string A, string B) {
        if (A.size() != B.size())   return false;

        int diff = 0, repeat = 0, diff_i;
        vector<int>map(26);
        for (int i=0; i<A.size(); ++i) {
            if (map[A[i] - 'a'])
                repeat ++;
            else
                map[A[i] - 'a'] ++;

            repeat += i > 0 ? A[i] == A[i-1] : 0;
            if (A[i] != B[i]) {
                if (!diff)  {
                    diff_i = i;
                    diff ++;
                } else if (A[i] != B[diff_i] || A[diff_i] != B[i] || diff > 2) {
                    return false;
                }
            }
        }
        return diff || repeat;
    }

    void test() {
        cout<<buddyStrings("aa", "aa")<<endl;
        cout<<buddyStrings("abcaa", "abcbb")<<endl;
        cout<<buddyStrings("abab", "abab")<<endl;
    }
};


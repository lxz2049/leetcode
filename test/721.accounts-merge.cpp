/*
 * [721] Accounts Merge
 *
 * https://leetcode.com/problems/accounts-merge/description/
 *
 * algorithms
 * Medium (35.18%)
 * Total Accepted:    16.5K
 * Total Submissions: 47K
 * Testcase Example:  '[["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]'
 *
 * Given a list accounts, each element accounts[i] is a list of strings, where
 * the first element accounts[i][0] is a name, and the rest of the elements are
 * emails representing emails of the account.
 * 
 * Now, we would like to merge these accounts.  Two accounts definitely belong
 * to the same person if there is some email that is common to both accounts.
 * Note that even if two accounts have the same name, they may belong to
 * different people as people could have the same name.  A person can have any
 * number of accounts initially, but all of their accounts definitely have the
 * same name.
 * 
 * After merging the accounts, return the accounts in the following format: the
 * first element of each account is the name, and the rest of the elements are
 * emails in sorted order.  The accounts themselves can be returned in any
 * order.
 * 
 * Example 1:
 * 
 * Input: 
 * accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John",
 * "johnnybravo@mail.com"], ["John", "johnsmith@mail.com",
 * "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
 * Output: [["John", 'john00@mail.com', 'john_newyork@mail.com',
 * 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary",
 * "mary@mail.com"]]
 * Explanation: 
 * The first and third John's are the same person as they have the common email
 * "johnsmith@mail.com".
 * The second John and Mary are different people as none of their email
 * addresses are used by other accounts.
 * We could return these lists in any order, for example the answer [['Mary',
 * 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
 * ['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']]
 * would still be accepted.
 * 
 * 
 * 
 * Note:
 * The length of accounts will be in the range [1, 1000].
 * The length of accounts[i] will be in the range [1, 10].
 * The length of accounts[i][j] will be in the range [1, 30].
 * 
 */
class Solution {
public:
    unordered_map<string, pair<string, int>> disjointSet;
    unordered_map<string, string> accountMapping;
    unordered_map<string, set<string>> ans;

    string find(string a) {
        while (disjointSet[a].first != a) {
            disjointSet[a].first = disjointSet[disjointSet[a].first].first;
            a = disjointSet[a].first;
        }
        return a;
    }

    void merge(string a, string b) {
        if (disjointSet.find(a) == disjointSet.end()) {
            disjointSet[a] = pair<string, int>(a, 1);
        }
        if (disjointSet.find(b) == disjointSet.end()) {
            disjointSet[b] = pair<string, int>(b, 1);
        }

        string parent_a = find(a);
        string parent_b = find(b);

        if (parent_a != parent_b) {
            if (disjointSet[parent_a].second > disjointSet[parent_b].second) {
                disjointSet[parent_b].first = parent_a;
                disjointSet[parent_a].second += disjointSet[parent_b].second;
            } else {
                disjointSet[parent_a].first = parent_b;
                disjointSet[parent_b].second += disjointSet[parent_a].second;
            }
        }
    }

    vector<vector<string>> accountsMerge(vector<vector<string>>& accounts) {
        disjointSet.clear();       
        accountMapping.clear();
        ans.clear();
        for (int i=0; i<accounts.size(); ++i) {
            string name = accounts[i][0];
            for (int j=1; j<accounts[i].size(); ++j) {
                accountMapping[accounts[i][j]] = name;
                if (j > 1) merge(accounts[i][j], accounts[i][j-1]);
            }
        }

        for (unordered_map<string, pair<string, int>>::iterator it = disjointSet.begin(); it != disjointSet.end(); it++) {
            string parent = find(it->second);
            ans[parent].insert(it->second);
        }

        vector<vector<string>> ret;
        for (unordered_map<string, set<string>>::iterator it = ans.begin(); it != ans.end(); it++) {
            vector<string> account;
            string name = accountMapping[it->first];
            account.push_back(name);
            account.assign(it->second.begin(), it->second.end());
            ret.push_back(account);
        }
        return ret;
    }

    void test() {
        vector<vector<string>> input = {{"a", "a"}};
        vector<vector<string>> ret = accountsMerge(input);
        cout<<ret[0]<<" "<<ret[1]<<endl;
    }
};

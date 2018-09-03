/*
 * [684] Redundant Connection
 *
 * https://leetcode.com/problems/redundant-connection/description/
 *
 * algorithms
 * Medium (44.22%)
 * Total Accepted:    22.3K
 * Total Submissions: 48.7K
 * Testcase Example:  '[[1,2],[1,3],[2,3]]'
 *
 * 
 * In this problem, a tree is an undirected graph that is connected and has no
 * cycles.
 * 
 * The given input is a graph that started as a tree with N nodes (with
 * distinct values 1, 2, ..., N), with one additional edge added.  The added
 * edge has two different vertices chosen from 1 to N, and was not an edge that
 * already existed.
 * 
 * The resulting graph is given as a 2D-array of edges.  Each element of edges
 * is a pair [u, v] with u < v, that represents an undirected edge connecting
 * nodes u and v.
 * 
 * Return an edge that can be removed so that the resulting graph is a tree of
 * N nodes.  If there are multiple answers, return the answer that occurs last
 * in the given 2D-array.  The answer edge [u, v] should be in the same format,
 * with u < v.
 * Example 1:
 * 
 * Input: [[1,2], [1,3], [2,3]]
 * Output: [2,3]
 * Explanation: The given undirected graph will be like this:
 * ⁠ 1
 * ⁠/ \
 * 2 - 3
 * 
 * 
 * Example 2:
 * 
 * Input: [[1,2], [2,3], [3,4], [1,4], [1,5]]
 * Output: [1,4]
 * Explanation: The given undirected graph will be like this:
 * 5 - 1 - 2
 * ⁠   |   |
 * ⁠   4 - 3
 * 
 * 
 * Note:
 * The size of the input 2D-array will be between 3 and 1000.
 * Every integer represented in the 2D-array will be between 1 and N, where N
 * is the size of the input array.
 * 
 * 
 * 
 * 
 * 
 * Update (2017-09-26):
 * We have overhauled the problem description + test cases and specified
 * clearly the graph is an undirected graph. For the directed graph follow up
 * please see Redundant Connection II). We apologize for any inconvenience
 * caused.
 * 
 */
class Solution {
public:
    vector<pair<int, int>> disjointSet;

    Solution() {
        disjointSet = vector<pair<int, int>>(1000);
    }

    int find_parent(int a) {
        int parent = disjointSet[a].first;
        while (a != parent) {
            disjointSet[a].first = disjointSet[parent].first;
            a = parent;
            parent = disjointSet[a].first;
        }
        return parent;
    }

    bool add_edge(int a, int b) {
        if (!disjointSet[a].second) {
            disjointSet[a].first = a;
            disjointSet[a].second = 1;
        }
        if (!disjointSet[b].second) {
            disjointSet[b].first = b;
            disjointSet[b].second = 1;
        }

        int parent_a = find_parent(a);
        int parent_b = find_parent(b);
        //cout<<"a "<<a<<" parent_a "<<parent_a<<endl;
        //cout<<"b "<<b<<" parent_b "<<parent_b<<endl;
        if (parent_a != parent_b) {
            disjointSet[parent_a].first = parent_b;
            return true;
        }
 
        return false;
    }

    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        disjointSet.clear();
        for (int i=0; i<edges.size(); ++i) {
            if (!add_edge(edges[i][0],edges[i][1]))
                return {edges[i]};
        }
        return {};
    }

    void test() {
        /*
        vector<vector<int>> edges = {{1,2}, {2,3}, {3,4}, {1,4}, {1,5}};
        vector<int> ans = findRedundantConnection(edges);
        cout<<ans[0]<<" "<<ans[1]<<endl;
        */

        vector<vector<int>> edges = {{1,2}, {1,3}, {2,3}};
        vector<int> ans = findRedundantConnection(edges);
        cout<<ans[0]<<" "<<ans[1]<<endl;
    }
};

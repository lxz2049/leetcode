class Solution {
public:
    vector<pair<int, int>> disjointSet;
    int candidate_a;
    int candidate_b;
    int candidate_c;

    Solution() {
        disjointSet = vector<pair<int, int>>(1001);
    }

    int find_parent(int a) {
        int parent = disjointSet[a].first;
        while (a != parent) {
            a = parent;
            parent = disjointSet[a].first;
        }
        return parent;
    }

    void add_edge(int i, int a, int b) {
        if (!disjointSet[a].first) {
            disjointSet[a].first = a;
            disjointSet[a].second = i;
        }
        if (!disjointSet[b].first) {
            disjointSet[b].first = b;
            disjointSet[b].second = i;
        }

        int parent_a = find_parent(a);
        int parent_b = find_parent(b);
        //cout<<"a "<<a<<" parent_a "<<parent_a<<endl;
        //cout<<"b "<<b<<" parent_b "<<parent_b<<endl;
        
        if (parent_a == parent_b) {
            // loop found
            candidate_c = i;
        } 
        else if (b != parent_b) {
            // b already has a parent, so skip a->b and save both edges as candidates
            // also this should only happen once as there are only one extra edge
            candidate_a = disjointSet[b].second;
            candidate_b = i;
        }
        else {
            // connect b to a
            disjointSet[b].first = parent_a;
            disjointSet[b].second = i;
        }
    }

    vector<int> findRedundantDirectedConnection(vector<vector<int>>& edges) {
        fill(disjointSet.begin(), disjointSet.end(), pair<int, int>(0,0));
        candidate_a = candidate_b = candidate_c = -1;
        for (int i=0; i<edges.size(); ++i) {
            add_edge(i, edges[i][0], edges[i][1]);
        }
        if (candidate_c >= 0) {
            if (candidate_a >= 0)
                return {edges[candidate_a]};
            return {edges[candidate_c]};
        }
        return {edges[candidate_b]};
    }

    void test() {
        //vector<vector<int>> edges = {{1,2}, {2,3}, {3,4}, {1,4}, {1,5}};
        //vector<vector<int>> edges = {{1,2}, {1,3}, {2,3}};
        //vector<vector<int>> edges = {{2,1}, {3,1}, {4,2}, {1,4}};
        //vector<vector<int>> edges = {{3,4}, {4,1}, {1,2}, {2,3}, {5,1}};
        vector<vector<int>> edges = {{3,4}, {4,1}, {1,2}, {2,3}, {5,3}};
        vector<int> ans = findRedundantDirectedConnection(edges);
        cout<<ans[0]<<" "<<ans[1]<<endl;
    }
};

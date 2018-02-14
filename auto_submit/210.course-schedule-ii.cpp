/*
 * [210] Course Schedule II
 *
 * https://leetcode.com/problems/course-schedule-ii/description/
 *
 * algorithms
 * Medium (29.85%)
 * Total Accepted:    84.1K
 * Total Submissions: 281.7K
 * Testcase Example:  '2\n[[1,0]]'
 *
 * 
 * There are a total of n courses you have to take, labeled from 0 to n - 1.
 * 
 * Some courses may have prerequisites, for example to take course 0 you have
 * to first take course 1, which is expressed as a pair: [0,1]
 * 
 * 
 * Given the total number of courses and a list of prerequisite pairs, return
 * the ordering of courses you should take to finish all courses.
 * 
 * There may be multiple correct orders, you just need to return one of them.
 * If it is impossible to finish all courses, return an empty array.
 * 
 * 
 * For example:
 * 2, [[1,0]]
 * There are a total of 2 courses to take. To take course 1 you should have
 * finished course 0. So the correct course order is [0,1]
 * 
 * 4, [[1,0],[2,0],[3,1],[3,2]]
 * There are a total of 4 courses to take. To take course 3 you should have
 * finished both courses 1 and 2. Both courses 1 and 2 should be taken after
 * you finished course 0. So one correct course order is [0,1,2,3]. Another
 * correct ordering is[0,2,1,3].
 * 
 * Note:
 * 
 * The input prerequisites is a graph represented by a list of edges, not
 * adjacency matrices. Read more about how a graph is represented.
 * You may assume that there are no duplicate edges in the input
 * prerequisites.
 * 
 * 
 * 
 * click to show more hints.
 * 
 * Hints:
 * 
 * This problem is equivalent to finding the topological order in a directed
 * graph. If a cycle exists, no topological ordering exists and therefore it
 * will be impossible to take all courses.
 * Topological Sort via DFS - A great video tutorial (21 minutes) on Coursera
 * explaining the basic concepts of Topological Sort.
 * Topological sort could also be done via BFS.
 * 
 * 
 */
class Solution {
public:
    vector<int> findOrder(int numCourses, vector<pair<int, int> >& prerequisites) {
		// construct graph
 		vector<vector<int> > g(numCourses);
		for (int i=0; i<prerequisites.size(); ++i) {
			g[prerequisites[i].second].push_back(prerequisites[i].first);
		}

		/*
		printf ("printing graph: \n");
		for (int i=0; i<g.size(); ++i) {
			printf ("%d -> ", i);
			for (int j=0; j<g[i].size(); ++j) {
				printf ("%d ", g[i][j]);
			}
			printf ("\n");
		}
		*/

		// dfs
 		vector<int> visited(numCourses);
 		vector<int> topoOrder;
		for (int i=0; i<numCourses; ++i) {
			if (!visited[i] && !dfs(g, visited, topoOrder, i)) {
				return vector<int>();
			}
		}
		reverse(topoOrder.begin(), topoOrder.end());
		return topoOrder;
    }

	bool dfs(vector<vector<int> > &g, vector<int> &visited, vector<int> &topoOrder, int n) {
		visited[n] = 1;
		for (int i=0; i<g[n].size(); ++i) {
			int pre = g[n][i];
			if (visited[pre] == 1 || !visited[pre] && !dfs(g, visited, topoOrder, pre)) {	// loop detected
				return false;
			}
		}
		visited[n] = 2;
		//printf("%d\n", n);
		topoOrder.push_back(n);
		return true;
	}

	bool test() {
		vector<pair<int, int> > pre;	
		pre.push_back(pair<int, int> (1, 0));
		pre.push_back(pair<int, int> (2, 0));
		pre.push_back(pair<int, int> (3, 1));
		pre.push_back(pair<int, int> (3, 2));
		vector<int> ans = findOrder(4, pre);
		for (int i=0; i<ans.size(); ++i) {
			printf("%d ", ans[i]);
		}
		printf("\n");
		return true;
	}
};

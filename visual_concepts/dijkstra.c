#include <stdio.h>
#include <stdbool.h>

static const int MAXDIST = 0x7FFFFFFF;

bool visited[100] = {0};
int cities[100][100] = {0};
int dist[100];
int n;

void dijkstra() {
	// init
	int i;
	for (i = 0; i < n; ++i) {	
		dist[i] = MAXDIST;
	}
	dist[0] = 0;

	// traverse
	while (true) {
		// find nearest unvisited city
		int minDist = MAXDIST;
		int minCity = -1;
		for (i = 0; i < n; ++i)	{
			if (!visited[i] && dist[i]< minDist) {
				minDist = dist[i];
				minCity = i;
			}
		}
		if (minCity == -1) {
			// we have traversed all reachable cities
			break;
		}

		// update distances
		visited[minCity] = true;
		for (i = 0; i < n; ++i) {
			int len = cities[minCity][i];
			if (!visited[i] && len != -1 && minDist + len < dist[i]) {
				dist[i] = minDist + len;
			}
		}
	}
}

int main() {
	// input
	int i,j;
	scanf("%d", &n);
	for (i = 0; i < n; ++i) {
		for (j = 0; j < i; ++j) {
			char s[10]; 
			scanf("%s", s);
			int len;
			if (s[0] == 'x') {
				len = -1;
			} else {
				len = atoi(s);
			}
			cities[j][i] = cities[i][j] = len;
		}
	}

	// find shortest paths
	dijkstra();

	// output the distance of the farthest city
	int maxMinDist = 0; 
	for (i = 0; i < n; ++i) {
		if (dist[i] > maxMinDist) {
			maxMinDist = dist[i];
		}
	}
	printf("%d\n", maxMinDist);

	return 0;
}

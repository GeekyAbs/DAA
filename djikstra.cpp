#include <climits>
#include <functional>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

class Solution {
public:
  vector<int> dijkstra(int V, vector<vector<int>> &edges, int src) {

    // Step 1: Build adjacency list
    vector<vector<pair<int, int>>> adj(V);

    for (auto &edge : edges) {
      int u = edge[0];
      int v = edge[1];
      int w = edge[2];

      adj[u].push_back({v, w});
      adj[v].push_back({u, w}); // remove this line if graph is directed
    }

    // Step 2: Min-heap (distance, node)
    priority_queue<pair<int, int>, vector<pair<int, int>>,
                   greater<pair<int, int>>>
        pq;

    // Step 3: Distance array
    vector<int> dist(V, INT_MAX);
    dist[src] = 0;

    pq.push({0, src});

    // Step 4: Dijkstra
    while (!pq.empty()) {
      int dis = pq.top().first;
      int node = pq.top().second;
      pq.pop();

      // Skip if we already found a better distance
      if (dis > dist[node])
        continue;

      for (auto &it : adj[node]) {
        int adjNode = it.first;
        int edgeWeight = it.second;

        if (dis + edgeWeight < dist[adjNode]) {
          dist[adjNode] = dis + edgeWeight;
          pq.push({dist[adjNode], adjNode});
        }
      }
    }

    return dist;
  }
};

int main() {
  int V = 5;

  vector<vector<int>> edges = {{0, 1, 2}, {0, 2, 4}, {1, 2, 1},
                               {1, 3, 7}, {2, 4, 3}, {3, 4, 1}};

  int src = 0;

  Solution sol;
  vector<int> result = sol.dijkstra(V, edges, src);

  cout << "Shortest distances from source " << src << ":\n";
  for (int i = 0; i < V; i++) {
    cout << "Node " << i << " -> ";
    if (result[i] == INT_MAX)
      cout << "INF";
    else
      cout << result[i];
    cout << endl;
  }

  return 0;
}

import heapq
import math


class Solution:
    def dijkstra(self, V, edges, src):

        # Step 1: Build adjacency list
        adj = []

        # create V empty lists
        for i in range(V):
            adj.append([])

        # fill adjacency list
        for i in range(len(edges)):
            u = edges[i][0]
            v = edges[i][1]
            w = edges[i][2]

            # if directed graph → only this line
            adj[u].append((v, w))

            # if undirected graph → uncomment below
            # adj[v].append((u, w))

        # Step 2: Create empty min heap
        minHeap = []

        # Step 3: Create distance array
        dist = []

        for i in range(V):
            dist.append(math.inf)

        dist[src] = 0

        # push source into heap
        heapq.heappush(minHeap, (0, src))

        # Step 4: Dijkstra
        while len(minHeap) > 0:
            top = heapq.heappop(minHeap)
            dis = top[0]
            node = top[1]

            # Skip outdated entries
            if dis > dist[node]:
                continue

            # Traverse neighbors
            neighbors = adj[node]

            for i in range(len(neighbors)):
                adjNode = neighbors[i][0]
                edgeWeight = neighbors[i][1]

                if dis + edgeWeight < dist[adjNode]:
                    dist[adjNode] = dis + edgeWeight
                    heapq.heappush(minHeap, (dist[adjNode], adjNode))

        return dist


def main():

    V = 5

    edges = [[0, 1, 2], [0, 2, 4], [1, 2, 1], [1, 3, 7], [2, 4, 3], [3, 4, 1]]

    src = 0

    sol = Solution()
    result = sol.dijkstra(V, edges, src)

    print("Shortest distances from source", src)

    for i in range(V):
        if result[i] == math.inf:
            print("Node", i, "-> INF")
        else:
            print("Node", i, "->", result[i])


if __name__ == "__main__":
    main()

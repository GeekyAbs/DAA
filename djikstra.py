from typing import List, Dict
import heapq


class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        # Build adjacency list
        adj = {i: [] for i in range(n)}
        for s, d, weight in edges:
            adj[s].append((d, weight))

        shortest = {}  # vertex -> shortest distance

        minHeap = [(0, src)]  # (distance, node)

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)

            if n1 in shortest:
                continue

            shortest[n1] = w1

            for n2, w2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(minHeap, (w1 + w2, n2))

        # Mark unreachable nodes as -1
        for i in range(n):
            if i not in shortest:
                shortest[i] = -1

        return shortest


def main():
    n = 5
    edges = [[0, 1, 2], [0, 2, 4], [1, 2, 1], [1, 3, 7], [2, 4, 3], [3, 4, 1]]
    src = 0

    sol = Solution()
    result = sol.shortestPath(n, edges, src)

    print("Shortest distances from source:", src)
    for node in sorted(result.keys()):
        print(f"Node {node} -> {result[node]}")


if __name__ == "__main__":
    main()

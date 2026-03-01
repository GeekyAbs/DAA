from collections import deque


def bfs(graph, source):
    seen = set()
    q = deque()
    q.append(source)
    seen.add(source)

    while q:
        node = q.popleft()
        print(node, end=" ")
        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                q.append(neighbor)


def main():
    graph = {0: [1, 2], 1: [3, 4], 2: [5], 3: [], 4: [5], 5: []}
    source = 0
    bfs(graph, source)


if __name__ == "__main__":
    main()

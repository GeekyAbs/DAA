# REMEMBER:
# Bellman Ford Algorithm works for directed graphs even when there are negative weights
# Bellman Ford Algorithm is used to detect negative cycles in a graph
def bellman_ford(graph, vertices, source):
    dist = [float("inf")] * vertices
    dist[source] = 0
    # relaxation step
    for _ in range(vertices - 1):
        for n1, n2, cost in graph:
            if dist[n1] != float("inf") and dist[n1] + cost < dist[n2]:
                dist[n2] = dist[n1] + cost
    # checking for negative cycle
    for n1, n2, cost in graph:
        if dist[n1] != float("inf") and dist[n1] + cost < dist[n2]:
            return -1
    return dist


def main():
    vertices = 5
    graph = {
        (0, 1, -1),
        (0, 2, 4),
        (1, 2, 3),
        (1, 3, 2),
        (1, 4, 2),
        (3, 2, 5),
        (3, 1, 1),
        (4, 3, -3),
    }
    source = 0
    ans = bellman_ford(graph, vertices, source)
    if ans == -1:
        print("Negative Cycle Present")
    else:
        for i in range(vertices):
            print(f"Vertex {i} -> {ans[i]}")


if __name__ == "__main__":
    main()

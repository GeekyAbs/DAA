def dfs(graph, source):
    seen = set()
    stack = [source]
    seen.add(source)
    ans = []
    while stack:
        node = stack.pop()
        ans.append(node)
        for neighbor in graph[node]:
            if neighbor not in stack:
                seen.add(neighbor)
                stack.append(neighbor)

    return ans


def main():
    graph = {0: [1, 2], 1: [3, 4], 2: [5], 3: [], 4: [5], 5: []}
    source = 0
    res = dfs(graph, source)
    print(res)


if __name__ == "__main__":
    main()

def minimax(depth, node_idx, is_max, values, max_depth):
    if depth == max_depth:
        return values[node_idx]
    if is_max:
        return max(
            minimax(depth + 1, node_idx * 2, False, values, 3),
            minimax(depth + 1, node_idx * 2 + 1, False, values, 3),
        )
    else:
        return min(
            minimax(depth + 1, node_idx * 2, True, values, 3),
            minimax(depth + 1, node_idx * 2 + 1, True, values, 3),
        )


tree = [3, 5, 6, 9, 1, 2, 0, -1]
max_depth = 3
optimal_value = minimax(0, 0, True, tree, 3)
print(optimal_value)

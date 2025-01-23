def manhattan_distance(state, goal_state):
    distance = 0
    for i, tile in enumerate(state):
        if tile == 0: 
            continue
        goal_index = goal_state.index(tile)
        distance += abs(i // 3 - goal_index // 3) + abs(i % 3 - goal_index % 3)
    return distance

initial_state = [1, 2, 3, 4, 0, 5, 6, 7, 8]
goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
heuristic_value = manhattan_distance(initial_state, goal_state)
print(f"Manhattan Distance: {heuristic_value}")


def block_heuristic(state, goal_state):
    return sum(1 for i in range(len(state)) if state[i] != goal_state[i])

initial_state = ["A", "B", "C", "D"]
goal_state = ["B", "A", "D", "C"]
heuristic_value = block_heuristic(initial_state, goal_state)
print(f"Heuristic Value: {heuristic_value}")

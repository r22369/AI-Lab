def calculate_heuristic(current_state, goal_state):
    heuristic = 0
    num_blocks = len(current_state)

    for i in range(num_blocks):
        current_block = current_state[i]
        try:
            goal_index = goal_state.index(current_block)
        except ValueError:
            return -num_blocks

        if i == goal_index:
            heuristic += 1
        else:
            heuristic -= 1

    return heuristic


def calculate_heuristic_extended(current_state, goal_state):
    heuristic = 0
    num_blocks = len(current_state)

    for i in range(num_blocks):
        current_block = current_state[i]
        try:
            goal_index = goal_state.index(current_block)
        except ValueError:
            return -num_blocks

        if i == goal_index:
            heuristic += 1
            for j in range(i + 1, num_blocks):
                below_block_current = current_state[j]
                try:
                    below_block_goal_index = goal_state.index(below_block_current)

                    if j == below_block_goal_index:
                        heuristic += 1
                    else:
                        heuristic -=1
                except ValueError:
                    heuristic -=1
        else:
            heuristic -= 1
            for j in range(i + 1, num_blocks):
                below_block_current = current_state[j]
                try:
                    below_block_goal_index = goal_state.index(below_block_current)
                    if j == below_block_goal_index:
                        heuristic -= 1
                    else:
                        heuristic += 1
                except ValueError:
                    heuristic += 1
    return heuristic

start_state = ['A', 'D', 'C', 'B']
goal_state = ['D', 'C', 'B', 'A']

heuristic_value = calculate_heuristic(start_state, goal_state)
print(f"Heuristic value (basic): {heuristic_value}")

heuristic_value_extended = calculate_heuristic_extended(start_state, goal_state)
print(f"Heuristic value (extended): {heuristic_value_extended}")

start_state = ['A', 'B', 'C', 'D']
goal_state = ['D', 'C', 'B', 'A']

heuristic_value = calculate_heuristic(start_state, goal_state)
print(f"Heuristic value (basic): {heuristic_value}")

heuristic_value_extended = calculate_heuristic_extended(start_state, goal_state)
print(f"Heuristic value (extended): {heuristic_value_extended}")

start_state = ['A', 'B', 'C']
goal_state = ['A','C','B','D']

heuristic_value_extended = calculate_heuristic_extended(start_state, goal_state)
print(f"Heuristic value (extended): {heuristic_value_extended}")

import heapq
import random

def misplaced_tiles(state, goal):
    misplaced = 0
    for i in range(9):
        if state[i] != 0 and state[i] != goal[i]:
            misplaced += 1
    return misplaced

def manhattan_distance(state, goal):
    distance = 0
    for i in range(9):
        if state[i] != 0:
            x1, y1 = i % 3, i // 3
            x2, y2 = goal.index(state[i]) % 3, goal.index(state[i]) // 3
            distance += abs(x1 - x2) + abs(y1 - y2)
    return distance

def find_blank(state):
    return state.index(0)

def generate_neighbors(state):
    blank_index = find_blank(state)
    row, col = blank_index // 3, blank_index % 3
    neighbors = []

    moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # Left, Right, Up, Down
    for dr, dc in moves:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_blank_index = new_row * 3 + new_col
            neighbor = state[:]  # Create a copy
            neighbor[blank_index], neighbor[new_blank_index] = neighbor[new_blank_index], neighbor[blank_index]
            neighbors.append(neighbor)
    return neighbors

def steepest_ascent_hill_climbing(start_state, goal_state, heuristic=manhattan_distance):
    current_state = start_state
    current_heuristic = heuristic(current_state, goal_state)
    path = [current_state]

    while True:
        neighbors = generate_neighbors(current_state)
        best_neighbor = None
        best_heuristic = current_heuristic

        for neighbor in neighbors:
            neighbor_heuristic = heuristic(neighbor, goal_state)
            if neighbor_heuristic < best_heuristic:
                best_heuristic = neighbor_heuristic
                best_neighbor = neighbor
        
        if best_neighbor is None or best_heuristic >= current_heuristic:
            break  # Local optimum or no better neighbor

        current_state = best_neighbor
        current_heuristic = best_heuristic
        path.append(current_state)

    return path

# Example usage:
start_state = [1, 2, 3, 4, 0, 5, 6, 7, 8]
goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

path = steepest_ascent_hill_climbing(start_state, goal_state, manhattan_distance)

if path:
    print("Path found:")
    for state in path:
        print(state)
    print("Steps:",len(path)-1)
else:
    print("No solution found (local optimum reached).")

start_state = [1, 2, 3, 4, 5, 6, 0, 7, 8]
goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

path = steepest_ascent_hill_climbing(start_state, goal_state, manhattan_distance)

if path:
    print("Path found:")
    for state in path:
        print(state)
    print("Steps:",len(path)-1)
else:
    print("No solution found (local optimum reached).")

start_state = [8, 1, 3, 4, 0, 2, 7, 6, 5]
goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

path = steepest_ascent_hill_climbing(start_state, goal_state, manhattan_distance)

if path:
    print("Path found:")
    for state in path:
        print(state)
    print("Steps:",len(path)-1)
else:
    print("No solution found (local optimum reached).")

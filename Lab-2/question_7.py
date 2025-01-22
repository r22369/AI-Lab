import heapq

class PuzzleSolver:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.rows, self.cols = 3, 3

    def find_blank(self, state):
        """Find the position of the blank (0) in the puzzle."""
        return state.index(0)

    def manhattan_distance(self, state):
        """Calculate the Manhattan distance heuristic."""
        distance = 0
        for i, tile in enumerate(state):
            if tile == 0:
                continue
            goal_position = self.goal_state.index(tile)
            distance += abs(i // self.cols - goal_position // self.cols) + abs(i % self.cols - goal_position % self.cols)
        return distance

    def get_neighbors(self, state):
        """Generate all possible moves from the current state."""
        blank_index = self.find_blank(state)
        row, col = divmod(blank_index, self.cols)
        moves = []

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < self.rows and 0 <= new_col < self.cols:
                new_blank_index = new_row * self.cols + new_col
                new_state = list(state)
                new_state[blank_index], new_state[new_blank_index] = new_state[new_blank_index], new_state[blank_index]
                moves.append(tuple(new_state))
        return moves

    def solve(self):
        open_list = []
        heapq.heappush(open_list, (0, self.initial_state, 0, None)) 
        closed_set = set()
        came_from = {}

        while open_list:
            _, current_state, g, parent = heapq.heappop(open_list)

            if current_state in closed_set:
                continue
            closed_set.add(current_state)
            came_from[current_state] = parent

            # Goal test
            if current_state == self.goal_state:
                return self.reconstruct_path(came_from, current_state)

            for neighbor in self.get_neighbors(current_state):
                if neighbor in closed_set:
                    continue
                h = self.manhattan_distance(neighbor)
                f = g + 1 + h
                heapq.heappush(open_list, (f, neighbor, g + 1, current_state))

        return None  

    def reconstruct_path(self, came_from, current_state):
        path = []
        while current_state:
            path.append(current_state)
            current_state = came_from[current_state]
        return path[::-1]

if __name__ == "__main__":
    initial_state = (1, 2, 3, 4, 0, 5, 6, 7, 8) 
    goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)

    solver = PuzzleSolver(initial_state, goal_state)
    solution = solver.solve()

    if solution:
        print(f"Solution found in {len(solution) - 1} moves:")
        for state in solution:
            print(state[:3])
            print(state[3:6])
            print(state[6:])
            print()
    else:
        print("No solution found.")


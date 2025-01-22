class HillClimbingSolver:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.rows, self.cols = 3, 3 

    def find_blank(self, state):
        return state.index(0)

    def manhattan_distance(self, state):
        distance = 0
        for i, tile in enumerate(state):
            if tile == 0:
                continue
            goal_position = self.goal_state.index(tile)
            distance += abs(i // self.cols - goal_position // self.cols) + abs(i % self.cols - goal_position % self.cols)
        return distance

    def get_neighbors(self, state):
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
        current_state = self.initial_state
        current_h = self.manhattan_distance(current_state)

        while True:
            neighbors = self.get_neighbors(current_state)
            best_neighbor = None
            best_h = float("inf")

            for neighbor in neighbors:
                h = self.manhattan_distance(neighbor)
                if h < best_h:
                    best_neighbor = neighbor
                    best_h = h

            if best_h >= current_h:
                return current_state, current_h

            current_state = best_neighbor
            current_h = best_h

if __name__ == "__main__":
    initial_state = (1, 2, 3, 4, 0, 5, 6, 7, 8) 
    goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)

    solver = HillClimbingSolver(initial_state, goal_state)
    final_state, final_heuristic = solver.solve()

    print("Final State:")
    print(final_state[:3])
    print(final_state[3:6])
    print(final_state[6:])
    print(f"Final Heuristic Value: {final_heuristic}")


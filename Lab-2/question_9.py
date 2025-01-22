import math
import random

class SimulatedAnnealing:
    def __init__(self, initial_state, goal_state, initial_temp, cooling_rate):
        self.current_state = initial_state
        self.goal_state = goal_state
        self.temperature = initial_temp
        self.cooling_rate = cooling_rate
        self.rows, self.cols = 3, 3

    def manhattan_distance(self, state):
        distance = 0
        for i, tile in enumerate(state):
            if tile == 0:
                continue
            goal_position = self.goal_state.index(tile)
            distance += abs(i // self.cols - goal_position // self.cols) + abs(i % self.cols - goal_position % self.cols)
        return distance

    def find_blank(self, state):
        return state.index(0)

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
        current_h = self.manhattan_distance(self.current_state)

        while self.temperature > 1e-3: 
            neighbors = self.get_neighbors(self.current_state)
            next_state = random.choice(neighbors)
            next_h = self.manhattan_distance(next_state)
            delta_h = next_h - current_h

            if delta_h < 0 or random.uniform(0, 1) < math.exp(-delta_h / self.temperature):
                self.current_state = next_state
                current_h = next_h

            self.temperature *= self.cooling_rate

        return self.current_state, current_h

if __name__ == "__main__":
    initial_state = (1, 2, 3, 4, 0, 5, 6, 7, 8) 
    goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)

    initial_temp = 100.0
    cooling_rate = 0.99

    solver = SimulatedAnnealing(initial_state, goal_state, initial_temp, cooling_rate)
    final_state, final_heuristic = solver.solve()

    print("Final State:")
    print(final_state[:3])
    print(final_state[3:6])
    print(final_state[6:])
    print(f"Final Heuristic Value: {final_heuristic}")


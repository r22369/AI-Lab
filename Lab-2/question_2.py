from collections import deque

class WaterJug:
    def __init__(self, jug1_cap, jug2_cap, goal):
        self.j1_cap = jug1_cap
        self.j2_cap = jug2_cap
        self.goal = goal

    def is_goal(self, state):
        return state == self.goal

    def next_states(self, state):
        j1, j2 = state
        states = []

        states.append((self.j1_cap, j2))  # Fill jug1
        states.append((j1, self.j2_cap))  # Fill jug2
        states.append((0, j2))           # Empty jug1
        states.append((j1, 0))           # Empty jug2

        pour = min(j1, self.j2_cap - j2)
        states.append((j1 - pour, j2 + pour))  # Pour j1 to j2

        pour = min(j2, self.j1_cap - j1)
        states.append((j1 + pour, j2 - pour))  # Pour j2 to j1
        return states

def search(problem, start, method="bfs"): 
    queue = deque([(start, None)]) if method == "bfs" else [(start, None)]
    seen = {start: None}

    while queue:
        current, parent = queue.popleft() if method == "bfs" else queue.pop()
        if problem.is_goal(current):
            return make_path(seen, current)
        for next_state in problem.next_states(current):
            if next_state not in seen:
                queue.append((next_state, current))
                seen[next_state] = current
    return None

def make_path(seen, goal):
    path = []
    current = goal
    while current:
        path.append(current)
        current = seen[current]
    return path[::-1]

def get_input():
    while True:
        try:
            j1_cap = int(input("Jug 1 capacity: "))
            j2_cap = int(input("Jug 2 capacity: "))
            goal_j1 = int(input("Goal in Jug 1: "))
            goal_j2 = int(input("Goal in Jug 2: "))
            start_j1 = int(input("Start in Jug 1: "))
            start_j2 = int(input("Start in Jug 2: "))

            if j1_cap <=0 or j2_cap <= 0 or goal_j1 < 0 or goal_j1 > j1_cap or goal_j2 < 0 or goal_j2 > j2_cap or start_j1 < 0 or start_j1 > j1_cap or start_j2 <0 or start_j2 > j2_cap:
                raise ValueError
            
            return j1_cap, j2_cap, (goal_j1, goal_j2), (start_j1, start_j2)
        except ValueError:
            print("Invalid input. Positive integers only, goal and start within capacity.")

j1_cap, j2_cap, goal, start = get_input()
problem = WaterJug(j1_cap, j2_cap, goal)

print("\nBFS:")
bfs_solution = search(problem, start, "bfs")
print(bfs_solution if bfs_solution else "No solution")

print("\nDFS:")
dfs_solution = search(problem, start, "dfs")
print(dfs_solution if dfs_solution else "No solution")

print("\nNext states from start:")
for s in problem.next_states(start):
    print(s)

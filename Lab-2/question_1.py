from collections import deque

class WaterJug:
    def __init__(self, jug1_capacity, jug2_capacity, the_goal):
        self.jug1_capacity = jug1_capacity
        self.jug2_capacity = jug2_capacity
        self.goal = the_goal

    def is_goal(self, current_state):
        if current_state == self.goal:
            return True
        else:
            return False

    def get_next_states(self, current_state):
        x, y = current_state 

        possible_states = []

        possible_states.append((self.jug1_capacity, y))

        possible_states.append((x, self.jug2_capacity))

        possible_states.append((0, y))

        possible_states.append((x, 0))

        pour_amount = min(x, self.jug2_capacity - y)
        possible_states.append((x - pour_amount, y + pour_amount))

        pour_amount = min(y, self.jug1_capacity - x)
        possible_states.append((x + pour_amount, y - pour_amount))

        return possible_states

def do_bfs(problem, start_state):
    queue = deque([(start_state, None)]) 
    already_checked = {start_state: None}

    while queue:
        current_state, parent = queue.popleft()

        if problem.is_goal(current_state):
            return make_path(already_checked, current_state)

        for next_state in problem.get_next_states(current_state):
            if next_state not in already_checked:
                queue.append((next_state, current_state))
                already_checked[next_state] = current_state

    return None 

def do_dfs(problem, start_state):
    stack = [(start_state, None)]
    already_checked = {start_state: None}

    while stack:
        current_state, parent = stack.pop()

        if problem.is_goal(current_state):
            return make_path(already_checked, current_state)

        for next_state in problem.get_next_states(current_state):
            if next_state not in already_checked:
                stack.append((next_state, current_state))
                already_checked[next_state] = current_state

    return None

def make_path(checked_states, goal_state):
    path = []
    current = goal_state
    while current:
      path.append(current)
      current = checked_states[current]

    return path[::-1] 

our_problem = WaterJug(4, 3, (2, 0))
start = (4, 0)  

print("Doing BFS:")
bfs_solution = do_bfs(our_problem, start)

if bfs_solution:
    for step in bfs_solution:
        print(step)
else:
    print("No BFS solution found!")

print("\nDoing DFS:")
dfs_solution = do_dfs(our_problem, start)

if dfs_solution:
    for step in dfs_solution:
        print(step)
else:
    print("No DFS solution found!")

print("\nChecking the next states from (4,0)")
for s in our_problem.get_next_states((4,0)):
    print(s)

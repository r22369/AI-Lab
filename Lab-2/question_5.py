class BlocksWorld:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state

    def heuristic(self, state):
        heuristic_value = 0
        visited = set()

        def calculate_support(block, is_correct):
            score = 1 if is_correct else -1
            while block != "table" and block not in visited:
                visited.add(block)
                heuristic_value[block] += score
                block = state.get(block, "table")

        heuristic_value = {block: 0 for block in state.keys()}
        for block in state.keys():
            current_support = state.get(block, "table")
            goal_support = self.goal_state.get(block, "table")
            if current_support == goal_support:
                calculate_support(block, is_correct=True)
            else:
                calculate_support(block, is_correct=False)

        return sum(heuristic_value.values())

if __name__ == "__main__":
    initial_state = {"A": "B", "B": "table", "C": "A"}
    goal_state = {"A": "table", "B": "A", "C": "B"}

    blocks_world = BlocksWorld(initial_state, goal_state)
    heuristic_value = blocks_world.heuristic(initial_state)
    print(f"Heuristic Value: {heuristic_value}")


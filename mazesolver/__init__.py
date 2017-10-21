from typing import Tuple, List
import numpy as np

from astar import AStar


class MazeSolver(AStar):
    """
    Each node is represented by its index (x,y) in the maze array
    """
    REACHABLE_NODES = ['A', 'B', '.']

    def __init__(self, maze: str) -> None:
        lines = maze.split('\n')

        # All lines need to be of the same width as the first line
        self.width = len(lines[0])

        items = [
            [c for c in line]
            for line
            in lines
            if len(line) == self.width
        ]
        self.height = len(items)

        self.maze = np.array(items)

        assert self.height, self.width == self.maze.shape

        start_index = np.where(self.maze == 'A')
        self.start = (start_index[0][0], start_index[1][0],)

        goal_index = np.where(self.maze == 'B')
        self.goal = (goal_index[0][0], goal_index[1][0],)

    def neighbors(self, node: Tuple):
        x, y = node
        nnodes = ((x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1))
        return tuple(nnode for nnode in nnodes if self.reachable(nnode))

    def reachable(self, node: Tuple[int, int]) -> bool:
        # Numpy allows negative indexing, so this needs to be guarded against
        if node[0] < 0 or node[1] < 0:
            return False

        try:
            return self.maze[node] in self.REACHABLE_NODES
        except IndexError:
            # Too big an index is out of bounds of the maze
            return False

    def distance_between(self, n1: Tuple, n2: Tuple) -> int:
        # Neighbouring nodes are always 1 units apart
        return 1

    def heuristic_cost_estimate(self, current: Tuple, goal: Tuple) -> int:
        return abs(goal[0] - current[0]) + abs(goal[1] - current[1])

    def is_goal_reached(self, current, goal):
        return current == self.goal

    def solve(self) -> List[Tuple]:
        # self.astar() returns a generator, so it is cast into a list
        self.path = list(self.astar(self.start, self.goal))

        self.solved_maze = self.maze.copy()
        for position in self.path:
            self.solved_maze[position] = 'O'

        return self.path

    def visualize(self) -> None:
        if not hasattr(self, 'solved_maze'):
            self.solve()

        print('-' * (self.width + 2))
        for row in range(0, self.height):
            print('|', end='')
            for col in range(0, self.width):
                print(self.solved_maze[row, col], end='')
            print('|')
        print('-' * (self.width + 2))


all = ['MazeSolver']

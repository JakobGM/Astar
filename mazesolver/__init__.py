from typing import Tuple
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

        items = [[c for c in line] for line in lines if len(line) == self.width]
        self.height = len(items)

        self.maze = np.array(items)

        assert self.height, self.width == self.maze.shape

        start_index = np.where(self.maze=='A')
        self.start = (start_index[0][0], start_index[1][0],)

        goal_index = np.where(self.maze == 'B')
        self.goal = (goal_index[0][0], goal_index[1][0],)

    def neighbors(self, node: Tuple):
        x, y = node
        nnodes = ((x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1))
        return tuple(nnode for nnode in nnodes if self.reachable(nnode))

    def reachable(self, node: Tuple) -> bool:
        x, y = node

        if not ((0 <= x < self.width) and (0 <= y < self.height)):
            return False
        else:
            return self.maze[x, y] in self.REACHABLE_NODES

    def distance_between(self, n1: Tuple, n2: Tuple) -> int:
        # Neighbouring nodes are always 1 units apart
        return 1

    def heuristic_cost_estimate(self, current: Tuple, goal: Tuple) -> int:
        return abs(goal[0] - current[0]) + abs(goal[1] - current[1])


all = ['MazeSolver']

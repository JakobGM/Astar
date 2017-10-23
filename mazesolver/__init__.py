from typing import Tuple, List

import colored
from colored import stylize
import numpy as np

from astar import AStar


Node = Tuple[int, int]


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

        self.solve_attempted = False

    def neighbors(self, node: Node):
        x, y = node
        nnodes = ((x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1))
        return tuple(nnode for nnode in nnodes if self.reachable(nnode))

    def reachable(self, node: Node) -> bool:
        # Numpy allows negative indexing, so this needs to be guarded against
        if node[0] < 0 or node[1] < 0:
            return False

        try:
            return self.maze[node] in self.REACHABLE_NODES
        except IndexError:
            # Too big an index is out of bounds of the maze
            return False

    def distance_between(self, n1: Node, n2: Node) -> int:
        # Neighbouring nodes are always 1 units apart
        return 1

    def heuristic_cost_estimate(self, current: Node, goal: Node) -> int:
        return abs(goal[0] - current[0]) + abs(goal[1] - current[1])

    def is_goal_reached(self, current, goal):
        return current == self.goal

    def solve(self, method='Astar') -> List[Node]:
        self.path = self.astar(self.start, self.goal, method=method)

        # Successful self.astar() returns a generator, so it is cast into a
        # list
        if not self.path is None:
            self.path = list(self.path)
            self.success = True

            self.solved_maze = self.maze.copy()

            # Fill in the found path, except for start and goal
            for position in self.path[1:-1]:
                self.solved_maze[position] = 'O'
        else:
            self.success = False

        self.solve_attempted = True

        return self.path

    def visualize(self) -> None:
        if not self.solve_attempted:
            self.solve()

        if self.success:
            self.print_maze(self.solved_maze)
        else:
            print("Could not find solution to the maze!")
            self.print_maze(self.maze)

    @classmethod
    def print_maze(cls, maze) -> None:
        # Print top boarder of maze
        print('-' * (maze.shape[1] + 2))

        for row in range(0, maze.shape[0]):
            # Print left boarder of maze
            print('|', end='')

            for col in range(0, maze.shape[1]):
                # Print the text representation of each individual node
                print(
                    cls.node_representation(
                        maze=maze,
                        node=(row, col),
                    ),
                    end='',
                )

            # Print left boarder of maze
            print('|')

        # Print bottom boarder of maze
        print('-' * (maze.shape[1] + 2))

    @classmethod
    def node_representation(cls, maze: np.array, node: Node) -> str:
        STYLE_OF = {
            '.': colored.bg('black'),
            '#': colored.bg(239),
            '-': colored.bg('white'),
            '|': colored.bg('white'),
            'A': colored.bg(1),
            'B': colored.bg(1),
            'O': colored.bg('dark_orange_3b'),
        }
        type = maze[node]
        return stylize(type[-1], STYLE_OF[type[0]] + colored.fg('white'))

    def representation(
        self,
        with_path=True,
        with_open_closed=False,
    ) -> np.array:
        """
        Returns a matrix which when printed elemntwise shows a nice visual
        representation of the maze.
        """
        rows = self.height + 2
        cols = self.width + 2

        # Preallocate varstring array
        items = rows * cols
        self._rep_mat = np\
            .array(('',) * items, dtype=object)\
            .reshape(
                (self.height + 2),
                (self.width + 2),
            )

        # Boarder of maze
        self._rep_mat[:, 0] = '|'
        self._rep_mat[:, -1] = '|'
        self._rep_mat[0, :] = '-'
        self._rep_mat[-1, :] = '-'

        if with_path:
            self._rep_mat[1:-1, 1:-1] = self.solved_maze
        else:
            self._rep_mat[1:-1, 1:-1] = self.maze

        if with_open_closed:
            for node in self.open_set:
                self._rep_mat[node] += '*'
            for node in self.closed_set:
                self._rep_mat[node] += 'x'

        for row in range(rows):
            for col in range(cols):
                self._rep_mat[row, col] = self.node_representation(
                    self._rep_mat,
                    (row, col),
                )

        rows, cols = self._rep_mat.shape
        for row in range(rows):
            for col in range(cols):
                print(self._rep_mat[row, col], end='')
            print()


class TerrainMazeSolver(MazeSolver):
    REACHABLE_NODES = ['w', 'm', 'f', 'g', 'r', 'A', 'B']
    COST_OF = {
        'w': 100,
        'm': 50,
        'f': 10,
        'g': 5,
        'r': 1,
        # Start and goal nodes need to always be traversed, so the cost does
        # not matter
        'A': 0,
        'B': 0,
    }

    def distance_between(self, n1: Node, n2: Node) -> int:
        return self.COST_OF[self.maze[n2]]

    @classmethod
    def node_representation(cls, maze: np.array, node: Node) -> str:
        STYLE_OF = {
            '-': colored.bg('white'),
            '|': colored.bg('white'),
            'w': colored.bg('blue'),
            'm': colored.bg(243),
            'f': colored.bg(28),
            'g': colored.bg(119),
            'r': colored.bg(130),
            'A': colored.bg(1),
            'B': colored.bg(1),
            'O': colored.bg('dark_orange_3b'),
        }
        type = maze[node]
        return stylize(type[-1], STYLE_OF[type[0]] + colored.fg('white'))


all = ['MazeSolver', 'TerrainMazeSolver']


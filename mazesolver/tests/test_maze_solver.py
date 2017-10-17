import numpy as np

from mazesolver import MazeSolver


class TestMazeSolver:
    def test_init_with_file(self):
        with open('mazesolver/tests/boards/board-1-1.txt') as f:
            ms = MazeSolver(f.read())

        assert ms.maze.shape == (7, 20)

    def test_simple_maze_string(self):
        maze = '.#\nAB'
        ms = MazeSolver(maze)

        assert np.array_equal(ms.maze, np.array([['.', '#'], ['A', 'B']]))

    def test_dimensions_of_maze(self):
        maze = '.#.\nAB.'
        ms = MazeSolver(maze)

        assert ms.width == 3
        assert ms.height == 2

    def test_reachable(self):
        maze = 'A#B\n.#.\n...'
        ms = MazeSolver(maze)

        # Check all points within maze
        assert ms.reachable((0, 0)) is True
        assert ms.reachable((0, 1)) is False
        assert ms.reachable((0, 2)) is True

        assert ms.reachable((1, 0)) is True
        assert ms.reachable((1, 1)) is False
        assert ms.reachable((1, 2)) is True

        assert ms.reachable((2, 0)) is True
        assert ms.reachable((2, 1)) is True
        assert ms.reachable((2, 2)) is True

        # Out of bounds
        assert ms.reachable((-1, 0)) is False
        assert ms.reachable((0, -1)) is False
        assert ms.reachable((3, -1)) is False
        assert ms.reachable((0, 3)) is False

    def test_neighbours(self):
        maze = 'A#B\n.#.\n...'
        ms = MazeSolver(maze)

        assert ms.neighbors((0,0)) == ((1,0),)

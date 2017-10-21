import numpy as np
import pytest

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

    def test_start_and_goal_index(self):
        maze = '.#.\nAB.'
        ms = MazeSolver(maze)

        assert ms.start == (1, 0,)
        assert ms.goal == (1, 1,)

    def test_is_goal_reached(self):
        maze = '.#.\nAB.'
        ms = MazeSolver(maze)

        assert ms.is_goal_reached((0, 0), (0, 0)) is False
        assert ms.is_goal_reached((1, 0), (0, 0)) is False
        assert ms.is_goal_reached((1, 1), (0, 0)) is True

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

        assert ms.neighbors((0, 0)) == ((1, 0),)

    def test_complex_neighbours_case(self):
        maze =  '######\n' + \
                '..A.#B\n' + \
                '.####.\n' + \
                '......\n'
        ms = MazeSolver(maze)
        assert ms.neighbors((1, 2)) == (
            (1, 3),
            (1, 1),
        )
        assert ms.neighbors((2, 5)) == (
            (3, 5),
            (1, 5),
        )

    def test_distance_between_adjacent_nodes(self, maze_solver):
        assert maze_solver.distance_between(None, None) == 1

    def test_heuristic_cost_estimate(self, maze_solver):
        f = maze_solver.heuristic_cost_estimate

        assert f((0, 0), (0, 0)) == 0
        assert f((0, 1), (0, 0)) == 1
        assert f((0, 0), (0, 1)) == 1
        assert f((3, 3), (0, 1)) == 5

    def test_solve(self, maze_solver):
        solution = [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (1, 2), (0, 2)]
        assert maze_solver.solve() == solution

    @pytest.mark.skip(reason='Can not find out how to capture stdout')
    def test_visualize(self, maze_solver, capsys):
        maze_solver.visualize()
        out, _ = capsys.readouterr()
        assert out == '-----\n|O#O|\n|O#O|\n|OOO|\n-----\n'

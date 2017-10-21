import pytest

from mazesolver import MazeSolver


@pytest.fixture
def maze_solver():
    maze_str = 'A#B\n' + \
               '.#.\n' + \
               '...\n'
    return MazeSolver(maze_str)

import pytest

from mazesolver import MazeSolver


@pytest.fixture
def maze_solver():
    maze_str = 'A#B' + \
               '.#.' + \
               '...'
    return MazeSolver(maze_str)

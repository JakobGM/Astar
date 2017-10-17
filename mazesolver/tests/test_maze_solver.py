import pytest

from mazesolver import MazeSolver

class TestMazeSolver:
    def test_init_with_file(self):
        with open('mazesolver/tests/boards/board-1-1.txt') as f:
            ms = MazeSolver(f)

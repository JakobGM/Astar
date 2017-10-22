from sys import argv

from mazesolver import MazeSolver, TerrainMazeSolver

if argv[1] == 'task_1.2':
    board_paths = 'mazesolver/tests/boards/board-1-'

    for board_number in [1, 2, 3, 4]:
        with open(board_paths + str(board_number) + '.txt') as board_file:
            maze_solver = MazeSolver(board_file.read())
            maze_solver.visualize()

if argv[1] == 'task_2.2':
    board_paths = 'mazesolver/tests/boards/board-2-'

    for board_number in [1, 2, 3, 4]:
        with open(board_paths + str(board_number) + '.txt') as board_file:
            maze_solver = TerrainMazeSolver(board_file.read())
            maze_solver.visualize()

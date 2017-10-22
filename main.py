from mazesolver import MazeSolver

if __name__ == '__main__':
    board_paths = 'mazesolver/tests/boards/board-1-'

    for board_number in [1, 2, 3, 4]:
        with open(board_paths + str(board_number) + '.txt') as board_file:
            maze_solver = MazeSolver(board_file.read())
            maze_solver.visualize()

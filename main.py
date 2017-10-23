from sys import argv

from mazesolver import MazeSolver, TerrainMazeSolver

if argv[1] == '1':
    board_paths = 'mazesolver/tests/boards/board-1-'

    for board_number in [1, 2, 3, 4]:
        with open(board_paths + str(board_number) + '.txt') as board_file:
            maze_solver = MazeSolver(board_file.read())
            maze_solver.visualize()

if argv[1] == '2':
    board_paths = 'mazesolver/tests/boards/board-2-'

    for board_number in [1, 2, 3, 4]:
        with open(board_paths + str(board_number) + '.txt') as board_file:
            maze_solver = TerrainMazeSolver(board_file.read())
            maze_solver.visualize()

if argv[1] == '3':
    base_path = 'mazesolver/tests/boards/'
    board_names = (
        ('board-1-1.txt', MazeSolver),
        ('board-2-1.txt', TerrainMazeSolver),
    )
    methods = ('Astar', 'Dijkstra', 'BFS',)

    for board_name, Solver in board_names:
        for method in methods:
            with open(base_path + board_name) as board_file:
                maze_solver = Solver(board_file.read())
                maze_solver.solve(method=method)

                print('\n' + '\u2500' * 60)
                print(
                    'Solution for board "{}" found with the {}-algorithm'\
                    .format(board_name, method)
                )
                maze_solver.visualize()
                print('\u2500' * 60)

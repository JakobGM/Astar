from mazesolver import TerrainMazeSolver


class TestTerrainMazeSolver:
    def test_distance_between_adjacent_nodes(self):
        maze = 'Aw\ngB\n'
        ms = TerrainMazeSolver(maze)

        water_cost = ms.distance_between(
            (0, 0),
            (0, 1),
        )
        assert water_cost == 100

        grasslands_cost = ms.distance_between(
            (1, 0),
            (1, 0),
        )
        assert grasslands_cost == 5

    def test_with_the_given_boards(self):
        solvable_maze_numbers = ['1', '2', '3', '4']

        for num in solvable_maze_numbers:
            with open('mazesolver/tests/boards/board-2-' + num + '.txt') as f:
                ms = TerrainMazeSolver(f.read())
                ms.solve()
                assert ms.success

class TestModificationsOfTheAstarAlgorithm:
    def test_closed_set(self):
        maze = 'Aw\ngB\n'
        ms = TerrainMazeSolver(maze)
        ms.solve()

        # Non-deterministic ordering
        assert (ms.closed_set == ((0, 0), (1, 0))) \
            or (ms.closed_set == ((1, 0), (0, 0)))

    def test_open_set(self):
        maze = 'Aw\ngB\n'
        ms = TerrainMazeSolver(maze)
        ms.solve()

        assert ms.open_set == ((0, 1),)

    def test_dijkstra_with_the_given_boards(self):
        solvable_maze_numbers = ['1', '2', '3', '4']

        for num in solvable_maze_numbers:
            with open('mazesolver/tests/boards/board-2-' + num + '.txt') as f:
                ms = TerrainMazeSolver(f.read())
                ms.solve(method='dijkstra')
                assert ms.success

    def test_bfs_with_the_given_boards(self):
        solvable_maze_numbers = ['1', '2', '3', '4']

        for num in solvable_maze_numbers:
            with open('mazesolver/tests/boards/board-2-' + num + '.txt') as f:
                ms = TerrainMazeSolver(f.read())
                ms.solve(method='BFS')
                assert ms.success

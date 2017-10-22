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

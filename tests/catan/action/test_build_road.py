from ...context import catan

import unittest


class TestBuildRoad(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.game = catan.game.Game()
        setup = catan.setup.default.DefaultGameSetup()
        setup(self.game)
        road_ids = self.game.ids[catan.road.Road]
        road_id = next(iter(road_ids))
        self.road = self.game.game_objects[road_id]
        self.agent = self.game.agent_order[0]
        self.action = catan.action.build_road.BuildRoad(self.agent, None, self.road)
    
    def testObservation(self):
        observation = self.action.observation()
        self.assertListEqual(observation, [self.agent.id, self.road.id, 0])


class TestBuildRoadFactory(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.game = catan.game.Game()
        setup = catan.setup.default.DefaultGameSetup()
        setup(self.game)

    def testTest(self):
        pass
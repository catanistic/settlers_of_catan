from ...context import catan

import unittest


class TestBuildRoad(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.game = catan.game.Game()
        setup = catan.setup.default.DefaultGameSetup()
        setup(self.game)
        road_ids = self.game.ids[catan.shared.objects.GameObjectType.Road]
        road_id = next(iter(road_ids))
        self.road = self.game.game_objects[road_id]
        self.agent = catan.agent.Agent(agent_name="Bob")
        self.action = catan.action.build_road.BuildRoad(self.agent.id, None, self.road)
    
    def testObservation(self):
        observation = self.action.observation()
        self.assertListEqual(observation, [self.agent.id, self.road.id, 0])


class TestBuildRoadFactory(unittest.TestCase):
    def setUp(self):
        pass

    def testTest(self):
        pass
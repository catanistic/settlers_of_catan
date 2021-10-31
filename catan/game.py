from catan.shared.objects import GameObject

class Game(GameObject):
    def __init__(self):
        super().__init__()

        self.tile_ids = []
        self.actor_ids = []
        self.node_ids = []
        self.road_ids = []

        self.game_objects = {}

    @property
    def observation(self):
        pass
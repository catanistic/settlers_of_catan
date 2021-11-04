from catan.setup.base import GameSetup 
from catan.resource import ResourceType


TILE_RESOURCES = [
    ResourceType.Ore,
    ResourceType.Wool,
    ResourceType.Wood,

    ResourceType.Wheat,
    ResourceType.Clay,
    ResourceType.Wool,
    ResourceType.Clay,

    ResourceType.Wheat,
    ResourceType.Wood,
    ResourceType.Null,
    ResourceType.Wood,
    ResourceType.Ore,

    ResourceType.Wood,
    ResourceType.Ore,
    ResourceType.Wheat,
    ResourceType.Wool,

    ResourceType.Clay,
    ResourceType.Wheat,
    ResourceType.Wool
]

TILE_NUMBER_TOKENS = [
    10, 2, 9,
    12, 6, 4, 10,
    9, 11, 0, 3, 8,
    8, 3, 4, 5,
    5, 6, 11,
]

ROBBER_POSITION = (2, 2)


class DefaultGameSetup(GameSetup):
    def _setTileProperties(self, game):
        pass

    def _setPortProperties(self, game):
        pass

    def setup(self, game):
        super().setup(game)
        self._setPortProperties(game)
        self._setTileProperties(game)

        resource_types = iter(TILE_RESOURCES)
        number_tokens = iter(TILE_NUMBER_TOKENS)

        for tiles in self.tiles:
            for tile in tiles:
                tile.resource = next(resource_types)
                tile.number_token = next(number_tokens)
        
        self.setRobberPosition(game, ROBBER_POSITION)
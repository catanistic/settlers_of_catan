from catan.setup.base import GameSetup 
from catan.resource import ResourceType


TILE_RESOURCES = [
    ResourceType.Wheat,
    ResourceType.Wool,
    ResourceType.Wheat,

    ResourceType.Wool,
    ResourceType.Clay,
    ResourceType.Wood,
    ResourceType.Ore,

    ResourceType.Wood,
    ResourceType.Ore,
    ResourceType.Wheat,
    ResourceType.Wool,
    ResourceType.Wood,

    ResourceType.Clay,
    ResourceType.Wood,
    ResourceType.Wool,
    ResourceType.Wheat,

    ResourceType.Null,
    ResourceType.Clay,
    ResourceType.Ore,
]

TILE_NUMBER_TOKENS = [
    9, 10, 8,
    12, 5, 4, 3,
    11, 6, 11, 9, 6,
    4, 3, 10, 2,
    0, 8, 5,
]

ROBBER_POSITION = (4, 0)

PORT_CONFIGURATIONS = [
    (ResourceType.Everything, 3),
    (ResourceType.Everything, 3),
    (ResourceType.Clay, 2),
    (ResourceType.Wood, 2),
    (ResourceType.Everything, 3),
    (ResourceType.Wheat, 2),
    (ResourceType.Ore, 2),
    (ResourceType.Everything, 3),
    (ResourceType.Wool, 2),
]


class DefaultGameSetup(GameSetup):
    def _setTileProperties(self, game):
        resource_types = iter(TILE_RESOURCES)
        number_tokens = iter(TILE_NUMBER_TOKENS)
        for tiles in self.tiles:
            for tile in tiles:
                tile.resource_type = next(resource_types)
                tile.number_token = next(number_tokens)
        
        self.setRobberPosition(game, ROBBER_POSITION)

    def _setPortProperties(self, game):
        for port, configuration in zip(self.ports, PORT_CONFIGURATIONS):
            port.resource_type, port.exchange_rate = configuration

    def __call__(self, game):
        super().__call__(game)
        self._setPortProperties(game)
        self._setTileProperties(game)

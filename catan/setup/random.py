from catan.setup.base import GameSetup 
from catan.resource import ResourceType
from catan.setup.default import TILE_RESOURCES, TILE_NUMBER_TOKENS, PORT_CONFIGURATIONS

import random


class RandomGameSetup(GameSetup):
    def _setTileProperties(self, game):
        resource_types = TILE_RESOURCES[:]
        random.shuffle(resource_types)
        resource_types = iter(resource_types)

        number_tokens = list(filter(lambda x: x != 0, TILE_NUMBER_TOKENS))
        random.shuffle(number_tokens)
        number_tokens = iter(number_tokens)

        for tiles in self.tiles:
            for tile in tiles:
                tile.resource = next(resource_types)
                if tile.resource != ResourceType.Null:
                    tile.number_token = next(number_tokens)
                else:
                    tile.number_token = 0
                    self.setRobberPosition(game, tile.position)

    def _setPortProperties(self, game):
        port_configurations = PORT_CONFIGURATIONS[:]
        random.shuffle(port_configurations)
        for port, configuration in zip(self.ports, port_configurations):
            port.resource_type, port.exchange_rate = configuration

    def __call__(self, game):
        super().__call__(game)
        self._setPortProperties(game)
        self._setTileProperties(game)

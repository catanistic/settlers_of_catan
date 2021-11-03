from catan.setup.base import GameSetup 


class RandomGameSetup(GameSetup):
    def _setTileProperties(self, game):
        pass

    def _setPortProperties(self, game):
        pass

    def setup(self, game):
        super().setup(game)
        self._setPortProperties(game)
        self._setTileProperties(game)
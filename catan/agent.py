from catan.card import ValidDevelopmentCardTypes
from catan.resource import ValidResourceTypes
from catan.shared import GameObject, FieldType


class Agent(GameObject):
    def __init__(self, agent_name=None, num_roads=15, num_settlements=5, num_cities=4):
        """Initializer for agent object.

        Args:
            agent_name: the name displayed in the str(agent).
            num_roads: maximum number of roads that the agent can build.
            num_settlements: maximum number of settlements that the agent can build.
            num_cities: maximum number of cities that the agent can build.
        """
        super().__init__()
        self.agent_name = agent_name if agent_name else str(self.object_id)
        self.resources = {r:0 for r in ValidResourceTypes}
        self.development_cards = {c:0 for c in ValidDevelopmentCardTypes}
        self.development_cards_buffer = {c:0 for c in ValidDevelopmentCardTypes}
        self.played_development_cards = {c:0 for c in ValidDevelopmentCardTypes}

        self.available_roads = num_roads 
        self.available_settlements = num_settlements
        self.available_cities = num_cities

    def __str__(self):
        return "Player ({})".format(self.agent_name)

    def canAfford(self, price):
        """Checks if the agent has enough resources to pay the price.

        Args:
            price: dict (ResourceType:Int) that represents the price in resources.
        
        Returns:
            True if agent has enough resources to cover the price, False otherwise.
        """
        for resource_type in price:
            if self.resources[resource_type] < price[resource_type]:
                return False
        return True

    def pay(self, price, game):
        """Pays the resources specified in the price argument.

        Args:
            price: dict (ResourceType:Int) that represents the price in resources.
            game: catan.game.Game object.
        """
        for resource_type in price:
            num_resources = price[resource_type]
            self.resources[resource_type] -= num_resources
            game.game_state.resources[resource_type] += num_resources

    @property
    def resource_count(self):
        return sum(self.resources[r] for r in ValidResourceTypes)

    @property
    def reward(self):
        return 0

    @property
    def victory_points(self):
        return 0

    def observation(self, spectator_id=None):
        if spectator_id == self.id:
            return []
        else:
            return []
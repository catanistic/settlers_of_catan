from catan.shared import GameObject, FieldType 

from enum import Enum


class ActionType(Enum):
    BuildStructure = "build"
    BuyDevelopementCard = "buy_development_card"
    DiscardResources = "discard_resources"
    EndTurn = "end" 
    Lose = "lose"
    Monopoly = "monopoly"
    MoveRobber = "connector"
    PlayDevelopmentCard = "development_card"
    RoadBuildingCard = "road_building"
    Spectate = "spectate"
    TargetRobbing = "target_robbing"
    TradeWithEnvironment = "trade"
    Win = "win"
    YearOfPlentyPick = "year_of_plenty"


class Action(GameObject):
    action_type = None 

    def __init__(self, agent_id, next_state):
        super().__init__()
        self.agent_id = agent_id
        self.next_state = next_state

        self.schema.append_field("actor_id", FieldType.GameObjectReference)
        self.schema.append_field("shared_state_id", FieldType.GameObjectReference)

    def observation(self):
        raise NotImplementedError()

    @property
    def id(self):
        return "{}.{}".format(super().id, self.action_type.value)

    def __call__(self, game):
        raise NotImplementedError()


class ActionFactory():
    action_type = None

    def action_space(self, game, agent_id):
        """Returns a list of available actions of type action_type for the player.

        Args:
            game: A catan.game.Game object.
            agent_id: Agent id for the agend that.

        Returns:
            List of legal action of type action_type.
        """
        raise NotImplementedError()
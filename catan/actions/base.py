from catan.shared import GameObject, FieldType 

from enum import Enum


class ActionType(Enum):
    BuildStructure = "build"
    BuyDevelopementCard = "buy_development_card"
    DiscardResources = "discard_resources"
    EndTurn = "end" 
    Monopoly = "monopoly"
    MoveRobber = "connector"
    PlayDevelopmentCard = "development_card"
    RoadBuildingCard = "road_building"
    Spectate = "spectate"
    TargetRobbing = "target_robbing"
    TradeWithEnvironment = "trade"
    YearOfPlentyPick = "year_of_plenty"


class Action(GameObject):
    action_type = None 

    def __init__(self, actor_id=None, shared_state_id=None, next_state=None):
        super().__init__()
        self.actor_id = actor_id
        self.shared_state_id = shared_state_id
        self.next_state = next_state

        self.schema.append_field("actor_id", FieldType.GameObjectReference)
        self.schema.append_field("shared_state_id", FieldType.GameObjectReference)

    @property
    def observation(self):
        raise NotImplementedError()

    @property
    def id(self):
        return "{}.{}".format(super().id, self.action_type.value)

    def __call__(self, game):
        raise NotImplementedError()


class ActionFactory():
    action_type = None

    def __call__(self, game):
        """Returns a list of available actions of type action_type for the player.

        Args:
            game: A catan.game.Game object

        Returns:
            List of legal action of type action_type.
        """
        raise NotImplementedError()
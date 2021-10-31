from catan import shared
from catan.shared import GameObject, FieldType 

from enum import Enum


class ActionType(Enum):
    AcceptTrade = "accept_trade"
    BuildStructure = "build"
    Default = "default"
    EndTurn = "end" 
    KnightCard = "knight"
    MonopolyCard = "monopoly"
    MoveRobber = "connector"
    PlayDevelopmentCard = "development_card"
    ProposeTrade = "propose_trade"
    RejectTrade = "reject_trade"
    RoadBuildingCard = "road_building"
    RobPlayer = "rob"
    RollDice = "roll"
    TradeWithEnvironment = "trade"
    YearOfPlentyCard = "year_of_plenty"


class Action(GameObject):
    action_type = ActionType.Default

    def __init__(self, actor_id, shared_state_id):
        super().__init__()
        self.actor_id = actor_id
        self.shared_state_id = shared_state_id

        self.schema.append_field("actor_id", FieldType.GameObjectReference)
        self.schema.append_field("shared_state_id", FieldType.GameObjectReference)

    @property
    def observation(self):
        raise NotImplementedError()
        return self.schema(
            self.actor_id,
            self.shared_state_id,
        )

    @property
    def id(self):
        return "{}.{}".format(super().id, self.action_type.value)

    def execute(self, shared_state, actor_collection, board):
        raise NotImplementedError()


class ActionFactory():
    action_type = ActionType.Default

    def __call__(self, game):
        """Returns a list of available actions of type action_type for the player.

        Args:
            game: A catan.game.Game object

        Returns:
            List of legal action of type action_type.
        """
        raise NotImplementedError()
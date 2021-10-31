from catan.shared import GameObject, FieldType 

from enum import Enum


class ActionType(Enum):
    AcceptTrade = "accept_trade"
    BuildStructure = "build"
    BuyDevelopementCard = "buy_development_card"
    Default = "default"
    EndTurn = "end" 
    KnightCard = "knight"
    MonopolyCard = "monopoly"
    MoveRobber = "connector"
    PassRobbing = "pass_robbing"
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
    action_type = ActionType.Default

    def __call__(self, game):
        """Returns a list of available actions of type action_type for the player.

        Args:
            game: A catan.game.Game object

        Returns:
            List of legal action of type action_type.
        """
        raise NotImplementedError()
from catan.shared import GameObject, FieldType 

from enum import Enum


class ActionType(Enum):
    BuildRoad = "build_road"
    BuildSettlement = "build_settlement"
    BuyDevelopementCard = "buy_development_card"
    DiscardResources = "discard_resources"
    EarnAchievement = "earn_achievement"
    EarnResource = "earn_resource"
    EndTurn = "end_turn"
    Lose = "lose"
    LoseAchievement = "lose_achievement"
    Monopoly = "monopoly"
    MoveRobber = "move_robber"
    NextPhase = "next_phase" 
    PlayDevelopmentCard = "play_development_card"
    RoadBuildingCard = "play_road_building"
    RobPlayer = "rob_player"
    RollDice = "roll_dice"
    TradeWithEnvironment = "trade"
    UpgradeSettlement = "upgrade_settlement"
    Win = "win"
    YearOfPlentyPick = "year_of_plenty"

    Spectate = "spectate"


class Action(GameObject):
    action_type = None 
    is_spectable = True

    def __init__(self, agent_id, next_state):
        super().__init__()
        self.agent_id = agent_id
        self.next_state = next_state

        self.schema.append_field("actor_id", FieldType.GameObjectReference)
        self.schema.append_field("shared_state_id", FieldType.GameObjectReference)

    def observation(self, spectator_id=None, inverse=False):
        raise NotImplementedError()

    @property
    def id(self):
        return "{}.{}".format(super().id, self.action_type.value)

    def __str__(self):
        raise NotImplementedError()

    def __call__(self, game):
        raise NotImplementedError()


class ActionFactory():
    action_type = None

    def __call__(self, game, agent_id):
        """Returns a list of available actions of type action_type for the player.

        Args:
            game: A catan.game.Game object.
            agent_id: Agent id for the agend that.

        Returns:
            List of legal action of type action_type.
        """
        raise NotImplementedError()
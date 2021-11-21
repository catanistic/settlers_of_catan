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

    def __init__(self, agent, next_state):
        super().__init__()
        self.agent = agent
        self.next_state = next_state
        self.schema.append_field("agent_id", FieldType.GameObjectReference)

    def observation(self, spectator=None):
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

    def __init__(self, game, agent, next_state):
        self.game = game
        self.agent = agent
        self.next_state = next_state

    def __call__(self):
        """Returns a list of available actions of type action_type for the player.

        Returns:
            List of legal action of type action_type.
        """
        raise NotImplementedError()
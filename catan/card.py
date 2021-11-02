from enum import Enum


class DevelopmentCardType(Enum):
    Knight = "Knight"
    Monopoly = "Monopoly"
    RoadBuilding = "Road Building"
    VictoryPoint = "Victory Point"
    YearOfPlenty = "Year of Plenty"
    Uknown = "Uknown"


ValidDevelopmentCardTypes = {
    DevelopmentCardType.Knight,
    DevelopmentCardType.Monopoly,
    DevelopmentCardType.RoadBuilding,
    DevelopmentCardType.VictoryPoint,
    DevelopmentCardType.YearOfPlenty,
}
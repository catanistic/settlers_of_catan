from enum import Enum


class ResourceType(Enum):
    Clay = "Clay"
    Everything = "Everything"
    Null = "Nothing"
    Ore = "Ore" 
    Unknown = "Unknown"
    Wheat = "Wheat"
    Wood = "Wood" 
    Wool = "Wool" 


ValidResourceTypes = {
    ResourceType.Clay,
    ResourceType.Ore,
    ResourceType.Wheat,
    ResourceType.Wood,
    ResourceType.Wool,
}
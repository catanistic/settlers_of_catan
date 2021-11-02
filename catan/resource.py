from enum import Enum


class ResourceType(Enum):
    Clay = "Clay"
    Null = "null"
    Ore = "Ore" 
    Unknown = "unknown"
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
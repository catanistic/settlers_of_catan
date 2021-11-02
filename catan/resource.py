from enum import Enum


class ResourceType(Enum):
    Clay = "clay"
    Null = "null"
    Ore = "ore" 
    Unknown = "unknown"
    Wheat = "wheat"
    Wood = "wood" 
    Wool = "wool" 


ValidResourceTypes = {
    ResourceType.Clay,
    ResourceType.Ore,
    ResourceType.Wheat,
    ResourceType.Wood,
    ResourceType.Wool,
}
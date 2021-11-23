from catan.shared import GameObject, FieldType


class Road(GameObject):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.owner = None
        self.nodes = []
    
    @property
    def occupied(self):
        return not(self.owner is None)